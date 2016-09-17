import sys

"""
Description: Main function for the battleship client.
			 Takes in 2 system arguments from command line
Input:		 sys.argv[1] - The ip address of the server
			 sys.argv[2] - The port number
			 sys.argv[3] - The x coordinate sent by the client
			 sys.argv[4] - The y coordinate sent by the client
"""
def main():
	ip_address = sys.argv[1]
	port_number = int(sys.argv[2])
	x_coord = int(sys.argv[3])
	y_coord = int(sys.argv[4])

	#TEST FUNCTION
	test_client(ip_address, port_number, x_coord, y_coord)


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
