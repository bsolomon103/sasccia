from .models import Client 

allClientsclients = Client.objects.all()
def requestCount():
    all_clients = Client.objects.all()
    jan = list()
    feb = list()
    mar = list()
    apr = list()
    may = list()
    jun = list()
    jul = list()
    aug = list()
    sep = list()
    octo = list()
    nov = list()
    dec = list()
    d_one = dict()
    d_two = dict()
    d_three = dict()
    d_four = dict()
    d_five = dict()
    d_six = dict()
    d_seven = dict()
    d_eight = dict()
    d_nine = dict()
    d_ten = dict()
    d_eleven = dict()
    d_twelve = dict()
    
    for person in all_clients:
        month = person.requestStart.month
        if month == 1:
            jan.append(month)
        if month == 2:            
            feb.append(month)
        if month == 3:
            mar.append(month)
        if month == 4:
            apr.append(month)
        if month == 5:
            may.append(month)
        if month == 6:
            jun.append(month)
        if month == 7:
            jul.append(month)
        if month == 8:
            aug.append(month)
        if month == 9:
            sep.append(month)
        if month == 10:
            octo.append(month)
        if month == 11:
            nov.append(month)
        if month == 12:
            dec.append(month)
    d_one['month'] = '01'
    d_one['count'] = len(jan)
    d_two['month'] = '02'
    d_two['count'] = len(feb)
    d_three['month'] = '03'
    d_three['count'] = len(mar)
    d_four['month'] = '04'
    d_four['count'] = len(apr)
    d_five['month'] = '05'
    d_five['count'] = len(may)
    d_six['month'] = '06'
    d_six['count'] = len(jun)
    d_seven['month'] = '07'
    d_seven['count'] = len(jul)
    d_eight['month'] = '08'
    d_eight['count'] = len(aug)
    d_nine['month'] = '09'
    d_nine['count'] = len(sep)
    d_ten['month'] = '10'
    d_ten['count'] = len(octo)
    d_eleven['month'] = '11'
    d_eleven['count'] = len(nov)
    d_twelve['month'] = '12'
    d_twelve['count'] = len(dec)
    return d_one, d_two, d_three, d_four, d_five, d_six, d_seven, d_eight, d_nine, d_ten, d_eleven, d_twelve