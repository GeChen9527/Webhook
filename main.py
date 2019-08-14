# encoding: utf-8

from Socket.rest import Chanel

if __name__ == '__main__':
    Chanel.app.run(host='0.0.0.0', port=3000, debug=True)