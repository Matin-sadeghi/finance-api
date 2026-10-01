from marshmallow import Schema, fields, validate

class HealthSchema(Schema):
    status = fields.String(required=True, validate=validate.Length(max=255))
    

