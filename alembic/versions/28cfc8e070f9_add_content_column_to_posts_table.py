"""add content column to posts table

Revision ID: 28cfc8e070f9
Revises: edf624778540
Create Date: 2023-01-28 23:17:03.866736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "28cfc8e070f9"
down_revision = "edf624778540"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))

    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
