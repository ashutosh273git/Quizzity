from fastapi import APIRouter

from app.api.routes import (
    attempts,
    documents,
    health,
    quizzes,
)


api_router = APIRouter(prefix="/api")


api_router.include_router(
    health.router,
    prefix="/health",
    tags=["Health"],
)


api_router.include_router(
    documents.router,
    prefix="/documents",
    tags=["Documents"],
)


api_router.include_router(
    quizzes.router,
    prefix="/quizzes",
    tags=["Quizzes"],
)


api_router.include_router(
    attempts.router,
    prefix="/attempts",
    tags=["Attempts"],
)