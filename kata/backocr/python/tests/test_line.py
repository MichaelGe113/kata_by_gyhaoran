#!/usr/bin/env python3

from bankocr import Line


class Test_Line():

    def setup_method(self):
        self.line = Line()

    def test_all_blank(self):
        assert self.line.parse(["   ",
                                "   ",
                                "   "
                                ]) == "?"

    def test_single_digit(self):
        assert self.line.parse(["   ",
                                "  |",
                                "  |"
                                ]) == "1"

    def test_hyphen_is_not_underline(self):
        assert self.line.parse([" - ",
                                " _|",
                                "|_ "
                                ]) == "?"

    def test_l_and_1_is_not_vertical_line(self):
        assert self.line.parse(["   ",
                                "  1",
                                "  |"
                                ]) == "?"

        assert self.line.parse(["   ",
                                "  l",
                                "  |"
                                ]) == "?"

    def test_three_vertical_line_is_not_1(self):
        assert self.line.parse(["  |",
                                "  |",
                                "  |"
                                ]) == "?"

    def test_error_position_of_vertical_line_is_not_1(self):
        assert self.line.parse(["|  ",
                                "|  ",
                                "   "
                                ]) == "?"

        assert self.line.parse(["   ",
                                "|  ",
                                "|  "
                                ]) == "?"

        assert self.line.parse(["  |",
                                "  |",
                                "   "
                                ]) == "?"

        assert self.line.parse([" | ",
                                " | ",
                                "   "
                                ]) == "?"

        assert self.line.parse(["   ",
                                " | ",
                                " | "
                                ]) == "?"

    def test_contains_illegible_digit_x(self):
        assert self.line.parse(["    _  _ ",
                                "  | _| _|",
                                "  ||_ x_|"
                                ]) == "12?"

    def test_all_digit(self):
        assert self.line.parse([" _     _  _     _  _  _  _  _ ",
                                "| |  | _| _||_||_ |_   ||_||_|",
                                "|_|  ||_  _|  | _||_|  ||_| _|"
                                ]) == "0123456789" 
