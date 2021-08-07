from datetime import datetime

from django_celery_beat.models import IntervalSchedule, PeriodicTask

from .tasks import show_future_date_sample_task


def initial_show_future_date_sample_task():
    """This function creates a period task to execute based on period time.

    The first line creates a record of the interval schedule information of
    the task execution into the database and in the second line creates or updates
    the period of the task execution. Finally, execute the task.
    """
    interval_obj, created = IntervalSchedule.objects.get_or_create(
        every=12, period=IntervalSchedule.HOURS)

    PeriodicTask.objects.update_or_create(
        interval=interval_obj,
        name=f'show_future_date_{datetime.now().date()}',
        task="show_future_date",
        defaults={
            "kwargs": {
                "date": datetime.now().date(),
            },
        })
    task_id = show_future_date_sample_task.delay(date=datetime.now().date())
    return task_id
