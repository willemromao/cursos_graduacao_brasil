from app.flask_app import Flask
from .flask_app import api_bp

def create_app():
    app = Flask(__name__)
    
    # Importa as rotas da API
    from .flask_app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app


