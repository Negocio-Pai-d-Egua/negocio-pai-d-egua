"""empty message

Revision ID: 2e41e5088b37
Revises: 
Create Date: 2020-06-27 13:56:53.300870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e41e5088b37'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pedido',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('carrinho',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mesa', sa.Integer(), nullable=False),
    sa.Column('totalpreco', sa.String(length=200), nullable=False),
    sa.Column('pedido_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pedido_id'], ['pedido.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('produto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=200), nullable=False),
    sa.Column('preco', sa.String(length=200), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=200), nullable=False),
    sa.Column('carrinho_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['carrinho_id'], ['carrinho.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produto')
    op.drop_table('carrinho')
    op.drop_table('pedido')
    # ### end Alembic commands ###
