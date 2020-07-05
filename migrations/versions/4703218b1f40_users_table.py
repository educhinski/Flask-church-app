"""Users table

Revision ID: 4703218b1f40
Revises: 
Create Date: 2020-07-06 00:31:58.844039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4703218b1f40'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=124), nullable=True),
    sa.Column('firstname', sa.String(length=124), nullable=True),
    sa.Column('lastname', sa.String(length=124), nullable=True),
    sa.Column('email', sa.String(length=124), nullable=True),
    sa.Column('about_me', sa.String(length=150), nullable=True),
    sa.Column('avatar', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_firstname'), 'user', ['firstname'], unique=False)
    op.create_index(op.f('ix_user_lastname'), 'user', ['lastname'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_lastname'), table_name='user')
    op.drop_index(op.f('ix_user_firstname'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
