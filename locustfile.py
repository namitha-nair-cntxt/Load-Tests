from locust import HttpUser, task, between


class FlightSearchUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://superxpnsebe.dev.us.nrml.tools"

    @task
    def search_flights(self):
        payload = {
            "departure_date": "2026-04-20",
            "from_location": "DXB",
            "to_location": "AMM",
            "return_date": "2026-04-26",
            "class_type": "Economy",
            "passengers": 1,
            "sort_by": "best_match",
            "stops": 0
        }

        headers = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjbW1kYmlxNWIwNjRtdnAwMW1mcjF4ODkyIiwidXVpZCI6IjAxOWNiZDg2LTczZGYtNzJjNC05OWY0LWVlNWU3YjIzMzg5ZSIsInNlc3Npb25JZCI6IjA1NGE2MGFkLTNhZDktNDBmZi1iN2QzLTkxYmM1NDMwZjM1NSIsInR5cGUiOiJhY2Nlc3MiLCJwaG9uZU51bWJlciI6Iis5NzE1MjM5NzgxMjMiLCJpYXQiOjE3NzU3MjY1MDAsImV4cCI6MTc3NjMzMTMwMCwiYXVkIjoid2FsbGV0LXNlcnZpY2UtdXNlcnMiLCJpc3MiOiJ3YWxsZXQtYXV0aC1zZXJ2aWNlIn0.O04P-5aJRUVLucnQqEAraYK4K_7SJ3qgRTxYcq2i1bs"
        }

        with self.client.post(
            "/v2/trip-planner/flights/search",
            json=payload,
            headers=headers,
            catch_response=True
        ) as response:

            if response.status_code != 201:
                response.failure(f"Expected 201, got {response.status_code}")
                return

            try:
                body = response.json()
                assert "data" in body
                response.success()
            except Exception as e:
                response.failure(f"Invalid response structure: {e}")
