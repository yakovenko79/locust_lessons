from locust import task, between, HttpUser, SequentialTaskSet


class UserBehaviour(SequentialTaskSet):

    @task
    def launch_url(self):
        resp1 = self.client.get("/V1/index.php", name="launch")
        print(resp1.text)
        print(resp1.status_code)
        print(resp1.headers)

    @task
    def login(self):
        resp2 = self.client.post("/V1/index.php", name="login", data={'uid': 'mngr576707',
                                                              'password': 'aqegAqA',
                                                              'btnLohin': 'LOGIN'})
        print(resp2.text)
        print(resp2.status_code)
        print(resp2.headers)


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://demo.guru99.com"
    tasks = [UserBehaviour]
