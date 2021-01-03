class Board:
    def __init__(self, board5):
        self.board = []
        for i in range(len(board5)):
            self.board.append(board[i])
        self.board = board5

    def __str__(self):
        display = '-------------\n| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |\n-------------\n' \
                  '| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |\n-------------\n' \
                  '| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |\n-------------\n'
        return display

    @staticmethod
    def space_check(pos):
        if board[pos] == ' ':
            return True
        else:
            return False

    @staticmethod
    def win_check(mark):
        return ((board[1] == board[2] == board[3] == mark) or
                (board[4] == board[5] == board[6] == mark) or
                (board[7] == board[8] == board[9] == mark) or
                (board[1] == board[4] == board[7] == mark) or
                (board[2] == board[5] == board[8] == mark) or
                (board[3] == board[6] == board[9] == mark) or
                (board[1] == board[5] == board[9] == mark) or
                (board[3] == board[5] == board[7] == mark))

    @staticmethod
    def full_board():
        for i, elem in enumerate(board):
            if board[i] == ' ':
                return False
        return True

    @staticmethod
    def play_again():
        while True:
            ans = input("Play again: Y/N ")
            if ans.upper() == "N":
                return True
            elif ans.upper() == "Y":
                return False
            else:
                continue


class Player:
    def __init__(self, name, marker='X', turn=False):
        self.name = name
        self.marker = marker
        self.turn = turn

    def player_pos(self):
        while True:
            pos = input(f"Please, {self.name} Enter Your position choice from 1  to 9: ")
            if pos.isdigit() and int(pos) in range(1, 10) and Board.space_check(int(pos)):
                return int(pos)

    def place_marker(self, pos):
        board[pos] = self.marker


if __name__ == "__main__":
    name1 = input("Enter Player name: ")
    player1 = Player(name1)
    name2 = input("Enter Player_2 name: ")
    player2 = Player(name2, 'O')
    cur_player = player1
    game_on = True
    while game_on:
        board = [' '] * 10
        board[0] = 'PlayGame'
        b = Board(board)
        print(b)
        while True:
            position = cur_player.player_pos()
            cur_player.place_marker(position)
            marked = cur_player.marker
            print(b)
            if b.win_check(marked):
                print(f"Congratulation, {cur_player.name} win Game!\n")
                if cur_player == player1:
                    cur_player = player2
                else:
                    cur_player = player1
                break

            if b.full_board():
                print('Game is Pie!\n')
                break

            if cur_player == player1:
                cur_player = player2
            else:
                cur_player = player1

        if b.play_again():
            game_on = False
