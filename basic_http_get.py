from locust import task, between, HttpUser


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://demo.guru99.com/V1"

    @task
    def launch_url(self):
        self.client.get("/index.php")
# login mngr576707
#password aqehAqA