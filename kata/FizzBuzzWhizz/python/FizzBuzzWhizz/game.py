#!/usr/bin/env python3

from FizzBuzzWhizz.match import Match


class Game():

    def __init__(self, n=100):
        self._num = n + 1

    def game(self, sp1=3, sp2=5, sp3=7):
        return [Match(sp1, sp2, sp3).match(i) for i in range(1, self._num)]
