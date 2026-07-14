# Flask E-Commerce Application

A lightweight **E-Commerce web application** built with **Flask**, **SQLite3**, and **HTML/CSS**. The project demonstrates full-stack web development concepts, including user authentication, role-based authorization, product management, product filtering, shopping cart functionality, inventory management, and database operations.

## Features

### User Features

- User registration with input validation.
- User login and logout using Flask sessions.
- Browse the product catalog.
- Search products by name.
- Filter products by:
  - Category
  - Brand
  - Color
  - Discount status
  - Minimum and maximum price
- Add products to the shopping cart.
- Remove products from the shopping cart.
- Automatic stock verification before adding products.
- Automatic inventory updates when products are added to or removed from the cart.

### Administrator Features

Administrator-only pages allow product management:

- Add new products.
- Edit existing products.
- Delete products.
- Manage product information, including:
  - Name
  - Price
  - Stock quantity
  - Category
  - Brand
  - Color
  - Discount status
  - Discount price
  - Product image path

## Input Validation

The application performs validation using Python property setters.

### Product Validation

- Product name validation.
- Positive price validation.
- Non-negative stock validation.
- Image path validation.
- Category validation.
- Brand validation.
- Color validation.
- Discount value validation.
- Discount price validation.

### User Validation

- Username validation.
- Password length validation.
- User role validation.

## Technology Stack

### Backend

- Python 3
- Flask

### Database

- SQLite3
- Raw SQL queries
- Parameterized SQL queries
- SQLite Row Factory

### Frontend

- HTML5
- CSS3
- Jinja2 Templates

### Session Management

- Flask Sessions

## Project Structure

```text
├── db/
│   ├── db.py              # Database utilities, validation classes, and services
│   └── shop.db            # SQLite database
│
├── static/
│   ├── images/            # Product images
│   └── *.css              # Stylesheets
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── Register.html
│   ├── cart.html
│   ├── add.html
│   ├── edit.html
│   ├── edit_page.html
│   ├── delete_page.html
│   ├── about.html
│   └── info.html
│
├── app.py                 # Flask application and routes
├── .gitignore
└── README.md
```

## Application Workflow

1. Users register an account.
2. Users log in using their credentials.
3. Products are loaded from the SQLite database.
4. Users search and filter products.
5. Products can be added to the shopping cart.
6. Available stock is checked before adding items.
7. Stock quantities are automatically updated.
8. Administrators can add, edit, and delete products.

## Concepts Demonstrated

- Flask Routing
- Template Rendering (Jinja2)
- User Authentication
- Role-Based Authorization
- Session Management
- CRUD Operations
- SQLite Database Design
- SQL Queries
- Data Validation
- Product Search and Filtering
- Shopping Cart Logic
- Inventory Management

## Running the Project

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project folder:

```bash
cd Flask-E-Commerce
```

Install Flask:

```bash
pip install flask
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

## Future Improvements

- Password hashing
- Order management
- Order history
- Payment integration
- Product reviews
- Wishlist
- REST API
- Responsive mobile interface
