import psycopg2
import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
conn = psycopg2.connect(database="root2",
                        user="postgres",
                        password="Nguyentuandung2901",
                        host="localhost",
                        port="5432")

cur = conn.cursor()
drop_root= "DELETE FROM hotel_roothotel"
drop_quality= "DELETE FROM hotel_hotelquality"
drop_info= "DELETE FROM hotel_hotelinfo"
drop_province= "DELETE FROM hotel_province"
drop_district= "DELETE FROM hotel_district"
drop_street= "DELETE FROM hotel_street"
drop_url= "DELETE FROM hotel_hotelurl"
drop_domain = "DELETE FROM hotel_domain"
province = "COPY hotel_province FROM "+"'"+BASE_DIR+"/Data/province.csv"+"'"+" DELIMITER ',' CSV HEADER;"
district = "COPY hotel_district FROM "+"'"+BASE_DIR+"/Data/district.csv"+"'"+" DELIMITER ',' CSV HEADER;"
street = "COPY hotel_street FROM "+"'"+BASE_DIR+"/Data/street.csv"+"'"+" DELIMITER ',' CSV HEADER;"
domain = "COPY hotel_domain FROM "+"'"+BASE_DIR+"/Data/domain.csv"+"'"+" DELIMITER ',' CSV HEADER;"
root_hotel = "COPY hotel_roothotel FROM "+"'"+BASE_DIR+"/Data/root.csv"+"'"+" DELIMITER ',' CSV HEADER;"
hotel_quality = "COPY hotel_hotelquality FROM "+"'"+BASE_DIR+"/Data/quality.csv"+"'"+" DELIMITER ',' CSV HEADER;"
hotel_info = "COPY hotel_hotelinfo FROM "+"'"+BASE_DIR+"/Data/info.csv"+"'"+" DELIMITER ',' CSV HEADER;"
hotel_url = "COPY hotel_hotelurl FROM "+"'"+BASE_DIR+"/Data/url.csv"+"'"+" DELIMITER ',' CSV HEADER;"

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