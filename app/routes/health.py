from flask_smorest import Blueprint
from flask.views import MethodView
from app.schemas.health import HealthSchema

health_bp = Blueprint("health", __name__,url_prefix="/api/v1/health",description="Health endpoints")





@health_bp.route("/")
class Health(MethodView):
    @health_bp.response(200, HealthSchema)
    def get(self):
        return {"status": "ok"}