from fastapi import APIRouter

from app.models.client import Client

router = APIRouter(
  prefix="/clients"
)

CLIENT_LIST = [
    Client(nome="Eduardo",email="teste@gmail.com", phone="123456", id_=1),
    Client(nome="Raphaela",email="tesasde@gmail.com", phone="12345426", id_=2),
    Client(nome="Marcos",email="tesasde@gmail.com", phone="12345156", id_=3)
  ]


@router.get("/", response_model=list[Client])
async def list_clients():
  return CLIENT_LIST

@router.get("/{client_id}", response_model=Client | None)
async def get_client(client_id: int):
  for client in CLIENT_LIST:
    if client.id_ == client_id:
      return client
  
  return None


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