# AI Finance Manager

## Overview
AI Finance Manager is a comprehensive financial management application designed to help users manage their expenses, budgets, savings, and investments. The application leverages machine learning to categorize expenses and provides an intuitive interface for users to interact with their financial data.

## Features
- **Expense Management:** Track and categorize your expenses automatically.
- **Budgeting:** Create and manage budgets to control your spending.
- **Savings:** Plan and monitor your savings goals.
- **Investments:** Keep track of your investments and analyze their performance.

## Technology Stack
- **Backend:** Flask
- **Frontend:** Vue.js
- **Machine Learning:** Scikit-learn

## Requirements
- Python 3.x
- Flask
- Vue.js
- Scikit-learn
- NumPy

## Installation

### Backend
1. Clone the repository:
    ```bash
    git clone https://github.com/amanhij/AIFinanceManager.git
    cd AIFinanceManager
    ```

2. Set up a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Run the Flask application:
    ```bash
    python app.py
    ```

### Frontend
1. Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Run the Vue.js application:
    ```bash
    npm run serve
    ```

## Usage
### AI Service
The `ai_service.py` script categorizes expenses into 'Low', 'Medium', and 'High' categories using KMeans clustering.
```python
import numpy as np
from ai_service import categorize_expenses

# Example usage
expenses = [
    {'amount': 50, 'category': None},
    {'amount': 200, 'category': None},
    {'amount': 500, 'category': None}
]
categorized_expenses = categorize_expenses(expenses)
print(categorized_expenses)
