"""Create models

Revision ID: fdeb79d83c4a
Revises: 
Create Date: 2022-02-22 14:57:45.040643

"""
from alembic import op
import sqlalchemy as sa

from db.models import ProductModel

# revision identifiers, used by Alembic.
revision = 'fdeb79d83c4a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('unique_code', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('unique_code')
    )
    op.create_table('packages',
    sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
    sa.Column('cut_id', sa.String(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('lot_code', sa.Integer(), nullable=False),
    sa.Column('is_validated', sa.Boolean(), nullable=False),
    sa.Column('product_code', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_code'], ['products.unique_code'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cut_id')
    )
    # ### end Alembic commands ###

    seed()


def seed():
    op.bulk_insert(ProductModel.__table__,
        [
            {'id': 1, 'name': 'Chicken Legs', 'unique_code': '13242'},
            {'id': 2, 'name': 'Chicken Breast', 'unique_code': '13247'},
            {'id': 3, 'name': 'Chicken Whole', 'unique_code': '13249'},
        ]
    )
