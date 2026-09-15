from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class chaiVerity(models.Model):
    CHAI_TYPE_CHOICES = [   # YE EK enum type ka field hai jisme ham chai ke types ko define kar rahe hai hai taki hamare model me chai ke types ko restrict kar sake matlab ki hamare model me chai ke types ko sirf yehi values hi accept kare
        ('ML', 'MASASLA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now) # ye date_added field hamare model me date and time ko store karega jab bhi hamara chaiVerity ka object create hoga to ye field automatically current date and time ko store karega
    type = models.CharField(max_length=2 , choices=CHAI_TYPE_CHOICES) # ye type field hamare model me chai ke types ko store karega aur ye field sirf CHAI_TYPE_CHOICES me diye gaye values ko hi accept karega
    description = models.TextField(default='') # ye description field hamare model me chai ke description ko store karega

    def __str__(self): # ye __str__ method hamare model ka string representation ko define karega yani ki jab bhi hamara chaiVerity ka object print hoga to ye method automatically call hoga aur ye method hamare object ka name return karega
        return self.name
    
    


# one to many 

class chaiReview(models.Model):
    chai = models.ForeignKey(chaiVerity , on_delete=models.CASCADE , related_name='reviews') # ye chai field hamare model me chaiVerity model ke saath one to many relationship ko define karega yani ki ek chaiVerity ka object ke saath multiple chaiReview ke objects ho sakte hai aur ye field chaiVerity model ke primary key ko reference karega aur agar chaiVerity ka object delete hoga to uske saath associated chaiReview ke objects bhi delete ho jayenge
    user = models.ForeignKey(User , on_delete=models.CASCADE) # ye user field hamare model me User model ke saath one to many relationship ko define karega yani ki ek User ka object ke saath multiple chaiReview ke objects ho sakte hai aur ye field User model ke primary key ko reference karega aur agar User ka object delete hoga to uske saath associated chaiReview ke objects bhi delete ho jayenge
    rating = models.IntegerField(default=0) # ye rating field hamare model me chai ke rating ko store karega aur ye field integer type ka hoga aur iska default value 0 hoga
    review = models.TextField(default='') # ye review field hamare model me chai ke
    date_added = models.DateTimeField(default=timezone.now) # ye date_added field hamare model me date and time ko store karega jab bhi hamara chaiReview ka object create hoga to ye field automatically current date and time ko store karega


    def __str__(self): # ye __str__ method hamare model ka string representation ko define karega yani ki jab bhi hamara chaiReview ka object print hoga to ye method automatically call hoga aur ye method hamare object ka rating return karega
        return f'{self.user.username} review for {self.chai.name}'
    

# Many to Many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chair_verities = models.ManyToManyField(chaiVerity, related_name='stores')

    def __str__(self):
        return self.name



# one to one

class chaiCertificate(models.Model):
    chai = models.OneToOneField(chaiVerity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateField(default=timezone.now)
    valid_until = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return f'Certificate for {self.name.chai}'


    

