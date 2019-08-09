#!/usr/bin/env python3

from bankocr import CheckSum


class Test_CheckSum():

    def setup_method(self):
        self.chk = CheckSum()

    def test_valid_account_should_be_true(self):
        assert self.chk.check("000000000")
        assert self.chk.check("123456789")
    
    def test_error_account_should_be_false(self):
        assert not self.chk.check("111111111")

    def test_invalid_account_length_should_be_false(self):
        assert not self.chk.check("00000000")
        assert not self.chk.check("0000000000")
