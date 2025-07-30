"""create audios

Revision ID: 96feea1e37e7
Revises: 50fe47749231
Create Date: 2025-07-30 21:46:40.819108

"""
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision: str = '96feea1e37e7'
down_revision: Union[str, Sequence[str], None] = '50fe47749231'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('audios',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('data', postgresql.BYTEA(), nullable=False),
    sa.Column('filename', sa.String(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('audios')
