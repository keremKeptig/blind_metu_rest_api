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
    choice1 = fields.Str(required=False)
    choice2 = fields.Str(required=False)
    choice3 = fields.Str(required=False)
    choice4 = fields.Str(required=False)
    choice5 = fields.Str(required=False)
    test_id = fields.Str(load_only=True)

