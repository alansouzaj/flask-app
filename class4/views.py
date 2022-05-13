"""Extensão Flask"""
from flask import Flask

def init_app(app: Flask):
    """Inicialização da extensão"""

    @app.route("/")
    def index():
        return "Hello CodeShow!"

    @app.route("/contato")
    def contato():
        return "<form><input type='text'></input></form>"