from marshmallow import Schema, fields


class UserRegisterSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    # Load only because of processing passwords secretly
    password = fields.Str(required=True, load_only=True)
    gender = fields.Int(required=True)
    date_of_birth = fields.Str(required=False)
    sexual_interest = fields.Int(required=False)


# class PlainAnswer(Schema):
#     id = fields.Int(dump_only=True)
#     user_id = fields.Int(dump_only=True)
#
#
# class PlainMatches(Schema):
#     id = fields.Int(dump_only=True)
#     user_id = fields.Int(dump_only=True)
# class PlainQuestions(Schema):
#     id = fields.Int(dump_only=True)
#     user_id = fields.Int(dump_only=True)

# class UserRegisterSchema(UserSchema):
#     answers = fields.List(fields.Nested(PlainAnswer()), dump_only=True)
#     matches = fields.List(fields.Nested(PlainMatches()), dump_only=True)
#     questions = fields.List(fields.Nested(PlainQuestions()), dump_only=True)
#
