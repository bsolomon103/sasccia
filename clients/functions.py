from clients.models import Client, RequestOutcome, Gender, Ethnicity, PrimarySupportReason, RouteOfAccess, ServiceType, Eligibility
from django.db.models import Count, F, Avg, FloatField
from django.db.models.functions import Cast


def outcomes_list():
    composite = {}
    allGender = Client.objects.values('gender__name', 'requestOutcome__name').annotate(count=Count('gender')).order_by()
    nofilter = Client.objects.values('requestOutcome__name').annotate(count=Count('requestOutcome')).order_by()
    genders = Gender.objects.all()
    for items in genders:
        gender_names = items.name
        composite[gender_names] = allGender.filter(gender__name=gender_names)
        
    composite['all'] = nofilter
    return composite

def routesOfAccessCount():
    composite = {}
    routes = Client.objects.values('ethnicity__name','routeOfAccess__name').annotate(reqcount=Count('requestStart')).order_by()
    races = Ethnicity.objects.all()
    for items in races:
        race_names = items.name
        composite[race_names] = routes.filter(ethnicity__name=race_names)
    return composite

def ethnicity():
    ethees = []
    ethnicitySet = (Client.objects.values('ethnicity__name').annotate(count=Count('ethnicity')).order_by())
    ethnicities = Ethnicity.objects.all()
    for item in ethnicities:
        ethnicity_name = item.name
        qs = ethnicitySet.filter(ethnicity__name = ethnicity_name)
        ethees.append(qs[0])   
    return ethees

def support_reasons():
    psrs = []
    psrSet = Client.objects.values('primarySupportReason__name').annotate(count=Count('primarySupportReason')).order_by()
    reasons = PrimarySupportReason.objects.all()
    for items in reasons:
        reason_name = items.name
        qs = psrSet.filter(primarySupportReason__name = reason_name)
        psrs.append(qs[0])
    return psrs

def routes_of_access():
    roa = []
    roaSet = Client.objects.values('routeOfAccess__name').annotate(count=Count('routeOfAccess')).order_by()
    routes = RouteOfAccess.objects.all()
    for items in routes:
        routes_name = items.name
        qs = roaSet.filter(routeOfAccess__name = routes_name)
        roa.append(qs[0])
    return roa
 
def services(): 
    sers = []
    serviceSet = Client.objects.values('serviceType__name').annotate(count=Count('serviceType')).order_by()
    types = ServiceType.objects.all()
    for items in types:
        types_name = items.name
        qs = serviceSet.filter(serviceType__name = types_name)
        sers.append(qs[0])
    return sers

def request_count_month():
    month = Client.objects.values('requestStart__month').annotate(count=Count('lasID')).order_by()
    return month
 
def average(lst):
    avg = round(sum(lst)/len(lst),2)
    return avg
    
def assessment_delta():
    have_assessments = Client.objects.filter(assessmentStart__isnull = False)
    races = Ethnicity.objects.all()
    routes = RouteOfAccess.objects.all()
    reasons = PrimarySupportReason.objects.all()
    bag = {}
    one = []
    two = []
    three = []
    for items in races:
        ethnicities = {}
        work = []
        qs = have_assessments.filter(ethnicity__name = items.name)
        for persons in qs:
            delta = abs((persons.assessmentStart - persons.assessmentEnd).days)
            work.append(delta)
            if len(work) > 0:
                avg = average(work)
        ethnicities['category'] = items.name
        ethnicities['delta'] = avg
        one.append(ethnicities)
        bag['ethnicities'] = one
        
    
    for items in routes:
        routes = {}
        work = []
        qs = have_assessments.filter(routeOfAccess__name = items.name)
        for persons in qs:
            delta = abs((persons.assessmentStart - persons.assessmentEnd).days)
            work.append(delta)
            if len(work) > 0:
                avg = average(work)
        routes['category'] = items.name
        routes['delta'] = avg
        two.append(routes)
        bag['routes'] = two
    
    for items in reasons:
        reasons = {}
        work = []
        qs = have_assessments.filter(primarySupportReason__name = items.name)
        for persons in qs:
            delta = abs((persons.assessmentStart - persons.assessmentEnd).days)
            work.append(delta)
            if len(work) > 0:
                avg = average(work)
        reasons['category'] = items.name
        reasons['delta'] = avg
        three.append(reasons)
        bag['reasons'] = three
    return bag
    
def age_assessmentDelta():
    ass_delta = Client.objects.filter(assessmentStart__isnull=False).exclude(eligibility__name = '')\
    .values('age','eligibility__name').annotate(delta = F('assessmentEnd') - F('assessmentStart'))
    xx = ass_delta.values('age','eligibility__name').annotate(mean = Avg('delta'))
    elig_list = []
 
    for items in xx:
        person = {}
        person['age'] = items['age']
        person['delta'] = items['mean'].days
        person['eligibility'] = items['eligibility__name']
        elig_list.append(person)
    return elig_list
    
def acc_employment():
    types = ['Not in Paid Employment (not actively seeking work / retired)',
            'Not in Paid Employment (seeking work)',
            'Paid: 16 or more hours a week',
            'Paid: Less than 16 hours a week',
            'Unknown']
    composite = {}
    all_clients = Client.objects.exclude(employment__name  = '').exclude(accommodationStatus__name = '')
    total = len(all_clients)
    xx = all_clients.values('employment__name','accommodationStatus__name')\
    .annotate(count=Count('accommodationStatus'))\
    .exclude(employment__name = '')\
    .annotate(percentage = Cast('count',FloatField())/Cast(total,FloatField())*100)
    for a in types:
        output = xx.filter(employment__name=a)
        composite[a] = output
    return composite
    
    
def unit_cost():
    bag = []
    a = Client.objects.exclude(assessmentStart__isnull = True)
    b = a.exclude(serviceStart__isnull = True)
    c = a.exclude(serviceEnd__isnull = True)
    d = Client.objects.exclude(deathDate__isnull = True)
    e = Client.objects.all()
    
    open_count = b.values('requestStart').annotate(count=Count('serviceStart'))
    ass_count = a.values('requestStart').annotate(count=Count('assessmentStart'))
    closed_count = c.values('requestStart').annotate(count=Count('serviceEnd'))
    death_count = d.values('requestStart').annotate(count=Count('lasID', distinct=True))
    req_count = e.values('requestStart').annotate(count=Count('requestStart'))
    
    composite = {}
    composite['requests'] = req_count
    composite['assessments'] = ass_count
    composite['opened'] = open_count
    composite['closed'] = closed_count
    composite['deaths'] = death_count
  
    return composite
    

def providers():

    all_clients = Client.objects.exclude(serviceType__name='')
    types = ['Long Term Support: Community',
            'Long Term Support: Nursing Care',
            'Long Term Support: Residential Care',
            'Short Term Support: Other Short Term',
            'Short Term Support: ST-Max']
    composite = {}
    for service in types:
        output = all_clients.values('serviceProvider__name','serviceComponent__name').annotate(count=Count('serviceComponent'))\
        .filter(serviceType__name=service).order_by('-count')[:10]
        composite[service] = output
    
    return composite
    

def health_costs():
    all_clients = Client.objects.all()
    copd = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(copd_id=2).exclude(visits__isnull = True)
    cancer = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(cancer_id=2).exclude(visits__isnull = True)
    physical = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(physical_id=2).exclude(visits__isnull = True)
    hiv_aids = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(hivAIDS_id=2).exclude(visits__isnull = True)
    other_physical = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(otherPhysical_id=2).exclude(visits__isnull = True)
    stroke = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(stroke_id=2).exclude(visits__isnull = True)
    parkinsons = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(parkinsons_id=2).exclude(visits__isnull = True)
    motor_neuron = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(motorNeuron_id=2).exclude(visits__isnull = True)
    brain_injury = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(brainInjury_id=2).exclude(visits__isnull = True)
    other_neuro = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(otherNeuro_id=2).exclude(visits__isnull = True)
    visually = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(visuallyImpaired_id=2).exclude(visits__isnull = True)
    hearing = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(hearingImpaired_id=2).exclude(visits__isnull = True)
    other_sensory = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(otherSensory_id=2).exclude(visits__isnull = True)
    learning = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(learningDisability_id=2).exclude(visits__isnull = True)
    include = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(ldIncl_id=2).exclude(visits__isnull = True)
    exclude = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(ldExcl_id=2).exclude(visits__isnull = True)
    other_ld = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(otherLd_id=2).exclude(visits__isnull = True)
    other_mental = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(otherMental_id=2).exclude(visits__isnull = True)
    dementia = all_clients.values('serviceType__name').annotate(visits=Avg('weeklyVisits'),cost=Avg('weeklyCost')).filter(dementiaMental_id=2).exclude(visits__isnull = True)
    
    dictionary = {'COPD':copd, 'Cancer':cancer, 'Physical Injury':physical,
        'HIV/AIDS':hiv_aids, 'Other Physical':other_physical, 'Stroke':stroke, 
        "Parkinson's":parkinsons, 'Motor Neurone Disease':motor_neuron, 
        'Acquired Brain Injury':brain_injury, 'Other Neurological':other_neuro, 
        'Visually Impaired':visually, 'Hearing Impaired':hearing, 
        'Other Sensory':other_sensory, 'Learning Disability': learning, 
        "Autism(excluding Asperger's)":exclude, 
        "Autism(including Asperger's)":include, 
        'Other LD':other_ld, 
        'Other Mental':other_mental, 'Dementia': dementia
    }
    composite = {}
    for k,v in dictionary.items():
        if len(v) > 0:
            composite[k] = v
        
    return composite

    
    
    