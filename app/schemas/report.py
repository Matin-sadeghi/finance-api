from marshmallow import Schema, fields, validates_schema, ValidationError

class FinancialSummarySchema(Schema):
    total_income = fields.Decimal(as_string=True, places=2)
    total_expense = fields.Decimal(as_string=True, places=2)
    net_balance = fields.Decimal(as_string=True, places=2)



class ReportQuerySchema(Schema):
    start_date = fields.Date(required=False)
    end_date = fields.Date(required=False)

    @validates_schema
    def validate_date_range(self, data, **kwargs):
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        if start_date and end_date and start_date > end_date:
            raise ValidationError(
                "start_date must be earlier than or equal to end_date."
            )