"""Renaming students to scholars

Revision ID: 8d9c19db1e67
Revises: 791279dd0760
Create Date: 2023-05-20 17:23:12.952897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d9c19db1e67'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
