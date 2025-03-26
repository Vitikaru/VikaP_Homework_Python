import requests


class ProjectApi:
    # Инициализация
    def __init__(self, url, headers={
            "Authorization": (
                "Bearer ..."),
            "Content-Type": "application/json"
            }):
        self.url = url
        self.headers = headers

    def create_project(self, title, users):
        body = {
            "title": title,
            "users": {users: "admin"}
        }
        resp = requests.post(self.url + "/projects", json=body,
                             headers=self.headers)
        projectID = resp.json().get("id")
        assert resp.status_code == 201
        return projectID

    def modern_project(self, new_id, new_title, new_users):
        url = f"{self.url}/projects/{new_id}"
        body = {
            "title": new_title,
            "users": {new_users: "admin"}
        }
        resp = requests.put(url, json=body, headers=self.headers)
        projectID = resp.json().get('id')
        assert resp.status_code == 200
        return projectID

    def get_project(self, id):
        url = f"{self.url}/projects/{id}"
        project = requests.get(url, headers=self.headers)
        assert project.status_code == 200
