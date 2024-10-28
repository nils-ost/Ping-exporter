import cherrypy
from helpers import generate_output, conv_int, conv_float


class PingExporter():
    def __init__(self):
        self.ping = ping()


@cherrypy.popargs('host', 'count', 'timeout')
class ping():
    @cherrypy.expose()
    def index(self, host, count=3, timeout=0.5):
        from collectors import do_ping
        cherrypy.response.headers['Cache-Control'] = 'no-cache'
        cherrypy.response.headers['Content-Type'] = 'text/plain; version=0.0.4'
        results = do_ping(host, conv_int(count, 3), conv_float(timeout, 0.5))
        return generate_output(*results)


if __name__ == '__main__':
    conf = {}
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})
    cherrypy.quickstart(PingExporter(), '/', conf)
