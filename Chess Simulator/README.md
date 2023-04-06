# Chess-Simulator
In this assignment I was asked to write a chess simulator which will be able to take specific commands from the user (as a file), execute the commands, and return the results (if any) to the user.

Game:
The program is able to initialize the chess board and move pieces on the board, and also print the board’s layout and show possible moves of the given pieces on the board. When the program is requested to move pieces on the board, it firstly checks whether the piece is allowed to move to the destination square or not. When the program is requested to move pieces on the board, it checks whether the destination square already contains another piece. If there is an opponent piece on the destination square and the program determines that the move is valid, moving piece will capture the piece at the destination square, removing it from play. If there is a friendly piece on the destination square, the move is considered invalid.

For this assignment, pawns are different than the actual chess game. White pawns are only able to move upwards (from 1 to 8) and black pawns are only able to move downwards. The two-square starting move of pawns is not available. Also, there is one exception case for Knight. If the square is unoccupied, it can move on the same closest diagonal square, too. Another exception in this assignment is about moving Bishop. The bishop can move on just forward according to its moving direction. The program processes and responds to 5 different commands, which are defined below.

initialize:
This command load the pieces to the board.

showmoves:
Lists the possible target positions of the given piece can move.
(showmoves piece)

move:
Moves the given piece to the given position.
(move piece position)

print:
Prints the status of the board to the console.

exit:
Instructs the program to exit.
