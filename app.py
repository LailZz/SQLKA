from flask import Flask, redirect, url_for
from models import db  # Імпортуємо db з models.py


def create_app():
    app = Flask(__name__)
    
    # Конфігурація бази даних
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Vova246878906v@127.0.0.1:3306/users'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key-here'
    
    # Ініціалізація бази даних
    db.init_app(app)
    
    # Імпорт блюпринтів після ініціалізації db
    from routes.districts import districts_bp
    from routes.payments import payments_bp
    from routes.pensioners import pensioners_bp
    from routes.pensions import pensions_bp
    
    # Реєстрація блюпринтів
    app.register_blueprint(districts_bp)
    app.register_blueprint(payments_bp)
    app.register_blueprint(pensioners_bp)
    app.register_blueprint(pensions_bp)
    
    @app.route('/')
    def home():
        return redirect(url_for('pensioners.index'))
    
    return app

if __name__ == '__main__':
    app = create_app()
    
    # Створення таблиць у базі даних
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)