# Backend Django - Slot Machine

Developed using Django version 5.0.6.

## Setup Instructions

1. **Create a virtual environment**:

   ```
   python -m venv .venv
   ```

2. **Enable script execution (Windows PowerShell)**:

   ```
   Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
   ```

3. **Activate the virtual environment**:

   ```
   .\.venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```
   pip install django
   pip install django-cors-headers
   pip install mysqlclient
   ```

## Available Commands

| Command                      | Description                                                       |
| ---------------------------- | ----------------------------------------------------------------- |
| `python manage.py`           | Display command help`                                             |
| `python manage.py runserver` | Starts a local Django server on port 8000 `http://localhost:8000` |

## Available API

| Command                   | Description                               |
| ------------------------- | ----------------------------------------- |
| `GET /api/get-reels-slot` | Saves a matrix in json format, and prints |

### Example Response:

The API `/api/get-reels-slot` returns a JSON response with a 3x5 matrix structure. Each cell in the matrix represents a symbol on the slot machine reels.

```
{
  "reels": [
    ["symbol1", "symbol2", "symbol3", "symbol4", "symbol5"],
    ["symbol2", "symbol3", "symbol4", "symbol5", "symbol1"],
    ["symbol3", "symbol4", "symbol5", "symbol1", "symbol2"]
  ]
}
```
