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

cur.execute('''CREATE TABLE price_update
     (index                 INT, 
      domain_hotel_id       VARCHAR(100)        NOT NULL,
      min_price_update      BIGINT,
      PRIMARY KEY (index));
      ''')

province = "COPY price_update FROM "+"'"+"/tmp/data/min_price_update.csv"+"'"+" DELIMITER ',' CSV HEADER;"

cur.execute(province)

cur.execute('''update hotel_url
                    set min_price = pu.min_price_update
               from price_update pu
               where pu.domain_hotel_id = hotel_url.domain_hotel_id;
               ''')

conn.commit()

print("Operation done successfully")
conn.close()
