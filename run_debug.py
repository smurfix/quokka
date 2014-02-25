#!/usr/bin/env python
import argparse

import logging,sys
class noURLdebug(object):
        def filter(self,record):
                if record.levelno >= logging.DEBUG:
                        return True
                if record.name.startswith("urllib3."):
                        return False
                if record.name.startswith("requests.packages.urllib3."):
                        return False
                return True

def init_logging():
        logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)
        for h in logging.getLogger().handlers: h.addFilter(noURLdebug())

from quokka import create_app
from gevent.wsgi import WSGIServer

init_logging()
logging.debug("Start")

parser = argparse.ArgumentParser(description="Run Quokka App")
parser.add_argument('-p', '--port', help='App Port')
parser.add_argument('--host', help='App Host')
parser.add_argument('-r', action='store_true', help='Turn reloader on')
args = parser.parse_args()

host = args.host or '127.0.0.1'
port = int(args.port) if args.port else 5000
reloader = args.r or False

def debugger():
	import pdb;pdb.set_trace()

app = create_app()
app.jinja_env.globals.update(debugger=debugger)

if reloader:
	app.run(use_reloader=True, host=host, port=port)
else:
	http_server = WSGIServer((host, port), app)
	http_server.serve_forever()
