import sqlite3
import time
import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
DB_PATH = os.path.join(BASE_DIR, "shop.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
class Product:
    def __init__(self, name, price, stock, image_path,
                 category, brand, color,
                 discount=0, discount_price=None):

        self.name = name
        self.price = price
        self.stock = stock
        self.image_path = image_path
        self.category = category
        self.brand = brand
        self.color = color
        self.discount = discount
        self.discount_price = discount_price

   

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Product name must be at least 2 characters")
        self._name = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be positive")
        self._price = value

    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = value

    @property
    def image_path(self):
        return self._image_path
    
    @image_path.setter
    def image_path(self, value):
        if not isinstance(value, str) or len(value) < 5:
            raise ValueError("Invalid image path")

        valid_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")

        if value.startswith("http://") or value.startswith("https://"):
            if not value.lower().endswith(valid_extensions):
                raise ValueError("URL must point to an image file")
        else:
            if not value.lower().endswith(valid_extensions):
                raise ValueError("Local file must be an image")

        self._image_path = value

    # ---------------- NEW FIELDS ----------------

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not value:
            raise ValueError("Category is required")
        self._category = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not value:
            raise ValueError("Brand is required")
        self._brand = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not value:
            raise ValueError("Color is required")
        self._color = value

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if value not in (0, 1):
            raise ValueError("Discount must be 0 or 1")
        self._discount = value

    @property
    def discount_price(self):
        return self._discount_price

    @discount_price.setter
    def discount_price(self, value):
        if value is not None and value < 0:
            raise ValueError("Discount price cannot be negative")
        self._discount_price = value


    def __str__(self):
        return (
            f"{self.name} | Price: {self.price} | "
            f"Stock: {self.stock} | Category: {self.category} | "
            f"Brand: {self.brand} | Color: {self.color} | "
            f"Discount: {self.discount}"
        )

class Database:
    def __init__(self):
        self.conn = get_connection()
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conn.cursor()

    def execute(self, query, params=(), fetch=False):
        self.cursor.execute(query, params)
        self.conn.commit()
        if fetch:
            return self.cursor.fetchall()

    def close(self):
        self.conn.close()

class ProductService:
    def __init__(self):
        self.db = Database()
        self._create_table()
        self._update_table()

    def _create_table(self):
        self.db.execute("""
        CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            stock INTEGER NOT NULL,
            image_path TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

    def _update_table(self):
        try:
            self.db.execute("ALTER TABLE products ADD COLUMN category TEXT")
        except:
            pass

        try:
            self.db.execute("ALTER TABLE products ADD COLUMN brand TEXT")
        except:
            pass

        try:
            self.db.execute("ALTER TABLE products ADD COLUMN color TEXT")
        except:
            pass

        try:
            self.db.execute("ALTER TABLE products ADD COLUMN discount INTEGER DEFAULT 0")
        except:
            pass

        try:
            self.db.execute("ALTER TABLE products ADD COLUMN discount_price INTEGER")
        except:
            pass

    def get_products(self):
        return self.db.execute("SELECT * FROM products", fetch=True)
    
    def add_product(self, product: Product):
        self.db.execute("""
        INSERT INTO products 
        (name, price, stock, image_path, category, brand, color, discount, discount_price)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
        product.name,
        product.price,
        product.stock,
        product.image_path,
        product.category,
        product.brand,
        product.color,
        product.discount,
        product.discount_price
        ))

    def close(self):
        self.db.close()


class Users:
    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password
        self.role = role

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not value or len(value) < 3:
            raise ValueError("Username must be at least 3 characters")

        if not re.match("^[a-zA-Z0-9_]+$", value):
            raise ValueError("Username must contain only letters, numbers, _")

        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters")

        self._password = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if value not in ("user", "admin"):
            raise ValueError("Role must be 'user' or 'admin'")

        self._role = value

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

    
def main():
    products = [
    Product("iPhone 14", 900, 10, "images/iphone.jpg", "phone", "Apple", "black", 0, None),
    Product("Samsung S23", 800, 15, "images/s23.jpg", "phone", "Samsung", "white", 1, 700),
    Product("MacBook Pro", 2000, 5, "images/macbook.jpg", "laptop", "Apple", "gray", 0, None),
    Product("Dell XPS", 1500, 8, "images/dell.jpg", "laptop", "Dell", "black", 1, 300),
    Product("AirPods", 200, 30, "images/airpods.jpg", "accessory", "Apple", "white", 0, None)
    ]

    service = ProductService()

    for p in products:
        service.add_product(p)

    service.close()

def add_user(user):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO Users (username, password, role)
        VALUES (?, ?, ?)
    """, (user.username, user.password, user.role))

    conn.commit()
    conn.close()
    
root = Users("root", "root123", "admin")
add_user(root)
if __name__ == "__main__":

    main()
    
    