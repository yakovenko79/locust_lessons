from locust import task, between, HttpUser


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = 'http://newtours.demoaut.com/'

    @task
    def login(self):
        print("I am login url")
