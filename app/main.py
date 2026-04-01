from fastapi import FastAPI

from app.routes import client

app = FastAPI(
  title="Techlog Solutions API",
  description="CRM para Techlog Solutions",
  version="1.0.0",
)

app.include_router(client.router)

@app.get("/")
async def health_check():
  return {"status": "ok"}

@app.get("/front",)
async def front_page():
  return """"
  <html>
  </html>
  """