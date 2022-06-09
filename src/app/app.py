from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

tags_metadata = [
    {
        'name': 'app',
        'description': 'API к микросервису Partner',
    },
]

app = FastAPI(
    title='Partner',
    description='Микросервис Partner',
    version='0.0.2',
    openapi_tags=tags_metadata,
    redoc_url=None,
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router)
