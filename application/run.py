from application.app import create_app
from config import Config

if __name__ == "__main__":
    app = create_app(Config)
    app.run(port=25000)