"""empty message

Revision ID: 61c9db884c97
Revises: e34b18657776
Create Date: 2017-07-04 18:41:32.654173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61c9db884c97'
down_revision = 'e34b18657776'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leafcycles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('enum', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lifespans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('enum', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('enum', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('woodtypes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('enum', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('friendly_name', sa.String(), nullable=False),
    sa.Column('latin_name', sa.String(), nullable=True),
    sa.Column('drought_tolerant', sa.Boolean(), nullable=True),
    sa.Column('medicinal', sa.Boolean(), nullable=True),
    sa.Column('edible', sa.Boolean(), nullable=True),
    sa.Column('image_large', sa.String(), nullable=True),
    sa.Column('image_small', sa.String(), nullable=True),
    sa.Column('type_fk', sa.Integer(), nullable=True),
    sa.Column('lifespan_fk', sa.Integer(), nullable=True),
    sa.Column('wood_type_fk', sa.Integer(), nullable=True),
    sa.Column('leaf_cycle_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['leaf_cycle_fk'], ['leafcycles.id'], ),
    sa.ForeignKeyConstraint(['lifespan_fk'], ['lifespans.id'], ),
    sa.ForeignKeyConstraint(['type_fk'], ['types.id'], ),
    sa.ForeignKeyConstraint(['wood_type_fk'], ['woodtypes.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('latin_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plants')
    op.drop_table('woodtypes')
    op.drop_table('types')
    op.drop_table('lifespans')
    op.drop_table('leafcycles')
    # ### end Alembic commands ###
