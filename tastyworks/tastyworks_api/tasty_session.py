import logging

from tastyworks.models import session

LOGGER = logging.getLogger(__name__)


def create_new_session(username, password, token=None):
    return session.TastyAPISession(username, password, token)
