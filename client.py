import sys
import http.client
import re
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
		#test_client(ip_address, port_number, x_coord, y_coord)

		init_opponent_board()
		#Establish connection
		url = build_url(x_coord, y_coord)
		connect_to_server(ip_address, port_number, url)

"""

"""
def init_opponent_board():
		#Read the current state of the board from the HTML file
		f = open('opponent_board.html', 'r')
		contents = f.read()

		#Filter out all the board characters
		new_string = ''

		for i in range(len(contents)):
			if contents[i] == '_' or contents[i] == 'H' or contents[i] == 'M':
				new_string += contents[i]

		print(new_string)

		x = 10 #board size
		y = 10
		global opponent_board

		k = 0
		opponent_board = [ [ 0 for i in range(x) ] for j in range (y) ]
		for i in range(0, len(opponent_board[0])):
			for j in range(0, len(opponent_board[1])):
				opponent_board[i][j] = new_string[k]
				k += 1

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
        opponent_board[x_coord][y_coord] = 'H'
    if(hit == 0):
        opponent_board[x_coord][y_coord] = 'M'

    write_board_to_html()
    

def write_board_to_html():
	global opponent_board

	board = opponent_board

	f = open('opponent_board.html', 'w')

	#Write the header stuff
	header = """
	<!DOCTYPE html>
	<html>
	<head>
	<style>
	</style>
	</head>
	<body>

	<table>
	"""

	f.write(header)

	current_line = ''

	for i in range(0, len(board[0])):
		f.write('<tr>')
		for j in range(0, len(board[0])):
			f.write('<th>' + str(board[i][j]) + '</th>')
			if(j == len(board[0]) - 1):
				f.write('</tr>')

	footer = """
	</table>
	</body>
	</html>
	"""

	f.write(footer)



"""
Description: Builds a url from the input x and y coordinates
"""
def build_url(x_coord, y_coord):
		print('Coordinates selected:' + str(x_coord) + ', '+str(y_coord))
		return "x="+str(x_coord)+"&y="+str(y_coord)

"""
Description: Uses HTTP client to connect to a server
Params: ip_address - the IP address of the server
		port_number - the port number to use
"""
def connect_to_server(ip_address, port_number, url):
		print('Connecting to opponent server...')

		connection = http.client.HTTPConnection(ip_address, port_number)

		print('Sending coordinates...')
		
		connection.request("POST", url, url, headers={"Content-Length": len(url)})

		print('Coordinates sent successfully!')
		print('Waiting for response...')
		response = connection.getresponse()

		interpret_response(response)

		connection.close()

"""

"""
def interpret_response(response):
		o = urlparse(response.getheader("Response"))
		query = parse_qs(o.path)

		hit = query['hit'][0]
		sunk = query['sink'][0]

		if(int(hit) == 1):
			print('Server responded with a HIT!')
		elif(int(hit) == 0):
			print('Server responded with a MISS!')

		if(sunk == 'C'):
			print('Carrier was SUNK!')
		elif(sunk == 'B'):
			print('Battleship was SUNK!')
		elif(sunk == 'R'):
			print('Cruiser was SUNK!')
		elif(sunk == 'S'):
			print('Submarine was SUNK!')
		elif(sunk == 'D'):
			print('Destroyer was SUNK!')

		update_opponent_board(int(hit))


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
