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
drop_review = "DELETE FROM hotel_review"
drop_url= "DELETE FROM hotel_url"
drop_domain = "DELETE FROM hotel_domain"
province = "COPY hotel_province FROM "+"'"+"/tmp/province.csv"+"'"+" DELIMITER ',' CSV HEADER;"
district = "COPY hotel_district FROM "+"'"+"/tmp/district.csv"+"'"+" DELIMITER ',' CSV HEADER;"
street = "COPY hotel_street FROM "+"'"+"/tmp/street.csv"+"'"+" DELIMITER ',' CSV HEADER;"
domain = "COPY hotel_domain FROM "+"'"+"/tmp/domain.csv"+"'"+" DELIMITER ',' CSV HEADER;"
root_hotel = "COPY hotel_root FROM "+"'"+"/tmp/root_new.csv"+"'"+" DELIMITER ',' CSV HEADER;"
hotel_quality = "COPY hotel_quality FROM "+"'"+"/tmp/quality_new.csv"+"'"+" DELIMITER ',' CSV HEADER;"
hotel_info = "COPY hotel_info FROM "+"'"+"/tmp/info.csv"+"'"+" DELIMITER ',' CSV HEADER;"
hotel_url = "COPY hotel_url FROM "+"'"+"/tmp/url_new.csv"+"'"+" DELIMITER ',' CSV HEADER;"
hotel_review = "COPY hotel_review FROM "+"'"+"/tmp/review.csv"+"'"+" DELIMITER ',' CSV HEADER;"
cur.execute(drop_quality)
conn.commit()

cur.execute(drop_info)
conn.commit()

cur.execute(drop_url)
conn.commit()

cur.execute(drop_review)
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

cur.execute(hotel_review)
conn.commit()

print("Operation done successfully")
conn.close()
