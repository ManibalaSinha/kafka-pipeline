"""test migration

Revision ID: 375abd2e3df6
Revises: 53ab38f59a03
Create Date: 2026-06-29 11:09:00.104220

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '375abd2e3df6'
down_revision: Union[str, None] = '53ab38f59a03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
