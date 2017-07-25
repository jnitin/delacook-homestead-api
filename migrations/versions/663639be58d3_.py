"""empty message

Revision ID: 663639be58d3
Revises: cbf8d26e3258
Create Date: 2017-07-22 11:39:44.579548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '663639be58d3'
down_revision = 'cbf8d26e3258'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plantingphysicalsources',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('enum', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plantlineages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plant_fk', sa.Integer(), nullable=True),
    sa.Column('planting_physical_source_fk', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('is_dead', sa.Boolean(), nullable=True),
    sa.Column('lineage_source', sa.String(), nullable=True),
    sa.Column('date_lineage_started', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['plant_fk'], ['plants.id'], ),
    sa.ForeignKeyConstraint(['planting_physical_source_fk'], ['plantingphysicalsources.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plantlineages')
    op.drop_table('plantingphysicalsources')
    # ### end Alembic commands ###