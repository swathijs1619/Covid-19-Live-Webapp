from django.shortcuts import render
import json
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "63d8353893mshdcaa4d24bb83353p1f3b06jsn35fe0b06800e",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def helloworldview(request):
    lst = []
    noofresults = int(response['results'])
    for i in range(0, noofresults):
        lst.append(response['response'][i]['country'])
        
    if request.method=="POST":
        selectedcountry = request.POST['selectedcountry']
        
        noofresults = int(response['results'])
        for x in range(0, noofresults):
            if selectedcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {'selectedcountry': selectedcountry, 'lst':lst, 'new':new, 'active':active, 'critical':critical, 'total':total, 'deaths':deaths, 'recovered':recovered}
        return render(request, 'helloworld.html', context)
    
    lst = []
    noofresults = int(response['results'])
    for i in range(0, noofresults):
        lst.append(response['response'][i]['country'])
    
    context = {'lst': lst}

    return render(request, 'helloworld.html', context)