import sys
import http.client
from urllib.parse import urlparse, parse_qs


opponent_board = 0
x_coord = 0
y_coord = 0

"""
Description: Main function for the battleship client.
			 Takes in 2 system arguments from command line
Input:		 sys.argv[1] - The ip address of the server
			 sys.argv[2] - The port number
			 sys.argv[3] - The x coordinate sent by the client
			 sys.argv[4] - The y coordinate sent by the client
"""
def main():
		global x_coord, y_coord
		#Receive input
		ip_address = sys.argv[1]
		port_number = int(sys.argv[2])
		x_coord = int(sys.argv[3])
		y_coord = int(sys.argv[4])


		#TEST FUNCTION
		test_client(ip_address, port_number, x_coord, y_coord)

		init_opponent_board()
		print_opponent_board()

		#Establish connection
		url = build_url(x_coord, y_coord)
		connect_to_server(ip_address, port_number, url)

"""

"""
def init_opponent_board():
		x = 10 #board size
		y = 10
		global opponent_board

		opponent_board = [ [ 0 for i in range(x) ] for j in range (y) ]
		for i in range(0, len(opponent_board[0])):
			for j in range(0, len(opponent_board[1])):
				opponent_board[i][j] = '_'

def print_opponent_board():
		global opponent_board
		s = ''
		for i in range(0, len(opponent_board[0])):
			for j in range(0, len(opponent_board[0])):
				s += str(opponent_board[i][j])
				if(j == len(opponent_board[0]) - 1):
					print(s)
					s = ''

def update_opponent_board(hit):
    #x_coord, y_coord were made global for this.
    global x_coord, y_coord, opponent_board

    if(hit == 1):
        opponent_board[x_coord][y_coord] = 'X'
    if(hit == 0):
        opponent_board[x_coord][y_coord] = 'O'
    
    
"""
Description: Builds a url from the input x and y coordinates
"""
def build_url(x_coord, y_coord):
		return "x="+str(x_coord)+"&y="+str(y_coord)

"""
Description: Uses HTTP client to connect to a server
Params: ip_address - the IP address of the server
		port_number - the port number to use
"""
def connect_to_server(ip_address, port_number, url):
		connection = http.client.HTTPConnection(ip_address, port_number)

		#I'm thinking we'll use POST to send a fire message and GET to get the board state(s)
		connection.request("POST", url, url, headers={"Content-Length": len(url)})

		response = connection.getresponse()

		interpret_response(response)

		connection.close()

"""

"""
def interpret_response(response):
		print(response.getheaders())

		#Here we should get our hit/miss/sunk message
		print(response.read())

		o = urlparse(response.getheader("Response"))
		query = parse_qs(o.path)

		hit = query['hit'][0]
		sunk = query['sink'][0]

		print(hit)
		print(sunk)

		update_opponent_board(int(hit))
		print_opponent_board()

		print(response.status)


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
