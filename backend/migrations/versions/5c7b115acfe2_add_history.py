"""add history

Revision ID: 5c7b115acfe2
Revises: 7a57838f1210
Create Date: 2023-12-13 15:11:43.603614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c7b115acfe2'
down_revision: Union[str, None] = '7a57838f1210'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('history',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('purchase_id', sa.Integer(), nullable=False),
                    sa.Column('purchase_date', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['purchase_id'], ['purchase.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('history')
