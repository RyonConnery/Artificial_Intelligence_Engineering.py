# Define the Tic-Tac-Toe board
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_winner = None  # Track the winner

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return len(self.available_moves())

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter

            if self.winner(square, letter):
                self.current_winner = letter

            return True

        return False

    def winner(self, square, letter):
        # Check rows
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]

        if all([s == letter for s in row]):
            return True

        # Check columns
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]

        if all([s == letter for s in column]):
            return True

        # Check diagonals
        if square % 2 == 0:  # Only even-numbered squares can be on a diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]

            if all([s == letter for s in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]

            if all([s == letter for s in diagonal2]):
                return True

        return False


# Minimax algorithm with Alpha-Beta Pruning
def minimax(state, depth, alpha, beta, maximizing_player):
    valid_moves = state.available_moves()

    if (
        depth == 0
        or not state.empty_squares()
        or state.current_winner is not None
    ):
        if state.current_winner == 'X':
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() + 1)
            }

        elif state.current_winner == 'O':
            return {
                'position': None,
                'score': -1 * (state.num_empty_squares() + 1)
            }

        else:
            return {
                'position': None,
                'score': 0
            }

    if maximizing_player:
        best = {
            'position': None,
            'score': -float('inf')
        }

        for move in valid_moves:
            state.make_move(move, 'X')

            sim_score = minimax(
                state,
                depth - 1,
                alpha,
                beta,
                False
            )

            state.board[move] = ' '
            state.current_winner = None

            sim_score['position'] = move

            if sim_score['score'] > best['score']:
                best = sim_score

            alpha = max(alpha, best['score'])

            if beta <= alpha:
                break

        return best

    else:
        best = {
            'position': None,
            'score': float('inf')
        }

        for move in valid_moves:
            state.make_move(move, 'O')

            sim_score = minimax(
                state,
                depth - 1,
                alpha,
                beta,
                True
            )

            state.board[move] = ' '
            state.current_winner = None

            sim_score['position'] = move

            if sim_score['score'] < best['score']:
                best = sim_score

            beta = min(beta, best['score'])

            if beta <= alpha:
                break

        return best


# Play the game
def play_game():
    game = TicTacToe()
    game.print_board()

    human_letter = input("Choose your letter (X or O): ").upper()
    ai_letter = 'X' if human_letter == 'O' else 'O'

    current_letter = 'X'  # X starts the game

    while game.empty_squares():

        if current_letter == human_letter:
            square = int(input("Enter your move (0-8): "))

            if game.make_move(square, human_letter):

                if game.current_winner:
                    print(f"{human_letter} wins!")
                    break

            else:
                print("Invalid move. Try again.")
                continue

        else:
            maximizing_player = ai_letter == 'X'

            move = minimax(
                game,
                len(game.available_moves()),
                -float('inf'),
                float('inf'),
                maximizing_player
            )['position']

            game.make_move(move, ai_letter)

            if game.current_winner:
                print(f"{ai_letter} wins!")
                break

        current_letter = 'O' if current_letter == 'X' else 'X'
        game.print_board()

    if not game.current_winner:
        print("It's a tie!")


# Run the game
if __name__ == "__main__":
    play_game()
