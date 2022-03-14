from django.db import models


# Create your models here.

class Ethnicity(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
        
class Gender(models.Model):
    name = models.CharField(max_length=6)
    
    def __str__(self):
        return self.name

class PrimarySupportReason(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class AccommodationStatus(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class ServiceComponent(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name 

class ServiceType(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name 
        
class Employment(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class HasInformalCarer(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class RouteOfAccess(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class RequestOutcome(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name 

class AssessmentOutcome(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class AssessmentType(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Eligibility(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
        

class ServiceProvider(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class DeliveryMechanism(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name 

class CostFrequency(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name 

class PhysicalCOPD(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class PhysicalCancer(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 

class PhysicalAcquiredPhysical(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 

class PhysicalHIVAIDS(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 

class PhysicalOther(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
        

class NeuroStroke(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
        
class NeuroParkinsons(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 

class NeuroMotorNeuron(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
        

class NeuroAcquiredBrain(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
        

class NeuroOther(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 

class SensoryVisuallyImpaired(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
        

class SensoryHearingImpaired(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
        

class SensoryOther(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 

class LDLearningDisability(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
        

class LDAutismInclASHF(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
        

class LDAutismExclASHF(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
        
        
class LDOther(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
        
class MentalHealthOther(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
        
class MentalHealthDementia(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
        

class Client(models.Model):
    lasID = models.PositiveIntegerField(null=False)
    nhsNumber = models.CharField(max_length=50, null=True)
    firstName = models.CharField(max_length=50, null=True)
    lastName = models.CharField(max_length=50, null=True)
    birthDate = models.DateField(null=True, blank=True) #
    deathDate = models.DateField(null=True, blank=True) #
    postCode = models.CharField(max_length=50,null=True)
    requestEvent = models.CharField(max_length=7, null=True)
    requestStart = models.DateField(null=True, blank=True) #
    requestEnd = models.DateField(null=True, blank=True) #
    requestOutcome = models.ForeignKey('RequestOutcome', on_delete=models.SET_NULL, null=True)
    assessmentEvent = models.CharField(max_length=50, null=True)
    assessmentStart = models.DateField(null=True, blank=True) #
    assessmentEnd = models.DateField(null=True, blank=True) #
    assessmentOutcome = models.ForeignKey('AssessmentOutcome', on_delete=models.SET_NULL, null=True)
    assessmentType = models.ForeignKey('AssessmentType', on_delete=models.SET_NULL, null=True)
    eligibility = models.ForeignKey('Eligibility', on_delete=models.SET_NULL, null=True)
    weeklyVisits = models.FloatField(null=True, blank=True) #
    weeklyCost = models.DecimalField(max_digits=6,decimal_places=2, null=True)
    weeklyMins = models.FloatField(null=True, blank=True)
    unitCost = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    weeklyUnits = models.FloatField(null=True, blank=True)
    ethnicity = models.ForeignKey('Ethnicity', on_delete=models.SET_NULL, null=True)
    gender = models.ForeignKey('Gender', on_delete=models.SET_NULL, null=True)
    primarySupportReason = models.ForeignKey('PrimarySupportReason', on_delete=models.SET_NULL, null=True)
    accommodationStatus = models.ForeignKey('AccommodationStatus', on_delete=models.SET_NULL, null=True)
    serviceComponent = models.ForeignKey('ServiceComponent', on_delete=models.SET_NULL, null=True)
    serviceType = models.ForeignKey('ServiceType', on_delete=models.SET_NULL, null=True)
    employment = models.ForeignKey('Employment', on_delete=models.SET_NULL, null=True)
    informalCarer = models.ForeignKey('HasInformalCarer', on_delete=models.SET_NULL, null=True)
    routeOfAccess = models.ForeignKey('RouteOfAccess',on_delete=models.SET_NULL, null=True)
    serviceEvent = models.CharField(max_length=50, null=True)
    serviceStart = models.DateField(null=True, blank=True) #
    serviceEnd = models.DateField(null=True, blank=True) #
    serviceProvider = models.ForeignKey('ServiceProvider', on_delete=models.SET_NULL, null=True)
    deliveryMechanism = models.ForeignKey('DeliveryMechanism', on_delete=models.SET_NULL, null=True)
    costFrequency = models.ForeignKey('CostFrequency', on_delete=models.SET_NULL, null=True)
    copd = models.ForeignKey('PhysicalCOPD',on_delete=models.SET_NULL, null=True)
    cancer = models.ForeignKey('PhysicalCancer', on_delete=models.SET_NULL, null=True)
    physical = models.ForeignKey('PhysicalAcquiredPhysical', on_delete=models.SET_NULL, null=True)
    hivAIDS = models.ForeignKey('PhysicalHIVAIDS', on_delete=models.SET_NULL, null=True)
    otherPhysical = models.ForeignKey('PhysicalOther', on_delete=models.SET_NULL, null=True)
    stroke = models.ForeignKey('NeuroStroke', on_delete=models.SET_NULL, null=True)
    parkinsons = models.ForeignKey('NeuroParkinsons', on_delete=models.SET_NULL, null=True)
    motorNeuron = models.ForeignKey('NeuroMotorNeuron', on_delete=models.SET_NULL, null=True)
    brainInjury = models.ForeignKey('NeuroAcquiredBrain', on_delete=models.SET_NULL, null=True)
    otherNeuro = models.ForeignKey('NeuroOther', on_delete=models.SET_NULL, null=True)
    visuallyImpaired = models.ForeignKey('SensoryVisuallyImpaired', on_delete=models.SET_NULL, null=True)
    hearingImpaired = models.ForeignKey('SensoryHearingImpaired', on_delete=models.SET_NULL, null=True)
    otherSensory = models.ForeignKey('SensoryOther', on_delete=models.SET_NULL, null=True)
    learningDisability = models.ForeignKey('LDLearningDisability', on_delete=models.SET_NULL, null=True)
    ldIncl = models.ForeignKey('LDAutismInclASHF', on_delete=models.SET_NULL, null=True)
    ldExcl = models.ForeignKey('LDAutismExclASHF', on_delete=models.SET_NULL, null=True)
    otherLd = models.ForeignKey('LDOther', on_delete=models.SET_NULL, null=True)
    otherMental = models.ForeignKey('MentalHealthOther', on_delete=models.SET_NULL, null=True)
    dementiaMental = models.ForeignKey('MentalHealthDementia', on_delete=models.SET_NULL, null=True)
    age = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return self.firstName + ' ' + self.lastName



