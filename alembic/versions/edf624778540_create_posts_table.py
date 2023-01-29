"""create posts table

Revision ID: edf624778540
Revises: 
Create Date: 2023-01-28 23:03:43.192871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "edf624778540"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade() -> None:
    pass
