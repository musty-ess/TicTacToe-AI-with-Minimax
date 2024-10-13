# Tic-Tac-Toe AI with Minimax

This project implements an AI that plays Tic-Tac-Toe optimally using the Minimax algorithm. The AI is designed to never lose when played against, as Tic-Tac-Toe, when played optimally by both players, always results in a tie. The project includes a graphical interface for easy interaction.

## Getting Started

To get started with the project, follow the steps below:

1. **Clone the project**: You can clone the project using: `https://github.com/musty-ess/tic-tac-toe.git`
   
2. **Install dependencies**: After cloning the repo, navigate to the project directory and run the following command to install the necessary Python package (`pygame`): `pip3 install -r requirements.txt`
3. **Run the game**: The command for running the game is: `python runner.py`

![Sample Output](assets/output_sample.png)

## Project Overview

The project consists of two main files:

- **`runner.py`**: This file contains the graphical interface for playing Tic-Tac-Toe.  
- **`tictactoe.py`**: This file contains the core game logic and is where the AI is implemented using the Minimax algorithm.

## How the Game Works

The game board is represented as a 3x3 grid where each cell can contain either:

- **X**: Player X's move
- **O**: Player O's move
- **EMPTY**: An empty cell

## Functions

Inside `tictactoe.py`:

1. **`player(board)`**: Returns the player who has the next turn on the board (either X or O). In the initial state, X always goes first.

2. **`actions(board)`**: Returns a set of all possible moves on the board. Each move is represented as a tuple `(i, j)` where `i` is the row and `j` is the column of the move.

3. **`result(board, action)`**: Takes the current board and an action, and returns a new board with the action applied. The original board remains unchanged.

4. **`winner(board)`**: Determines if there is a winner on the current board. It returns `X` if player X wins, `O` if player O wins, and `None` if there is no winner yet.

5. **`terminal(board)`**: Checks if the game is over, either because a player has won or the board is full (tie). Returns `True` if the game is over, `False` otherwise.

6. **`utility(board)`**: Returns the utility of the board. The utility is `1` if X has won, `-1` if O has won, and `0` if it's a tie.

7. **`minimax(board)`**: This function implements the Minimax algorithm to determine the optimal move for the player whose turn it is. If the game is over (i.e., the board is terminal), it returns `None`. Otherwise, it returns the optimal move `(i, j)`.

## Key Considerations

- **Immutable Board States**: In the `result()` function, I avoided modifying the original board directly. Instead, I created a deep copy and returned the modified version.

- **Optimal Play**: The AI is designed to play optimally using Minimax, so it should never lose. If both players play optimally, the game will always result in a tie.

- **Efficiency**: Alpha-beta pruning was used to improve the efficiency of the Minimax algorithm

## Conclusion

By implementing the Minimax algorithm and completing the core game logic, I was able to create an unbeatable Tic-Tac-Toe AI. The game is now fully functional with a user-friendly interface, and the AI always ensures an optimal outcome.

Feel free to play against the AI yourself—you won't be able to beat it!

# tic-tac-toe
