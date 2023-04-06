from players import HumanPlayer,ComputerPlayer

class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    def printing_the_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | ' . join(row) + ' |')

    @staticmethod
    def print_the_board_nums():
        board_nums = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in board_nums:
            print('| ' + ' | ' . join(row) + ' |')

    def available_moves(self):
        return [i for i ,spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def number_of_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self,square,player_letter):
        if self.board[square] == ' ':
            self.board[square] = player_letter
            if self.winner(square,player_letter):
                self.current_winner = player_letter
            return True
        return False
    
    def winner(self,square,player_letter):
        row_index = square // 3 
        row = self.board[row_index*3 : (row_index+1)*3]
        if all([spot == player_letter for spot in row]):
            return True
        
        column_index = square % 3
        column = [self.board[column_index+i*3]for i in range(3)]
        if all([spot == player_letter for spot in column]):
            return True
        
        if square % 2 == 0:
            first_diagonal = [self.board[i] for i in [0, 4, 8]]
            if all([spot == player_letter for spot in first_diagonal]):
                return True
            
            second_diagonal = [self.board[i] for i in [2, 4, 6]]
            if all([spot == player_letter for spot in second_diagonal]):
                return True
        return False
    
def play_the_game(game,player_x,player_o,print_game=True):
    if print_game:
        game.print_the_board_nums()
        
    player_letter = 'X'
    while game.empty_squares():
        if player_letter == 'O':
            square = player_o.make_move(game)
        else:
            square = player_x.make_move(game)

        if game.make_move(square,player_letter):
            if print_game:
                print(player_letter + f'𝕄𝕒𝕜𝕖𝕤 𝕒 𝕞𝕠𝕧𝕖 𝕥𝕠 {square}')
                game.printing_the_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f'°·.¸.·°¯°·.¸.·°¯°·.¸.-> 𝕎𝕚𝕟𝕟𝕖𝕣 {player_letter} !>-.¸.·°¯°·.¸.·°¯°·.¸.·°')
                return player_letter
            
            player_letter = 'O' if player_letter == 'X' else 'X'
        
    if print_game:
        print("𝕀𝕥'𝕤 𝕒 𝕋𝕚𝕖 !")

if __name__ == '__main__':
    player_x = HumanPlayer('X')
    player_o = ComputerPlayer('O')
    t = Game()
    play_the_game(t,player_x,player_o,print_game=True)


