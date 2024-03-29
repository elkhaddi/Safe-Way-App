"""empty message

Revision ID: 391aae5aaadc
Revises: b74b6bc642af
Create Date: 2022-05-31 09:04:05.822366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '391aae5aaadc'
down_revision = 'b74b6bc642af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('declare',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('localisation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('long', sa.Float(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('localisation')
    op.drop_table('declare')
    # ### end Alembic commands ###
