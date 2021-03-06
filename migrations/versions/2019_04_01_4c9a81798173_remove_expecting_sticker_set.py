"""Remove expecting Sticker set

Revision ID: 4c9a81798173
Revises: b17dcce8c3f3
Create Date: 2019-04-01 11:03:29.828968

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4c9a81798173"
down_revision = "b17dcce8c3f3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("only_one_action_check", "chat")
    op.create_check_constraint(
        "only_one_action_check",
        "chat",
        """
        (tagging_random_sticker IS TRUE AND fix_single_sticker IS FALSE AND full_sticker_set IS FALSE) OR \
        (fix_single_sticker IS TRUE AND tagging_random_sticker IS FALSE AND full_sticker_set IS FALSE) OR \
        (full_sticker_set IS TRUE AND tagging_random_sticker IS FALSE AND fix_single_sticker IS FALSE) OR \
        (full_sticker_set IS FALSE AND tagging_random_sticker IS FALSE AND fix_single_sticker IS FALSE)
    """,
    )
    op.drop_column("chat", "expecting_sticker_set")
    op.alter_column(
        "sticker_usage", "usage_count", existing_type=sa.INTEGER(), nullable=True
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "sticker_usage", "usage_count", existing_type=sa.INTEGER(), nullable=False
    )
    op.add_column(
        "chat",
        sa.Column(
            "expecting_sticker_set", sa.BOOLEAN(), autoincrement=False, nullable=False
        ),
    )
    op.drop_constraint("only_one_action_check", "chat")
    op.create_check_constraint(
        "only_one_action_check",
        "chat",
        """
        (expecting_sticker_set IS TRUE AND tagging_random_sticker IS FALSE AND fix_single_sticker IS FALSE AND full_sticker_set IS FALSE) OR \
        (tagging_random_sticker IS TRUE AND expecting_sticker_set IS FALSE AND fix_single_sticker IS FALSE AND full_sticker_set IS FALSE) OR \
        (fix_single_sticker IS TRUE AND tagging_random_sticker IS FALSE AND expecting_sticker_set IS FALSE AND full_sticker_set IS FALSE) OR \
        (full_sticker_set IS TRUE AND tagging_random_sticker IS FALSE AND fix_single_sticker IS FALSE AND expecting_sticker_set IS FALSE) OR \
        (full_sticker_set IS FALSE AND tagging_random_sticker IS FALSE AND fix_single_sticker IS FALSE AND expecting_sticker_set IS FALSE)
    """,
    )

    # ### end Alembic commands ###
