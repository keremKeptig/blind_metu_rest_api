from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    # Load only because of processing passwords secretly




class UserRegisterSchema(UserSchema):
    password = fields.Str(required=True, load_only=True)
    gender = fields.Int(required=True)
    date_of_birth = fields.Str(required=False)
    sexual_interest = fields.Int(required=False)


