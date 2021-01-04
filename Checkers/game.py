from enum import Enum
from abc import abstractmethod, ABCMeta
from typing import Tuple
from typing import List, Optional

letter = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
numbers = (0, 1, 2, 3, 4, 5, 6, 7)
symb = '░'
LETTER_TO_INT = dict(zip(letter, numbers))


class Spot:
    def __init__(self, y: int, x: int, piece: 'Piece' = None):
        self.x = x
        self.y = y
        self.piece = piece

    def __bool__(self):
        return self.piece is not None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.piece) if self.piece else ' '


class Color(Enum):
    WHITE = 'WHITE'
    BLACK = 'BLACK'


class Piece(metaclass=ABCMeta):

    @property
    @abstractmethod
    def display(self):
        pass

    def __init__(self, color: Color):
        self.color = color

    @staticmethod
    def get_distance(start: 'Spot', end: 'Spot') -> Tuple[int, int]:
        return abs(start.y - end.y), abs(start.x - end.x)

    @abstractmethod
    def can_move(self, start: 'Spot', end: 'Spot', board: 'Board'):
        if (start is end) or (end and end.piece.color == self.color):
            return False

    def moved(self, ):
        pass

    def __str__(self):
        return self.display[self.color]


class Bishop(Piece):
    display = {
        Color.WHITE: '♗',
        Color.BLACK: '♝',
    }

    def can_move(self, start: 'Spot', end: 'Spot', board: 'Board'):
        super().can_move(start, end, board)
        dy, dx = end.y - start.y, end.x - start.x

        if abs(dx) != abs(dy):
            return False

        # Normalizing dx, dy to get directions
        # ნორმალიზება dx, dy ცვლადების რათა ფიგურის მოძრაობის მიმართულება გავიგოთ
        x_inc = dx // abs(dx)
        y_inc = dy // abs(dy)

        x, y = start.x, start.y
        for _ in range(abs(dx)):
            x += x_inc
            y += y_inc
            if board.get_spot(x, y):
                return False

        return True


class Player:
    def __init__(self, color: 'Color', turn):
        self.color = color
        self.turn = turn

    def __bool__(self):
        return self.turn

    @staticmethod
    def ask_for_move(select: bool = False) -> [int, int]:
        text = 'სად გადავიდე: '
        if select:
            text = 'მონიშნეთ ფიგურა: '
        move = input(text)

        return LETTER_TO_INT.get(move[0].upper()), int(move[1:]) - 1


class Board:
    def __init__(self):
        self.board: 'List[List[Spot]]' = []
        self.board.append([
            Spot(0, 0, Bishop(Color.WHITE)),
            Spot(0, 1, symb),
            Spot(0, 2, Bishop(Color.WHITE)),
            Spot(0, 3, symb),
            Spot(0, 4, Bishop(Color.WHITE)),
            Spot(0, 5, symb),
            Spot(0, 6, Bishop(Color.WHITE)),
            Spot(0, 7, symb)
        ])
        self.board.append([
            Spot(1, 0, '░'),
            Spot(1, 1, Bishop(Color.WHITE)),
            Spot(1, 2, '░'),
            Spot(1, 3, Bishop(Color.WHITE)),
            Spot(1, 4, '░'),
            Spot(1, 5, Bishop(Color.WHITE)),
            Spot(1, 6, '░'),
            Spot(1, 7, Bishop(Color.WHITE))
        ])

        self.board.append([
            Spot(2, 0, Bishop(Color.WHITE)),
            Spot(2, 1, '░'),
            Spot(2, 2, Bishop(Color.WHITE)),
            Spot(2, 3, '░'),
            Spot(2, 4, Bishop(Color.WHITE)),
            Spot(2, 5, '░'),
            Spot(2, 6, Bishop(Color.WHITE)),
            Spot(2, 7, '░')
        ])

        self.board.append([
            Spot(3, 0, '░'),
            Spot(3, 1),
            Spot(3, 2, '░'),
            Spot(3, 3),
            Spot(3, 4, '░'),
            Spot(3, 5),
            Spot(3, 6, '░'),
            Spot(3, 7)
        ])
        self.board.append([
            Spot(4, 0),
            Spot(4, 1, '░'),
            Spot(4, 2),
            Spot(4, 3, '░'),
            Spot(4, 4),
            Spot(4, 5, '░'),
            Spot(4, 6),
            Spot(4, 7, '░'),
        ])
        self.board.append([
            Spot(5, 0, '░'),
            Spot(5, 1, Bishop(Color.BLACK)),
            Spot(5, 2, '░'),
            Spot(5, 3, Bishop(Color.BLACK)),
            Spot(5, 4, '░'),
            Spot(5, 5, Bishop(Color.BLACK)),
            Spot(5, 6, '░'),
            Spot(5, 7, Bishop(Color.BLACK)),
        ])
        self.board.append([
            Spot(6, 0, Bishop(Color.BLACK)),
            Spot(6, 1, '░'),
            Spot(6, 2, Bishop(Color.BLACK)),
            Spot(6, 3, '░'),
            Spot(6, 4, Bishop(Color.BLACK)),
            Spot(6, 5, '░'),
            Spot(6, 6, Bishop(Color.BLACK)),
            Spot(6, 7, '░'),
        ])
        self.board.append([
            Spot(7, 0, '░'),
            Spot(7, 1, Bishop(Color.BLACK)),
            Spot(7, 2, '░'),
            Spot(7, 3, Bishop(Color.BLACK)),
            Spot(7, 4, '░'),
            Spot(7, 5, Bishop(Color.BLACK)),
            Spot(7, 6, '░'),
            Spot(7, 7, Bishop(Color.BLACK)),
        ])

    def __str__(self):
        board = "   ---------------------------------------"
        for y in range(7, -1, -1):
            board += f'\n {y + 1}|'
            for x in range(0, 8):
                board += f' [{self.board[y][x]}] '
        board += "\n   ---------------------------------------\n"
        board += '     A    B    C    D    E    F    G    H'
        return board

    def get_spot(self, x, y):
        # @TODO: return if possible
        return self.board[y][x]


class GameStatus(Enum):
    ACTIVE = 'ACTIVE'
    FOREFIET = 'FORFEIT'


class Game:
    def __init__(self):
        self.board = Board()
        self.player_1 = Player(Color.WHITE, True)
        self.player_2 = Player(Color.BLACK, False)
        self.current_player = self.player_1 or self.player_2
        self.status = GameStatus.ACTIVE

    def run(self):
        print(self.board)
        while self.status == GameStatus.ACTIVE:
            move = self.get_valid_move()
            if move is None:
                self.status = GameStatus.FOREFIET
                break

            self.make_move(*move)
            self.update_turn()
            print(self.board)

    def update_turn(self):
        """ Updates Turn """
        self.player_1.turn = not self.player_1
        self.player_2.turn = not self.player_2
        self.current_player = self.player_1 or self.player_2

    @staticmethod
    def make_move(start: Spot, end: Spot):
        piece = start.piece
        start.piece = None
        end.piece = piece
        piece.moved()

    def get_valid_move(self) -> Optional[Tuple[Spot, Spot]]:
        while True:
            try:
                user_start = self.current_player.ask_for_move(select=True)
                if user_start is None:
                    y = input('დარწმუნებული ხარ რომ გინდა დანებდე ?: [დიახ|არა] ')
                    if y == 'დიახ':
                        return None
                user_end = self.current_player.ask_for_move()

                start: Spot = self.board.get_spot(*user_start)
                end: Spot = self.board.get_spot(*user_end)

                valid = start.piece and self.current_player.color == start.piece.color and start.piece.can_move(start, end, self.board)
                if valid:
                    return start, end
            except (IndexError, KeyError, ValueError):
                pass


if __name__ == '__main__':
    g = Game()
    g.run()
