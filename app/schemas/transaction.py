from marshmallow import Schema, fields, validate

class TransactionCreateSchema(Schema):
    amount = fields.Decimal(required=True, as_string=True, places=2, validate=validate.Range(min=0.01))
    type = fields.String(required=True, validate=validate.OneOf(["income", "expense"]))
    category = fields.String(required=True, validate=validate.Length(min=1,max=50))
    description = fields.String(required=False, allow_none=True, validate=validate.Length(max=255))
    date = fields.Date(required=True)

class TransactionSchema(Schema):
    id = fields.Int(dump_only=True)
    amount = fields.Decimal(as_string=True, places=2)
    type = fields.String()
    category = fields.String()
    description = fields.String(allow_none=True)
    date = fields.Date()
    user_id = fields.Int()
    created_at = fields.DateTime(dump_only=True)


class TransactionUpdateSchema(Schema):
    amount = fields.Decimal(required=False, as_string=True, places=2, validate=validate.Range(min=0.01))
    type = fields.String(required=False, validate=validate.OneOf(["income", "expense"]))
    category = fields.String(required=False, validate=validate.Length(min=1, max=50))
    description = fields.String(required=False, allow_none=True, validate=validate.Length(max=255))
    date = fields.Date(required=False)
