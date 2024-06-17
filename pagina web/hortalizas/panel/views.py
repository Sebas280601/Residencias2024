from django.shortcuts import render
from django.http import HttpResponse
from .models import jitomate,lechuga,papa,zanahoria
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR,"templates")'
)

def index(request):
    return render(request,'index.html')

def kevin(request):
    return render(request,'kevin.html')

def sebas(request):
    lec = lechuga.find_one({"vegetal": "lechuga"})
    jit = jitomate.find_one({"vegetal": "jitomate"})
    pa = papa.find_one({"vegetal": "papa"})
    zana = zanahoria.find_one({"vegetal": "zanahoria"})
    # Si se envió un formulario
    if request.method == 'POST':
        hortaliza = request.POST.get('hortaliza')
        temperatura = float(request.POST.get('temperatura'))
        humedad = float(request.POST.get('humedad'))
        ph = float(request.POST.get('ph'))
        print(hortaliza)
        print(temperatura)
        print(humedad)
        print(ph)
        # Si se obtuvo todo lo del formulario
        if hortaliza and temperatura and humedad and ph:
            #Obtener cual hortaliza se envió en el formulario
            if hortaliza == 'zanahoria':
                resultado = zanahoriaDS(temperatura,humedad,ph,zana)
                return render(request,'sebas.html',{'parametro': resultado})
            elif hortaliza == 'lechuga':
                resultado = lechugaDS(temperatura,humedad,ph,lec)
                return render(request,'sebas.html',{'parametro': resultado})
            elif hortaliza == 'papa':
                resultado = papaDS(temperatura,humedad,ph,pa)
                return render(request,'sebas.html',{'parametro': resultado})
            elif hortaliza == 'jitomate':
                resultado = jitomateDS(temperatura,humedad,ph,jit)
                return render(request,'sebas.html',{'parametro': resultado})
            else:
                resultado = 8
                return render(request,'sebas.html',{'parametro': resultado})
        else:
            return render(request,'sebas.html')

    else:
        return render(request,'sebas.html')


def zanahoriaDS(t,h,p,z):
    max_temperatura = float(z["estadisticas"]["temperatura"]["max"])
    min_temperatura = float(z["estadisticas"]["temperatura"]["min"])
    max_humedad = float(z["estadisticas"]["humedad"]["max"])
    min_humedad = float(z["estadisticas"]["humedad"]["min"])
    max_ph = float(z["estadisticas"]["ph"]["max"])
    min_ph = float(z["estadisticas"]["ph"]["min"])
    
    if min_temperatura <= t <= max_temperatura:
        temp_status = True
    else:
        temp_status = False

    if min_humedad <= h <= max_humedad:
        hum_status = True
    else:
        hum_status = False

    if min_ph <= p <= max_ph:
        ph_status = True
    else:
        ph_status = False

    # Determinar el código numérico de acuerdo al estado de las variables
    if hum_status and temp_status and ph_status:
        return 0  # Humedad: bien, Temperatura: bien, pH: bien
    elif hum_status and temp_status and not ph_status:
        return 1  # Humedad: bien, Temperatura: bien, pH: mal
    elif hum_status and not temp_status and ph_status:
        return 2  # Humedad: bien, Temperatura: mal, pH: bien
    elif hum_status and not temp_status and not ph_status:
        return 3  # Humedad: bien, Temperatura: mal, pH: mal
    elif not hum_status and temp_status and ph_status:
        return 4  # Humedad: mal, Temperatura: bien, pH: bien
    elif not hum_status and temp_status and not ph_status:
        return 5  # Humedad: mal, Temperatura: bien, pH: mal
    elif not hum_status and not temp_status and ph_status:
        return 6  # Humedad: mal, Temperatura: mal, pH: bien
    elif not hum_status and not temp_status and not ph_status:
        return 7  # Humedad: mal, Temperatura: mal, pH: mal


def lechugaDS(t,h,p,z):
    max_temperatura = float(z["estadisticas"]["temperatura"]["max"])
    min_temperatura = float(z["estadisticas"]["temperatura"]["min"])
    max_humedad = float(z["estadisticas"]["humedad"]["max"])
    min_humedad = float(z["estadisticas"]["humedad"]["min"])
    max_ph = float(z["estadisticas"]["ph"]["max"])
    min_ph = float(z["estadisticas"]["ph"]["min"])
    
    if min_temperatura <= t <= max_temperatura:
        temp_status = True
    else:
        temp_status = False

    if min_humedad <= h <= max_humedad:
        hum_status = True
    else:
        hum_status = False

    if min_ph <= p <= max_ph:
        ph_status = True
    else:
        ph_status = False

    # Determinar el código numérico de acuerdo al estado de las variables
    if hum_status and temp_status and ph_status:
        return 0  # Humedad: bien, Temperatura: bien, pH: bien
    elif hum_status and temp_status and not ph_status:
        return 1  # Humedad: bien, Temperatura: bien, pH: mal
    elif hum_status and not temp_status and ph_status:
        return 2  # Humedad: bien, Temperatura: mal, pH: bien
    elif hum_status and not temp_status and not ph_status:
        return 3  # Humedad: bien, Temperatura: mal, pH: mal
    elif not hum_status and temp_status and ph_status:
        return 4  # Humedad: mal, Temperatura: bien, pH: bien
    elif not hum_status and temp_status and not ph_status:
        return 5  # Humedad: mal, Temperatura: bien, pH: mal
    elif not hum_status and not temp_status and ph_status:
        return 6  # Humedad: mal, Temperatura: mal, pH: bien
    elif not hum_status and not temp_status and not ph_status:
        return 7  # Humedad: mal, Temperatura: mal, pH: mal
    
def papaDS(t,h,p,z):
    max_temperatura = float(z["estadisticas"]["temperatura"]["max"])
    min_temperatura = float(z["estadisticas"]["temperatura"]["min"])
    max_humedad = float(z["estadisticas"]["humedad"]["max"])
    min_humedad = float(z["estadisticas"]["humedad"]["min"])
    max_ph = float(z["estadisticas"]["ph"]["max"])
    min_ph = float(z["estadisticas"]["ph"]["min"])
    
    if min_temperatura <= t <= max_temperatura:
        temp_status = True
    else:
        temp_status = False

    if min_humedad <= h <= max_humedad:
        hum_status = True
    else:
        hum_status = False

    if min_ph <= p <= max_ph:
        ph_status = True
    else:
        ph_status = False

    # Determinar el código numérico de acuerdo al estado de las variables
    if hum_status and temp_status and ph_status:
        return 0  # Humedad: bien, Temperatura: bien, pH: bien
    elif hum_status and temp_status and not ph_status:
        return 1  # Humedad: bien, Temperatura: bien, pH: mal
    elif hum_status and not temp_status and ph_status:
        return 2  # Humedad: bien, Temperatura: mal, pH: bien
    elif hum_status and not temp_status and not ph_status:
        return 3  # Humedad: bien, Temperatura: mal, pH: mal
    elif not hum_status and temp_status and ph_status:
        return 4  # Humedad: mal, Temperatura: bien, pH: bien
    elif not hum_status and temp_status and not ph_status:
        return 5  # Humedad: mal, Temperatura: bien, pH: mal
    elif not hum_status and not temp_status and ph_status:
        return 6  # Humedad: mal, Temperatura: mal, pH: bien
    elif not hum_status and not temp_status and not ph_status:
        return 7  # Humedad: mal, Temperatura: mal, pH: mal
    

def jitomateDS(t,h,p,z):
    max_temperatura = float(z["estadisticas"]["temperatura"]["max"])
    min_temperatura = float(z["estadisticas"]["temperatura"]["min"])
    max_humedad = float(z["estadisticas"]["humedad"]["max"])
    min_humedad = float(z["estadisticas"]["humedad"]["min"])
    max_ph = float(z["estadisticas"]["ph"]["max"])
    min_ph = float(z["estadisticas"]["ph"]["min"])
    
    if min_temperatura <= t <= max_temperatura:
        temp_status = True
    else:
        temp_status = False

    if min_humedad <= h <= max_humedad:
        hum_status = True
    else:
        hum_status = False

    if min_ph <= p <= max_ph:
        ph_status = True
    else:
        ph_status = False

    # Determinar el código numérico de acuerdo al estado de las variables
    if hum_status and temp_status and ph_status:
        return 0  # Humedad: bien, Temperatura: bien, pH: bien
    elif hum_status and temp_status and not ph_status:
        return 1  # Humedad: bien, Temperatura: bien, pH: mal
    elif hum_status and not temp_status and ph_status:
        return 2  # Humedad: bien, Temperatura: mal, pH: bien
    elif hum_status and not temp_status and not ph_status:
        return 3  # Humedad: bien, Temperatura: mal, pH: mal
    elif not hum_status and temp_status and ph_status:
        return 4  # Humedad: mal, Temperatura: bien, pH: bien
    elif not hum_status and temp_status and not ph_status:
        return 5  # Humedad: mal, Temperatura: bien, pH: mal
    elif not hum_status and not temp_status and ph_status:
        return 6  # Humedad: mal, Temperatura: mal, pH: bien
    elif not hum_status and not temp_status and not ph_status:
        return 7  # Humedad: mal, Temperatura: mal, pH: mal