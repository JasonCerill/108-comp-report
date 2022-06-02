import json 
from flask import Flask, abort
from autobio import me
from mock_data import catalog



app = Flask('whoknows')

@app.route("/", methods=['GET'])
def home():
    return "WhoKnows?"

@app.route("/about")
def about():
   
    
    return me["first"] + " " + me["last"]


@app.route("/myaddress")
def address():
    return f'Address:  {me["address"]["street"]} {me["address"]["number"]} '



################ API ENDPOINTS ############

#  Postman --> test endpoints of REST API's


@app.route("/api/catalog", methods=["Get"])
def get_catalog():
    return json.dumps(catalog)

@app.route("/api/catalog/inventory", methods=["Get"])
def get_inventory():

        inventory = len(catalog)

        return json.dumps(inventory)


@app.route("/api/product/<id>", methods=["Get"])
def get_product(id):

    for prod in catalog:
        if prod["_id"] == id:
            return json.dumps(prod)

    return abort(404, "ID does not match")


@app.get("/api/catalog/total")
def get_total():

    total = 0
    for prod in catalog:
        total = total + prod["price"]

    return json.dumps(total)


@app.get("/api/catalog/<category>")
def products_by_category(category):

    results = []
    category = category.lower()
    for prod in catalog:
        if prod["category"].lower() == category:
           results.append(prod)


    return json.dumps(results)

@app.get("/api/categories")
def get_unique_categories():
    results = []
    for prod in catalog:
        cat = prod["category"]
        if not cat in results:
            results.append(cat)

    return json.dumps(results) 


app.get("/api/product/cheapest")
def get_cheapest_product():
    solution = catalog[0]
    for prod in catalog:
        if prod["price"] < solution["price"]:
            solution = prod

    return json.dumps(solution)        



@app.get("/api/exercise1")
def get_exe1():
    nums = [123,123,654,124,8865,532,4768,8476,45762,345,-1,234,0,-12,-456,-123,-865,532,4768]

    # print the lowest number

    # count and print how many numbers are lowe than 500

    # sum and print all the negatives


    # return the sum of numbers except negatives

app.run(debug=True)