#!/usr/bin/env python3


class CheckSum():
    
    def _sum(self, value):
        return sum([(len(value) - i) * int(element) for i, element in enumerate(value)])

    def _check_sum(self, value):
        return self._sum(value) % 11        

    def check(self, value):
        return len(value) == 9 and self._check_sum(value) == 0
