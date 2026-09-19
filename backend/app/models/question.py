import uuid

from sqlalchemy import String, Text, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    quiz_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("quizzes.id", ondelete="CASCADE"),
        nullable=False,
    )

    question_text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    option_a: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    option_b: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    option_c: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    option_d: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    correct_answer: Mapped[str] = mapped_column(
        String(1),
        nullable=False,
    )

    explanation: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    marks: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )