from locust import task, between, User


def add_cart(userclass):
    print("I am add to cart")


def view_product(userclass):
    print("I am vuew product")


class MyUser(User):
    wait_time = between(1, 2)
    # tasks=[add_cart, view_product]
    tasks = {add_cart:3, view_product:1}

    # @task(2)
    # def add_cart(self):
    #     print("I am add to cart")
    #
    # @task(4)
    # def view_product(self):
    #     print("I am vuew product")
