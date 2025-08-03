from app.extensions import ma
from app.models.cart import CartItem

class CartItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CartItem
        load_instance = True
        include_fk = True
        fields = ("id", "user_id", "product_id", "quantity")

cart_item_schema = CartItemSchema()
cart_items_schema = CartItemSchema(many=True)
