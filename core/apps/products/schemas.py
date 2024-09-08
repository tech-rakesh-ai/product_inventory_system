from pydantic import BaseModel, field_validator


class BaseProduct(BaseModel):
    name: str
    price: float
    stock_level: int


class ProductCreate(BaseProduct):

    @field_validator('name')
    def validate_name(cls, v):
        if not v or len(v) < 3:
            raise ValueError("Product name must be at least 3 characters long.")
        return v

    @field_validator('price')
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError("Price must be positive.")
        return v

    @field_validator('stock_level')
    def validate_stock_level(cls, v):
        if v < 0:
            raise ValueError("Stock level cannot be negative.")
        return v


class ProductUpdate(BaseModel):
    price: float
    stock_level: int


class ProductResponse(BaseProduct):
    id: int

    class Config:
        from_attributes = True
