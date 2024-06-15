from locust import task, between, User


class MyUser(User):
    wait_time = between(1, 2)

    def on_start(self):
        print("I am login url")

    @task
    def doing_work(self):
        print("I am doing smthng work")

    def on_stop(self):
        print("I am logging out")

