import sqlalchemy
from sqlalchemy import text
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:admin@127.0.0.1/challenge")

with engine.connect() as conn:
    conn.execute(text("create schema if not exists pythondb"))
    conn.execute(text("use pythondb"))
    conn.execute(text("DROP TABLE test_table"))
    conn.commit()
    conn.execute(text("CREATE TABLE if not exists test_table ("
                      "id int PRIMARY KEY auto_increment,"
                      "name_field varchar(20),"
                      "yes_no boolean default 0"
                      ")"))
    conn.commit()
    print(conn.execute(text("show tables")).all())
    conn.execute(text("insert into test_table (name_field) values ('Derrick')"))
    conn.execute(text("insert into test_table (name_field, yes_no) values ('Drem', 1)"))
    conn.execute(text("insert into test_table (id, name_field, yes_no) values (12, 'Dwr3k', 1)"))
    conn.execute(text("insert into test_table (name_field) values ('Dwrek')"))
    conn.commit()
    values = conn.execute(text("select * from test_table"))
    print(values.all())


