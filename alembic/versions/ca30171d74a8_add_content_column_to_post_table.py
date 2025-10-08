"""add content column to post table

Revision ID: ca30171d74a8
Revises: ed1da3e2645b
Create Date: 2025-10-08 10:07:49.851932

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca30171d74a8'
down_revision: Union[str, Sequence[str], None] = 'ed1da3e2645b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
