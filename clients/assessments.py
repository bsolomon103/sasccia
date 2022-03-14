'''
from clients.models import Client, RouteOfAccess, Gender, PrimarySupportReason, Ethnicity
from django.db.models import Avg, Count


def average(lst):
    tot = sum(lst)
    size = len(lst)
    avg = tot/size
    return round(avg,2)
    
def ass_delta():
    cohort = Client.objects.exclude(assessmentStart = None)
    
    # Route of access
    hosp = []
    hosp_serv = []
    comm = []
    carer = []
    dep = []
    trans = []
   
    
    #PSR
    asylum = []
    personal = []
    memory = []
    isolation = []
    visual = []
    hearing = []
    mobility = []
    not_known = []
    misuse = []
    dual = []


    
    for people in cohort:
        if people.routeOfAccess_id == 1:
            delta = abs(people.assessmentStart - people.assessmentEnd)
            route = RouteOfAccess.objects.get(id=people.routeOfAccess_id)
            comm.append(delta.days)
        
        if people.routeOfAccess_id == 3:
            delta = abs(people.assessmentStart - people.assessmentEnd)
            route = RouteOfAccess.objects.get(id=people.routeOfAccess_id)
            hosp.append(delta.days)
            
        if people.routeOfAccess_id == 4:
            delta = abs(people.assessmentStart - people.assessmentEnd)
            route = RouteOfAccess.objects.get(id=people.routeOfAccess_id)
            carer.append(delta.days)
            
        if people.routeOfAccess_id == 5:
            delta = abs(people.assessmentStart - people.assessmentEnd)
            route = RouteOfAccess.objects.get(id=people.routeOfAccess_id)
            hosp_serv.append(delta.days)
        
        if people.routeOfAccess_id == 6:
            delta = abs(people.assessmentStart - people.assessmentEnd)
            route = RouteOfAccess.objects.get(id=people.routeOfAccess_id)
            trans.append(delta.days)
        
        if people.routeOfAccess_id == 7:
            delta = abs(people.assessmentStart - people.assessmentEnd)
            route = RouteOfAccess.objects.get(id=people.routeOfAccess_id)
            dep.append(delta.days)
    
        
    for people in cohort:
        if people.primarySupportReason_id == 1:
            delta = abs(people.assessmentStart - people.assessmentEnd)
            reason = PrimarySupportReason.objects.get(id=people.primarySupportReason_id)
            not_known.append(delta.days)
        
        if people.primarySupportReason_id == 2:
            delta = abs(people.assessmentStart - people.assessmentEnd)
            reason = PrimarySupportReason.objects.get(id=people.primarySupportReason_id)
            mobility.append(delta.days)
        
        if people.primarySupportReason_id == 3:
            delta = abs(people.assessmentStart - people.assessmentEnd)
            reason = PrimarySupportReason.objects.get(id=people.primarySupportReason_id)
            personal.append(delta.days)
        
        if people.primarySupportReason_id == 4:
            delta = abs(people.assessmentStart - people.assessmentEnd)
            reason = PrimarySupportReason.objects.get(id=people.primarySupportReason_id)
            dual.append(delta.days)
        
        if people.primarySupportReason_id == 5:
            delta = abs(people.assessmentStart - people.assessmentEnd)
            reason = PrimarySupportReason.objects.get(id=people.primarySupportReason_id)
            visual.append(delta.days)
        
        if people.primarySupportReason_id == 6:
            delta = abs(people.assessmentStart - people.assessmentEnd)
            reason = PrimarySupportReason.objects.get(id=people.primarySupportReason_id)
            isolation.append(delta.days)
        
        if people.primarySupportReason_id == 7:
            delta = abs(people.assessmentStart - people.assessmentEnd)
            reason = PrimarySupportReason.objects.get(id=people.primarySupportReason_id)
            memory.append(delta.days)
        
        if people.primarySupportReason_id == 8:
            delta = abs(people.assessmentStart - people.assessmentEnd)
            reason = PrimarySupportReason.objects.get(id=people.primarySupportReason_id)
            hearing.append(delta.days)
        
        if people.primarySupportReason_id == 9:
            delta = abs(people.assessmentStart - people.assessmentEnd)
            reason = PrimarySupportReason.objects.get(id=people.primarySupportReason_id)
            misuse.append(delta.days)
        
        if people.primarySupportReason_id == 10:
            delta = abs(people.assessmentStart - people.assessmentEnd)
            reason = PrimarySupportReason.objects.get(id=people.primarySupportReason_id)
            asylum.append(delta.days)
            
        
    community = {}
    community['category'] = 'Community/Other Route'
    community['mean'] = average(comm)
    hospital = {}
    hospital['category'] = 'Discharge From Hospital'
    hospital['mean'] = average(hosp)
    support_for_carer = {}
    support_for_carer['category'] = 'Support For Carer'
    support_for_carer['mean'] = average(carer)
    diversion = {}
    diversion['category'] = 'Diversion From Hospital Service'
    diversion['mean'] = average(hosp_serv)
    transition = {}
    transition['category'] = 'Planned Entry(Transition)'
    transition['mean'] = average(trans)
    depleted = {}
    depleted['category'] = 'Self Funder with Depleted Funds'
    depleted['mean'] = average(dep)
    
    route_of_access = []
    route_of_access.append(community)
    route_of_access.append(hospital)
    route_of_access.append(support_for_carer)
    route_of_access.append(diversion)
    route_of_access.append(transition)
    route_of_access.append(depleted)
    

    d_asylum = {}
    d_asylum['category'] = 'Social Support: Asylum seeker support'
    d_asylum['mean'] = average(asylum)
    d_pers = {}
    d_pers['category'] = 'Physical Support: Personal care support'
    d_pers['mean'] = average(personal)
    d_mem = {}
    d_mem['category'] = 'Support with Memory & Cognition'
    d_mem['mean'] = average(memory)
    d_iso = {}
    d_iso['category'] = 'Social Support: Support for Social Isolation/Other'
    d_iso['mean'] = average(isolation)
    d_vis = {}
    d_vis['category'] = 'Sensory Support: Support for visual impairment'
    d_vis['mean'] = average(visual)
    d_hear = {}
    d_hear['category'] = 'Sensory Support: Support for hearing impairment'
    d_hear['mean'] = average(hearing)
    d_mob = {}
    d_mob['category'] = 'Physical Support: Access & mobility only'
    d_mob['mean'] = average(mobility)
    d_not = {}
    d_not['category'] = 'PSR Not Known'
    d_not['mean'] = average(not_known)
    d_mis = {}
    d_mis['category'] = 'Social Support: Substance misuse support'
    d_mis['mean'] = average(misuse)
    d_dual = {}
    d_dual['category'] = 'Sensory Support: Support for dual impairment'
    d_dual['mean'] = average(dual)
    psrs = []
    psrs.append(d_asylum)
    psrs.append(d_pers)
    psrs.append(d_mem)
    psrs.append(d_iso)
    psrs.append(d_vis)
    psrs.append(d_hear)
    psrs.append(d_mob)
    psrs.append(d_not)
    psrs.append(d_mis)
    psrs.append(d_dual)


    composite = {}
    composite['Routes Of Access'] = route_of_access
    composite['Primary Support Reason'] = psrs
 
    
    
    return composite
    '''
            
