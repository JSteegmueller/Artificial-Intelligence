from multiprocessing.queues import Queue
from numbers import Number
from typing import List

from ChessEngine import GameState, Move

pawn_values = {
    "K": 1000,
    "R": 5,
    "B": 3,
    "N": 3,
    "p": 1
}


class Agent:
    def __init__(self):
        self.move_queue = None

    def get_move(self):
        move = None
        while not self.move_queue.empty():
            move = self.move_queue.get()
        return move

    def update_move(self, move, score, depth):
        """
        :param move: Object of class Move, like a list element of gamestate.getValidMoves()
        :param score: Integer; not really necessary, just for informative printing
        :param depth: Integer; not really necessary, just for informative printing
        :return:
        """
        self.move_queue.put([move, score, depth])

    def clear_queue(self, outer_queue):
        self.move_queue = outer_queue

    def findBestMove(self, gs: GameState):
        """
        Parameters
        ----------
        gs : Gamestate
            current state of the game
        validMoves : list
            list of valid moves
        returnQueue : Queue
            multithreading queue

        Returns
        -------
        none

        """
        validMoves: List[Move] = gs.getValidMoves()
        # random.shuffle(validMoves)

        # evaluate Moves
        highscore = -1
        for move in validMoves:
            evaluateScore(move)
            if(move.score > highscore):
                highscore = move.score
                self.update_move(move=move, score=move.score, depth=-1)

        return


def evaluateScore(move: Move):
    move.score = 0
    if move.isCastleMove:
        move.score += 100
    if move.isPawnPromotion:
        move.score += 100

    if move.isCapture:
        # K King, R Rook, B Bishop, N Knight, p pawn
        cap = move.pieceCaptured[-1]
        move.score += pawn_values[cap]

    return
