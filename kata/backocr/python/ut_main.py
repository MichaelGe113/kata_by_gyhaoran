#!/usr/bin/env python3

import pytest


def main():
    ut_list = ['tests',
               '--cov=./bankocr',
               '-v'
              ]
    pytest.main(ut_list)


if __name__ == '__main__':
    main()
