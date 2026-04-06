from typing import Annotated
from fastapi import Depends

from app.database.local import LocalDatabase
from app.database.client_repo import ClientRepo
database = LocalDatabase()

def get_database() -> LocalDatabase:
   return database

def get_client_repo(local_database: Annotated[LocalDatabase,
                                               Depends(get_database)]) -> ClientRepo:
   return ClientRepo(local_database)