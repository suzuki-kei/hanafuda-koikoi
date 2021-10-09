from koikoi import Game
from koikoi import HandJudgement
from koikoi import SimplePlayer


def main():
    player1 = SimplePlayer()
    player2 = SimplePlayer()
    hand_judgement = HandJudgement()
    game = Game(player1, player2, hand_judgement)
    while not game.is_over():
        print(game)
        game.next()


if __name__ == "__main__":
    main()

