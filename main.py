# encoding: utf-8

from Socket.rest import Search

if __name__ == '__main__':
    Search.app.run(host='0.0.0.0', port=3000, debug=True)