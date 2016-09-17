import sys

"""
Description: Main function for the battleship client.
			 Takes in 2 system arguments from command line
Input:		 sys.argv[1] - The port number
			 sys.argv[2] - The input board file for the client (.txt)
"""
def main():
	port_num = int(sys.argv[1])
	file_name = open(sys.argv[2], "r")

	file_content = file_name.read()

	#TEST FUNCTION
	test_server(port_num, file_content)


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
