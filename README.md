# fastApi_python

create virtual Env: py -3 -m venv [anyName] 
command Palette :venv\Scripts\python.exe
In terminal command: venv\scripts\activate 
install: pip install fastapi[all]
it will show what we install the driver:
pip freeze 
run the main: uvicorn main:app --reload
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
alembic history 
alembic upgrade head
alembic revision --autogenerate -m "Auto vote generate"

**********************************************************
sudo -s [login as a root shell]
whoami
exit [for logout]

sudo passwd root
new-password:******

su root

//update command
sudo apt update && sudo apt upgrade -y

sudo apt install python3-pip
sudo pip3 install virtualenv
sudo apt install postgresql postgresql-contrib
psql --version
psql -U postgres 
sudo cat /etc/passwd
su - postgres [change the user in the machine]
psql -U postgres [now i can login postgres database]
\password postgres [create password]
exit [it back to root user]
cd /etc/postgresql/12/main
ls
sudo vi postgresql.conf
sudo vi pg_hba.conf 
psql -U postgres [login postgresql]
hostname -I //  

 
 

