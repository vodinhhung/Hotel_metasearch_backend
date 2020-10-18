from django.db import models


class Province(models.Model):
    index = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)


class District(models.Model):
    index = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    province = models.ForeignKey(Province,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=50)


class Street(models.Model):
    index = models.IntegerField()
    id = models.BigIntegerField(primary_key=True)
    province = models.ForeignKey(Province,on_delete=models.SET_NULL,null=True)
    district = models.ForeignKey(District,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=100)


class Domain(models.Model):
    index = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)


class Root(models.Model):
    index = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500, null=True)
    logo = models.CharField(max_length=2083, null=True)
    province = models.ForeignKey(Province,  on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    lat = models.FloatField(max_length=20, null=True)
    long = models.FloatField(max_length=20, null=True)
    star = models.IntegerField(null=True)
    check_in = models.CharField(max_length=20, null=True)
    check_out = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    street = models.CharField(max_length=500, null=True)


class Info(models.Model):
    index = models.IntegerField()
    root = models.ForeignKey(Root, primary_key=True, on_delete=models.CASCADE)
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


class Quality(models.Model):
    index = models.IntegerField()
    root = models.ForeignKey(Root, primary_key=True, on_delete=models.CASCADE)
    cleanliness_scores = models.FloatField(max_length=5)
    meal_score = models.FloatField(max_length=5)
    location_score = models.FloatField(max_length=5)
    sleep_quality_score = models.FloatField(max_length=5)
    room_score = models.FloatField(max_length=5)
    service_score = models.FloatField(max_length=5)
    facility_score = models.FloatField(max_length=5)
    overall_score = models.FloatField(max_length=5)


class Url(models.Model):
    index = models.IntegerField(primary_key=True)
    root = models.ForeignKey(Root, on_delete=models.CASCADE)
    domain_hotel_id = models.CharField(max_length=100)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    url = models.CharField(max_length=2083)


