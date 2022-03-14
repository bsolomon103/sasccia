from clients.models import Ethnicity, Client
from django.db.models import Count

def health_profile():
    races = Ethnicity.objects.all()
    clients = Client.objects.all()
    
    #HEALTH CONDITIONS
    copd = clients.values('ethnicity__name').annotate(count=Count('copd')).filter(copd_id=2)
    cancer = clients.values('ethnicity__name').annotate(count=Count('cancer')).filter(cancer_id=2)
    physical = clients.values('ethnicity__name').annotate(count=Count('physical')).filter(physical_id=2)
    aids = clients.values('ethnicity__name').annotate(count=Count('hivAIDS')).filter(hivAIDS_id=2)
    otherphysical = clients.values('ethnicity__name').annotate(count=Count('otherPhysical')).filter(otherPhysical_id=2)
    stroke = clients.values('ethnicity__name').annotate(count=Count('stroke')).filter(stroke_id=2)
    parkinsons = clients.values('ethnicity__name').annotate(count=Count('parkinsons')).filter(parkinsons_id=2)
    motorneuron = clients.values('ethnicity__name').annotate(count=Count('motorNeuron')).filter(motorNeuron_id=2)
    braininjury = clients.values('ethnicity__name').annotate(count=Count('brainInjury')).filter(brainInjury_id=2)
    otherneuro = clients.values('ethnicity__name').annotate(count=Count('otherNeuro')).filter(otherNeuro_id=2)
    visual = clients.values('ethnicity__name').annotate(count=Count('visuallyImpaired')).filter(visuallyImpaired_id=2)
    hearing = clients.values('ethnicity__name').annotate(count=Count('hearingImpaired')).filter(hearingImpaired=2)
    other_sensory = clients.values('ethnicity__name').annotate(count=Count('otherSensory')).filter(otherSensory_id=2)
    learning_disability = clients.values('ethnicity__name').annotate(count=Count('learningDisability')).filter(learningDisability_id=2)
    incl = clients.values('ethnicity__name').annotate(count=Count('ldIncl')).filter(ldIncl_id=2)
    excl = clients.values('ethnicity__name').annotate(count=Count('ldExcl')).filter(ldExcl_id=2)
    other_ld = clients.values('ethnicity__name').annotate(count=Count('otherLd')).filter(otherLd_id=2)
    other_mental = clients.values('ethnicity__name').annotate(count=Count('otherMental')).filter(otherMental_id=2)
    dementia = clients.values('ethnicity__name').annotate(count=Count('dementiaMental')).filter(dementiaMental_id=2)
    
    chinese = []
    white_british = []
    mixed = []
    refused = []
    indian = []
    undeclared = []
    other_ethnic = []
    other_white = []
    bangladeshi = []
    white_irish = []
    pakistani = []
    white_black_african = []
    african = []
    other_black = []
    caribbean = []
    other_asian = []
    white_asian = []
    white_black_carr = []
    arab = []
    white_gypsy = []
    composite = {}
    health_conditions = {'COPD':copd, 'Cancer':cancer, 'Physical Injury':physical,
                        'HIV/AIDS':aids, 'Other Physical': otherphysical, 'Stroke':stroke,
                        "Parkinson's":parkinsons, 'Motor Neurone Disease':motorneuron, 
                        'Acquired Brain Injury':braininjury, 'Other Neurological':otherneuro, 
                        'Visually Impaired':visual, 'Hearing Impaired':hearing, 'Other Sensory':other_sensory, 
                        'Learning Disability':learning_disability, 
                        "Autism(excluding Asperger's)":incl, 
                        "Autism(including Asperger's)":excl, 'Other LD':other_ld, 
                        'Other Mental':other_mental, 'Dementia':dementia}

    for a in races:
        for k,v in health_conditions.items():
            dictionary = {}
            output = v.filter(ethnicity__name = a)
            if len(output) > 0: 
                dictionary['ethnicity__name'] = output[0]['ethnicity__name']
                dictionary['count'] = output[0]['count']
                dictionary['health_condition'] = k
                if dictionary['ethnicity__name'] == 'White British':
                    white_british.append(dictionary)
                    composite[dictionary['ethnicity__name']] = white_british
                if dictionary['ethnicity__name'] == 'Other Mixed':
                    mixed.append(dictionary)
                    composite[dictionary['ethnicity__name']] = mixed
                if dictionary['ethnicity__name'] == 'Refused':
                    refused.append(dictionary)
                    composite[dictionary['ethnicity__name']] = refused
                if dictionary['ethnicity__name'] == 'Indian':
                    indian.append(dictionary)
                    composite[dictionary['ethnicity__name']] = indian
                if dictionary['ethnicity__name'] == 'Unknown/Undeclared':
                    undeclared.append(dictionary)
                    composite[dictionary['ethnicity__name']] = undeclared
                if dictionary['ethnicity__name'] == 'Other Ethnicity':
                    other_ethnic.append(dictionary)
                    composite[dictionary['ethnicity__name']] = other_ethnic
                if dictionary['ethnicity__name'] == 'Other White':
                    other_white.append(dictionary)
                    composite[dictionary['ethnicity__name']] = other_white
                if dictionary['ethnicity__name'] == 'Bangladeshi':
                    bangladeshi.append(dictionary)
                    composite[dictionary['ethnicity__name']] = bangladeshi
                if dictionary['ethnicity__name'] == 'White Irish':
                    white_irish.append(dictionary)
                    composite[dictionary['ethnicity__name']] = white_irish
                if dictionary['ethnicity__name'] == 'Pakistani':
                    pakistani.append(dictionary)
                    composite[dictionary['ethnicity__name']] = pakistani
                if dictionary['ethnicity__name'] == 'White and Black African':
                    white_black_african.append(dictionary)
                    composite[dictionary['ethnicity__name']] = white_black_african
                if dictionary['ethnicity__name'] == 'African':
                    african.append(dictionary)
                    composite[dictionary['ethnicity__name']] = african
                if dictionary['ethnicity__name'] == 'Any other Black':
                    other_black.append(dictionary)
                    composite[dictionary['ethnicity__name']] = other_black
                if dictionary['ethnicity__name'] == 'Caribbean':
                    caribbean.append(dictionary)
                    composite[dictionary['ethnicity__name']] = caribbean
                if dictionary['ethnicity__name'] == 'Other Asian':
                    other_asian.append(dictionary)
                    composite[dictionary['ethnicity__name']] = other_asian
                if dictionary['ethnicity__name'] == 'White and Asian':
                    white_asian.append(dictionary)
                    composite[dictionary['ethnicity__name']] = white_asian
                if dictionary['ethnicity__name'] == 'White and Black Caribbean':
                    white_black_carr.append(dictionary)
                    composite[dictionary['ethnicity__name']] = white_black_carr
                if dictionary['ethnicity__name'] == 'Arab':
                    arab.append(dictionary)
                    composite[dictionary['ethnicity__name']] = arab
                if dictionary['ethnicity__name'] == 'White Gypsy':
                    white_gypsy.append(dictionary)
                    composite[dictionary['ethnicity__name']] = white_gypsy
                if dictionary['ethnicity__name'] == 'Chinese':
                    chinese.append(dictionary)
                    composite[dictionary['ethnicity__name']] = chinese

    return composite
        
        
        
        

        


    
    

