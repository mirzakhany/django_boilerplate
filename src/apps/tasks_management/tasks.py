import logging
from datetime import datetime, timedelta

from src.proj.settings import base

from src.proj import celery_app

logger = logging.getLogger(__name__)


@celery_app.task(bind=True,
                 name="show_future_date",
                 queue=base.TASKS_MANAGEMENT_QUEUE)
def show_future_date_sample_task(date: datetime):
    """Print the future date based on the date argument.

    Args:
        date (datetime):
    """
    try:
        logger.info(f"Calling show_future_date_sample for date `{date}`")
        future_date = date + timedelta(1)
        print(future_date)
    except Exception as Ex:
        logger.exception(
            f"Exception occurred at running show future date task sample -> {str(Ex)}"
        )
