"""add new column to medicine table

Revision ID: 9fc4a1e42152
Revises: dd428725bdde
Create Date: 2023-12-02 19:27:41.390619

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9fc4a1e42152'
down_revision: Union[str, None] = 'dd428725bdde'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('medicine', sa.Column('description', sa.String(length=500), nullable=False))


def downgrade() -> None:
    op.drop_column('medicine', 'description')
