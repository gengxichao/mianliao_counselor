# -*- coding: utf-8 -*-

from gevent.wsgi import WSGIServer
from mianliao import app

if __name__ == '__main__':
  http_server = WSGIServer(('localhost', 5000), app)
  http_server.serve_forever()
