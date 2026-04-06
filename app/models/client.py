from pydantic import BaseModel

class Client(BaseModel):
  id: int | None
  name: str
  email: str
  phone: str

class CreateAndUpdateClient(BaseModel):
  name: str
  email: str
  phone: str