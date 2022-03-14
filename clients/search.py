from clients.models import Client
from django.db.models import Sum, Count, F, Avg, FloatField
from django.db.models.functions import Cast

def request_service_ratio(queryset):
    ratio = queryset.values('lasID').annotate(rcount=Count('requestStart', distinct=True),scount=Count('serviceStart',distinct=True))\
    .annotate(ratio=Cast('scount',FloatField())/Cast('rcount',FloatField()))
    return ratio

def basics(queryset):
    info = queryset[0]
    dictionary = {}
    dictionary['name'] = info.firstName + ' ' +info.lastName
    dictionary['gender'] = info.gender.name
    dictionary['ethnicity'] = info.ethnicity.name
    dictionary['age'] = info.age
    dictionary['postcode'] = info.postCode
    return dictionary


def psr(queryset):
    psr = queryset.values('primarySupportReason__name','serviceStart').distinct()
    return psr

def components(queryset):
    component = queryset.values('serviceComponent__name').distinct()
    return component

def health_conditions(queryset):
    alist = {'COPD':'copd_id', 'Cancer':'cancer_id', 'Physical Injury':'physical_id', 'HIV/AIDS':'hivAIDS_id',
            'Other Physical':'otherPhysical_id', 'Stroke':'stroke_id', 'Parkinsons':'parkinsons_id',
            'Motor Neurone Disease':'motorNeuron_id', 'Brain Injury':'brainInjury_id','Other Neurological':'otherNeuro_id',
            'Visually Impaired':'visuallyImpaired_id','Hearing Impaired':'hearingImpaired_id','Other Sensory':'otherSensory_id',
            'Learning Disability':'learningDisability_id',"Autism(including Asperger's)" :'ldIncl_id',
            "Autism(excluding Asperger's)":'ldExcl_id', 'Other LD':'otherLd_id','Other Mental':'otherMental_id',
            'Dementia':'dementiaMental_id'}
    bag = []
    record = queryset[0].__dict__
    for a in record:
        profile = {}
        for b,c in alist.items():
            if a == c and record[c] == 2:
                profile['condition'] = b
                bag.append(profile)
            
    return bag

def delivery_mechanism(queryset):
    record = queryset.values('deliveryMechanism__name').distinct()
    return record

def service_particulars(queryset):
    record = queryset.values('serviceProvider__name','deliveryMechanism__name','serviceComponent__name','serviceStart','serviceEnd','weeklyVisits','weeklyCost','unitCost','weeklyMins').distinct()
    return record
                

def plan_type(queryset):
    record = queryset.values('serviceType__name').distinct()
    return record

def eligibility(queryset):
    record = queryset.values('eligibility__name').annotate(count=Count('assessmentStart', distinct=True))
    return record

def deceased(queryset):
    record = queryset[0]
    composite = {}
    death_date = record.deathDate
    if death_date is None:
        composite['status'] = 'Not Deceased'
    else:
        composite['status'] = 'Deceased'
    return composite
        
    
    
 