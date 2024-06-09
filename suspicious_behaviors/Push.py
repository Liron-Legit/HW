from datetime import datetime
from suspicious_behaviors.Event import Event
from exceptions import StartHourBiggerThanEndHour, InvalidHours

MIN_START_HOUR = 0
MAX_START_HOUR = 23


class Push(Event):
    def __init__(self, notifier, start_hour, end_hour, suspicious_behavior_message):
        self.notifier = notifier
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.suspicious_behavior_message = suspicious_behavior_message

        if start_hour > end_hour:
            raise StartHourBiggerThanEndHour()
        if (start_hour < MIN_START_HOUR or start_hour > MAX_START_HOUR
                or end_hour < MIN_START_HOUR or end_hour > MAX_START_HOUR):
            raise InvalidHours()

    def is_suspicious(self, request):
        push_time_in_epoch = request["repository"]["pushed_at"]
        push_hour = datetime.fromtimestamp(push_time_in_epoch).hour
        if self.start_hour < push_hour < self.end_hour:
            return True
        return False

    def notify(self, request):
        prefix_message = f"[{datetime.now()}]"
        suffix_message = f"Repository: {request["repository"]["full_name"]}, Pusher: {request["pusher"]["name"]}"
        self.notifier.notify(prefix_message + self.suspicious_behavior_message + suffix_message)
