import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        # The self.client attribute is what locust uses to make calls.
        self.client.get("/hello")
        self.client.get("/world")

    # Adding the 3, here gives the task a weight for how likely it will be called.
    # The view_items task will be 3x more likely to be caled.
    @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            # The name attribute here will group all of the calls together so that they
            # will show up as one in the locust statistics instead of 10 seperate entries
            time.sleep(1)

    # Locust offers both on start and on stop methods,
    # These are methods for every time a new
    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})


# Special Notes:
# There is also a @tag decorator so that you can pick and choose which tasks are run:
# https://docs.locust.io/en/stable/writing-a-locustfile.html#tag-decorator