#!/usr/bin/env python
import argparse

from quokka import create_app
from gevent.wsgi import WSGIServer

parser = argparse.ArgumentParser(description="Run Quokka App")
parser.add_argument('-p', '--port', help='App Port')
parser.add_argument('--host', help='App Host')
parser.add_argument('-r', action='store_true', help='Turn reloader on')
args = parser.parse_args()

host = args.host or '127.0.0.1'
port = int(args.port) if args.port else 5000
reloader = args.r or False

app = create_app()
if reloader:
	app.run(use_reloader=True, host=host, port=port)
else:
	http_server = WSGIServer((host, port), app)
	http_server.serve_forever()
