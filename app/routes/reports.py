from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_smorest import Blueprint

from app.schemas.report import FinancialSummarySchema, ReportQuerySchema
from app.services.report_service import get_financial_summary


reports_blp = Blueprint(
    "reports",
    __name__,
    url_prefix="/api/v1/reports",
    description="Financial reports",
)


@reports_blp.route("/summary")
class FinancialSummary(MethodView):

    @reports_blp.doc(security=[{"BearerAuth": []}])
    @jwt_required()
    @reports_blp.arguments(ReportQuerySchema, location="query")
    @reports_blp.response(200, FinancialSummarySchema)
    def get(self, args):
        user_id = int(get_jwt_identity())

        return get_financial_summary(
            user_id=user_id,
            start_date=args.get("start_date"),
            end_date=args.get("end_date"),
        )