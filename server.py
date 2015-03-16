#! /usr/bin/env python2
import cherrypy
import os
import ConfigParser
import finite_automata
import json
from finite_automata import DeterministicFiniteAutomata
from jinja2 import Environment, FileSystemLoader
class Server():

    @cherrypy.expose
    def index(self):

        template = env.get_template('index.html')
        return template.render()

if __name__ == '__main__':
    ''' Setting up the Server with Specified Configuration'''

    server_config = ConfigParser.RawConfigParser()
    env = Environment(loader=FileSystemLoader(''))
    conf = {
        '/':{
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/resources': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './resources'
        }
    }
    server_config.read('server.conf')
    server_port=server_config.get('Server','port')
    server_host=server_config.get('Server','host')
    cherrypy.config.update({'server.socket_host': server_host})
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', server_port))})
    cherrypy.quickstart(Server(),'/',conf)