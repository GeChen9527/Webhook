#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, request
from manager import createurl
from webhook import project


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

    @app.route('/webhook', methods=['GET', 'POST'])
    def webhook():
        if request.method == 'GET':
            return "企迈云商 error methods"
        else:
            return project.test()


