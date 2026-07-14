# Flask E-Commerce Application

A fully functional **E-Commerce web application** built with **Flask**, **SQLite3**, and **HTML/CSS**. The project demonstrates full-stack web development concepts, including user authentication, product management, shopping cart functionality, inventory control, and role-based access for administrators.

## Features

### User Features

- User registration and authentication.
- Secure login with password validation.
- Browse the product catalog.
- Search products by name.
- Filter products by:
  - Category
  - Brand
  - Color
  - Discount status
  - Price range
- Add products to the shopping cart.
- Remove products from the shopping cart.
- Automatic stock availability verification.
- Automatic inventory updates when products are added or removed from the cart.

### Administrator Features

- Administrator control panel.
- Add new products.
- Edit existing products.
- Delete products.
- Manage inventory quantities.
- Configure product information including:
  - Name
  - Category
  - Brand
  - Color
  - Price
  - Discount price
  - Stock quantity
  - Product image

## Technology Stack

### Backend

- Python 3
- Flask

### Database

- SQLite3
- Parameterized SQL queries
- Raw SQL database operations

### Frontend

- HTML5
- CSS3
- Jinja2 Templates

### Session Management

- Flask Sessions

## Project Structure

```text
├── db/
│   ├── db.py              # Database utilities and SQL operations
│   └── shop.db            # Local SQLite database (ignored by Git)
│
├── static/
│   ├── images/            # Product images
│   └── *.css              # Stylesheets
│
├── templates/
│   └── *.html             # Jinja2 templates
│
├── app.py                 # Application entry point
├── .gitignore
└── README.md
```

## Application Workflow

1. Users register and log in.
2. Products are loaded from the SQLite database.
3. Users can search and filter products.
4. Selected products are added to the shopping cart.
5. Inventory is automatically updated.
6. Administrators manage the product catalog through the control panel.

## Technologies Demonstrated

- Flask Routing
- Jinja2 Template Engine
- User Authentication
- Session Management
- CRUD Operations
- SQLite Database Design
- SQL Queries
- Product Search & Filtering
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

Install the required dependencies:

```bash
pip install flask
```

Run the application:

```bash
python app.py
```

Then open your browser and visit:

```
http://127.0.0.1:5000
```

## Future Improvements

- Order history
- Online payment integration
- Product reviews and ratings
- Wishlist functionality
- Responsive mobile interface
- REST API support
- Admin dashboard analytics
