from locust import task, between, User, TaskSet


class UserBehaviour(TaskSet):
    @task()
    class CartModule(TaskSet):
        @task()
        def add_cart(self):
            print("I am add to cart")

        @task()
        def delete_cart(self):
            print("I am delete cart")

    @task()
    class ProductModule(TaskSet):
        @task()
        def view_product(self):
            print("I am view product")

        @task()
        def add_product(self):
            print("I am add product")


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [UserBehaviour]



