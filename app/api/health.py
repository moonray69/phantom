from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("", summary="Check application health")
def health_check():
    return {"status": "ok", "service": "phantom"}


