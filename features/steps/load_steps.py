<<<<<<< HEAD
######################################################################
# Copyright 2016, 2023 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
######################################################################

"""
Product Steps

Steps file for products.feature

For information on Waiting until elements are present in the HTML see:
    https://selenium-python.readthedocs.io/waits.html
"""
import requests
from behave import given

# HTTP Return Codes
=======
import requests
from behave import given

>>>>>>> 59ad4ca (Initial commit)
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_204_NO_CONTENT = 204

@given('the following products')
def step_impl(context):
    """ Delete all Products and load new ones """
<<<<<<< HEAD
    #
    # List all of the products and delete them one by one
    #
=======

>>>>>>> 59ad4ca (Initial commit)
    rest_endpoint = f"{context.base_url}/products"
    context.resp = requests.get(rest_endpoint)
    assert(context.resp.status_code == HTTP_200_OK)
    for product in context.resp.json():
        context.resp = requests.delete(f"{rest_endpoint}/{product['id']}")
        assert(context.resp.status_code == HTTP_204_NO_CONTENT)

<<<<<<< HEAD
    #
    # load the database with new products
    #
    for row in context.table:
     @given('the following products')
def step_impl(context):
    """ Delete all Products and load new ones """
    # Eliminar todos los productos existentes
    rest_endpoint = f"{context.base_url}/products"
    context.resp = requests.get(rest_endpoint)
    assert(context.resp.status_code == HTTP_200_OK)
    for product in context.resp.json():
        context.resp = requests.delete(f"{rest_endpoint}/{product['id']}")
        assert(context.resp.status_code == HTTP_204_NO_CONTENT)

    # Cargar la base de datos con los nuevos productos
    for row in context.table:
        product_data = {
            "name": row['name'],
            "category": row['category'],
            "price": float(row['price']),
            "quantity": int(row['quantity'])
        }
        context.resp = requests.post(rest_endpoint, json=product_data)
        assert(context.resp.status_code == HTTP_201_CREATED)

=======
    for row in context.table:
>>>>>>> 59ad4ca (Initial commit)
