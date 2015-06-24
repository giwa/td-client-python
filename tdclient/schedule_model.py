#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

from tdclient.model import Model
from tdclient.job_model import Job

class ScheduledJob(Job):
    """Scheduled job on Treasure Data Service
    """
    def __init__(self, client, scheduled_at, job_id, type, query, **kwargs):
        super(ScheduledJob, self).__init__(client, job_id, type, query, **kwargs)
        self._scheduled_at = scheduled_at

    @property
    def scheduled_at(self):
        """
        Returns: a :class:`datetime.datetime` represents the schedule of next invocation of the job
        """
        return self._created_at

    def __str__(self):
        print_fmt = "{class_name}(scheduled_at={scheduled_at})"
        scheduled_job_str = print_fmt.format(scheduled_at=self.scheduled_at)
        return scheduled_job_str

class Schedule(Model):
    """Schedule on Treasure Data Service
    """

    def __init__(self, client, name, cron, query, database=None, result_url=None, timezone=None, delay=None, next_time=None, priority=None, retry_limit=None, org_name=None):
        super(Schedule, self).__init__(client)
        self._name = name
        self._cron = cron
        self._query = query
        self._database = database
        self._result_url = result_url
        self._timezone = timezone
        self._delay = delay
        self._next_time = next_time
        self._priority = priority
        self._retry_limit = retry_limit
        self._org_name = org_name

    @property
    def name(self):
        """
        TODO: add docstring
        """
        return self._name

    @property
    def cron(self):
        """
        TODO: add docstring
        """
        return self._cron

    @property
    def query(self):
        """
        TODO: add docstring
        """
        return self._query

    @property
    def database(self):
        """
        TODO: add docstring
        """
        return self._database

    @property
    def result_url(self):
        """
        TODO: add docstring
        """
        return self._result_url

    @property
    def timezone(self):
        """
        TODO: add docstring
        """
        return self._timezone

    @property
    def delay(self):
        """
        TODO: add docstring
        """
        return self._delay

    @property
    def priority(self):
        """
        TODO: add docstring
        """
        return self._priority

    @property
    def retry_limit(self):
        """
        TODO: add docstring
        """
        return self._retry_limit

    @property
    def org_name(self):
        """
        TODO: add docstring
        """
        return self._org_name

    @property
    def next_time(self):
        """
        TODO: add docstring
        """
        return self._next_time

    def run(self, time, num):
        """
        TODO: add docstring
        """
        return self._client.run_schedule(time, num)

    def __str__(self):
        print_fmt = """\
{class_name}(
    name={name},
    cron={cron},
    query={query},
    database={database},
    result_url={result_url},
    timezone={timezone},
    delay={delay},
    next_time={next_time},
    priority={priority},
    retry_limit={retry_limit},
    org_name={org_name}
)
"""

        schedule_str = print_fmt.format(
            name=self.name,
            cron=self.name,
            query=self.query,
            database=self.database,
            result_url=self.result_url,
            timezone=self.timezone,
            delay=self.dealy,
            next_time=self.next_time,
            priority=self.priority,
            retry_limit=self.retry_limit,
            org_name=self.org_name
            )

        return schedule_str
