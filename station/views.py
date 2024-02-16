from django.shortcuts import redirect, render
from django.http import HttpResponse
from division.models import Divisions
from district.models import Districts
from .models import Station
import pandas as pd
from django.core.exceptions import ValidationError




def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            raise ValidationError('File is not a CSV')
        df = pd.read_csv(csv_file)
        for index, row in df.iterrows():
            div_id = row['div_id']  # Assuming 'div_id' is a column in the CSV
            dis_id = row['dis_id']  # Assuming 'dis_id' is a column in the CSV
            name = row['name']  # Assuming 'name' is a column in the CSV
            div = Divisions.objects.get(id=div_id)
            dis = Districts.objects.get(id=dis_id)
            Station.objects.create(name=name, div_id=div, dis_id=dis)
        return HttpResponse("Data inserted Successfully.")
    
    return redirect('station_index')


def search(request): 
   search_value = request.POST.get('search')
   search_result = Station.objects.filter(name__icontains=search_value)
   print(len(search_result))
   return HttpResponse(len(search_result))


def index(request):
    # data = Divisions.objects.all().order_by('divisionname')
    data2 = Districts.objects.values_list('div_id__divisionname', 'div_id__id', flat=False).distinct()
    # data3 = Districts.objects.values_list('Districtname', flat=True).distinct()
    
    data3 = Districts.objects.all()
    data4 = Station.objects.select_related('div_id','dis_id').all()

    data_context = {'d2':data2,'d3':data3,'d4':data4}
    return render(request,'admin/station.html',data_context)


def district_insert(request):
    div_id = request.POST.get('div_id')
    dis_id = request.POST.get('dis_id')
    name = request.POST.get('name')
    image = request.FILES.get('image')

    st_obj = Station()

    div_obj = Divisions.objects.get(id=div_id)
    dis_obj = Districts.objects.get(id=dis_id)

    st_obj.name = name
    st_obj.div_id = div_obj
    st_obj.dis_id = dis_obj
    st_obj.image = image
    st_obj.save()

    return redirect('station_index')



def hospitals(request):
    return render(request, 'admin/search.html')


