from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from django.http import HttpResponse
import json
from sqlalchemy import create_engine
from clickhouse_sqlalchemy import make_session

uri = 'clickhouse://CFF:Q3bohJmeuQcItP9vmhVE@phoenix-db.data.tripi.vn:443/PhoeniX?ssl=true&charset=utf8&protocol=https'
engine = create_engine(uri)
session = make_session(engine)

def hotel_list(request):
    result = session.execute('''select *
                                from roothotel_info
                                limit 5''').fetchall()

    b = []
    for i in range(len(result)):
        a = {'id': result[i][0],'fields': {'name': result[i][1],'address': result[i][2]}}
        b.append(a)

    c = json.dumps(b)

    return HttpResponse(c, content_type="application/json")

def hotel_detail(request, id):
    result = session.execute('''select *
                                from roothotel_info
                                where id = :var''', {'var':  id}).fetchall()
    b = []
    for i in range(len(result)):
        a = {'id': result[i][0],'fields': {'name': result[i][1],'address': result[i][2]}}
        b.append(a)

    c = json.dumps(b)

    return HttpResponse(c, content_type="application/json")