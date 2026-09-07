from django.db import models
from django.utils import timezone
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


    def __str__(self): # ye __str__ method hamare model ka string representation ko define karega yani ki jab bhi hamara chaiVerity ka object print hoga to ye method automatically call hoga aur ye method hamare object ka name return karega
        return self.name
    
    