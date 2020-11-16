#add columns name_no_accent
import psycopg2
import sys, os
import pandas as pd
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
conn = psycopg2.connect(database="hotel_metasearch",
                        user="postgres",
                        password="123",
                        host="localhost",
                        port="5432")

cur = conn.cursor()

cur.execute('''CREATE TABLE province_update
     (index                 INT, 
      id                    INT        NOT NULL,
      name                  VARCHAR(20),
      name_no_accent        VARCHAR(20),
      PRIMARY KEY (id));
      ''')

province = "COPY province_update FROM "+"'"+"/tmp/province_new.csv"+"'"+" DELIMITER ',' CSV HEADER;"

cur.execute(province)

cur.execute('''update hotel_province
                    set name_no_accent = pu.name_no_accent
               from province_update pu
               where pu.name = hotel_province.name;
               ''')

conn.commit()

print("Operation done successfully")
conn.close()
