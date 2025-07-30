"""create users

Revision ID: 59614516552e
Revises: 
Create Date: 2025-07-30 17:41:07.630280

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

revision: str = '59614516552e'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('token', sa.UUID(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_token'), 'users', ['token'], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_users_token'), table_name='users')
    op.drop_table('users')
