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

cur.execute('''CREATE TABLE root_name_update
     (index                 INT, 
      id                    INT        NOT NULL,
      name                  VARCHAR(500),
      name_no_accent        VARCHAR(500),
      min_price_domain      BIGINT,
      PRIMARY KEY (id));
      ''')

province = "COPY root_name_update FROM "+"'"+"/tmp/update_root_name.csv"+"'"+" DELIMITER ',' CSV HEADER;"

cur.execute(province)

cur.execute('''update hotel_root
                    set name_no_accent = ru.name_no_accent
               from root_name_update ru
               where ru.name = hotel_root.name;
               ''')

conn.commit()

print("Operation done successfully")
conn.close()
