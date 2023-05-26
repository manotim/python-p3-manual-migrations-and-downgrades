"""Renaming students to scholars

Revision ID: 0d76f347adea
Revises: 791279dd0760
Create Date: 2023-05-26 23:49:17.240209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d76f347adea'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')

def downgrade() -> None:
    op.rename_table('scholars', 'students')
