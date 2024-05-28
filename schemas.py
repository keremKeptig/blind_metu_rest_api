from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    # Load only because of processing passwords secretly
    password = fields.Str(required=True, load_only=True)



class UserRegisterSchema(UserSchema):
    gender = fields.Int(required=True)
    date_of_birth = fields.Str(required=False)
    sexual_interest = fields.Int(required=False)


class QuestionSchema(Schema):
    q_id = fields.Int(dump_only=True)
    q_text = fields.Str(required=False)

    test_id = fields.Int(load_only=True)

class AnswerSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(load_only=True)
    q_id = fields.Int(load_only=True)
    choice = fields.Str(required=False)

class ProblemSchema(Schema):
    form_id = fields.Int(dump_only=True)
    comment = fields.Str(required=False)
    id = fields.Int(load_only=True)