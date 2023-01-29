"""add two more column posts table

Revision ID: 142ae5c141c7
Revises: 818c9bf79c36
Create Date: 2023-01-29 21:49:26.981687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "142ae5c141c7"
down_revision = "818c9bf79c36"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_defualt="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_defualt=sa.text("NOW()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
