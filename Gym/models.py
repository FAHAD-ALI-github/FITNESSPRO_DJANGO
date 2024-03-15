from django.db import models

# Create your models here.

class Gym_split(models.Model):
    
    split_name = models.CharField(max_length=500)
    
    def __str__(self):
        return self.split_name




class Gender(models.Model):
    
    gender = models.CharField(max_length=30)
    
    def __str__(self):
        return self.gender




class Muscle_strength(models.Model):
    
    type = models.CharField(max_length=20)
    
    def __str__(self):
        return self.type




class Address(models.Model):

    area = models.CharField(max_length=30)
    
    def __str__(self):
        return self.area
    



class Gym_user(models.Model):

    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    no_of_days = models.IntegerField(default=0)
    dob = models.DateField()
    phone_number = models.IntegerField()
    image = models.ImageField(upload_to="users_profile_images/", default="users_profile_images/image.png")
    weight = models.IntegerField()
    height = models.IntegerField()
    date_of_joining = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    gym_split = models.ForeignKey(Gym_split, on_delete=models.CASCADE)
    muscle_strength = models.ForeignKey(Muscle_strength, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name +" "+ self.last_name
    
    @staticmethod
    def get_all_users(self):
        return Gym_user.objects.all()
    
    @staticmethod
    def get_user_by_id(user_id):
        return Gym_user.objects.get(id=user_id)
    
    @staticmethod
    def get_searched_members(query):
        return Gym_user.objects.filter(first_name__contains=query)
    @staticmethod
    def by_lastName(query):
        return Gym_user.objects.filter(last_name__contains=query)
    @staticmethod
    def by_username(query):
        return Gym_user.objects.filter(username__contains=query)
    @staticmethod
    def by_id(query):
        return Gym_user.objects.filter(id=int(query))
    @staticmethod
    def by_dob(query):
        return Gym_user.objects.filter(dob__contains=query)
    
    @staticmethod
    def get_username_authen(em):
        return Gym_user.objects.filter(username=em)
    
    @staticmethod
    def get_user_by_username(user):
        try:
            comment = Gym_user.objects.get(username=user)
        except Gym_user.DoesNotExist:
            comment = None
        return comment
    

class Gym_admin(models.Model):

    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    dob = models.DateField()
    phone_number = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="admin_images/", default="images/find_user.png")
    date_of_joining = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name +" "+ self.last_name +"--Admin "
    
    @staticmethod
    def get_admin_by_username(admin):
        try:
            comment = Gym_admin.objects.get(username=admin)
        except Gym_admin.DoesNotExist:
            comment = None
        return comment
    
    @staticmethod
    def get_admin_by_id(admin_id):
        return Gym_admin.objects.get(id=admin_id)