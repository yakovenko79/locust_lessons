from locust import task, between, HttpUser, User


class MyWebUser(User):
    wait_time = between(1, 2)
    weight = 3

    @task
    def login(self):
        print("I am login web url")


class MyMobileUser(User):
    wait_time = between(1, 2)
    weight = 1

    @task
    def login(self):
        print("I am login mobile url")
