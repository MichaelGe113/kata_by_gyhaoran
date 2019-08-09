#!/usr/bin/env python3

from functools import reduce

from bankocr.check_sum import CheckSum
from bankocr.line import Line, to_digits

like_digits = {
    "0": ["8"],
    "1": ["7"],
    "3": ["9"],
    "5": ["6", "9"],
    "6": ["5", "8"],
    "7": ["1"],
    "8": ["0", "6", "9"],
    "9": ["3", "5", "8"]
}

class Alternative():
    
    def __init__(self):
        self.alt = []
        self.chk = CheckSum()
        self.line = Line()

    def _cmp_symbol(self, src, des):
        diff_char_num = 0
        for i in range(len(src)):
            if src[i] != des[i]:
                diff_char_num = diff_char_num + 1
        return diff_char_num == 1

    def _repair_single_symbol(self, symbol):
        guess_list = [value for key, value in to_digits.items() if self._cmp_symbol(key, symbol)]
        return guess_list

    def _repair_illegible_symbol(self, symbol):
        return self._repair_single_symbol(reduce(lambda x, y: x + y, symbol))

    def _alter_illegible_account(self, account):
        if account.count("?") == 1:
            i = account.find('?')
            for x in self._repair_illegible_symbol(self.line.symbol_list[i]):
                if self.chk.check(account[:i] + x + account[i + 1:]):
                    self.alt.append(account[:i] + x + account[i + 1:])

    def _alter_no_illegible_account(self, account):
        for i, s in enumerate(account):
            if like_digits.get(s) != None:
                for x in like_digits.get(s):
                    if self.chk.check(account[:i] + x + account[i+1:]):
                        self.alt.append(account[:i] + x + account[i+1:])

    def alter(self, account):
        self.alt = []
        account = self.line.parse(account)
        if account.find("?") != -1:
            self._alter_illegible_account(account)
        else:
            self._alter_no_illegible_account(account)
