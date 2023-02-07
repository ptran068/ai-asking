import signal
from abc import ABC

from celery import Task
from celery.utils.log import get_logger


class CeleryBaseTask(Task, ABC):
    """A custom Celery Base Task class.

    This class is used for overriding several methods from the base Task of Celery to have custom behaviors.
    Especially, in this case, we override the __call__ method to handle SIGTERM so that workers can be able to be restarted properly.
    Ref:
    https://github.com/celery/celery/issues/2700
    https://github.com/celery/celery/pull/5423
    """

    logger = get_logger(__name__)

    def __call__(self, *args, **kwargs):
        signal.signal(
            signal.SIGTERM,
            lambda signum, frame: self.logger.info(f"SIGTERM {signum} received, wait till the task finished."),
        )
        return super().__call__(*args, **kwargs)