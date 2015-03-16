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

    @cherrypy.expose
    def dfa(self):

        received_data = cherrypy.request.body.read()
        decoded_data = json.loads(received_data)
        try:
            no_of_states = decoded_data['no_of_states']
            no_of_symbols = decoded_data['no_of_symbols']
            states = decoded_data['states']
            symbols = decoded_data['symbols']
            string = decoded_data['string']
            temp_states = {}
            for key in states.keys():
                temp_states[int(key)]=states[key]
            states = temp_states
        except KeyError:
            return json.dumps({"status":2, "message":"Invalid Data Sent to the Server"})

        dfa = DeterministicFiniteAutomata(no_of_symbols, no_of_states, states, symbols)
        return json.dumps(dfa.validate_dfa(string))

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