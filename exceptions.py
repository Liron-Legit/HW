class EventWithoutHandler(BaseException):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class InvalidHandler(BaseException):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class StartHourBiggerThanEndHour(BaseException):
    def __init__(self):
        self.message = "Start hour must be smaller than the end hour"
        super().__init__(self.message)


class InvalidHours(BaseException):
    def __init__(self):
        self.message = "Start and End hours must be between 0 to 23"
        super().__init__(self.message)


class InvalidTimerange(BaseException):
    def __init__(self):
        self.message = "Time range must be a positive number"
        super().__init__(self.message)
