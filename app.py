from flask import Flask, request, redirect, render_template, session
from db.db import Users, get_connection, add_user, ProductService, Product



app = Flask(__name__)
app.secret_key = "secret123"

def is_admin():
    return session.get("user") and session["user"]["role"] == "admin"
@app.route("/")
def home():
    query = request.args.get("q")
    category = request.args.get("category")
    brand = request.args.get("brand")
    color = request.args.get("color")
    discount = request.args.get("discount")
    min_price = request.args.get("min_price")
    max_price = request.args.get("max_price")

    conn = get_connection()
    cursor = conn.cursor()

    sql = "SELECT * FROM products WHERE 1=1"
    params = []

    if query:
        sql += " AND name LIKE ?"
        params.append("%" + query + "%")

    if category:
        sql += " AND category = ?"
        params.append(category)

    if brand:
        sql += " AND brand = ?"
        params.append(brand)

    if color:
        sql += " AND color = ?"
        params.append(color)

    if discount:
        sql += " AND discount = ?"
        params.append(int(discount))

    if min_price:
        sql += " AND price >= ?"
        params.append(int(min_price))

    if max_price:
        sql += " AND price <= ?"
        params.append(int(max_price))

    cursor.execute(sql, params)

    rows = cursor.fetchall()
    products = [dict(row) for row in rows]  

    conn.close()

    return render_template("home.html", products=products)


@app.route("/Register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        try:
            user = Users(
                username=request.form["username"],
                password=request.form["password"]
            )
            add_user(user)
            return redirect("/login")

        except ValueError as e:
           error = "password must be at least 6 characters"

    return render_template("Register.html", error=error)



@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM Users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            session["user"] = dict(user)
            return redirect("/")
        else:
            error = "User not found or wrong password"

    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/about")
def about():
    return render_template("aboute.html")
@app.route("/add", methods=["GET", "POST"])
def add_product():
    if not is_admin():
        return "Access denied"

    service = ProductService()
    error = None

    if request.method == "POST":
        try:
            discount = int(request.form["discount"])
            discount_price = request.form.get("discount_price")

  
            if discount == 0 or not discount_price:
                discount_price = None
            else:
                discount_price = int(discount_price)

            product = Product(
                name=request.form["name"],
                price=int(request.form["price"]),
                stock=int(request.form["stock"]),
                image_path=request.form["image"],
                category=request.form["category"],
                brand=request.form["brand"],
                color=request.form["color"],
                discount=discount,
                discount_price=discount_price
            )

            service.add_product(product)

            return redirect("/")

        except Exception as e:
            error = str(e)

    return render_template("add.html", error=error)

@app.route("/edit_page")
def edit_page():
    if not is_admin():
        return "Access denied"

    service = ProductService()
    products = service.get_products()
    return render_template("edit_page.html", products=products)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_product(id):
    if not is_admin():
        return "Access denied"

    if request.method == "POST":
        name = request.form["name"]
        price = int(request.form["price"])
        stock = int(request.form["stock"])

        category = request.form.get("category")
        brand = request.form.get("brand")
        color = request.form.get("color")

        discount = int(request.form.get("discount", 0))
        discount_price = request.form.get("discount_price")

        if discount_price == "":
            discount_price = None
        else:
            discount_price = int(discount_price)

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE products
            SET name=?,
                price=?,
                stock=?,
                category=?,
                brand=?,
                color=?,
                discount=?,
                discount_price=?
            WHERE product_id=?
        """, (
            name,
            price,
            stock,
            category,
            brand,
            color,
            discount,
            discount_price,
            id
        ))

        conn.commit()
        conn.close()

        return redirect("/edit_page")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products WHERE product_id=?", (id,))
    product = cursor.fetchone()

    conn.close()

    return render_template("edit.html", product=product)

@app.route("/delete_page")
def delete_page():
    if not is_admin():
        return "Access denied"

    service = ProductService()
    products = service.get_products()

    return render_template("delete_page.html", products=products)

@app.route("/delete/<int:id>")
def delete_product(id):
    if not is_admin():
        return "Access denied"

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products WHERE product_id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/delete_page")

@app.route("/info")
def info():
    return render_template("info.html")


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    product_id = int(request.form["product_id"])
    quantity = int(request.form["quantity"])

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT stock FROM products WHERE product_id=?", (product_id,))
    product = cursor.fetchone()

    if not product:
        conn.close()
        return "Product not found"

    stock = product["stock"]

    if quantity > stock:
        conn.close()
        return f"Only {stock} items available!"

    new_stock = stock - quantity

    cursor.execute("""
        UPDATE products SET stock=? WHERE product_id=?
    """, (new_stock, product_id))

    conn.commit()
    conn.close()

    if "cart" not in session:
        session["cart"] = {}

    cart = session["cart"]

    if str(product_id) in cart:
        cart[str(product_id)] += quantity
    else:
        cart[str(product_id)] = quantity

    session["cart"] = cart

    return redirect("/")



@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    conn = get_connection()
    cursor = conn.cursor()

    products = []
    total = 0

    for product_id, qty in cart.items():
        cursor.execute("SELECT * FROM products WHERE product_id=?", (product_id,))
        product = cursor.fetchone()

        if product:
            subtotal = product["price"] * qty
            total += subtotal

            products.append({
                "product": product,
                "quantity": qty,
                "subtotal": subtotal
            })

    conn.close()

    return render_template("cart.html", products=products, total=total)


@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    product_id = request.form["product_id"]

    cart = session.get("cart", {})

    if product_id in cart:
        quantity = cart[product_id]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE products
            SET stock = stock + ?
            WHERE product_id = ?
        """, (quantity, product_id))

        conn.commit()
        conn.close()

        del cart[product_id]

    session["cart"] = cart

    return redirect("/cart")





if __name__ == "__main__":
    app.run(debug=True)