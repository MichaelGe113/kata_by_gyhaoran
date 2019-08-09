#!/usr/bin/env python3

from functools import reduce

to_digits = {" _ "
             "| |"
             "|_|": "0",
             "   "
             "  |"
             "  |": "1",
             " _ "
             " _|"
             "|_ ": "2",
             " _ "
             " _|"
             " _|": "3",
             "   "
             "|_|"
             "  |": "4",
             " _ "
             "|_ "
             " _|": "5",
             " _ "
             "|_ "
             "|_|": "6",
             " _ "
             "  |"
             "  |": "7",
             " _ "
             "|_|"
             "|_|": "8",
             " _ "
             "|_|"
             " _|": "9",
             }

class Line():
    __slots__ = ('symbol_list')

    def __init__(self):
        self.symbol_list = []

    def _find_result(self, result):
        if to_digits.get(result) != None:
            return to_digits.get(result)
        else:
            return "?"

    def _parse_single_symbol(self, symbol):
        return self._find_result(reduce(lambda x, y: x + y, symbol))
  
    def _parse_symbols(self):
        result = ""
        for symbol in self.symbol_list:
            result = result + self._parse_single_symbol(symbol)
        return result
    
    def _transpose(self, matrix):
        new_matrix = []
        for i in range(len(matrix[0])):
            matrix1 = []
            for j in range(len(matrix)):
                matrix1.append(matrix[j][i])
            new_matrix.append(matrix1)
        return new_matrix

    def _pare_symbol_to_list(self, symbols):
        self.symbol_list = []
        for element in symbols:
            res = []
            for i in range(0, int(len(element)/3)):
                res.append(element[:3])
                element = element[3:]
            self.symbol_list.append(res)
        self.symbol_list = self._transpose(self.symbol_list)

    def parse(self, symbols):
        self._pare_symbol_to_list(symbols)
        return self._parse_symbols()
