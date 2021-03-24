import csv
from itertools import islice

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views import View
# import bulk_update_or_create
from django.views.generic import DetailView, ListView

from webapp.models import Firma, People, OpenBudget


class SearchView(LoginRequiredMixin, ListView):
    model = Firma
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        search_str_1 = self.request.GET.get('search_str')
        if search_str_1:
            search_str = " ".join(search_str_1.split())


            if search_str:
                firma_objects = Firma.objects.filter((Q(full_name_ru__icontains=search_str) | Q(full_name_kg__icontains=search_str)
                                                      | Q(director__icontains=search_str) | Q(founders__icontains=search_str) |
                                                      Q(inn__icontains=search_str)))
                # print(firma_objects)
                context['firmas'] = firma_objects
                context['search_str'] = search_str

            return context


class FirmaView(LoginRequiredMixin, ListView):
    model = Firma
    template_name = 'detail.html'
    paginate_by = 5
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        firma_inn = []
        context = {}
        firma = Firma.objects.get(pk=kwargs['pk'])
        firma_inn.append(firma)
        print(firma, 'ddddd')

        print(len(firma.director.upper().split()))
        director = firma.director.upper().split()
        print(director[0])
        print(director[1])
        if len(director) == 3:
            director_objects = People.objects.filter((Q(last_name__icontains=director[0]) & Q(first_name__icontains=director[1]) & Q(middle_name__icontains=director[2])))
        else:
            director_objects = People.objects.filter((Q(last_name__icontains=director[0]) & Q(
                first_name__icontains=director[1])))
        firma_inn.append(director_objects)
        print(director_objects,'dfgfdg')
        for obj in director_objects:
            print(obj.first_name)

        # inn = firma.inn
        # inn_objects = OpenBudget.objects.filter(Q(inn__icontains=inn))
        # print(inn_objects, 'INN')
        # print(inn, 'BYYYYY')
        #
        # context['budget'] = inn_objects
        context['firma'] = firma_inn
        print(context['firma'])

        return render(request=request, template_name=self.template_name, context=context)


class FirmaSecondView(LoginRequiredMixin, ListView):
    template_name = 'detail_2.html'
    model = Firma
    paginate_by = 5
    paginate_orphans = 2

    def get(self, request, *args, **kwargs):
        context = {}
        firma = Firma.objects.get(pk=kwargs['pk'])

        f = []
        print(firma.founders)
        old_founders = firma.founders.strip('[]').split(',')
        print(old_founders,'foundres')
        founders = []
        for founder in old_founders:
            fo = founder.strip("' ")
            print(founder, 'цикл')
            founders.append(fo)
        print(founders,'за циклом')
        founders = founders
        print(len(founders))
        if founders.__contains__('Замените на физическое лицо 1'):
            pass
        else:
            if founders[0] != '':
                for founder in founders:
                    firma_objects_2 = Firma.objects.filter(Q(founders__icontains=founder) | Q(director__icontains=founder))
                    fff = {
                        'name': founder,
                        'firmas': firma_objects_2
                    }
                    f.append(fff)

            else:
                pass
            print('none')

        print(f)
        print(len(firma.director))
        print(firma.director ,'1111111')
        context['fir'] = firma.director
        if len(firma.director) != '':
            director_objects_2 = Firma.objects.filter(Q(founders__icontains=firma.director) | Q(director__icontains=firma.director))
            context['firmas_3'] = director_objects_2


        print(firma.address_street)
        if firma.address_street != None and firma.address_street != '':
            if '.' in firma.address_street:
                street = firma.address_street.split('.')[1]
            else:
                street = firma.address_street
            addresses = Firma.objects.filter(Q(address_street__icontains=street) & Q(house_number__icontains=firma.house_number))
            print(addresses)
            context['addresses'] = addresses
        else:
            pass
        context['firmas_2'] = f
        print(firma.phone, 'dfgfddfggit ')

        firma_inn = []
        firma_inn.append(firma)
        print(firma, 'ddddd')

        print(len(firma.director.upper().split()))
        director = firma.director.upper().split()
        print(director[0])
        print(director[1])
        if len(director) == 3:
            director_objects = People.objects.filter((Q(last_name__icontains=director[0]) & Q(
                first_name__icontains=director[1]) & Q(middle_name__icontains=director[2])))
        else:
            director_objects = People.objects.filter((Q(last_name__icontains=director[0]) & Q(
                first_name__icontains=director[1])))
        firma_inn.append(director_objects)
        print(director_objects, 'dfgfdg')
        for obj in director_objects:
            print(obj.first_name)

        context['firma'] = firma_inn
        print(context['firma'], 2222222)

        return render(request=request, template_name=self.template_name, context=context)