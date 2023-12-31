"""add task history table

Revision ID: 2bb9a3061564
Revises: 9c4c00595d1c
Create Date: 2023-10-27 12:41:12.383039

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2bb9a3061564'
down_revision: Union[str, None] = '9c4c00595d1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('previous_assignee_id', sa.Integer(), nullable=False),
    sa.Column('new_assignee_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['new_assignee_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['previous_assignee_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task_history')
    # ### end Alembic commands ###
