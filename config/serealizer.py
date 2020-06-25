from flask_marshmallow import Marshmallow
from config.model import Produto, Carrinho
ma= Marshmallow()

def configure(app):
    ma.init_app(app)

class ProdutoSchema(ma.ModelSchema):
    class Meta:
        model= Produto

class CarrinhoSchema(ma.ModelSchema):
    class Meta:
        model= Carrinho

class PedidoSchema(ma.ModelSchema):
    class Meta:
        model = Carrinho