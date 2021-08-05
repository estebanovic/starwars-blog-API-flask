"""empty message

Revision ID: ce26645c5687
Revises: 34959801c997
Create Date: 2021-08-05 01:43:34.385257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce26645c5687'
down_revision = '34959801c997'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(), nullable=False))
    op.drop_column('users', 'mail')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('mail', sa.VARCHAR(), nullable=False))
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
