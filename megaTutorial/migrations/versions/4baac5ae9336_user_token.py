"""user token

Revision ID: 4baac5ae9336
Revises: 06304b541f5a
Create Date: 2020-04-20 17:56:15.832328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4baac5ae9336'
down_revision = '06304b541f5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token', sa.String(length=32), nullable=True))
    op.add_column('user', sa.Column('token_expiration', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_column('user', 'token_expiration')
    op.drop_column('user', 'token')
    # ### end Alembic commands ###
