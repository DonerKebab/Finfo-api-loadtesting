from locust import HttpLocust, TaskSet, task


class  WebsiteTasks(TaskSet):

    def on_start(self):
        """ Run on start for every Locust hatched """
        # set headers
        # self.client.headers['token'] = value
        ## ...

    @task
    def derivatives(self):
        endpoint = "/api/trade/derivatives/intraday"
        self.client.request(method="GET", url=endpoint)

    @task
    def market(self):
        endpoint = "/api/index/securities/vnmarket/intraday"
        self.client.request(method="GET", url=endpoint)


class LoadTesting(HttpLocust):
    task_set = WebsiteTasks
