from locust import task, between, User, events


@events.test_start.add_listener
def script_start(**kwargs):
    print("I am connecting to db...")


@events.test_stop.add_listener
def script_stop(**kwargs):
    print("I am disconnecting from db...")


class MyUser(User):
    wait_time = between(1, 2)

    def on_start(self):
        print("I am login url")

    @task
    def doing_work(self):
        print("I am doing smthng work")

    def on_stop(self):
        print("I am logging out")
