from fastapi import FastAPI
from app.database import engine, Base
from app.api.products import router as product_router
from app.api.purchases import router as purchase_router
from app.api.sales import router as sales_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Dokonchi_bola")

app.include_router(product_router)
app.include_router(purchase_router)
app.include_router(sales_router)


@app.get("/")
def home():
    return {"message": "Dokonchi_bola backend ishlayapti 🚀"}
