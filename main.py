#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Socket.rest import Interface

if __name__ == '__main__':
    Interface.app.run(host='0.0.0.0', port=3000, debug=True)