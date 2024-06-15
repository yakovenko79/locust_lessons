from locust import task, between, HttpUser, SequentialTaskSet


class UserBehaviour(SequentialTaskSet):

    @task
    def launch_url(self):
        with self.client.get("/V1/index.php", name="launch", catch_response=True) as resp1:
            print("resp1" + resp1.text)
        # print(resp1.text)
        # print(resp1.status_code)
        # print(resp1.headers)

    @task
    def login(self):
        with self.client.post("/V1/index.php", name="login", data={'uid': 'mngr576707',
                                                              'password': 'aqegAqA',
                                                              'btnLohin': 'LOGIN'}) as resp2:
            print("resp2" + resp2.text)
        # print(resp2.text)
        # print(resp2.status_code)
        # print(resp2.headers)


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://demo.guru99.com"
    tasks = [UserBehaviour]
