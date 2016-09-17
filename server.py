import sys
import http.client
import urllib

"""
Description: Main function for the battleship client.
			 Takes in 2 system arguments from command line
Input:		 sys.argv[1] - The port number
			 sys.argv[2] - The input board file for the client (.txt)
"""
def main():
	#Receive Input
	port_num = int(sys.argv[1])
	file_name = open(sys.argv[2], "r")

	file_content = file_name.read()

	#TEST FUNCTION
	test_server(port_num, file_content)


"""
NOT IMPLEMENTED

This should be some sort of function to listen for HTTP commands from 
the client. (May be a infinite loop but I'm not sure, would have to 
be able to terminate it with a timeout of some sort)
"""
def http_listener(): 

"""
NOT IMPLEMENTED

This will probably be some function to grab the HTML for the player
board so we can determine a hit, miss, sunk, etc.
"""
def get_player_board():


"""
Description: Main function for the battleship client.
			 Takes in 2 system arguments from command line
Params:		 port_num - The port number
			 file_content - The input board file for the client (.txt)
"""
def test_server(port_num, file_content):
	print(port_num)
	print(file_content)


#MAIN FUNCTION CALL
main()
