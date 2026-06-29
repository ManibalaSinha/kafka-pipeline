"""test

Revision ID: a7c68fc4a096
Revises: 375abd2e3df6
Create Date: 2026-06-29 11:31:14.850172

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7c68fc4a096'
down_revision: Union[str, None] = '375abd2e3df6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
