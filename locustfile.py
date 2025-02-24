from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    @task
    def access_homepage(self):
        self.client.get("/")

    @task
    def access_form_authentication_and_logout(self):
        self.client.get("/login")

        # Perform login with correct credentials
        payload = {"username": "tomsmith", "password": "SuperSecretPassword!"}
        response = self.client.post("/authenticate", data=payload)

        # Check if login was successful (optional validation)
        if response.status_code == 200 and "You logged into a secure area!" in response.text:
            print("Login successful!")

    @task
    def access_file_download(self):
        self.client.get("/download/royal-blue.png")

class WebsiteUser(HttpUser):

    wait_time = between(5, 15)  
    host = "https://the-internet.herokuapp.com" 
    tasks = [UserBehavior]

