from fastapi import APIRouter

router=APIRouter(prefix="/sys_info")

@router.get("/health_check")
def health_check():
    return "server is up"