#!/usr/bin/env python3

import pytest
from bankocr import Account


class Test_Account():

    def setup_method(self):
        self.act = Account()

    def test_no_guess(self):
        assert self.act.parse_account([" _                         ",
                                       "  |  |  |  |  |  |  |  |  |",
                                       "  |  |  |  |  |  |  |  |  |"
                                       ]) == "711111111"

    def test_only_one_guess(self):
        assert self.act.parse_account(["                           ",
                                       "  |  |  |  |  |  |  |  |  |",
                                       "  |  |  |  |  |  |  |  |  |"
                                       ]) == "711111111"

        assert self.act.parse_account([" _  _  _  _  _  _  _  _  _ ",
                                       "  |  |  |  |  |  |  |  |  |",
                                       "  |  |  |  |  |  |  |  |  |"
                                       ]) == "777777177"

    def test_AMB_88888888(self):        
        assert self.act.parse_account([" _  _  _  _  _  _  _  _  _ ",
                                       "|_||_||_||_||_||_||_||_||_|",
                                       "|_||_||_||_||_||_||_||_||_|"
                                       ]) == "888888888 AMB ['888886888', '888888988', '888888880']"

    def test_ERR_no_valid_alternatives(self):
        assert self.act.parse_account(["                           ",
                                       "|_||_||_||_||_||_||_||_||_|",
                                       "  |  |  |  |  |  |  |  |  |"
                                       ]) == "444444444 ERR"

    def test_contains_one_illegible_digit(self):
        assert self.act.parse_account([" _     _  _  _  _  _  _    ",
                                       "| || || || || || || ||_   |",
                                       "|_||_||_||_||_||_||_| _|  |"
                                       ]) == "000000051"

    def test_contains_one_illegible_digit_but_no_alternative(self):
        assert self.act.parse_account(["    _  _  _  _  _  _     _ ",
                                       "|_||_|| || ||_   |  |  | _ ",
                                       "  | _||_||_||_|  |  |  | _|"
                                       ]) == "49006771? ILL"

    def test_contains_two_or_more_illegible_digit(self):
        assert self.act.parse_account(["    _  _  _  _  _  _     _ ",
                                       "|_||_|| ||_||_   |  |  | _ ",
                                       "    _||_||_||_|  |  |  | _|"
                                       ]) == "?9086771? ILL"

    def test_should_append_missing_space_at_end_lines(self):
        assert self.act.parse_account([" _",
                                       "  |  |  |  |  |  |  |  |  |",
                                       "  |  |  |  |  |  |  |  |  |"
                                       ]) == "711111111"

    def test_should_rtrim_all_blanks_at_end_lines(self):
        assert self.act.parse_account([" _                             ",
                                       "  |  |  |  |  |  |  |  |  |    ",
                                       "  |  |  |  |  |  |  |  |  |    "
                                       ]) == "711111111"

    def test_8_digits_should_append_missing_spaces_at_end_lines(self):
        assert self.act.parse_account(["    _  _     _  _  _  _ ",
                                       "  | _| _||_||_ |_   ||_|",
                                       "  ||_  _|  | _||_|  ||_|"
                                       ]) == "12345678? ILL"

    def test_should_not_ltrim_blanks_at_begin_lines(self):
        with pytest.raises(Exception):
            self.act.parse_account(["   _                         ",
                                    "    |  |  |  |  |  |  |  |   ",
                                    "    |  |  |  |  |  |  |  |   "
                                    ])

    def test_should_not_rtrim_non_blanks_at_end_lines(self):
        with pytest.raises(Exception):
            self.act.parse_account([" _     _  _     _  _  _  _  _ ",
                                    "| |  | _| _||_||_ |_   ||_||_|",
                                    "|_|  ||_  _|  | _||_|  ||_| _|"
                                    ])

    def test_should_only_blank_hyphen_vertical_but_contains_x(self):
        with pytest.raises(Exception):
            self.act.parse_account([" _  _  _  _  _  _  _  _  _ ",
                                    "|_||_||_||_||_||_||_||_||_|",
                                    "|_||_||_||_|x_||_||_||_||_|",
                                    ])

    def test_should_be_3_lines(self):
        with pytest.raises(Exception):
            self.act.parse_account(["  |  |  |  |  |  |  |  |  |",
                                    "  |  |  |  |  |  |  |  |  |"
                                    ])

    def test_parse_account_file(self):
        with open('./tests/input.txt', 'r') as fin:
            assert self.act.parse(fin) == ["777777177", "444444444 ERR"]
