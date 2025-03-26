import pytest
from ProjectApi import ProjectApi

url = ProjectApi("https://ru.yougile.com/api-v2")

# негативная проверка пустые обязательные поля


@pytest.mark.xfail
def test_create_project():
    title = ""
    users = ""
    url.create_project(title, users)


@pytest.mark.xfail
def test_modern_project():
    title = ""
    users = ""
    result = url.create_project(title, users)
    new_id = result
    new_title = ""
    new_users = ""
    url.modern_project(new_id, new_title, new_users)


@pytest.mark.xfail
def test_get_project():
    title = ""
    users = ""
    result = url.create_project(title, users)
    id = result
    url.get_project(id)
