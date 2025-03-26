from ProjectApi import ProjectApi

url = ProjectApi("https://ru.yougile.com/api-v2")


def test_create_project():
    title = "Test"
    users = "73dc7610-640b-4fc2-82f4-f5d74cc1896f"
    url.create_project(title, users)


def test_modern_project():
    title = "Test"
    users = "73dc7610-640b-4fc2-82f4-f5d74cc1896f"
    result = url.create_project(title, users)
    new_id = result
    new_title = "Avtotest"
    new_users = "73dc7610-640b-4fc2-82f4-f5d74cc1896f"
    url.modern_project(new_id, new_title, new_users)


def test_get_project():
    title = "Test"
    users = "73dc7610-640b-4fc2-82f4-f5d74cc1896f"
    result = url.create_project(title, users)
    id = result
    url.get_project(id)
