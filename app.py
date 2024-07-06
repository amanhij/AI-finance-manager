from flask import Flask
from api.routes.budget import budget_bp
from api.routes.expenses import expenses_bp
from api.routes.investments import investments_bp
from api.routes.savings import savings_bp

app = Flask(__name__)

app.register_blueprint(budget_bp, url_prefix='/api/budgets')
app.register_blueprint(expenses_bp, url_prefix='/api/expenses')
app.register_blueprint(investments_bp, url_prefix='/api/investments')
app.register_blueprint(savings_bp, url_prefix='/api/savings')

if __name__ == '__main__':
    app.run(debug=True)
