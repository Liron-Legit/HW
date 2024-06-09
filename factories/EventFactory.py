from exceptions import EventWithoutHandler, StartHourBiggerThanEndHour, InvalidHours, InvalidTimerange, InvalidHandler
from factories.NotifierFactory import NotifierFactory
from suspicious_behaviors.Push import Push
from suspicious_behaviors.TeamCreated import TeamCreated
from suspicious_behaviors.RepositoryDeleted import RepositoryDeleted
from configuration import *
import logging

PUSH_EVENT = "push"
REPOSITORY_DELETED_EVENT = "repository"
TEAM_CREATED = "team"
HANDLER_ERROR_MESSAGE_PREFIX = "Handler does not exists for: "
INVALID_HANDLER_ERROR = "There was a problem with the Push handler. See previous logs for further information."


class EventFactory():
    notifier_factory = NotifierFactory()
    push_event = None
    repository_deleted_event = None
    team_created_event = None
    logger = logging.getLogger('uvicorn.error')
    logger.setLevel(logging.ERROR)

    @staticmethod
    def get_event(event_type):
        if event_type == PUSH_EVENT:
            if EventFactory.push_event is None:
                EventFactory.create_push_event()
            return EventFactory.push_event

        elif event_type == REPOSITORY_DELETED_EVENT:
            if EventFactory.repository_deleted_event is None:
                EventFactory.create_repository_deleted_event()
            return EventFactory.repository_deleted_event

        elif event_type == TEAM_CREATED:
            if EventFactory.team_created_event is None:
                EventFactory.create_team_created_event()
            return EventFactory.team_created_event
        else:
            raise EventWithoutHandler(HANDLER_ERROR_MESSAGE_PREFIX + event_type)

    @staticmethod
    def create_push_event():
        try:
            EventFactory.push_event = Push(
                EventFactory.notifier_factory.get_notifier(NOTIFIER_TYPE),
                PUSH_EVENT_START_HOUR,
                PUSH_EVENT_END_HOUR,
                PUSH_EVENT_SUSPICIOUS_MESSAGE_PREFIX
            )
        except (StartHourBiggerThanEndHour, InvalidHours) as ex:
            EventFactory.logger.error(ex.message)
            raise InvalidHandler(INVALID_HANDLER_ERROR)

    @staticmethod
    def create_repository_deleted_event():
        try:
            EventFactory.repository_deleted_event = RepositoryDeleted(
                EventFactory.notifier_factory.get_notifier(NOTIFIER_TYPE),
                REPOSITORY_DELETED_EVENT_TIME_RANGE_IN_MINUTES,
                REPOSITORY_DELETED_EVENT_SUSPICIOUS_MESSAGE_PREFIX
            )
        except InvalidTimerange as ex:
            EventFactory.logger.error(ex.message)
            raise InvalidHandler(INVALID_HANDLER_ERROR)

    @staticmethod
    def create_team_created_event():
        EventFactory.team_created_event = TeamCreated(
            EventFactory.notifier_factory.get_notifier(NOTIFIER_TYPE),
            TEAM_CREATED_EVENT_SUSPICIOUS_PREFIX,
            TEAM_CREATED_EVENT_SUSPICIOUS_MESSAGE_PREFIX
        )
