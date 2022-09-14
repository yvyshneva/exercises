"""
Create a few classes to simulate a server that's taking connections 
from the outside and then a load balancer that ensures that there 
are enough servers to serve those connections.
"""

#################################
#Begin Portion 1#
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        if connection_id in self.connections:
            del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for c_id, c_load in self.connections.items():
            total += c_load
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
#End Portion 1#
#################################

server = Server()
server.add_connection("192.168.1.1")

print(server.load())

server.close_connection("192.168.1.1")
print(server.load())

#################################
#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        self.ensure_availability()
        server = random.choice(self.servers)
        self.connections[connection_id] = server
        server.add_connection(connection_id)
        # Add the connection to the dictionary with the selected server
        # Add the connection to the server

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        if connection_id not in self.connections:
            pass
        server = self.connections[connection_id]
        server.close_connection(connection_id)
        del self.connections[connection_id]
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer

    def avg_load(self):
        """Calculates the average load of all servers"""
        total_load = 0
        # Add up the load for each of the connections
        for server in self.servers:
            total_load += server.load()
        # Sum the load of each server and divide by the amount of servers
        return total_load / len(self.servers)

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            self.servers.append(Server())
            

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#
#################################

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

l.servers.append(Server())
print(l.avg_load())

l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

for connection in range(20):
    l.add_connection(connection)
print(l)

print(l.avg_load())
