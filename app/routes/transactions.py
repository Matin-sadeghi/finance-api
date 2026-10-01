from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.schemas import TransactionSchema, TransactionCreateSchema
from app.services import create_transaction



transaction_bp = Blueprint("Transactions", __name__, url_prefix="/api/v1/transactions", description="Transaction endpoints")

@transaction_bp.route("/")
class TransactionList(MethodView):
    @transaction_bp.doc(security=[{"BearerAuth": []}])
    @jwt_required()
    @transaction_bp.arguments(TransactionCreateSchema)
    @transaction_bp.response(201, TransactionSchema)
    def post(self, data):
        """Create a new transaction."""
        user_id = get_jwt_identity()
        transaction = create_transaction(user_id=int(user_id), data=data)
        return transaction