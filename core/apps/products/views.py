from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_cache.decorator import cache
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session
from core.apps.products.models import Product
from core.apps.products.schemas import ProductCreate, ProductResponse, ProductUpdate
from core.database import get_db

router = APIRouter(
    prefix="",
    tags=['Products']
)


@router.post("/products/", response_model=ProductResponse)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Create a new product.

    Args:
        product (ProductCreate): The product data.
        db (Session): Database session.

    Returns:
        ProductResponse: The created product.
    """
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.get("/products/{product_id}", response_model=ProductResponse,
            dependencies=[Depends(RateLimiter(times=2, minutes=5))])
# @cache(expire=60)
async def read_product(product_id: int, db: Session = Depends(get_db)):
    """
    Retrieve details of a single product by its ID.

    Args:
        product_id (int): The ID of the product.
        db (Session): Database session.

    Returns:
        ProductResponse: The product details.
    """
    product = db.query(Product).get(product_id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


@router.get("/products/", response_model=List[ProductResponse])
async def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of all products with pagination support.

    Args:
        skip (int): Number of items to skip.
        limit (int): Number of items to retrieve.
        db (Session): Database session.

    Returns:
        List[ProductResponse]: List of products.
    """
    return db.query(Product).offset(skip).limit(limit).all()


@router.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, product_data: ProductUpdate, db: Session = Depends(get_db)):
    """
    Update the price and stock level of a product.

    Args:
        product_id (int): The ID of the product to update.
        product (ProductUpdate): The updated product data
        db (Session): Database session.

    Returns:
        ProductResponse: The updated product details.
        :param product_id:
        :param product_data:
    """

    product = db.query(Product).get(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in product_data.dict().items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product
