"""empty message

Revision ID: 5fd52ac14804
Revises: 4bc2902acdde
Create Date: 2021-07-05 21:30:08.277409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fd52ac14804'
down_revision = '4bc2902acdde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('uid', sa.String(), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('_id', sa.String(), nullable=False),
    sa.Column('_v', sa.String(), nullable=False),
    sa.Column('result', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('species',
    sa.Column('uid', sa.String(), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('_id', sa.String(), nullable=False),
    sa.Column('_v', sa.String(), nullable=False),
    sa.Column('result', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('starships',
    sa.Column('uid', sa.String(), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('_id', sa.String(), nullable=False),
    sa.Column('_v', sa.String(), nullable=False),
    sa.Column('result', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('vehicles',
    sa.Column('uid', sa.String(), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('_id', sa.String(), nullable=False),
    sa.Column('_v', sa.String(), nullable=False),
    sa.Column('result', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('uid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicles')
    op.drop_table('starships')
    op.drop_table('species')
    op.drop_table('planets')
    # ### end Alembic commands ###
