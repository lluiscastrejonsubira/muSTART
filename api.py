#!/usr/bin/python

import requests

START_URL = 'Insert the URL to the appropiate START server'

class Server():
    """Interface to START server

    Serves as an interface to communicate with
    START servers using a common configuration
    and provides methods for the different possible
    requests
    """
    
    def __init__(self, server, uuid=None):
        """Initialize server interface

        Establishes the common parameters for 
        making petitions to the START server
        """
        self.server = server
        self.uuid = uuid
        self.referrer = 'Insert your own server URL or your ID'

    def request(self, 
                action,
                query,
                knowledge_base=False,
                ):
        """Make a request to the START server"""
        # Build request parameters into a dictionary
        parameters = {'server': self.server,
                      'referrer': self.referrer,
                      'action': action,
                      'kb': 'yes' if knowledge_base else 'no',
                      'te': 'formatted-text',
                      'query': query,
                      'uuid': self.uuid
                      }
       
        # Make request
        return requests.post(START_URL, data=parameters)            
        
    def parse(self, query):     
        """Request for a 'parse' query"""
        r = self.request('parse', query, knowledge_base=False)
        return r.text
    
    def insert(self, query):
        """Request for a 'insert' query"""
        r = self.request('parse', query, knowledge_base=True)
        return r.text
    
    def generate(self, query):
        """Request for a 'generate' query"""
        r = self.request('generate', query, knowledge_base=False)
        return r.text
    
    def match(self, query):
        """Request for a 'match' query"""
        r = self.request('match', query, knowledge_base=False)
        return r.text
    
    def flush_kb(self):
        """Request for a 'flush' query"""
        r = self.request('flush', 'ignored', knowledge_base=False)
        return r.text
        
if __name__ == '__main__':

      # Test the API
      server_name = 'Insert the name of the server to communicate with'
      uuid = 'Insert the name of a partition for your KB'

      server = Server(server_name, uuid)
    
      """ Insert your query here"""
      
      # Example
      print server.parse('The girl kicked the ball')
