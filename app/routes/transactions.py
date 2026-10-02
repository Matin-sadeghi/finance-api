from flask.views import MethodView
from flask_smorest import Blueprint,abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.schemas import TransactionSchema, TransactionCreateSchema,TransactionUpdateSchema,TransactionQuerySchema,TransactionPaginationSchema
from app.services import create_transaction , get_transactions_by_user , get_transaction,update_transaction,delete_transaction



transaction_bp = Blueprint("Transactions", __name__, url_prefix="/api/v1/transactions", description="Transaction endpoints")

@transaction_bp.route("")
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

    @transaction_bp.doc(security=[{"BearerAuth": []}])
    @jwt_required()
    @transaction_bp.arguments(TransactionQuerySchema, location="query")
    @transaction_bp.response(200, TransactionPaginationSchema)
    def get(self,args):
        """Get all transactions for the current user."""
        user_id = get_jwt_identity()
        paginatiom = get_transactions_by_user(user_id=int(user_id),filters=args)
        return {
            "items":paginatiom.items,
            "page":paginatiom.page,
            "per_page":paginatiom.per_page,
            "total":paginatiom.total,
            "pages":paginatiom.pages
        }

@transaction_bp.route("/<int:transaction_id>")
class TransactionDetail(MethodView):
    @transaction_bp.doc(security=[{"BearerAuth": []}])
    @jwt_required()
    @transaction_bp.response(200, TransactionSchema)
    def get(self,transaction_id):
        user_id = get_jwt_identity()

        tranasction = get_transaction(user_id,transaction_id)

        if tranasction is None:
            abort(404,message="Transaction not found")

        return tranasction

    @transaction_bp.doc(security=[{"BearerAuth": []}])
    @jwt_required()
    @transaction_bp.arguments(TransactionUpdateSchema)
    @transaction_bp.response(200, TransactionSchema)
    def patch(self,data,transaction_id ):

        user_id = get_jwt_identity()
        transaction = get_transaction(user_id,transaction_id)

        if transaction is None:
            abort(404,message="Transaction not found")

        updated_transaction = update_transaction(transaction, data)
        return updated_transaction  

    @transaction_bp.doc(security=[{"BearerAuth": []}])
    @jwt_required()
    @transaction_bp.response(204)
    def delete(self,transaction_id ):

        user_id = get_jwt_identity()
        transaction = get_transaction(user_id,transaction_id)

        if transaction is None:
            abort(404,message="Transaction not found")

        delete_transaction(transaction)
        