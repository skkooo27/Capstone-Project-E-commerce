# E-commerce Product API

A comprehensive REST API for an e-commerce platform built with Django and Django REST Framework. This API provides product management, user authentication, cart functionality, and order processing.

## Features

- **User Authentication**: JWT-based authentication with registration and login
- **Product Management**: Full CRUD operations for products with categories
- **Category Management**: CRUD for product categories
- **Cart Management**: Add, update, remove items from cart
- **Order Processing**: Create orders from cart, view order history, cancel orders
- **Search & Filtering**: Search products by name/category, filter by price range, stock availability
- **Pagination**: Efficient handling of large datasets

## Tech Stack

- Django 5.2
- Django REST Framework
- Django REST Framework Simple JWT
- SQLite (default database)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ecommerce-product-api
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt
   ```

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login and get JWT token

### Users
- `GET /api/users/` - List users (admin only)
- `GET /api/users/<id>/` - Get user details
- `PUT /api/users/<id>/` - Update user profile

### Categories
- `GET /api/categories/` - List all categories
- `POST /api/categories/` - Create new category (authenticated)
- `GET /api/categories/<id>/` - Get category details
- `PUT /api/categories/<id>/` - Update category (authenticated)
- `DELETE /api/categories/<id>/` - Delete category (authenticated)

### Products
- `GET /api/products/` - List products (with filtering/search)
  - Query parameters: `search`, `category`, `min_price`, `max_price`, `in_stock`
- `POST /api/products/` - Add new product (authenticated)
- `GET /api/products/<id>/` - Get product details
- `PUT /api/products/<id>/` - Update product (authenticated)
- `DELETE /api/products/<id>/` - Delete product (authenticated)

### Cart
- `GET /api/cart/` - View cart items (authenticated)
- `POST /api/cart/add/` - Add product to cart (authenticated)
  - Body: `{"product_id": 1, "quantity": 2}`
- `PUT /api/cart/update/` - Update cart item quantity (authenticated)
  - Body: `{"product_id": 1, "quantity": 3}`
- `DELETE /api/cart/remove/<product_id>/` - Remove item from cart (authenticated)

### Orders
- `POST /api/orders/` - Create order from cart (authenticated)
- `GET /api/orders/` - List user orders (authenticated)
- `GET /api/orders/<id>/` - Get order details (authenticated)
- `PUT /api/orders/<id>/cancel/` - Cancel order (authenticated)

## Authentication

Include the JWT token in the Authorization header for protected endpoints:
```
Authorization: Bearer <your-jwt-token>
```

## Testing the API

You can use tools like Postman or curl to test the endpoints. Here's an example:

1. Register a user:
   ```bash
   curl -X POST http://127.0.0.1:8000/api/auth/register/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "email": "test@example.com", "password": "password123"}'
   ```

2. Login to get token:
   ```bash
   curl -X POST http://127.0.0.1:8000/api/auth/login/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "password123"}'
   ```

3. Use the token for authenticated requests.

## Deployment

### PythonAnywhere

#### Prerequisites
- PythonAnywhere account
- Git repository with your code

#### Steps

1. **Clone your repository on PythonAnywhere:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Run the deployment script:**
   ```bash
   python deploy.py
   ```

3. **Configure the web app on PythonAnywhere:**
   - Go to the **Web** tab
   - Click **Add a new web app**
   - Choose **Manual configuration** and select your Python version
   - Set the source code directory to your project folder
   - Set the WSGI configuration file to `ecommerce_api/wsgi.py`
   - In the **Virtualenv** section, create a new virtualenv or use an existing one
   - Add `/static/` to the static files section, pointing to your `staticfiles` directory
   - Reload your web app

4. **Update settings for production:**
   - Edit `ecommerce_api/settings.py`
   - Replace `'your-username.pythonanywhere.com'` with your actual PythonAnywhere domain
   - Set a secure `SECRET_KEY`

### Heroku
1. Create a Heroku app
2. Set environment variables
3. Push to Heroku git
4. Run migrations on Heroku

## Project Structure

```
ecommerce_api/
├── ecommerce_api/          # Main project directory
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/                   # User management app
├── categories/             # Category management app
├── products/               # Product management app
├── cart/                   # Cart functionality app
├── orders/                 # Order processing app
├── manage.py
├── requirements.txt        # Dependencies
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.
