from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return "Hello, please open the /docs for more detail."


@router.get("/ping")
async def ping():
    return {"message": "pong"}
