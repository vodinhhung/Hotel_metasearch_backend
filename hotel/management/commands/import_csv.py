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
drop_root= "DELETE FROM hotel_root"
drop_quality= "DELETE FROM hotel_quality"
drop_info= "DELETE FROM hotel_info"
drop_province= "DELETE FROM hotel_province"
drop_district= "DELETE FROM hotel_district"
drop_street= "DELETE FROM hotel_street"
drop_url= "DELETE FROM hotel_url"
drop_domain = "DELETE FROM hotel_domain"
province = "COPY hotel_province FROM "+"'"+BASE_DIR+"/data/province.csv"+"'"+" DELIMITER ',' CSV HEADER;"
district = "COPY hotel_district FROM "+"'"+BASE_DIR+"/data/district.csv"+"'"+" DELIMITER ',' CSV HEADER;"
street = "COPY hotel_street FROM "+"'"+BASE_DIR+"/data/street.csv"+"'"+" DELIMITER ',' CSV HEADER;"
domain = "COPY hotel_domain FROM "+"'"+BASE_DIR+"/data/domain.csv"+"'"+" DELIMITER ',' CSV HEADER;"
root_hotel = "COPY hotel_root FROM "+"'"+BASE_DIR+"/data/root_new.csv"+"'"+" DELIMITER ',' CSV HEADER;"
hotel_quality = "COPY hotel_quality FROM "+"'"+BASE_DIR+"/data/quality_new.csv"+"'"+" DELIMITER ',' CSV HEADER;"
hotel_info = "COPY hotel_info FROM "+"'"+BASE_DIR+"/data/info.csv"+"'"+" DELIMITER ',' CSV HEADER;"
hotel_url = "COPY hotel_url FROM "+"'"+BASE_DIR+"/data/url_new.csv"+"'"+" DELIMITER ',' CSV HEADER;"

cur.execute(drop_quality)
conn.commit()

cur.execute(drop_info)
conn.commit()

cur.execute(drop_url)
conn.commit()

cur.execute(drop_root)
conn.commit()

cur.execute(drop_street)
conn.commit()

cur.execute(drop_district)
conn.commit()


cur.execute(drop_province)
conn.commit()

cur.execute(drop_domain)
conn.commit()

cur.execute(province)
conn.commit()

cur.execute(district)
conn.commit()

cur.execute(street)
conn.commit()

cur.execute(domain)
conn.commit()

cur.execute(root_hotel)
conn.commit()

cur.execute(hotel_quality)
conn.commit()

cur.execute(hotel_info)
conn.commit()

cur.execute(hotel_url)
conn.commit()

print("Operation done successfully")
conn.close()