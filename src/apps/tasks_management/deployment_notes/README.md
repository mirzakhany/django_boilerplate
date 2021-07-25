# Tasks management

This application enables you to store the periodic task schedule in the database and create the celery task queue.

## Models

* ``django_celery_beat.models.PeriodicTask``

This model defines a single periodic task to be run.

It must be associated with a schedule, which defines how often the task should run.

* ``django_celery_beat.models.IntervalSchedule``

A schedule that runs at a specific interval (e.g. every 5 seconds).

* `django_celery_beat.models.CrontabSchedule``

A schedule with fields like entries in cron: ``minute hour day-of-week day_of_month month_of_year.``

* ``django_celery_beat.models.PeriodicTasks``

This model is only used as an index to keep track of when the schedule has changed.

Whenever you update a ``PeriodicTask`` a counter in this table is also incremented, which tells the ``celery`` beat service to reload the schedule from the database.




## Installation

You need to install django-celery-beat and celery.

To install using ```pip```:

```bash
pip install celery
```

```bash
pip install django-celery-beat
```

After installation, add django_celery_beat to Django's settings module:

```python
INSTALLED_APPS = [
    ...,
    'django_celery_beat',
]
```

Run the ```django_celery_beat``` migrations using:

```bash
python manage.py migrate django_celery_beat
```



## Example running periodic tasks

The periodic tasks still need 'workers' to execute them. So make sure the default Celery package is installed.

Both the worker and beat services need to be running at the same time.

1- Start a Celery worker service (specify your Django project name):

```bash
celery -A [project-name] worker --loglevel=info
```

2- As a separate process, start the beat service (specify the Django scheduler):

```bash
celery -A [project-name] beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

**OR** you can use the -S (scheduler flag), for more options see ```celery beat --help```):

```bash
celery -A [project-name] beat -l info -S django
```

Now you need to execute the specific function in the ``scheduling.py``:

```python
from .scheduling import initial_show_future_date_sample_task

if __name__ == '__main__':
    initial_show_future_date_sample_task()
```

