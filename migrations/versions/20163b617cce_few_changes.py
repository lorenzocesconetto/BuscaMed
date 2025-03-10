"""few changes

Revision ID: 20163b617cce
Revises: c9e0fe94b252
Create Date: 2021-01-18 14:53:43.644542

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '20163b617cce'
down_revision = 'c9e0fe94b252'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('searches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('search', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('item', 'timestamp',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('item', 'timestamp',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_table('searches')
    # ### end Alembic commands ###
