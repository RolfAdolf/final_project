from fastapi import FastAPI

from src.utils.docs import app_docs
from src.api.base_router import router
from src.services.utils import test


app = FastAPI(
    title=app_docs.title,
    description=app_docs.description,
    version=app_docs.version,
    openapi_tags=app_docs.tags_dict,
)

app.include_router(router)


@app.on_event("startup")
def start():
    test.start()


@app.on_event("shutdown")
def stop():
    test.stop()
