# Product Inventory System

## Overview

The Product Inventory System is a RESTful API designed for managing product information. It provides endpoints to
retrieve, update, and search for products in a product inventory database.

## Features

- Retrieve details of a single product by its ID.
- Retrieve a list of all products with pagination support.
- Update the price and stock level of a product.
- Search for products based on name or price range.

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast, web framework for building APIs with Python 3.7+.
- [SQLAlchemy](https://www.sqlalchemy.org/): A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- [Redis](https://redis.io/): An in-memory data structure store used as a backend for FastAPILimiter.

## Installation

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set up your environment variables by creating a `.env` file. Example:

   ```env
   DATABASE_URL=your_database_url
   JWT_SECRET_KEY=your_jwt_secret_key
   ```

3. Install Redis on Ubuntu:

    ```bash
    # Update the package list
    sudo apt update
    
    # Install Redis
    sudo apt install redis-server
    
    # Start the Redis service
    sudo systemctl start redis
    
    # Enable Redis to start on system boot
    sudo systemctl enable redis
    
    # Verify that Redis is running
    redis-cli ping
    ```
    
## Usage

1. Run the application:

   ```bash
   uvicorn main:app --reload or python main.py
   ```

2. Access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   or [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) to interact with the endpoints.

## Endpoints

### Retrieving Product Information

#### a. Retrieve details of a single product by its ID

- **Endpoint:** `/products/{product_id}`
- **HTTP Method:** GET

#### b. Retrieve a list of all products with pagination support

- **Endpoint:** `/products/`
- **HTTP Method:** GET
- **Query Parameters:**
    - `skip`: Number of items to skip (default: 0)
    - `limit`: Number of items to retrieve (default: 10)

### Updating Product Information

#### a. Update the price and stock level of a product

- **Endpoint:** `/products/{product_id}`
- **HTTP Method:** PUT
- **Request Body:**
  ```json
  {
    "name": "Updated Product",
    "price": 19.99,
    "stock_level": 50
  }
  ```

### Searching for Products

#### a. Search for products based on name or price range

- **Endpoint:** `/search`
- **HTTP Method:** GET
- **Query Parameters:**
    - `name`: Search by product name (optional)
    - `min_price`: Minimum price for the search range (optional)
    - `max_price`: Maximum price for the search range (optional)

## Configuration

- `DATABASE_URL`: Database connection URL.
- `JWT_SECRET_KEY`: Secret key for JWT authentication.

