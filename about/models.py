from django.db import models



class About(models.Model):
    mission = models.CharField(max_length=300)
    objective = models.CharField(max_length=300)    
    feature = models.CharField(max_length=300)
    
    def __str__(self):
        return self.mission
    
    class Meta:
        verbose_name="About"
        verbose_name_plural = "About"
        

class Message(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=200)
    message = models.CharField(max_length=300)
    designation = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Message"

class History(models.Model):
    designation = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.designation


    class Meta:
        verbose_name = "History"
        verbose_name_plural = "History"
    
class BoardOfDirector(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    professional_history = models.ForeignKey(History,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Board of Director"
        verbose_name_plural = "Board of Director"

class AdministrativeBody(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Administrative Body"
        verbose_name_plural = "Administrative Body"
    
    
class AdvisoryBoard(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    education = models.CharField(max_length=200)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Advisory Board"
        verbose_name_plural = "Advisory Board"
        

class ServicesAndFacilities(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Services and Facilities"
        verbose_name_plural = "Services and Facilities"
    