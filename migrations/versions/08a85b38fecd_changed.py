"""changed

Revision ID: 08a85b38fecd
Revises: 5b418a0c89d5
Create Date: 2022-05-04 13:01:11.258180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08a85b38fecd'
down_revision = '5b418a0c89d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('color', sa.String(), nullable=True))
    op.drop_column('planet', 'distance_from_earth')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('distance_from_earth', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('planet', 'color')
    # ### end Alembic commands ###
