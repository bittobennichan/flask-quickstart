from flask import render_template


# Custom error pages
def page_not_found(e):
    return render_template('error/404.html'), 404


def internal_server_error(e):
    return render_template('error/500.html'), 500


class Production:
    DEBUG = False
    TESTING = False
    ENV = 'production'
    # This will be overwritten by the values in
    # instance/config.py
    SECRET_KEY = 'production_secret_key'

    @staticmethod
    def init_app(app):
        # flask-quickstart/instance/config.py
        app.config.from_pyfile('config.py', silent=True)
        app.register_error_handler(404, page_not_found)
        app.register_error_handler(500, internal_server_error)
        return


class Development:
    DEBUG = True
    TESTING = False
    ENV = 'development'
    SECRET_KEY = 'development_secret_key'

    @staticmethod
    def init_app(app):
        app.register_error_handler(404, page_not_found)
        return


class Testing:
    DEBUG = False
    TESTING = True
    ENV = 'testing'
    SECRET_KEY = 'testing_secret_key'

    @staticmethod
    def init_app(app):
        pass


config = {
    'production': Production,
    'development': Development,
    'testing': Testing
}
