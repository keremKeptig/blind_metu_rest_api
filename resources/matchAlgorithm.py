import os
from operator import and_

import requests
from flask import jsonify, request
from sqlalchemy import or_, func
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from sqlalchemy.orm import aliased

from database import db
from schemas import UserSchema, QuestionSchema, UserSlots, SlotsSchema
from models import QuestionTable, AnswerTable, MatchTable, ScheduleTable
from datetime import datetime
import jinja2
from datetime import date
# Creating a Flask-Smorest Blueprint
from datetime import datetime

import pytz
from sqlalchemy import and_


blp = Blueprint("Match", "match", description="match algorithm")



# Benzerlik hesaplama fonksiyonu
def calculate_similarity(ans1, ans2):
    assert len(ans1) == len(ans2), "Cevapların uzunluğu aynı olmalı"
    match_count = sum(1 for a, b in zip(ans1, ans2) if a == b)
    return (match_count / len(ans1)) * 100


# En iyi eşleşmeleri bulma fonksiyonu
def find_best_matches(answers, threshold=80.0):
    n = len(answers)
    best_matches = [-1] * n  # En iyi eşleşmeyi saklamak için
    best_similarities = [0.0] * n  # En iyi benzerlik oranını saklamak için

    for i in range(n):
        for j in range(n):
            if i != j:
                similarity = calculate_similarity(answers[i][1], answers[j][1])
                if similarity >= threshold and similarity > best_similarities[i]:
                    best_similarities[i] = similarity
                    best_matches[i] = j

    # En iyi eşleşmeleri bul
    matched = [False] * n  # Hangi kişilerin eşleştiğini takip edin
    final_matches = []

    for i in range(n):
        if not matched[i] and best_matches[i] != -1:
            partner = best_matches[i]
            if not matched[partner] and best_matches[partner] == i:
                matched[i] = True
                matched[partner] = True
                final_matches.append((i, partner, best_similarities[i]))

    return final_matches


# Kullanıcı cevaplarını veri tabanından almak
def get_user_answers():
    user_answers = db.session.query(AnswerTable.username,
                                    db.func.group_concat(AnswerTable.choice).label('answers')).group_by(
        AnswerTable.username).all()
    return user_answers


# Eşleşmeleri veri tabanına kaydetme
def save_matches(matches, user_answers):
    for match in matches:
        user1 = user_answers[match[0]][0]
        user2 = user_answers[match[1]][0]
        similarity = match[2]

        print(user1)
        print(user2)
        print(similarity)

        timezone = pytz.timezone('Europe/Istanbul')

        current_time = datetime.now(timezone)

        current_date = current_time.strftime('%Y-%m-%d')

        matched_user = MatchTable(user1_username=user1, user2_username=user2,
                          date=current_date, location="Lombard, Kalkanlı")

        # Add the user to the database
        db.session.add(matched_user)
        db.session.commit()


@blp.route("/matchusers/<int:test_id>")
class Match(MethodView):

    @blp.response(200)
    def get(self, test_id):


        # Fetch answers based on test_id
        questions = QuestionTable.query.filter_by(test_id=test_id).all()

        if not questions:
            abort(404, message="Test not found")

        # Collect all question ids
        question_ids = [question.question_id for question in questions]

        # Fetch answers based on question_ids
        all_answers = AnswerTable.query.filter(AnswerTable.question_id.in_(question_ids)).all()
        user_answer_pairs = {}
        for answer in all_answers:
            if not answer.username in user_answer_pairs:
                user_answer_pairs[answer.username] = []


            user_answer_pairs[answer.username].append(answer.choice)

        print(user_answer_pairs)
        # Cevapları işlemek ve eşleşmeleri bulmak
        answers = [(user, ''.join(choices)) for user, choices in user_answer_pairs.items()]
        print(answers)
        matches = find_best_matches(answers, 50.0)
        print(matches)
        # Eşleşmeleri veri tabanına kaydet
        save_matches(matches, answers)

        return "Successful"

@blp.route("/fetchmatch/<string:username>")
class TestFind(MethodView):

    @blp.response(200)
    def get(self, username):


        # to find latest match
        latest_date_match = MatchTable.query.filter(
            or_(MatchTable.user1_username == username, MatchTable.user2_username == username)) \
            .order_by(MatchTable.date.desc()).first()


        if username == latest_date_match.user1_username:
            return latest_date_match.user2_username
        elif username == latest_date_match.user2_username:
            return latest_date_match.user1_username
        else:
            return "No Match"

@blp.route("/slots")
class TestFind(MethodView):
    @blp.arguments(SlotsSchema)
    def post(self, slots_data):

        new_slot = ScheduleTable(
            day=slots_data['day'],
            start_time=slots_data['start_time'],
            end_time=slots_data['end_time'],
            username=slots_data['username']
        )


        try:
            db.session.add(new_slot)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"message": str(e)}, 500

        return {"message": "Slot successfully added"}, 201

@blp.route('/match_slots')
class MatchSlots(MethodView):

    @blp.arguments(UserSlots)
    @blp.response(200)
    def post(self, users):
        user1 = users["user1"]
        user2 = users["user2"]

        s1 = aliased(ScheduleTable)
        s2 = aliased(ScheduleTable)

        # Query to find matching slots using SQLAlchemy ORM
        result = db.session.query(
            s1.username.label('user1'),
            s2.username.label('user2'),
            s1.day,
            s1.start_time,
            s1.end_time
        ).join(
            s2,
            and_(
                s1.day == s2.day,
                s1.start_time == s2.start_time,
                s1.end_time == s2.end_time,
                s2.username == user2
            )
        ).filter(
            s1.username == user1
        ).all()

        # Process the results
        slots = []
        for row in result:
            slots.append({
                'user1': row.user1,
                'user2': row.user2,
                'day': row.day,
                'start_time': row.start_time,
                'end_time': row.end_time
            })

        return jsonify(slots)
