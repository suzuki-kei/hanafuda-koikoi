

from koikoi import Game
from koikoi import SimplePlayer


def main():
    player1 = SimplePlayer()
    player2 = SimplePlayer()
    game = Game(player1, player2)
    while not game.is_over():
        print(game)
        game.next()


if __name__ == "__main__":
    main()

