# Hotel metasearch with Django and clickhouse

## Requirements
- Python3
- Module Django
- PostgreSQL
## Installing

> Operating system: Ubuntu
### Install PostgreSQL
- Download PostSQL [link](https://www.postgresql.org/download/)
- Install tutorial [link](https://www.youtube.com/watch?v=VNy2nhho9Pg)
### Clone the remote repository to local

```bash
git clone https://github.com/vodinhhung/Hotel_metasearch_backend
```

### Config Database
- Open pg Admin4 or SQL Shell, enter your password
- If you use **pdAdmin4** Create Database in Object tab
![pd Admin 4 image](https://sp.postgresqltutorial.com/wp-content/uploads/2019/05/pgAdmin-connected-to-PostgreSQL-Database-Server.png)
- If you use **SQL Shell**, type in command
```bash
CREATE DATABASE yourdatabase;
```
- Open *./hotel_metasearch/settings.py*
- Change setting configs 
![database config](https://miro.medium.com/max/1596/1*pSmANFeDf2Zhj-WDSpGiVw.png)
### Install module

```bash
pip3 install Django
sudo apt-get install python3-psycopg2
```

### Database setup

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Import Data
- Go to *commnands* folder
```bash
cd hotel\management\commands
```
- Change Database connection to your database in **import_csv.py**
- Import database
```bash
python3 import_csv.py
```

### Run

```bash
python3 manage.py runserver
```





