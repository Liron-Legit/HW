import unittest

from exceptions import InvalidTimerange
from suspicious_behaviors.RepositoryDeleted import RepositoryDeleted


class RepositoryDeletedTest(unittest.TestCase):

    def test_raise_exception_when_range_is_negative(self):
        with self.assertRaises(InvalidTimerange):
            RepositoryDeleted(None, -10, "nothing")

    def test_raise_exception_when_range_is_zero(self):
        with self.assertRaises(InvalidTimerange):
            RepositoryDeleted(None, 0, "nothing")

    def test_isSuspicious_returns_true_when_delete_is_in_range(self):
        request = {
            "action": "deleted",
            "repository": {
                "created_at": "2024-06-08T15:17:51Z",
                "updated_at": "2024-06-08T15:22:29Z"
            }
        }
        repository_created_event = RepositoryDeleted(None, 10, "nothing")
        self.assertEqual(repository_created_event.is_suspicious(request), True)

    def test_isSuspicious_returns_false_when_delete_is_not_in_range(self):
        request = {
            "action": "deleted",
            "repository": {
                "created_at": "2024-06-08T15:17:51Z",
                "updated_at": "2024-06-08T16:22:29Z"
            }
        }
        repository_created_event = RepositoryDeleted(None, 10, "nothing")
        self.assertEqual(repository_created_event.is_suspicious(request), False)

    def test_isSuspicious_returns_false_when_action_is_not_deleted(self):
        request = {
            "action": "created"
        }

        repository_created_event = RepositoryDeleted(None, 10, "nothing")
        self.assertEqual(repository_created_event.is_suspicious(request), False)


if __name__ == '__main__':
    unittest.main()
