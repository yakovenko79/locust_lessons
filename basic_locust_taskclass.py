from locust import task, between, User, TaskSet


class UserBehaviour(TaskSet):
    @task()
    def add_cart(self):
        print("I am add to cart")

    @task()
    def view_product(self):
        print("I am vuew product")


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [UserBehaviour]

