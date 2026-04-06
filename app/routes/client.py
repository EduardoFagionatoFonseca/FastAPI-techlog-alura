from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.models.client import Client
from app.database.client_repo import ClientRepo
from app.dependencies import get_client_repo
router = APIRouter(
  prefix="/clients"
)

CLIENT_LIST = [
    Client(name="Eduardo",email="teste@gmail.com", phone="123456", id=1),
    Client(name="Raphaela",email="tesasde@gmail.com", phone="12345426", id=2),
    Client(name="Marcos",email="tesasde@gmail.com", phone="12345156", id=3)
  ]


@router.get("/", response_model=list[Client])
async def list_clients(client_repo: Annotated[ClientRepo, Depends(get_client_repo)]):
  return await client_repo.list_clients()

@router.get("/{client_id}", response_model=Client | None)
async def get_client(client_repo: Annotated[ClientRepo, Depends(get_client_repo)],
                     client_id: int):
  client = await client_repo.get_client(client_id=client_id)
  if not client:
    raise HTTPException(status_code=404, detail="Client not found")
  
  return client


@router.post("/create/")
async def create_client(client: Client):
  print(client)
  return {"message": "Item created"}
#   last_client_id = CLIENT_LIST[-1].id_
#   if not last_client_id:
#     last_client_id = 0
#   client = item
#   client.id_ = last_client_id + 1
#   return item