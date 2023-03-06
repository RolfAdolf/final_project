from fastapi import FastAPI
from src.utils.docs import app_docs

app = FastAPI(
    title=app_docs.title,
    description=app_docs.description,
    version=app_docs.version,
    openapi_tags=app_docs.tags_dict
)
