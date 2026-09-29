# Finance API

A RESTful API for personal finance management, built with Flask and PostgreSQL.

The goal of this project is to build a clean, scalable backend while demonstrating practical backend development concepts such as authentication, database design, validation, testing, and API architecture.

## Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* PostgreSQL
* JWT Authentication
* Marshmallow
* Pytest
* Docker

## Features

### Authentication

* User registration
* User login
* JWT-based authentication
* Password hashing
* Access and refresh tokens

### Transactions

* Create transactions
* Update transactions
* Delete transactions
* View transaction details
* List user transactions
* Filtering and pagination

### Categories

* Create categories
* Update categories
* Delete categories
* Assign categories to transactions

### Reports

* Monthly income and expenses
* Expense breakdown
* Financial summaries

### API

* RESTful API design
* JSON responses
* Input validation
* Error handling
* Pagination
* Filtering
* Rate limiting
* API documentation

## Project Structure

```text
finance-api/
├── app/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── extensions.py
│   └── __init__.py
│
├── migrations/
├── tests/
├── .env.example
├── .gitignore
├── config.py
├── requirements.txt
└── run.py
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/finance-api.git
cd finance-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file based on `.env.example`.

```env
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://username:password@localhost:5432/finance_db
```

### 5. Run database migrations

```bash
flask --app run db upgrade
```

### 6. Start the development server

```bash
python run.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

## API Health Check

```http
GET /api/v1/health
```

Response:

```json
{
  "status": "ok"
}
```

## Testing

Run the test suite with:

```bash
pytest
```

## Environment Variables

| Variable       | Description               |
| -------------- | ------------------------- |
| `FLASK_ENV`    | Application environment   |
| `SECRET_KEY`   | Application secret key    |
| `DATABASE_URL` | PostgreSQL connection URL |

## Project Status

🚧 This project is currently under development.

New features and improvements will be added incrementally.

## License

This project is licensed under the MIT License.
