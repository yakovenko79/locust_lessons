from locust import task, between, User, constant, constant_pacing
from datetime import datetime


class MyUser(User):
    # wait_time = between(1, 3)
    # wait_time = constant(3)
    wait_time = constant_pacing(5)

    @task
    def login(self):
        print(datetime.now())
