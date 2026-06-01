# API Testing Examples

# Use these curl commands to test the API

## Health Check

curl -X GET http://localhost:8000/health

## Dashboard Statistics

curl -X GET http://localhost:8000/orders/stats/dashboard

### PRODUCTS API

## Get all products

curl -X GET "http://localhost:8000/products?skip=0&limit=100"

## Get specific product

curl -X GET http://localhost:8000/products/1

## Create product

curl -X POST http://localhost:8000/products \
 -H "Content-Type: application/json" \
 -d '{
"name": "Laptop",
"sku": "SKU-LAPTOP-001",
"price": 999.99,
"stock_quantity": 10
}'

## Update product (update price)

curl -X PUT http://localhost:8000/products/1 \
 -H "Content-Type: application/json" \
 -d '{
"price": 899.99
}'

## Delete product

curl -X DELETE http://localhost:8000/products/1

### CUSTOMERS API

## Get all customers

curl -X GET "http://localhost:8000/customers?skip=0&limit=100"

## Get specific customer

curl -X GET http://localhost:8000/customers/1

## Create customer

curl -X POST http://localhost:8000/customers \
 -H "Content-Type: application/json" \
 -d '{
"name": "John Doe",
"email": "john@example.com",
"phone": "+1-555-0000"
}'

## Update customer

curl -X PUT http://localhost:8000/customers/1 \
 -H "Content-Type: application/json" \
 -d '{
"phone": "+1-555-1234"
}'

## Delete customer

curl -X DELETE http://localhost:8000/customers/1

### ORDERS API

## Get all orders

curl -X GET "http://localhost:8000/orders?skip=0&limit=100"

## Get specific order

curl -X GET http://localhost:8000/orders/1

## Create order

curl -X POST http://localhost:8000/orders \
 -H "Content-Type: application/json" \
 -d '{
"customer_id": 1,
"items": [
{
"product_id": 1,
"quantity": 2
},
{
"product_id": 2,
"quantity": 1
}
]
}'

### ERROR CASES

## Create order with insufficient stock

curl -X POST http://localhost:8000/orders \
 -H "Content-Type: application/json" \
 -d '{
"customer_id": 1,
"items": [
{
"product_id": 1,
"quantity": 1000
}
]
}'

## Create customer with duplicate email

curl -X POST http://localhost:8000/customers \
 -H "Content-Type: application/json" \
 -d '{
"name": "Jane Doe",
"email": "john@example.com",
"phone": "+1-555-0000"
}'

## Create product with duplicate SKU

curl -X POST http://localhost:8000/products \
 -H "Content-Type: application/json" \
 -d '{
"name": "Another Laptop",
"sku": "SKU-LAPTOP-001",
"price": 799.99,
"stock_quantity": 5
}'
