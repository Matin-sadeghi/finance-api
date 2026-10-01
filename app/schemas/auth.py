from marshmallow import Schema, fields, validate

class AuthSchema(Schema):
    email = fields.Email(required=True, validate=validate.Length(max=255))
    password = fields.String(required=True, validate=validate.Length(min=8, max=255))

class RegisterSchema(AuthSchema):
    pass

class LoginSchema(AuthSchema):
    pass

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True, validate=validate.Length(max=255))
    created_at = fields.DateTime(dump_only=True)

class TokenSchema(Schema):
    message = fields.String(required=True)
    access_token = fields.String(required=True)
    refresh_token = fields.String(required=True)
    user = fields.Nested(UserSchema, required=True)