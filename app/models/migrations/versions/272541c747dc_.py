"""empty message

Revision ID: 272541c747dc
Revises: 74f6b711d381
Create Date: 2019-03-24 22:41:52.434641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '272541c747dc'
down_revision = '74f6b711d381'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('periodicity_type', sa.Integer(), nullable=False),
    sa.Column('run_time', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('run_time')
    )
    op.create_table('scenario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('run_count', sa.Integer(), nullable=False),
    sa.Column('frequency', sa.Integer(), nullable=True),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.Column('schedule', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['users.id'], ),
    sa.ForeignKeyConstraint(['schedule'], ['schedule.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scenario')
    op.drop_table('schedule')
    # ### end Alembic commands ###
