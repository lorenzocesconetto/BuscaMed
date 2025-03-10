"""Store table

Revision ID: 607f62803f7f
Revises: 54585a88e1ba
Create Date: 2020-12-17 16:40:39.765958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '607f62803f7f'
down_revision = '54585a88e1ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('store',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('address', sa.String(length=256), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('is_ecommerce', sa.Boolean(), nullable=False),
    sa.Column('phone', sa.String(length=19), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('item', sa.Column('store_id', sa.Integer(), nullable=True))
    op.drop_constraint('_ean_store_uc', 'item', type_='unique')
    op.drop_constraint('_sku_store_uc', 'item', type_='unique')
    op.drop_index('ix_item_store', table_name='item')
    op.create_foreign_key(None, 'item', 'store', ['store_id'], ['id'])
    op.drop_column('item', 'store')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('store', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'item', type_='foreignkey')
    op.create_index('ix_item_store', 'item', ['store'], unique=False)
    op.create_unique_constraint('_sku_store_uc', 'item', ['sku', 'store'])
    op.create_unique_constraint('_ean_store_uc', 'item', ['ean', 'store'])
    op.drop_column('item', 'store_id')
    op.drop_table('store')
    # ### end Alembic commands ###
