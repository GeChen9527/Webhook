# encoding: utf-8
from flask import Flask, request


class chanel:
    app = Flask(__name__)

    @app.route('/')
    def index():
        return '企迈云商 webhook-apiserver'

    @app.route('/token/', methods=['GET', 'POST'])
    def create_url():
        if request.method == 'POST':
            return "error methods"
        else
            return

    @app.route('/manager')
    def index():
        return '企迈云商 webhook-apiserver'

