wre_w = '○'
wre_b = '●'
otx_w = '□'
otx_b = '■'

board = [' '] * 10
board[0] = 'PlayGame'


class Board:
    def __init__(self):
        self.board = []
        for i in range(1,10):
            self.board.append(([
                Spot(i)
            ]))

    def __str__(self):
        display = '-------------\n| '+ board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |\n-------------\n' \
                  '| '+ board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |\n-------------\n' \
                  '| '+ board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |\n-------------\n'
        return display


class Marker:
    def __init__(self):
        pass


class Spot:
    def __init__(self, x, marker = ' '):
        self.x = x
        self.marker = marker


name = input("Enter Player_1 name: ")

class Player:
    def __init__(self, name, marker, turn = False):
        self.name = name
        self.marker = marker
        self.turn = turn


class Game:
    def __init__(self):
        print("Welcome to game!")


if __name__ == "__main__":

    player1 = Player(name, marker, turn = 1)
    print(player1.name)
    print(player1.marker)
    print(player1.turn)
    # print(b.turn)


