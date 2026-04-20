from locust import HttpUser, task, between


class HotelSearchUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://superxpnsebe.dev.us.nrml.tools"

    @task
    def search_hotels(self):
        payload = {
            "checkin_dt": "2026-05-11",
            "checkout_dt": "2026-05-12",
            "city": "Dubai",
            "country": "UAE",
            "currency": "AED",
            "luxury": False,
            "min_price": 100,
            "num_adults": 1,
            "num_children": 0,
            "num_rooms": 3,
            "sort_by": "best_match",
            "top_n": 10
        }

        headers = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjbW1kYmlxNWIwNjRtdnAwMW1mcjF4ODkyIiwidXVpZCI6IjAxOWNiZDg2LTczZGYtNzJjNC05OWY0LWVlNWU3YjIzMzg5ZSIsInNlc3Npb25JZCI6IjgzZWE2NTVkLTAyOWMtNDRiYS1hNWI5LTk2YjEwMGM3YWI5ZCIsInR5cGUiOiJhY2Nlc3MiLCJwaG9uZU51bWJlciI6Iis5NzE1MjM5NzgxMjMiLCJpYXQiOjE3NzU2OTAxNzIsImV4cCI6MTc3NjI5NDk3MiwiYXVkIjoid2FsbGV0LXNlcnZpY2UtdXNlcnMiLCJpc3MiOiJ3YWxsZXQtYXV0aC1zZXJ2aWNlIn0.0NrLOYM-bVkijwtPaQEr5uJb9mrry3qaHyrNAd5Bw4Q"
        }

        with self.client.post(
            "/v2/trip-planner/hotels/search",
            json=payload,
            headers=headers,
            catch_response=True
        ) as response:

            if response.status_code != 200:
                response.failure(f"Expected 200, got {response.status_code}")
                return

            try:
                body = response.json()
                assert "data" in body
                response.success()
            except Exception as e:
                response.failure(f"Invalid response structure: {e}")
