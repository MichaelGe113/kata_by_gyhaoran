#!/usr/bin/env python3

from FizzBuzzWhizz.game import Game


class Test_Game():

    def test_num_35(self):
        assert Game(35).game(3, 5, 7) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 
                'Whizz', 8, 'Fizz', 'Buzz', 11, 'Fizz', 'Fizz', 'Whizz', 
                'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'FizzWhizz', 22, 
                'Fizz', 'Fizz', 'Buzz', 26, 'Fizz', 'Whizz', 29, 'Fizz', 
                'Fizz', 'Fizz', 'Fizz', 'Fizz', 'Fizz']
