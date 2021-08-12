from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.logger.debug(f'app.instance_path = {app.instance_path}')
    app.config.from_mapping(
        SECRET_KEY='.jHETCR4ER*@V{/'

    )
    
    from .blog import blog_bp
    app.register_blueprint(blog_bp)

    return app
