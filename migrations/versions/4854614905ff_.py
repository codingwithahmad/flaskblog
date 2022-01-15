"""empty message

Revision ID: 4854614905ff
Revises: ebe2523c6e81
Create Date: 2022-01-13 21:27:15.370438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4854614905ff'
down_revision = 'ebe2523c6e81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts_categories',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='cascade')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts_categories')
    # ### end Alembic commands ###