from scrapy_heroku.utils import get_spider_queues
from scrapyd.poller import QueuePoller


class Psycopg2QueuePoller(QueuePoller):
    def update_projects(self):
        self.queues = get_spider_queues(self.config)
