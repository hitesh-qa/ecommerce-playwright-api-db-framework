from flask import Flask, render_template, request, jsonify, redirect, url_for
import db

app = Flask(__name__)
DEMO_USER_ID = 1 #seeded via seed_data.sql (we'll build that next)

@app.route("/")
def index():
    products = db.get_all_products()
    return render_template("index.html", products=products)

@app.route("/order", methods=["POST"])
def place_order():
    product_id = int(request.form["product_id"])
    quantity = int(request.form.get("quantity", 1))

    product = db.get_product(product_id)
    if not product:
        return "Product not found", 404

    total_amount = round(product["price"] * quantity, 2)
    order_id = db.create_order(DEMO_USER_ID, product_id, quantity, total_amount)

    # no real payment gateway - simulate instant confirmation
    db.update_order_status(order_id, "confirmed")
    db.create_payment(order_id, total_amount, "paid")

    return redirect(url_for("order_confirmation", order_id=order_id))

@app.route("/order_confirmation/<int:order_id>")
def order_confirmation(order_id):
    order = db.get_order(order_id)
    return render_template("confirmation.html", order=order)

#---------API endpoints (same DB, no browser needed)-------

@app.route("/api/products", methods=["GET"])
def get_all_products():
    return jsonify(db.get_all_products())

@app.route("/api/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = db.get_order(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order)

@app.route("/api/orders", methods=["POST"])
def api_create_order():
    data = request.get_json()
    product_id = data["product_id"]
    quantity = data.get("quantity", 1)

    product = db.get_product(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    total_amount = round(product["price"] * quantity, 2)
    order_id = db.create_order(DEMO_USER_ID, product_id, quantity, total_amount)
    db.update_order_status(order_id, "confirmed")
    db.create_payment(order_id, total_amount, "paid")

    return jsonify({"order_id": order_id}), 201

if __name__ == "__main__":
    debug_mug = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(debug=debug_mug, port=5000)