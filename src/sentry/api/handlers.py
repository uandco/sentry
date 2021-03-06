from __future__ import absolute_import

from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled

from sentry.utils.snuba import RateLimitExceeded


def custom_exception_handler(exc):
    if isinstance(exc, RateLimitExceeded):
        # If Snuba throws a RateLimitExceeded then it'll likely be available
        # after another second.
        exc = Throttled(wait=1)

    return exception_handler(exc)
