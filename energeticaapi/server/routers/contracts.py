from fastapi import APIRouter
from server.models.schemas import *

router = APIRouter(
    prefix="/contracts",
    tags=["contracts"],
    responses={404: {"description": "Contract not found"}},
)


@router.get("/")
async def read_contract(skip: int = 0, limit: int = 10, ):
    return {"contract_id": contract_id}


@router.get("/{contract_id}")
async def read_contract(contract_id: int):
    return {"contract_id": contract_id}


@router.post("/")
async def create_contract(contract: Contract):
    return contract


@router.put("/{contract_id}")
async def update_contract(contract: Contract):
    return contract


@router.delete("/{contract_id}")
async def delete_contract(contract: Contract):
    return contract
