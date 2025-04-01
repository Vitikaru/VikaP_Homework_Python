from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:2312@localhost:5432/QA"
db = create_engine(db_connection_string)

scripts = {
    "list": "SELECT * FROM subject ORDER BY subject_id ASC",
    "add": "INSERT INTO subject (subject_id, subject_title) SELECT 17, 'Football'",
    "update": "UPDATE subject SET subject_title = 'Basketball' WHERE subject_id = 17",
    "delete": "DELETE FROM subject WHERE subject_id = 17"
}


def test_add():
    connection = db.connect()
    add = text(scripts["add"])
    connection.execute(add)
    sql_statement = text(scripts["list"])
    result = connection.execute(sql_statement)
    rows = result.mappings().all()

    assert rows[16]["subject_id"] == 17
    assert rows[16]["subject_title"] == 'Football'

    connection.close()


def test_update():
    connection = db.connect()
    add = text(scripts["add"])
    connection.execute(add)
    update = text(scripts["update"])
    connection.execute(update)
    sql_statement = text(scripts["list"])
    result = connection.execute(sql_statement)
    rows = result.mappings().all()

    assert rows[16]["subject_id"] == 17
    assert rows[16]["subject_title"] == 'Basketball'

    connection.close()


def test_delete():
    connection = db.connect()
    add = text(scripts["add"])
    connection.execute(add)
    delete = text(scripts["delete"])
    connection.execute(delete)
    sql_statement = text(scripts["list"])
    result = connection.execute(sql_statement)
    rows = result.mappings().all()

    assert len(rows) == 16

    connection.close()
