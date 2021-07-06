"""empty message

Revision ID: 6063343782ba
Revises: 00cd06ff05ff
Create Date: 2021-07-06 16:17:37.852688

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = '6063343782ba'
down_revision = '00cd06ff05ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('films',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('_id', sa.String(), nullable=False),
    sa.Column('_v', sa.String(), nullable=False),
    sa.Column('producer', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('episode_id', sa.Integer(), nullable=False),
    sa.Column('director', sa.String(), nullable=False),
    sa.Column('release_date', sa.String(), nullable=False),
    sa.Column('opening_crawl', sa.String(), nullable=False),
    sa.Column('created', sa.DATE(), nullable=False),
    sa.Column('edited', sa.DATE(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ulr', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('uid')
    )
    op.add_column('planets', sa.Column('diameter', sa.Integer(), nullable=False))
    op.add_column('planets', sa.Column('rotation_period', sa.Integer(), nullable=False))
    op.add_column('planets', sa.Column('orbital_period', sa.Integer(), nullable=False))
    op.add_column('planets', sa.Column('gravity', sa.String(), nullable=False))
    op.add_column('planets', sa.Column('population', sa.Integer(), nullable=False))
    op.add_column('planets', sa.Column('climate', sa.String(), nullable=False))
    op.add_column('planets', sa.Column('terrain', sa.String(), nullable=False))
    op.add_column('planets', sa.Column('surface_water', sa.Integer(), nullable=False))
    op.add_column('planets', sa.Column('created', sa.DATE(), nullable=False))
    op.add_column('planets', sa.Column('edited', sa.DATE(), nullable=False))
    op.add_column('planets', sa.Column('name', sa.String(), nullable=False))
    op.add_column('planets', sa.Column('ulr', sa.String(), nullable=False))
    op.drop_column('planets', 'result')
    op.add_column('species', sa.Column('classification', sa.String(), nullable=False))
    op.add_column('species', sa.Column('designation', sa.String(), nullable=False))
    op.add_column('species', sa.Column('average_height', sa.Integer(), nullable=False))
    op.add_column('species', sa.Column('average_lifespan', sa.String(), nullable=False))
    op.add_column('species', sa.Column('hair_color', sa.String(), nullable=False))
    op.add_column('species', sa.Column('skin_color', sa.String(), nullable=False))
    op.add_column('species', sa.Column('eye_color', sa.String(), nullable=False))
    op.add_column('species', sa.Column('lenguaje', sa.String(), nullable=False))
    op.add_column('species', sa.Column('created', sa.DATE(), nullable=False))
    op.add_column('species', sa.Column('edited', sa.DATE(), nullable=False))
    op.add_column('species', sa.Column('name', sa.String(), nullable=False))
    op.add_column('species', sa.Column('ulr', sa.String(), nullable=False))
    op.drop_column('species', 'result')
    op.add_column('starships', sa.Column('model', sa.String(), nullable=False))
    op.add_column('starships', sa.Column('starship_class', sa.String(), nullable=False))
    op.add_column('starships', sa.Column('manufacturer', sa.String(), nullable=False))
    op.add_column('starships', sa.Column('cost_in_credits', sa.String(), nullable=False))
    op.add_column('starships', sa.Column('length', sa.String(), nullable=False))
    op.add_column('starships', sa.Column('crew', sa.String(), nullable=False))
    op.add_column('starships', sa.Column('passengers', sa.String(), nullable=False))
    op.add_column('starships', sa.Column('max_atmosphering_speed', sa.String(), nullable=False))
    op.add_column('starships', sa.Column('hyperdrive_rating', sa.String(), nullable=False))
    op.add_column('starships', sa.Column('MGLT', sa.String(), nullable=False))
    op.add_column('starships', sa.Column('cargo_capacity', sa.String(), nullable=False))
    op.add_column('starships', sa.Column('consumables', sa.String(), nullable=False))
    op.add_column('starships', sa.Column('created', sa.DATE(), nullable=False))
    op.add_column('starships', sa.Column('edited', sa.DATE(), nullable=False))
    op.add_column('starships', sa.Column('name', sa.String(), nullable=False))
    op.add_column('starships', sa.Column('ulr', sa.String(), nullable=False))
    op.drop_column('starships', 'result')
    op.add_column('vehicles', sa.Column('model', sa.String(), nullable=False))
    op.add_column('vehicles', sa.Column('vehicle_class', sa.String(), nullable=False))
    op.add_column('vehicles', sa.Column('manufacturer', sa.String(), nullable=False))
    op.add_column('vehicles', sa.Column('cost_in_credits', sa.String(), nullable=False))
    op.add_column('vehicles', sa.Column('length', sa.String(), nullable=False))
    op.add_column('vehicles', sa.Column('crew', sa.String(), nullable=False))
    op.add_column('vehicles', sa.Column('passengers', sa.String(), nullable=False))
    op.add_column('vehicles', sa.Column('max_atmosphering_speed', sa.String(), nullable=False))
    op.add_column('vehicles', sa.Column('cargo_capacity', sa.String(), nullable=False))
    op.add_column('vehicles', sa.Column('consumables', sa.String(), nullable=False))
    op.add_column('vehicles', sa.Column('created', sa.DATE(), nullable=False))
    op.add_column('vehicles', sa.Column('edited', sa.DATE(), nullable=False))
    op.add_column('vehicles', sa.Column('name', sa.String(), nullable=False))
    op.add_column('vehicles', sa.Column('ulr', sa.String(), nullable=False))
    op.drop_column('vehicles', 'result')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vehicles', sa.Column('result', sqlite.JSON(), nullable=False))
    op.drop_column('vehicles', 'ulr')
    op.drop_column('vehicles', 'name')
    op.drop_column('vehicles', 'edited')
    op.drop_column('vehicles', 'created')
    op.drop_column('vehicles', 'consumables')
    op.drop_column('vehicles', 'cargo_capacity')
    op.drop_column('vehicles', 'max_atmosphering_speed')
    op.drop_column('vehicles', 'passengers')
    op.drop_column('vehicles', 'crew')
    op.drop_column('vehicles', 'length')
    op.drop_column('vehicles', 'cost_in_credits')
    op.drop_column('vehicles', 'manufacturer')
    op.drop_column('vehicles', 'vehicle_class')
    op.drop_column('vehicles', 'model')
    op.add_column('starships', sa.Column('result', sqlite.JSON(), nullable=False))
    op.drop_column('starships', 'ulr')
    op.drop_column('starships', 'name')
    op.drop_column('starships', 'edited')
    op.drop_column('starships', 'created')
    op.drop_column('starships', 'consumables')
    op.drop_column('starships', 'cargo_capacity')
    op.drop_column('starships', 'MGLT')
    op.drop_column('starships', 'hyperdrive_rating')
    op.drop_column('starships', 'max_atmosphering_speed')
    op.drop_column('starships', 'passengers')
    op.drop_column('starships', 'crew')
    op.drop_column('starships', 'length')
    op.drop_column('starships', 'cost_in_credits')
    op.drop_column('starships', 'manufacturer')
    op.drop_column('starships', 'starship_class')
    op.drop_column('starships', 'model')
    op.add_column('species', sa.Column('result', sqlite.JSON(), nullable=False))
    op.drop_column('species', 'ulr')
    op.drop_column('species', 'name')
    op.drop_column('species', 'edited')
    op.drop_column('species', 'created')
    op.drop_column('species', 'lenguaje')
    op.drop_column('species', 'eye_color')
    op.drop_column('species', 'skin_color')
    op.drop_column('species', 'hair_color')
    op.drop_column('species', 'average_lifespan')
    op.drop_column('species', 'average_height')
    op.drop_column('species', 'designation')
    op.drop_column('species', 'classification')
    op.add_column('planets', sa.Column('result', sqlite.JSON(), nullable=False))
    op.drop_column('planets', 'ulr')
    op.drop_column('planets', 'name')
    op.drop_column('planets', 'edited')
    op.drop_column('planets', 'created')
    op.drop_column('planets', 'surface_water')
    op.drop_column('planets', 'terrain')
    op.drop_column('planets', 'climate')
    op.drop_column('planets', 'population')
    op.drop_column('planets', 'gravity')
    op.drop_column('planets', 'orbital_period')
    op.drop_column('planets', 'rotation_period')
    op.drop_column('planets', 'diameter')
    op.drop_table('films')
    # ### end Alembic commands ###