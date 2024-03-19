"""renaming birthday to date_of_birth

Revision ID: 95294b0f6857
Revises: 8d9c19db1e67
Create Date: 2023-05-22 15:52:49.064271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95294b0f6857'
down_revision = '8d9c19db1e67'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars','birthday', new_column_name='date_of_birth', nullable=None)


def downgrade() -> None:
    op.alter_column('scholars', 'date_of_birth', new_column_name='birthday', nullable=None)
