from flask import Flask
from pathlib import Path
from .config import Config

def create_app():
    app = Flask(__name__, instance_relative_config=True,
                static_folder="static", template_folder="templates")
    app.config.from_object(Config)

    Path(app.config["UPLOAD_FOLDER"]).mkdir(parents=True, exist_ok=True)
    Path(app.config["OUTPUT_FOLDER"]).mkdir(parents=True, exist_ok=True)

    from .routes import main
    app.register_blueprint(main)
    return app
