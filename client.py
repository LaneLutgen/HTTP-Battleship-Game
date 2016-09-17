import sys
import http.client
import urllib

"""
Description: Main function for the battleship client.
			 Takes in 2 system arguments from command line
Input:		 sys.argv[1] - The ip address of the server
			 sys.argv[2] - The port number
			 sys.argv[3] - The x coordinate sent by the client
			 sys.argv[4] - The y coordinate sent by the client
"""
def main():
	#Receive input
	ip_address = sys.argv[1]
	port_number = int(sys.argv[2])
	x_coord = int(sys.argv[3])
	y_coord = int(sys.argv[4])

	#TEST FUNCTION
	test_client(ip_address, port_number, x_coord, y_coord)

	#Establish connection
	connect_to_server(ip_address, port_number)


"""
Description: Uses HTTP client to connect to a server
Params: ip_address - the IP address of the server
		port_number - the port number to use
"""
def connect_to_server(ip_address, port_number):
	connection = http.client.HTTPConnection(ip_address, port_number, timeout=10)

"""
NOT IMPLEMENTED

Should send HTTP command to opponent server

NOTE: Boards are 0 indexed (Ex. 0-9) 
"""
def fire_at_opponent(x_coord, y_coord):

"""
NOT IMPLEMENTED

Should update the HTML representation of the player board
"""
def update_player_board():

"""
NOT IMPLEMENTED

Should update the HTML representation of the opponent board
"""
def update_opponent_board():

"""
Description: Main function for the battleship client.
			 Takes in 2 system arguments from command line
Params:		 ip_address - The ip address of the server
			 port_number - The port number
			 x_coord - The x coordinate sent by the client
			 y_coord - The y coordinate sent by the client
"""
def test_client(ip_address, port_number, x_coord, y_coord):
	print(ip_address)
	print(port_number)
	print(x_coord)
	print(y_coord)


#MAIN FUNCTION CALL
main()
