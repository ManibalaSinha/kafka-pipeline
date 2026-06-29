"""test

Revision ID: 33fab8d5277c
Revises: a7c68fc4a096
Create Date: 2026-06-29 12:11:45.030950

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33fab8d5277c'
down_revision: Union[str, None] = 'a7c68fc4a096'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
