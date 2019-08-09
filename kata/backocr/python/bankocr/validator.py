#!/usr/bin/env python3


MAX_LINE, MAX_LENGTH = 3, 27

class Validator():

    def __init__(self):
        pass

    def _check_is_blanks_end(self, symbol):
        for element in symbol:
            for i in range(MAX_LENGTH, len(element)):
                assert element[i] == " "

    def _check_chars(self, symbol):
        for element in symbol:
            for s in element:
                assert s == " " or s == "_" or s == "|"

    def _check_length(self, symbol):
        assert len(symbol) == MAX_LINE

    def _check_blank_begin(self, symbol):
        assert symbol[0][:3] != "   " or symbol[1][:3] != "   " or symbol[2][:3] != "   "

    def _check(self, symbol):
        self._check_chars(symbol)
        self._check_length(symbol)
        self._check_blank_begin(symbol)
        self._check_is_blanks_end(symbol)

    def normalize(self, symbol):
        self._check(symbol)
        
        for i, element in enumerate(symbol):
            if len(element) < MAX_LENGTH:
                symbol[i] = element.ljust(MAX_LENGTH)
            elif len(element) > MAX_LENGTH:
                symbol[i] = element[:MAX_LENGTH]
        
        return symbol
