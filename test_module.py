import unittest
from time_calculator import add_time


class UnitTests(unittest.TestCase):
    maxDiff = None
    def test_same_period(self):
        actual = add_time("3:30 PM", "2:12")
        expected = "5:42 PM"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12" to return "5:42 PM"')
        print("testCase 7: test_same_period = ",end = "")
        print("Passed") if actual==expected else print("Failed")

    def test_different_period(self):
        actual = add_time("11:55 AM", "3:12")
        expected = "3:07 PM"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:55 AM", "3:12" to return "3:07 PM"')
        print("testCase 1: test_different_period = ",end = "")
        print("Passed") if actual==expected else print("Failed")

    def test_next_day(self):
        actual = add_time("9:15 PM", "5:30")
        expected = "2:45 AM (next day)"
        self.assertEqual(actual, expected, 'Expected time to end with "(next day)" when it is the next day.')
        print("testCase 4: test_next_day = ",end = "")
        print("Passed") if actual==expected else print("Failed")

    def test_period_change_at_twelve(self):
        actual = add_time("11:40 AM", "0:25")
        expected = "12:05 PM"
        self.assertEqual(actual, expected, 'Expected period to change from AM to PM at 12:00')
        print("testCase 6: test_period_change_at_twelve = ",end = "")
        print("Passed") if actual==expected else print("Failed")

    def test_twenty_four(self):
        actual = add_time("2:59 AM", "24:00")
        expected = "2:59 AM (next day)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00" to return "2:59 AM"')
        print("testCase 9: test_twenty_four = ",end = "")
        print("Passed") if actual==expected else print("Failed")

    def test_two_days_later(self):
        actual = add_time("11:59 PM", "24:05")
        expected = "12:04 AM (2 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:59 PM", "24:05" to return "12:04 AM (2 days later)"')
        print("testCase 11: test_two_days_later = ",end = "")
        print("Passed") if actual==expected else print("Failed")

    def test_high_duration(self):
        actual = add_time("8:16 PM", "466:02")
        expected = "6:18 AM (20 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "8:16 PM", "466:02" to return "6:18 AM (20 days later)"')
        print("testCase 2: test_high_duration = ",end = "")
        print("Passed") if actual==expected else print("Failed")

    def test_no_change(self):
        actual = add_time("5:01 AM", "0:00")
        expected = "5:01 AM"
        self.assertEqual(actual, expected, 'Expected adding 0:00 to return initial time.')
        print("testCase 5: test_no_change = ",end = "")
        print("Passed") if actual==expected else print("Failed")

    def test_same_period_with_day(self):
        actual = add_time("3:30 PM", "2:12", "Monday")
        expected = "5:42 PM, Monday"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12", "Monday" to return "5:42 PM, Monday"')
        print("testCase 8: test_same_period_with_day = ",end = "")
        print("Passed") if actual==expected else print("Failed")

    def test_twenty_four_with_day(self):
        actual = add_time("2:59 AM", "24:00", "saturDay")
        expected = "2:59 AM, Sunday (next day)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00", "saturDay" to return "2:59 AM, Sunday (next day)"')
        print("testCase 10 : test_twenty_four_with_day = ",end = "")
        print("Passed") if actual==expected else print("Failed")

    def test_two_days_later_with_day(self):
        actual = add_time("11:59 PM", "24:05", "Wednesday")
        expected = "12:04 AM, Friday (2 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:59 PM", "24:05", "Wednesday" to return "12:04 AM, Friday (2 days later)"')
        print("testCase 12: test_two_days_later_with_day = ",end = "")
        print("Passed") if actual==expected else print("Failed")

    def test_high_duration_with_day(self):
        actual = add_time("8:16 PM", "466:02", "tuesday")
        expected = "6:18 AM, Monday (20 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "8:16 PM", "466:02", "tuesday" to return "6:18 AM, Monday (20 days later)"')
        print("testCase 3: test_high_duration_with_day = ",end = "")
        print("Passed") if actual==expected else print("Failed")

if __name__ == "__main__":
    unittest.main()
