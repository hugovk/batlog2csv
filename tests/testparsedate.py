import unittest

from batlog2csv import Batlog2Csv


class TestParseDate(unittest.TestCase):
    def test_standard_date(self):
        date_string = "Mon Sep 12 13:29:00 CDT 2013"
        year = 2013
        month = 9
        day = 12
        hour = 13
        minute = 29
        second = 0

        parsed_date, key, is_date = Batlog2Csv.parse_date(date_string)

        self.assertEqual(parsed_date.year, year)
        self.assertEqual(parsed_date.month, month)
        self.assertEqual(parsed_date.day, day)
        self.assertEqual(parsed_date.hour, hour)
        self.assertEqual(parsed_date.minute, minute)
        self.assertEqual(parsed_date.second, second)

    def test_bst_date(self):
        date_string = "Fri 16 Aug 2013 21:47:02 BST"
        year = 2013
        month = 8
        day = 16
        hour = 21
        minute = 47
        second = 2

        parsed_date, key, is_date = Batlog2Csv.parse_date(date_string)

        self.assertEqual(parsed_date.year, year)
        self.assertEqual(parsed_date.month, month)
        self.assertEqual(parsed_date.day, day)
        self.assertEqual(parsed_date.hour, hour)
        self.assertEqual(parsed_date.minute, minute)
        self.assertEqual(parsed_date.second, second)

    def test_datetime_date(self):
        date_string = "2013-11-05 18:11:00"
        year = 2013
        month = 11
        day = 5
        hour = 18
        minute = 11
        second = 0

        parsed_date, key, is_date = Batlog2Csv.parse_date(date_string)

        self.assertEqual(parsed_date.year, year)
        self.assertEqual(parsed_date.month, month)
        self.assertEqual(parsed_date.day, day)
        self.assertEqual(parsed_date.hour, hour)
        self.assertEqual(parsed_date.minute, minute)
        self.assertEqual(parsed_date.second, second)


if __name__ == '__main__':
    unittest.main()