from locust import task, between, User, SequentialTaskSet


class UserBehaviour(SequentialTaskSet):
    def on_start(self) -> None:
        print("I will login")

    @task()
    def flight_finder(self):
        print("I will find flight by entering criteria")

    @task()
    def select_flight(self):
        print("select_flight")

    @task()
    def book_flight(self):
        print("book_flight")


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [UserBehaviour]

