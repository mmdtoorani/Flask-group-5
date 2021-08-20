from flask import Flask


def create_app():
    app = Flask(__name__)
    app.logger.debug(f'app.instance_path = {app.instance_path}')
    app.config.from_mapping(
        SECRET_KEY='.jHETCR4ER*@V{/'
    )
    
    from .blog import blog_bp
    from .user import user_bp
    from .api import api_bp
    app.register_blueprint(blog_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(api_bp)

    return app
