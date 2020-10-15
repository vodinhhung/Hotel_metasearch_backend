from django.db import models
from postgres_copy import CopyManager


class Province(models.Model):
    id = models.IntegerField()
    province_id = models.IntegerField(primary_key=True)
    province_name = models.CharField(max_length=20)
    objects = CopyManager()


class District(models.Model):
    id = models.IntegerField()
    district_id = models.IntegerField(primary_key=True)
    province_id = models.ForeignKey(Province,on_delete=models.SET_NULL,null=True)
    district_name = models.CharField(max_length=50)
    objects = CopyManager()


class Street(models.Model):
    id = models.IntegerField()
    street_id = models.BigIntegerField(primary_key=True)
    province_id = models.ForeignKey(Province,on_delete=models.SET_NULL,null=True)
    district_id = models.ForeignKey(District,on_delete=models.SET_NULL,null=True)
    street_name = models.CharField(max_length=100)
    objects = CopyManager()


class Domain(models.Model):
    id = models.IntegerField()
    domain_id = models.IntegerField(primary_key=True)
    domain_name = models.CharField(max_length=20)
    objects = CopyManager()


class RootHotel(models.Model):
    id = models.IntegerField()
    hotel_id = models.IntegerField(primary_key=True)
    hotel_name = models.CharField(max_length=500)
    hotel_address = models.CharField(max_length=500, null=True)
    hotel_logo = models.CharField(max_length=2083, null=True)
    province_id = models.ForeignKey(Province,  on_delete=models.CASCADE, null=True)
    district_id = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    street_id = models.CharField(max_length=500, null=True)
    hotel_lat = models.FloatField(max_length=20, null=True)
    hotel_long = models.FloatField(max_length=20, null=True)
    hotel_star = models.IntegerField(null=True)
    check_in = models.CharField(max_length=20, null=True)
    check_out = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=10000, null=True)
    objects = CopyManager()


class HotelInfo(models.Model):
    index = models.IntegerField()
    hotel_id = models.ForeignKey(RootHotel, primary_key=True, on_delete=models.CASCADE)
    have_breakfast = models.IntegerField()
    is_free_wifi = models.IntegerField()
    have_car_park = models.IntegerField()
    have_airport_transport = models.IntegerField()
    have_restaurant = models.IntegerField()
    have_deposit = models.IntegerField()
    have_baby_service = models.IntegerField()
    have_bar = models.IntegerField()
    have_laundry = models.IntegerField()
    have_tour = models.IntegerField()
    have_spa = models.IntegerField()
    have_pool = models.IntegerField()
    objects = CopyManager()


class HotelQuality(models.Model):
    index = models.IntegerField()
    hotel_id = models.ForeignKey(RootHotel, primary_key=True, on_delete=models.CASCADE)
    cleanliness_scores = models.FloatField(max_length=5)
    meal_score = models.FloatField(max_length=5)
    location_score = models.FloatField(max_length=5)
    sleep_quality_score = models.FloatField(max_length=5)
    room_score = models.FloatField(max_length=5)
    service_score = models.FloatField(max_length=5)
    facility_score = models.FloatField(max_length=5)
    overall_score = models.FloatField(max_length=5)
    objects = CopyManager()


class HotelUrl(models.Model):
    index = models.IntegerField(primary_key=True)
    hotel_id = models.ForeignKey(RootHotel, on_delete=models.CASCADE)
    domain_hotel_id = models.CharField(max_length=100)
    domain_id = models.ForeignKey(Domain, on_delete=models.CASCADE)
    url = models.CharField(max_length=2083)
    objects = CopyManager()


