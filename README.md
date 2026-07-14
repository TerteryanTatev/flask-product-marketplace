# Flask E-Commerce Application

A lightweight, fully functional E-Commerce web application built using the Flask web framework, SQLite3, and native HTML/CSS. This project features user and administrator role separation, a dynamic product catalog with advanced search and filtering, and an automated shopping cart management system.

##  Features

###  User Capabilities
* **Authentication:** Secure registration and login flows, including password validation (minimum of 6 characters).
* **Dynamic Product Catalog:** Search items by name or filter dynamically by category, brand, color, discount status, and price range[cite: 1, 2].
* **Shopping Cart:** Add or remove items dynamically. The system automatically verifies and updates warehouse stock levels upon addition or cancellation[cite: 1, 2].

###  Admin Capabilities (Control Panel)
* **Add Products:** Easily insert new products into the database with specific attributes (name, price, stock quantity, image path, category, brand, color, discount status, and promotional price)[cite: 1, 2].
* **Edit Products:** Update product information dynamically (CRUD operations).
* **Delete Products:** Permanently remove items from the catalog[cite: 1].

---

##  Technology Stack

* **Backend:** Python, Flask[cite: 1]
* **Database:** SQLite3 (leveraging raw SQL queries and parameterized queries to prevent SQL injections)[cite: 1, 2]
* **Frontend:** HTML5, CSS3, Jinja2 Templates[cite: 1]
* **Session Management:** Flask Client-side Sessions[cite: 1]

---

##  Project Architecture

```text
├── db/
│   ├── db.py          # Database models (Product, Users), services, and initial seed data
│   └── shop.db        # SQLite database file (locally generated, ignored by git)
├── static/
│   ├── images/        # Product and accessory images
│   └── *.css          # Page-specific styling stylesheets
├── templates/
│   └── *.html         # Jinja2 template engine views (Home, Cart, Authentication, etc.)
├── app.py             # Main entry point containing application routes and configuration
├── .gitignore         # Prevents virtual environments, caches, and local databases from being tracked
└── README.md          # Project documentation
