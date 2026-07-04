from fastapi import FastAPI
from app.database import engine, Base
from app.api.products import router as product_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Dokonchi_bola")

app.include_router(product_router)


@app.get("/")
def home():
    return {"message": "Dokonchi_bola backend ishlayapti 🚀"}
