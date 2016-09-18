import sys
import urllib
from http.server import BaseHTTPRequestHandler, HTTPServer

"""
Description:    Main function for the battleship client.
                Takes in 2 system arguments from command line
Input:          sys.argv[1] - The port number
                sys.argv[2] - The input board file for the client (.txt)
"""
def main():
        global ship_c
        global ship_b
        global ship_r 
        global ship_s 
        global ship_d

        #HANDLE CMD INPUT
        port_num = int(sys.argv[1])
        file_name = open(sys.argv[2], "r")

        file_content = file_name.read()
        
        #TEST FUNCTION
        test_server(port_num, file_content)
        init_ships()
        init_http_server(port_num)

"""
Description:    Initializes the ships with the number of hits left before sinking
"""
def init_ships():
        ship_c = 5
        ship_b = 4
        ship_r = 3
        ship_s = 3
        ship_d = 2

"""
Description:    Initializes the HTTP Server
"""
def init_http_server(port_num):
        ip_address = '127.0.0.1' #not sure if this is correct or not 
        server_address = (ip_address, port_num)
        httpd = HTTPServer(server_address, BattleShipHTTP_RequestHandler)
        print("HTTP Server Initialized")

        #This will need to be terminated somehow
        httpd.serve_forever()

"""
Description:    Test function for the command line input
Params:		port_num - The port number
		file_content - The input board file for the client (.txt)
"""
def test_server(port_num, file_content):
        print(port_num)
        print(file_content)


"""
Description: Function that detects a sink.
        Should be called in function that sends message to client.
        ship_(letter) variables should be decreased each by 1 whenever they get hit, once reaching 0, it detects a sink.
"""
def check_sink():
        if ship_c == 0: #Carrier
                return 'c' #sends back the letter of the ship, think this will work, not sure because not good with python.
                ship_c = -1 #Sets to -1, confirming that the ship has sunk, and it has been detected as such.
        if ship_b == 0: #Battleship
                return 'b'
                ship_b = -1
        if ship_r == 0: #Cruiser
                return 'r'
                ship_r = -1
        if ship_s == 0: #Submarine
                return 's'
                ship_s = -1
        if ship_d == 0: #Destroyer
                ship_d = -1
        return 0 #Returns a 0, for no new sinks. Not sure if this'll work.

"""
Description: Class for handling any GET messages
"""
class BattleShipHTTP_RequestHandler(BaseHTTPRequestHandler):

        """
        Handler for any GET messages received
        """
        def do_GET(self):
                self.protocol_version = 'HTTP/1.1'
                self.send_response(200, 'OK')



#MAIN FUNCTION CALL
main()

