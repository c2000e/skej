"""Initial migration

Revision ID: 79586432f7f2
Revises: 
Create Date: 2020-07-07 18:22:12.018806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79586432f7f2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deadlines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('deadlines')
    # ### end Alembic commands ###
