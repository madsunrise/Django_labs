# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

def index(request):
    s1 = {
        'id': '21',
        'title': u'Автомойка',
        'body': u'Автомойка на углу Ботанической улицы, время работы 9-18 пн-вс'
    }

    s2 = {
        'id': '22',
        'title': u'Кафе быстрого питания',
        'body': u'Приглашаем в наше кафе каждый день с 10 до 20 часов по адресу ул. Мясницкая, 22А'
    }

    services = [s1, s2]

    return render(request, 'index.html', {'services': services})

def service (request, service_id):
    #service = get_object_or_404(Service, pk=question_id)
    service = {
        'id': '21',
        'title': u'Автомойка',
        'body': u'Автомойка на углу Ботанической улицы, время работы 9-18 пн-вс'
    }
    return render(request, 'service.html', {'service': service})