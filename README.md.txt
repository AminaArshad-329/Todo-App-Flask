First create  virtual enviornment,activate and then apply these steps
Step 1: Install Flask==2.2.2
Step 2: flask-marshmallow==0.14.0
Step 3: Flask-RESTful==0.3.9
Step 4: Flask-SQLAlchemy==3.0.2
Step 5: marshmallow==3.19.0
Step 6: marshmallow-sqlalchemy==0.28.1
Step 7 : Flask-HTTPAuth==4.7.0

These are basics pakages which we shoud install and for more pakages you can see requirements.txt file.

In this project there is 5 endpoints
* create_product (for creating product objects)
* all_products (geting all products queryset)
* single_product/id  (which is used for geting single product)
* update_product/id (which is used for update product)
* delete_product/id (which is used for delete product)