from django.db import models
from django.contrib.auth.models import User

class Sex(models.TextChoices):
    MALE = 'MALE'
    FEMALE = 'FEMALE'

class Yes_No(models.TextChoices):
    NO = 'NO'
    YES = 'YES'

class Mr_mrs(models.TextChoices):
    MR = 'Mr'
    YES = 'Mrs'


class Job_Status(models.TextChoices):
    PRODUCT = 'PRODUCT'
    SERVICE = 'SERVICE'
    AMENDS = 'AMENDS'

class ClientSize(models.TextChoices):
    CHILDREN = 'C', ('Children')
    XTRA_SMALL = 'XS', ('Xtra Small')
    SMALL = 'S', ('Small')
    MEDIUM = 'M', ('Medium')
    LARGE = 'L', ('Large')
    XTRA_LARGE = 'XL', ('Xtra Large')
    XTRA_XTRA_LARGE = 'XXL', ('Xtra Xtra Large')


class ClientMeasurements(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=250, null=True)
    top_lenght = models.CharField(max_length=15,null=True, blank=True)
    shoulder = models.CharField(max_length=15, null=True, blank=True)
    Round_chest = models.CharField(max_length=15, null=True, blank=True)
    sleeve_lenght = models.CharField(max_length=15, null=True, blank=True)
    neck = models.CharField(max_length=15, null=True, blank=True)
    round_arm = models.CharField(max_length=15, null=True, blank=True)
    arm_hole = models.CharField(max_length=15, null=True, blank=True)
    front_chest = models.CharField(max_length=15, null=True, blank=True)
    back_chest = models.CharField(max_length=15, null=True, blank=True)
    cuff = models.CharField(max_length=15, null=True, blank=True)
    short_sleeve_width = models.CharField(max_length=15, null=True, blank=True)
    _3quarter_width = models.CharField(max_length=15, null=True, blank=True)
    long_sleeve_width = models.CharField(max_length=15, null=True, blank=True)
    trouser_lenght = models.CharField(max_length=15, null=True, blank=True)
    waist = models.CharField(max_length=15, null=True, blank=True)
    lap = models.CharField(max_length=15, null=True, blank=True)
    knee = models.CharField(max_length=15, null=True, blank=True)
    calf = models.CharField(max_length=15, null=True, blank=True)
    ankle = models.CharField(max_length=15, null=True, blank=True)
    BR = models.CharField(max_length=15, null=True, blank=True)
    RBR = models.CharField(max_length=15, null=True, blank=True)
    agbada_lenght = models.CharField(max_length=15, null=True, blank=True)
    agbada_shoulder = models.CharField(max_length=15, null=True, blank=True)
    agbada_sleeve = models.CharField(max_length=15, null=True, blank=True)
    cap = models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)

    

class Clients(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=10, choices=Mr_mrs.choices, default=Mr_mrs.MR)
    name = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=50, null=True)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    sex = models.CharField(max_length=50, choices=Sex.choices, default=Sex.MALE)
    birthday = models.DateField(null=True, blank=True)
    client_note = models.TextField(null=True, blank=True)
    size = models.CharField(max_length=50, choices=ClientSize.choices, default=ClientSize.LARGE)
    measurement = models.OneToOneField(ClientMeasurements, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)
    
    
class Workers(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=50, null=True)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    sex = models.CharField(max_length=50, choices=Sex.choices, default=Sex.MALE)
    birthday = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.name)
    
    

class Jobs(models.Model):
    name = models.ForeignKey(Clients, max_length=250, null=True, on_delete=models.SET_NULL)
    start_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=Job_Status.choices, default=Job_Status.PRODUCT)
    measurement = models.ForeignKey(ClientMeasurements, on_delete=models.SET_NULL, null=True)
    fabric_image_1 = models.ImageField(blank=True, null=True, upload_to='fabric_images')
    fabric_image_2 = models.ImageField(blank=True, null=True, upload_to='fabric')
    fabric_yardage = models.IntegerField(null=True, blank=True)
    fabric_note = models.TextField(null=True, blank=True)
    top_design_image_1 = models.ImageField(blank=True, null=True, upload_to='top_designs')
    top_design_image_2 = models.ImageField(blank=True, null=True, upload_to='top_designs')
    top_design_image_3 = models.ImageField(blank=True, null=True, upload_to='top_designs')
    top_design_note = models.TextField(null=True, blank=True)
    trouser_design_image = models.ImageField(blank=True, null=True, upload_to='trouser_designs')
    trouser_design_note = models.TextField(null=True, blank=True)
    agbada_design_image = models.ImageField(blank=True, null=True, upload_to='agbada_designs')
    agbada_design_note = models.TextField(null=True, blank=True)
    cap_design_image= models.ImageField(blank=True, null=True, upload_to='cap_designs')
    cap_design_note = models.TextField(null=True, blank=True)
    top_worker = models.ForeignKey(Workers, on_delete=models.SET_NULL, null=True, blank=True)
    """
    trouser_worker = models.ForeignKey(Workers, on_delete=models.SET_NULL, null=True, blank=True)
    agbada_worker = models.ForeignKey(Workers, on_delete=models.SET_NULL, null=True, blank=True)
    cap_worker = models.ForeignKey(Workers, on_delete=models.SET_NULL, null=True, blank=True)
    """
    def __str__(self):
        return str(self.name)
    
    def imageurl(self):
        if self.fabric_image_1:
            return self.fabric_image_1.url
        else:
            return 'core/static/core/images/no_image_available.png'
    

    
    def imageurl(self):
        if self.fabric_image_2:
            return self.fabric_image_2.url
        else:
            return 'core/static/core/images/no_image_available.png'

    def imageurl(self):
        if self.fabric_image_3:
            return self.fabric_image_3.url
        else:
            return 'core/static/core/images/no_image_available.png'


class Job_operation(models.Model):
    name = models.ForeignKey(Jobs, max_length=250, null=True, on_delete=models.SET_NULL)
    job_done = models.CharField(max_length=50, choices=Yes_No.choices, default=Yes_No.NO)
    measurement_confirmed = models.CharField(max_length=50, choices=Yes_No.choices, default=Yes_No.NO)
    any_issue = models.CharField(max_length=50, choices=Yes_No.choices, default=Yes_No.NO)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
    
    def job_is_done(self):
        if self.job_done:
            return self.job_done
        else:
            return f'please start this job'


class Job_payment(models.Model):
    name = models.ForeignKey(Job_operation, max_length=250, null=True, on_delete=models.SET_NULL)
    top_amount = models.IntegerField(null=True, blank=True)
    trouser_amount = models.IntegerField(null=True, blank=True)
    agbada_amount = models.IntegerField(null=True, blank=True)
    cap_amount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Job_delivery(models.Model):
    name = models.ForeignKey(Job_operation, max_length=250, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)
    














    
