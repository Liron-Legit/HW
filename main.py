from fastapi import FastAPI, Request
import logging
from exceptions import EventWithoutHandler, InvalidHandler
from factories.EventFactory import EventFactory

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.ERROR)

app = FastAPI()
eventFactory = EventFactory()


@app.post("/")
async def github_webhook_receiver(request: Request):
    event_type = request.headers["X-GitHub-Event"]
    request_as_json = await request.json()
    try:
        event = eventFactory.get_event(event_type)
        if event.is_suspicious(request_as_json):
            event.notify(request_as_json)

    except (EventWithoutHandler, InvalidHandler) as ex:
        logger.error(ex.message)
