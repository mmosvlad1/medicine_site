"""Remove category

Revision ID: 285798e82ee5
Revises: 9fc4a1e42152
Create Date: 2023-12-03 11:13:28.181774

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '285798e82ee5'
down_revision: Union[str, None] = '9fc4a1e42152'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category')
    op.drop_constraint(None, 'medicine', type_='foreignkey')
    op.drop_column('medicine', 'category_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('medicine', sa.Column('category_id', sa.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'medicine', 'category', ['category_id'], ['id'])
    op.create_table('category',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###