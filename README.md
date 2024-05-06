
# Setup

**• Clone Repository**

```bash
 git clone https://github.com/Akh-1191/backend-task.git
```

**• Create Virtual Enviornment**
```bash
python -m venv env
```

then activate it.

**• Install Requirements using**

```bash
pip install flask
pip install flask_peewee
```

##**Endpoints**  
Get All Products  
URL: /products  
Method: GET  
Description: Retrieves all products.  
Response:  
Status Code: 200 OK  
Body: Array of product objects  

**Get Product by ID**  
URL: /products/<product_id>  
Method: GET  
Description: Retrieves a specific product by its ID.  
Response:  
Status Code: 200 OK  
Body: Product object  
Example Request: /products/1  

**Create Product**  
URL: /products  
Method: POST  
Description: Creates a new product.  
Request Body:  
json  
```bash
{  
  "name": "Product Name",  
  "description": "Product Description",  
  "price": 29.99,  
  "category": "Electronics",  
  "availability": true,  
  "stock_quantity": 100  
}
```
Response:  
Status Code: 201 Created  
Body: Created product object  

**Update Product**  
URL: /products/<product_id>  
Method: PUT  
Description: Updates an existing product.  
Request Body:  
json
```bash
{
  "name": "New Product Name",  
  "description": "New Product Description",  
  "price": 39.99,  
  "category": "Electronics",  
  "availability": true,  
  "stock_quantity": 150  
}
```
Response:   
Status Code: 200 OK
Body: Updated product object
Example Request: /products/1

**Delete Product**  
URL: /products/<product_id>  
Method: DELETE  
Description: Deletes a product by its ID.  
Response:  
Status Code: 200 OK  
Body: Message indicating deletion success  
Example Request: /products/1  
    
