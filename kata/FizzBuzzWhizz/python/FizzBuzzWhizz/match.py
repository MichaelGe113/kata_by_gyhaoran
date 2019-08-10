#!/usr/bin/env python3


class Match():

    def __init__(self, sp1=3, sp2=5, sp3=7):
        self._sp1 = sp1
        self._sp2 = sp2
        self._sp3 = sp3

    def _match_rules(self, num):
        return "Fizz"*(num%self._sp1==0) + "Buzz"*(num%self._sp2==0) + "Whizz"*(num%self._sp3==0) or num

    def match(self, num):
        return self._match_rules(num) if "3" not in str(num) else "Fizz"
