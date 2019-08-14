# encoding: utf-8
from flask import Flask, request
import createurl


class Chanel:
    app = Flask(__name__)

    @app.route('/')
    def index():
        return '企迈云商 webhook-apiserver'

    @app.route('/manager/create', methods=['GET', 'POST'])
    def create():
        if request.method == 'GET':
            return "error methods"
        else:
            return createurl.url()


