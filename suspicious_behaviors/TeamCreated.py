from suspicious_behaviors.Event import Event
from datetime import datetime

class TeamCreated(Event):
    def __init__(self, notifier, suspicious_prefix, suspiciousBehaviorMessage):
        self.notifier = notifier
        self.suspicious_prefix = suspicious_prefix.lower()
        self.suspicious_behavior_message = suspiciousBehaviorMessage

    def is_suspicious(self, request):
        action = request["action"]
        team_name = request["team"]["name"].lower()
        if action == "created" and team_name.startswith(self.suspicious_prefix):
            return True
        return False

    def notify(self, request):
        prefix_message = f"[{datetime.now()}]"
        suffix_message = f"Team name: {request["team"]["name"]}, User who created the team: {request["sender"]["login"]}"
        self.notifier.notify(prefix_message + self.suspicious_behavior_message + suffix_message)
