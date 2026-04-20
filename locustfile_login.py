from locust import HttpUser, task, between
import random

class OTPLoginUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://superxpnsebe.dev.nrml.tools"

    @task
    def request_otp(self):
        phone_number = "+97150" + str(random.randint(1000000, 9999999))

        payload = {
            "phoneNumber": phone_number,
            "deviceInfo": {
                "deviceType": "mobile",
                "deviceId": "",
                "userAgent": "",
                "platform": "ios",
                "appVersion": ""
            }
        }

        headers = {
            "accept": "*/*",
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_TOKEN_HERE"
        }

        with self.client.post(
            "/auth/request-otp",
            json=payload,
            headers=headers,
            catch_response=True
        ) as response:

            if response.status_code != 201:
                response.failure(f"Expected 201, got {response.status_code}")
                return

            try:
                body = response.json()
                assert body["data"]["success"] is True
                assert "expiresIn" in body["data"]
                response.success()
            except Exception as e:
                response.failure(f"Invalid response structure: {e}")
