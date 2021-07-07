"""empty message

Revision ID: 59c9adb16af6
Revises: 6063343782ba
Create Date: 2021-07-07 10:43:11.030905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59c9adb16af6'
down_revision = '6063343782ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('url', sa.String(), nullable=False))
    op.drop_column('people', 'ulr')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('ulr', sa.VARCHAR(), nullable=False))
    op.drop_column('people', 'url')
    # ### end Alembic commands ###