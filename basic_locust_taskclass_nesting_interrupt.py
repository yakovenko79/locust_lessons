from locust import task, between, User, TaskSet


class UserBehaviour(TaskSet):
    @task(2)
    class CartModule(TaskSet):
        @task(4)
        def add_cart(self):
            print("I am add to cart")

        @task(2)
        def delete_cart(self):
            print("I am delete cart")

        @task(1)
        def stop(self):
            print("I am stop")
            self.interrupt()

    @task(4)
    class ProductModule(TaskSet):
        @task(4)
        def view_product(self):
            print("I am view product")

        @task(2)
        def add_product(self):
            print("I am add product")

        @task(1)
        def stop(self):
            print("I am stop")
            self.interrupt()


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [UserBehaviour]



