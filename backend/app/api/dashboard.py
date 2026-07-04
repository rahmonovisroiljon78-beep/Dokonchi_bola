from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.product import Product

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_dashboard(db: Session = Depends(get_db)):

    products = db.query(Product).all()

    total_products = len(products)
    low_stock = len([p for p in products if p.quantity < 5])

    total_stock_value = sum(p.quantity * p.sale_price for p in products)
    purchase_value = sum(p.quantity * p.purchase_price for p in products)
    profit = total_stock_value - purchase_value

    return {
        "total_products": total_products,
        "low_stock_products": low_stock,
        "stock_value": total_stock_value,
        "estimated_profit": profit
    }
