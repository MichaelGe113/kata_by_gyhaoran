#!/usr/bin/env python3

from bankocr.alternative import Alternative
from bankocr.check_sum import CheckSum
from bankocr.line import Line
from bankocr.validator import Validator, MAX_LINE


class Account(Alternative, CheckSum):
    __slots__ = ('line', 'validator')

    def __init__(self):
        super().__init__()
        self.line = Line()
        self.validator = Validator()

    def _illegible(self, account):
        return account.find("?") != -1
    
    def _valid(self, account):
        account = self.line.parse(account)
        return not self._illegible(account) and self.check(account)

    def _list_alt_set(self):
        res = ""
        for i, element in enumerate(self.alt):
            if i != len(self.alt) - 1:
                res = res + "'" + element + "', "
            else:
                res = res + "'" + element + "'"
        return res

    def _guess(self, account):
        self.alter(account)
        account = self.line.parse(account)
        if len(self.alt) == 1:
            return self.alt[0]
        elif len(self.alt) > 1:
            return account + " AMB [" + self._list_alt_set() + "]"
        elif self._illegible(account):
            return account + " ILL"
        else:
            return account + " ERR"

    def _decode_file(self, fin):
        return [line.strip('\n') for i, line in enumerate(fin.readlines()) if (i + 1) % 4 != 0]

    def _get_account_list(self, fin):
        line_lists = self._decode_file(fin)
        return [line_lists[i:i+MAX_LINE]  for i in range(0, len(line_lists), MAX_LINE)]

    def parse_account(self, account):
        account = self.validator.normalize(account)
        if self._valid(account):
            return self.line.parse(account)
        else:
            return self._guess(account)

    def parse(self, fin):
        return [self.parse_account(account) for account in self._get_account_list(fin)]
