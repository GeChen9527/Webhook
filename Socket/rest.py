# encoding: utf-8
from flask import Flask, request


class chanel:
    app = Flask(__name__)

    @app.route('/')
    def index():
        return '企迈云商 monitor-apiserver'

    @app.route('/search_log/', methods=['GET', 'POST'])
    def search_log():
        if request.method == 'POST':
            return "error methods"

