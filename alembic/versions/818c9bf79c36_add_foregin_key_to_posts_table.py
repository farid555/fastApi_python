"""add foregin key to posts table

Revision ID: 818c9bf79c36
Revises: 293be550334d
Create Date: 2023-01-29 21:32:29.590388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "818c9bf79c36"
down_revision = "293be550334d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_user_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
