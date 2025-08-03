from app.extensions import ma
from app.models.order import Order

class OrderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Order
        load_instance = True
        include_fk = True
        fields = ("id", "user_id", "total_price", "status", "created_at")

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
