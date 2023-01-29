"""add user table

Revision ID: 293be550334d
Revises: 28cfc8e070f9
Create Date: 2023-01-28 23:24:06.654270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "293be550334d"
down_revision = "28cfc8e070f9"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )

    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
