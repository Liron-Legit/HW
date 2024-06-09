import unittest
from suspicious_behaviors.TeamCreated import TeamCreated


class TeamCreatedTest(unittest.TestCase):

    def test_isSuspicious_returns_true_when_team_contains_prefix(self):
        request = {
            "action": "created",
            "team": {
                "name": "hacker something"
            }
        }
        team_created_event = TeamCreated(None, "hacker", "sus!")
        self.assertEqual(team_created_event.is_suspicious(request), True)

    def test_isSuspicious_returns_true_when_team_contains_prefix_capital_letters(self):
        request = {
            "action": "created",
            "team": {
                "name": "HaCeR something"
            }
        }
        team_created_event = TeamCreated(None, "hAcEr", "sus!")
        self.assertEqual(team_created_event.is_suspicious(request), True)

    def test_isSuspicious_returns_false_when_team_doesnt_contains_prefix(self):
        request = {
            "action": "created",
            "team": {
                "name": "something"
            }
        }
        team_created_event = TeamCreated(None, "hacker", "sus!")
        self.assertEqual(team_created_event.is_suspicious(request), False)


if __name__ == '__main__':
    unittest.main()
