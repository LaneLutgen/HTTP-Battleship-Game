import sys
import http.client
import urllib

#Global variables for sink checking.
ship_c = 5
ship_b = 4
ship_r = 3
ship_s = 3
ship_d = 1
ship_d2 = 1

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

"""
Description: Function that detects a sink.
        Should be called in function that sends message to client.
        ship_(letter) variables should be decreased each by 1 whenever they get hit, once reaching 0, it detects a sink.
"""
def check_sink():
        if ship_c == 0: #Carrier
                return c #sends back the letter of the ship, think this will work, not sure because not good with python.
                ship_c = -1 #Sets to -1, confirming that the ship has sunk, and it has been detected as such.
        if ship_b == 0: #Battleship
                return b
                ship_b = -1
        if ship_r == 0: #Cruiser
                return r
                ship_r = -1
        if ship_s == 0: #Submarine
                return s
                ship_s = -1
        if ship_d == 0: #There are two destroyers, so we'll need a way to check which one sunk, this might work, not sure though.
                return d
                ship_d = -1
        if ship_d2 == 0: 
                return d
                ship_d2 = -1
        return 0 #Returns a 0, for no new sinks. Not sure if this'll work.

#MAIN FUNCTION CALL
main()
