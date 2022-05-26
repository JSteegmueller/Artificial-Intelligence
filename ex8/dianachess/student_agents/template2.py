import copy
import random

from ChessEngine import GameState, Move

pawn_values = {
    "K": 10,
    "R": 5,
    "B": 3,
    "N": 3,
    "p": 1
}


class Agent:
    def __init__(self):
        self.move_queue = None
        self.gs_simulator = GameState()
        self.alpha = -1
        self.alphaMove = None
        self.beta = 20

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
        # TODO
        self.minMax(gs)
        return

    def evaluateBoard(self, gs: GameState):
        print(gs.board)
        pawnCount = 0
        for field in gs.board:
            if field[0] == 'w':
                pawnCount += pawn_values[field[1]]
        return pawnCount

    def minMax(self, gs: GameState):
        self.gs_simulator = GameState()
        self.gs_simulator.board = copy.copy(gs.board)
        for wmove in self.gs_simulator.getValidMoves():
            # White move
            self.gs_simulator.makeMove(wmove)
            # Black move
            beta = 20
            for bmove in self.gs_simulator.getValidMoves():
                self.gs_simulator.makeMove(bmove)
                eval = self.evaluateBoard(self.gs_simulator)
                print(eval)
                if eval < self.alpha:
                    self.gs_simulator.undoMove()
                    break
                if eval < beta:
                    beta = eval
                self.gs_simulator.undoMove()
            if beta > self.alpha:
                self.alpha = beta
                self.update_move(wmove, 0, 0)
            self.gs_simulator.undoMove()
        return



