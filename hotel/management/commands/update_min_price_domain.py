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

cur.execute('''CREATE TABLE price_domain_update
     (index                         INT, 
      id                            INT        NOT NULL,
      min_price_domain_update      BIGINT,
      PRIMARY KEY (index));
      ''')

province = "COPY price_domain_update FROM "+"'"+"/tmp/data/min_price_domain_update.csv"+"'"+" DELIMITER ',' CSV HEADER;"

cur.execute(province)

cur.execute('''update hotel_root
                    set min_price_domain = pdu.min_price_domain_update
               from price_domain_update pdu
               where pdu.id = hotel_root.id;
               ''')

conn.commit()

print("Operation done successfully")
conn.close()
