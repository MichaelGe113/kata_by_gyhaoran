#!/usr/bin/env python3

from FizzBuzzWhizz.match import Match


class Test_Match():

    def setup_method(self):
        self.mtch = Match(3, 5, 7)

    def test_num_output(self):
        assert self.mtch.match(1) == 1

    def test_rule_fizz_buzz_whizz_only(self):
        assert self.mtch.match(3) == 'Fizz'
        assert self.mtch.match(5) == 'Buzz'
        assert self.mtch.match(7) == 'Whizz'

    def test_rule_fizz_buzz_whizz_combine(self):
        assert self.mtch.match(15) == 'FizzBuzz'
        assert self.mtch.match(70) == 'BuzzWhizz'
        assert self.mtch.match(105) == 'FizzBuzzWhizz'

    def test_num_contain_first_special_num(self):
        assert self.mtch.match(13) == 'Fizz'
        assert self.mtch.match(35) == 'Fizz'
