# encoding: utf-8
from flask import Flask, request
from manager import createurl


class Interface:
    app = Flask(__name__)

    @app.route('/')
    def index():
        return '企迈云商 webhook-apiserver'

    @app.route('/manager/create', methods=['GET', 'POST'])
    def create():
        if request.method == 'GET':
            return "企迈云商 error methods"
        else:
            return createurl.url()

    def webhook():
        if request.method == 'Post':
            return "企迈云商 error methods"
        else:
            return createurl.url()


