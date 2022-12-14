import firebase_admin
from firebase_admin import firestore
import random
from firebase_admin import credentials
import time
from datetime import datetime

#Application defalut credentials 
cred = credentials.Certificate("credentials.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

while(True):
    current_date = datetime.now()
    date = current_date.strftime('%Y-%m-%d')
    hour = current_date.strftime('%H')
    print(date)
    print(hour)
    collection_name = u'sensor_1{0}'.format(date)
    hour_ref = db.collection(collection_name).document(hour)
    encendido = bool(random.getrandbits(1))
    hour_doc = hour_ref.get()
    hour_data = hour_doc.to_dict()
    totals_ref = db.collection(collection_name).document('totals')
    totals_doc = totals_ref.get()
    totals_data = totals_doc.to_dict()
    if totals_data == None:
        totals_ref.set({
            u'total_minutos_encendido' : 1 if encendido else 0
        })
    else:
        if encendido:
            totals_ref.update({
                u'total_minutos_encendido' : totals_data[u'total_minutos_encendido'] + 1
            })
    if hour_data == None:
        hour_ref.set({
            u'minutos_encendido' : 1 if encendido else 0,
            u'minutos_apagado' : 0 if not encendido else 0
        })
    else:
        if encendido:
            hour_ref.update({
                u'minutos_encendido' : hour_data[u'minutos_encendido'] + 1
            })
        else:
            hour_ref.update({
                u'minutos_apagado' : hour_data[u'minutos_apagado'] + 1
            })
    time.sleep(10)