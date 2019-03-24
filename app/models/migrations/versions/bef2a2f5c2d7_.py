"""empty message

Revision ID: bef2a2f5c2d7
Revises: af5ab168f3c7
Create Date: 2019-03-24 22:53:20.520798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bef2a2f5c2d7'
down_revision = 'af5ab168f3c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('schedule', 'periodicity_type',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'schedule', 'periodicity_type', ['periodicity_type'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'schedule', type_='foreignkey')
    op.alter_column('schedule', 'periodicity_type',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
