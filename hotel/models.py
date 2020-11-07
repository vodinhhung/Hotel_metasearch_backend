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

    def __str__(self):
        return self.name


class Street(models.Model):
    index = models.IntegerField()
    id = models.BigIntegerField(primary_key=True)
    province = models.ForeignKey(Province,on_delete=models.SET_NULL,null=True)
    district = models.ForeignKey(District,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Domain(models.Model):
    index = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


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
    min_price_domain = models.BigIntegerField()

    def __str__(self):
        return self.name


class Info(models.Model):
    index = models.IntegerField()
    root = models.OneToOneField(Root, primary_key=True, on_delete=models.CASCADE, unique=True)
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
    
    def __str__(self):
        return self.root.name

class Quality(models.Model):
    index = models.IntegerField()
    root = models.OneToOneField(Root, primary_key=True, on_delete=models.CASCADE)
    cleanliness_scores = models.FloatField(max_length=5)
    meal_score = models.FloatField(max_length=5)
    location_score = models.FloatField(max_length=5)
    sleep_quality_score = models.FloatField(max_length=5)
    room_score = models.FloatField(max_length=5)
    service_score = models.FloatField(max_length=5)
    facility_score = models.FloatField(max_length=5)
    overall_score = models.FloatField(max_length=5, null=True)
    num_review = models.IntegerField(null=True)
    review_score = models.FloatField(max_length=5, null=True)

class Url(models.Model):
    index = models.IntegerField(primary_key=True)
    root = models.ForeignKey(Root, on_delete=models.CASCADE)
    domain_hotel_id = models.CharField(max_length=100)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    url = models.CharField(max_length=2083)
    min_price = models.BigIntegerField()

    def __str__(self):
        return self.url


class Review(models.Model):
    index = models.IntegerField(primary_key=True)
    root = models.ForeignKey(Root, on_delete=models.CASCADE)
    domain_hotel_id = models.CharField(max_length=100)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    langcode = models.CharField(max_length=10, null=True)
    date_time = models.CharField(max_length=50)
    title = models.TextField(null=True)
    text = models.TextField(null=True)
    score = models.FloatField(max_length=5)


class User(models.Model):
    index = models.AutoField(primary_key=True)
    social_id = models.CharField(max_length=2083)
    name = models.CharField(max_length=2083)
    social_domain = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Like(models.Model):
    index = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    root = models.ForeignKey(Root, on_delete=models.CASCADE)
    status = models.IntegerField(null=True)

class View(models.Model):
    index = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    root = models.ForeignKey(Root, on_delete=models.CASCADE)