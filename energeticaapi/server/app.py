from fastapi import FastAPI
from server.routers.contracts import router as ContractsRouter
from server.routers.users import router as UsersRouter

tags_metadata = [{
    "name": "contracts",
    "description": "Operations with electricity supply contracts.",
}, {
    "name": "users",
    "description": "Operations with Energética coop.'s users.",
}]


app = FastAPI(
    title="Energética API",
    description="API for Energética coop.'s cooperatives, users and contracts management.",
    version="0.1", openapi_tags=tags_metadata
)

app.include_router(ContractsRouter)
app.include_router(UsersRouter)
