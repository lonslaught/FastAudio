"""update users

Revision ID: 50fe47749231
Revises: 59614516552e
Create Date: 2025-07-30 17:50:37.433688

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

revision: str = '50fe47749231'
down_revision: Union[str, Sequence[str], None] = '59614516552e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'created_at')
