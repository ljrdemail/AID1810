"""empty message

Revision ID: e8f3e8c1481a
Revises: 
Create Date: 2019-01-31 15:54:53.527478

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e8f3e8c1481a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wife', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'wife', ['user_id'])
    op.create_foreign_key(None, 'wife', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'wife', type_='foreignkey')
    op.drop_constraint(None, 'wife', type_='unique')
    op.drop_column('wife', 'user_id')
    # ### end Alembic commands ###