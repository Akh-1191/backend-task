from flask import Flask, request, jsonify
from models import Product
from database import initialize_database
from flask_peewee.utils import model_to_dict
import logging
from peewee import DatabaseError


app = Flask(__name__)
logging.basicConfig(filename='error.log', level=logging.ERROR)


initialize_database()


@app.route('/products', methods=['GET'])
def get_products():
    try:
       
        limit = request.args.get('limit', default=10, type=int)
        page = request.args.get('page', default=1, type=int)
        
       
        offset = (page - 1) * limit

       
        products = Product.select().offset(offset).limit(limit)

       
        products_json = []
        for product in products:
            product_dict = model_to_dict(product)
            
            product_dict['id'] = str(product_dict['id'])
            products_json.append(product_dict)

       
        total_count = Product.select().count()
        total_pages = (total_count + limit - 1) // limit
        metadata = {
            'total_count': total_count,
            'total_pages': total_pages,
            'page': page,
            'limit': limit
        }

        return jsonify({'metadata': metadata, 'products': products_json}), 200
    except DatabaseError as e:
        logging.error(f"Database error while retrieving products: {str(e)}")
        return jsonify({'error': 'Database error occurred'}), 500
    except Exception as e:
        logging.error(f"Error retrieving products: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

# Endpoint to retrieve a specific product by its UUID
@app.route('/products/<uuid:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = model_to_dict(Product.get(Product.id == product_id))
        return jsonify(product)
    except Product.DoesNotExist:
        return jsonify({'error': 'Product not found'}), 404
    except ValueError:
        return jsonify({'error': 'Invalid UUID format'}), 400
    except DatabaseError as e:
        logging.error(f"Database error while retrieving product: {str(e)}")
        return jsonify({'error': 'Database error occurred'}), 500
    except Exception as e:
        logging.error(f"Error retrieving product: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500



# Endpoint to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    try:
        if 'name' not in request.json or 'price' not in request.json or 'availability' not in request.json or 'stock_quantity' not in request.json:
            error_msg = "Missing mandatory fields: name, price, availability, stock_quantity"
            logging.error(error_msg)
            return jsonify({'error': error_msg}), 400

        new_product = Product.create(
            name=request.json.get('name'),
            description=request.json.get('description'),
            price=request.json.get('price'),
            category=request.json.get('category'),
            availability=request.json.get('availability'),
            stock_quantity=request.json.get('stock_quantity')
        )

        return jsonify(model_to_dict(new_product)), 201 
    except Exception as e:
        error_msg = f"Error creating product: {str(e)}"
        logging.error(error_msg)
        return jsonify({'error': error_msg}), 500

# Endpoint to update an existing product
@app.route('/products/<uuid:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        product = Product.get(Product.id == product_id)
        product.name = request.json.get('name')
        product.description = request.json.get('description')
        product.price = request.json.get('price')
        product.category = request.json.get('category')
        product.availability = request.json.get('availability')
        product.stock_quantity = request.json.get('stock_quantity')
        product.save()
        return jsonify(model_to_dict(product))
    except Product.DoesNotExist:
        return jsonify({'error': 'Product not found'}), 404
    except ValueError:
        return jsonify({'error': 'Invalid UUID format'}), 400
    except DatabaseError as e:
        logging.error(f"Database error while updating product: {str(e)}")
        return jsonify({'error': 'Database error occurred'}), 500
    except Exception as e:
        logging.error(f"Error updating product: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

# Endpoint to delete a product by its UUID
@app.route('/products/<uuid:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        product = Product.get(Product.id == product_id)
        product.delete_instance()
        return jsonify({'message': 'Product deleted'})
    except Product.DoesNotExist:
        return jsonify({'error': 'Product not found'}), 404
    except ValueError:
        return jsonify({'error': 'Invalid UUID format'}), 400
    except DatabaseError as e:
        logging.error(f"Database error while deleting product: {str(e)}")
        return jsonify({'error': 'Database error occurred'}), 500
    except Exception as e:
        logging.error(f"Error deleting product: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500


if __name__ == '__main__':
    app.run(debug=True)
