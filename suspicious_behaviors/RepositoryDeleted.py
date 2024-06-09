from suspicious_behaviors.Event import Event
from datetime import datetime
from exceptions import InvalidTimerange


class RepositoryDeleted(Event):
    def __init__(self, notifier, time_range_in_minutes, suspicious_behavior_message):
        self.notifier = notifier
        self.time_range_in_minutes = time_range_in_minutes
        self.suspicious_behavior_message = suspicious_behavior_message

        if time_range_in_minutes <= 0:
            raise InvalidTimerange()

    def is_suspicious(self, request):
        if request["action"] == "deleted":
            timestamp_created = datetime.fromisoformat(request["repository"]["created_at"])
            timestamp_deleted = datetime.fromisoformat(request["repository"]["updated_at"])
            diff_between_creation_and_deletion = ((timestamp_deleted - timestamp_created).total_seconds() // 60)
            if diff_between_creation_and_deletion <= self.time_range_in_minutes:
                return True
        return False

    def notify(self, request):
        prefix_message = f"[{datetime.now()}]"
        suffix_message = f"User who deleted the repository: {request["sender"]["login"]}"
        self.notifier.notify(prefix_message + self.suspicious_behavior_message + suffix_message)
