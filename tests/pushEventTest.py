import unittest

from exceptions import StartHourBiggerThanEndHour, InvalidHours
from suspicious_behaviors.Push import Push


class PushEventTest(unittest.TestCase):

    def test_raise_exception_when_starthour_bigger_than_endhour(self):
        with self.assertRaises(StartHourBiggerThanEndHour):
            Push(None, 20, 13, "nothing")

    def test_raise_exception_when_starthour_not_valid(self):
        with self.assertRaises(InvalidHours):
            Push(None, 24, 25, "nothing")
        with self.assertRaises(InvalidHours):
            Push(None, -9, 13, "nothing")

    def test_raise_exception_when_endhour_not_valid(self):
        with self.assertRaises(InvalidHours):
            Push(None, 20, 24, "nothing")

    def test_isSuspicious_returns_true_when_push_in_range(self):
        request = {
            "repository":
                {"full_name": "Liron-Legit/test", "pushed_at": 1717850404},
            "pusher":
                {"name": 'lironna'}
        }
        push_event = Push(None, 14, 16, "sus!")
        self.assertEqual(push_event.is_suspicious(request), True)

    def test_isSuspicious_returns_false_when_push_not_in_range(self):
        request = {
            "repository":
                {"full_name": "Liron-Legit/test", "pushed_at": 1717850404},
            "pusher":
                {"name": 'lironna'}
        }
        push_event = Push(None, 20, 23, "sus!")
        self.assertEqual(push_event.is_suspicious(request), False)


if __name__ == '__main__':
    unittest.main()
