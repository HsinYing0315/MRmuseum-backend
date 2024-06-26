"""Adjust interaction with type(question, time) and content

Revision ID: 0c98429f2cef
Revises: e0c1bec3a3bc
Create Date: 2024-05-30 10:57:19.373162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c98429f2cef'
down_revision = 'e0c1bec3a3bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('interaction', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('content', sa.String(length=100), nullable=False))
        batch_op.drop_column('question')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('interaction', schema=None) as batch_op:
        batch_op.add_column(sa.Column('question', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
        batch_op.drop_column('content')
        batch_op.drop_column('type')

    # ### end Alembic commands ###
