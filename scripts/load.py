import csv
#import pandas as pd

from clients.models import Ethnicity, Gender, PrimarySupportReason, AccommodationStatus, ServiceComponent, ServiceType, Client, Employment\
,HasInformalCarer, RouteOfAccess, RequestOutcome, AssessmentOutcome, AssessmentType, Eligibility, ServiceProvider, ServiceType\
,DeliveryMechanism, CostFrequency, PhysicalCOPD, PhysicalCancer, PhysicalAcquiredPhysical, PhysicalHIVAIDS, PhysicalOther\
, NeuroStroke, NeuroParkinsons, NeuroMotorNeuron, NeuroAcquiredBrain, NeuroOther, SensoryVisuallyImpaired, SensoryHearingImpaired\
, SensoryOther, LDLearningDisability, LDAutismExclASHF, LDAutismInclASHF, LDOther, MentalHealthOther, MentalHealthDementia


        

def run():
    with open('client_data/data.csv') as file2:
        reader = csv.reader(file2)
        next(reader)
        
        # Drop table if exists    
        Ethnicity.objects.all().delete()
        Gender.objects.all().delete()
        PrimarySupportReason.objects.all().delete()
        AccommodationStatus.objects.all().delete()
        ServiceComponent.objects.all().delete()
        ServiceType.objects.all().delete()
        Employment.objects.all().delete()
        HasInformalCarer.objects.all().delete()
        Client.objects.all().delete()
        RouteOfAccess.objects.all().delete()
        RequestOutcome.objects.all().delete()
        AssessmentOutcome.objects.all().delete()
        AssessmentType.objects.all().delete()
        Eligibility.objects.all().delete()
        ServiceProvider.objects.all().delete()
        ServiceType.objects.all().delete()
        DeliveryMechanism.objects.all().delete()
        CostFrequency.objects.all().delete()
        PhysicalCOPD.objects.all().delete()
        PhysicalCancer.objects.all().delete()
        PhysicalAcquiredPhysical.objects.all().delete()
        PhysicalHIVAIDS.objects.all().delete()
        PhysicalOther.objects.all().delete()
        NeuroStroke.objects.all().delete()
        NeuroParkinsons.objects.all().delete()
        NeuroMotorNeuron.objects.all().delete()
        NeuroAcquiredBrain.objects.all().delete()
        NeuroOther.objects.all().delete()
        SensoryVisuallyImpaired.objects.all().delete()
        SensoryHearingImpaired.objects.all().delete()
        SensoryOther.objects.all().delete()
        LDLearningDisability.objects.all().delete() 
        LDAutismExclASHF.objects.all().delete()
        LDAutismInclASHF.objects.all().delete()
        LDOther.objects.all().delete()
        MentalHealthOther.objects.all().delete()
        MentalHealthDementia.objects.all().delete()
        
        for row_2 in reader:
            print(row_2)
            requestOutcome, created = RequestOutcome.objects.get_or_create(name=row_2[16])
            ethnicity, created = Ethnicity.objects.get_or_create(name=row_2[5])
            gender, created = Gender.objects.get_or_create(name=row_2[4])
            primarySupportReason, crated = PrimarySupportReason.objects.get_or_create(name=row_2[8])
            accommodationStatus, created = AccommodationStatus.objects.get_or_create(name=row_2[9])
            serviceComponent, created = ServiceComponent.objects.get_or_create(name=row_2[49])
            serviceType, created = ServiceType.objects.get_or_create(name=row_2[48])
            employment, created = Employment.objects.get_or_create(name=row_2[10])
            informalCarer, created = HasInformalCarer.objects.get_or_create(name=row_2[12])
            routeOfAccess, created = RouteOfAccess.objects.get_or_create(name=row_2[17])
            assessmentOutcome, created = AssessmentOutcome.objects.get_or_create(name=row_2[40])
            assessmentType, created = AssessmentType.objects.get_or_create(name=row_2[41])
            eligibility, created = Eligibility.objects.get_or_create(name=row_2[42])
            serviceProvider, created = ServiceProvider.objects.get_or_create(name=row_2[58])
            deliveryMechanism, created = DeliveryMechanism.objects.get_or_create(name=row_2[50])
            costFrequency, created = CostFrequency.objects.get_or_create(name=row_2[55])
            copd, created = PhysicalCOPD.objects.get_or_create(name=row_2[18])
            cancer, created = PhysicalCancer.objects.get_or_create(name=row_2[19])
            physical, created = PhysicalAcquiredPhysical.objects.get_or_create(name=row_2[20])
            hivAIDS, created = PhysicalHIVAIDS.objects.get_or_create(name=row_2[21])
            otherPhysical, created = PhysicalOther.objects.get_or_create(name=row_2[22])
            stroke, created = NeuroStroke.objects.get_or_create(name=row_2[23])
            parkinsons, created = NeuroParkinsons.objects.get_or_create(name=row_2[24])
            motorNeuron, created = NeuroMotorNeuron.objects.get_or_create(name=row_2[25])
            brainInjury, created = NeuroAcquiredBrain.objects.get_or_create(name=row_2[26])
            otherNeuro, created = NeuroOther.objects.get_or_create(name=row_2[27])
            visuallyImpaired, created = SensoryVisuallyImpaired.objects.get_or_create(name=row_2[28])
            hearingImpaired, created = SensoryHearingImpaired.objects.get_or_create(name=row_2[29])
            otherSensory, created = SensoryOther.objects.get_or_create(name=row_2[30])
            learningDisability, created = LDLearningDisability.objects.get_or_create(name=row_2[31])
            ldIncl, created = LDAutismInclASHF.objects.get_or_create(name=row_2[33])
            ldExcl, created = LDAutismExclASHF.objects.get_or_create(name=row_2[32])
            otherLd, created = LDOther.objects.get_or_create(name=row_2[34])
            otherMental, created = MentalHealthOther.objects.get_or_create(name=row_2[36])
            dementiaMental, created = MentalHealthDementia.objects.get_or_create(name=row_2[35])
            
            lasID = row_2[0]
            nhsNumber = (row_2[1] if row_2[1] else None)
            firstName = row_2[2]
            lastName = row_2[3]
            birthDate = (row_2[6] if row_2[6] else None)
            deathDate = (row_2[7] if row_2[7] else None)
            postCode = (row_2[11] if row_2[11] else None)
            requestEvent = row_2[13]
            requestStart = (row_2[14] if row_2[14] else None)
            requestEnd = (row_2[15] if row_2[15] else None)
            assessmentEvent = (row_2[37] if row_2[37] else None)
            assessmentStart = (row_2[38] if row_2[38] else None)
            assessmentEnd = (row_2[39] if row_2[39] else None)
            weeklyVisits = (row_2[51] if row_2[51] else None)
            weeklyCost = (row_2[52] if row_2[52] else None)
            weeklyUnits = (row_2[56] if row_2[56] else None)
            serviceEvent = (row_2[43] if row_2[43] else None)
            serviceStart = (row_2[45] if row_2[45] else None)
            serviceEnd = (row_2[46] if row_2[46] else None)
            unitCost = (row_2[54] if row_2[54] else None)
            weeklyMins = (row_2[53] if row_2[53] else None)
            age = (row_2[57] if row_2[57] else None)
            
            
            client = Client(lasID=lasID, nhsNumber=nhsNumber, firstName=firstName, lastName=lastName, birthDate=birthDate, deathDate=deathDate,
                            postCode=postCode, requestEvent = requestEvent, requestStart=requestStart, requestEnd=requestEnd, assessmentEvent=assessmentEvent,
                            assessmentStart=assessmentStart, assessmentEnd=assessmentEnd, weeklyVisits=weeklyVisits, weeklyCost=weeklyCost, weeklyUnits=weeklyUnits,
                            unitCost=unitCost, weeklyMins=weeklyMins,
                            serviceEvent=serviceEvent, serviceStart=serviceStart, serviceEnd=serviceEnd,age=age, requestOutcome=requestOutcome, ethnicity=ethnicity, 
                            gender=gender, primarySupportReason=primarySupportReason, accommodationStatus=accommodationStatus, serviceComponent=serviceComponent, 
                            serviceType=serviceType, employment=employment, informalCarer=informalCarer, routeOfAccess=routeOfAccess, assessmentOutcome=assessmentOutcome,
                            assessmentType=assessmentType, eligibility=eligibility, serviceProvider=serviceProvider, deliveryMechanism=deliveryMechanism,
                            costFrequency=costFrequency, copd=copd, cancer=cancer, physical=physical, hivAIDS=hivAIDS, otherPhysical=otherPhysical,
                            stroke=stroke, parkinsons=parkinsons, motorNeuron=motorNeuron, brainInjury=brainInjury, otherNeuro=otherNeuro, 
                            visuallyImpaired=visuallyImpaired, hearingImpaired=hearingImpaired, otherSensory=otherSensory, learningDisability=learningDisability,
                            ldIncl=ldIncl, ldExcl=ldExcl, otherLd=otherLd, otherMental=otherMental, dementiaMental=dementiaMental
                            )
            client.save()
        
        
        
        print("Import Completed")
    
      
                    
        
    
        
        
     
        
      
    
        
     
        
    
    

