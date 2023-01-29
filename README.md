# fastApi_python

create virtual Env: py -3 -m venv [anyName] 
command Palette :venv\Scripts\python.exe
In terminal command: venv\scripts\activate 
install: pip install "fastapi[all]"
it will show what we install the driver:
pip freeze run the main: uvicorn main:app --reload
http://127.0.0.1:8000/docs 
create app folder and file init.py moved to main.py inside app folder 
run command uvicorn app.main:app --reload
pip install psycopg2 ....install for MySQL


https://alembic.sqlalchemy.org/en/latest/api/ddl.html
alembic --help
alembic revision --help (make a change the database)
alembic revision -m "create posts table"

def upgrade():
  change or update table
  pass


def downgrade():
  removing the table
  pss

alembic upgrade edf624778540 //created new table
alembic current
alembic heads (updated One)