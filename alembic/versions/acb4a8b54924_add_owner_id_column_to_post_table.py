"""add owner_id column to post table

Revision ID: acb4a8b54924
Revises: 62a8d1a46470
Create Date: 2025-10-08 10:18:44.591381

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'acb4a8b54924'
down_revision: Union[str, Sequence[str], None] = '62a8d1a46470'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('post_users_fk', 'posts', type_='foreignkey')
    op.drop_column('posts', 'owner_id')
