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
        global board

        #HANDLE CMD INPUT
        port_num = int(sys.argv[1])
        file_name = open(sys.argv[2], "r")

        file_content = file_name.read()
        
        #TEST FUNCTION
        test_server(port_num, file_content)
        init_ships()
        init_board()
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

def init_board():
        x = 10 #board size
        y = 10
        board = [ [ 0 for i in range(x) ] for j in range (y) ]

        
	#f = open('board.txt', 'r')
        #boardstr = f.read()
        boardstr = file_name.read() #assuming that file_name is board.txt, above can be used if that's not the case. file_name is also not global, so that might cause a problem, but I'll let you handle that.
        p = 0
        for i in range(0, len(boardstr[0])):
                for j in range(0, len(boardstr[0])):
                        if (test[p] == '\n'):
                                boardstr[i][j] = test[p+1]
                                p += 2
                        else:
                                boardstr[i][j] = test[p]
                                p += 1

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
Description: Function that detects hit, miss, error.
Very unsure about the return values, will probably need to be changed for the message.
"""
def hit_detect(x, y):
        if(x > len(board[x]) - 1 or y > len(board[x]) - 1): #out of bounds check, only need to check one dimension since board is square.
                return '010' #these return statements are probably placeholder, will depend on how we format the message that we send.
        
        if(board[x][y] == 'X'): #repeated coordinate.
                return '000' 
        
        if(board[x][y] == '_'): #miss check
                return '00'

        
        if(board[x][y] == 'C'): #carrier
                board[x][y] == 'X' #marks the spot to show it's been shot
                ship_c -= 1 
                if(check_sink() != 0):
                        return '1c' #hit and sunk
                else:
                        return '10' #just a hit
                
        if(board[x][y] == 'B'): #battleship
                board[x][y] == 'X'
                ship_b -= 1
                if(check_sink() != 0):
                        return '1b'
                else:
                        return '10'
                
        if(board[x][y] == 'R'): #cruiser
                board[x][y] == 'X'
                ship_r -= 1
                if(check_sink() != 0):
                        return '1r'
                else:
                        return '10'
                
        if(board[x][y] == 'S'): #submarine
                board[x][y] == 'X'
                ship_s -= 1
                if(check_sink() != 0):
                        return '1s'
                else:
                        return '10'
                
        if(board[x][y] == 'D'): #destroyer
                board[x][y] == 'X'
                ship_d -= 1
                if(check_sink() != 0):
                        return '1d'
                else:
                        return '10'

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
                return 'd'
                ship_d = -1
        return 0 #Returns a 0, for no new sinks. Not sure if this'll work.

"""
Description: This is a function that prints the current board, this could probably be used for updating the board, but I'm not sure. Regardless, here it is.
"""
def board_print():
        s = ''
        for i in range(0, len(board[0]) - 1):
                for j in range(0, len(board[0]) - 1):
                        s += str(board[i][j])
                        if(j == len(board[0]) - 2):
                                print(s)
                                s = ''
                                
"""
Description: Checks if the game is over, pretty sure we dont need it, but I made it just in case. Nothing calls this yet.
"""
def end_check():
        if (ship_c == -1 and ship_b == -1 and ship_r == -1 and ship_s == -1 and ship_d == -1):
                return 1 #game over
        else:
                return 0 #game not over


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

