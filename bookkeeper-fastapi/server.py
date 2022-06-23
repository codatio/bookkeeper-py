from fastapi import FastAPI
from pydantic import BaseModel


class Invoice(BaseModel):
    pass


app = FastAPI()


@app.post("/invoices/")
async def create_item(item: Invoice):
    return item