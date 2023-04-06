# Feeding-the-Rabbit-Game
This is my first Python Assignment. In this assignment, I was asked to implement a game called ’Feeding the Rabbit Game’. In this game, the rabbit which is placed in a board will move according to the commands and collect points according to the food it eats.


Game Rules:

The user plays the game by moving the the rabbit denoted by * to horizontally or vertically adjacent cells. The user earns/lose points if he/she move the rabbit to a cell that contains Carrot (C), Apple (A) or Meat (M). The game is over and the rabbit cannot move any more if user can move the rabbit to a cell that contains Poison (P). The board may contain Walls (W). The rabbit cannot break the wall, and if the rabbit is in the cell next to the wall, it remains in the cell where it is, even if commanded to move towards the wall. The user moves the rabbit (*) by giving directions to the computer about which direction it is to be moved. There are four allowed moves: Right (R), Left (L), Up (U), and Down (D). The rabbit can move one cell at a time.

Example Input:

Please enter feeding map as a list:
[[’W’, ’X’, ’W’, ’C’, ’X’], [’A’, ’X’, ’X’, ’A’, ’W’], [’C’, ’X’, ’X’,
’X’, ’P’], [’X’, ’X’, ’X’, ’X’, ’X’], [’X’, ’*’, ’X’, ’X’, ’X’]]
Please enter direction of movements as a list:
[’U’,’U’,’L’,’U’,’L’]

Example Output:

Your board is:

W X W C X

A X X A W

C X X X P

X X X X X

X * X X X

Your final board is:
W X W C X
* X X A W
X X X X P
X X X X X
X X X X X
Your score is: 15
