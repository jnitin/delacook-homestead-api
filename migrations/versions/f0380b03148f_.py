"""empty message

Revision ID: f0380b03148f
Revises: 74ba324c02bb
Create Date: 2017-07-23 15:21:58.856885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0380b03148f'
down_revision = '74ba324c02bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plantlineagegenerations', sa.Column('generation_slot', sa.Integer(), nullable=False))
    op.drop_constraint('plantlineagegenerations_plant_previous_generation_fk_fkey', 'plantlineagegenerations', type_='foreignkey')
    op.drop_column('plantlineagegenerations', 'plant_previous_generation_fk')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plantlineagegenerations', sa.Column('plant_previous_generation_fk', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('plantlineagegenerations_plant_previous_generation_fk_fkey', 'plantlineagegenerations', 'plantgenerations', ['plant_previous_generation_fk'], ['id'])
    op.drop_column('plantlineagegenerations', 'generation_slot')
    # ### end Alembic commands ###
