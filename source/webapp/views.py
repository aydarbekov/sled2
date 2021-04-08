import csv
from itertools import islice

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, render_to_response
from django.views import View
# import bulk_update_or_create
from django.views.generic import DetailView, ListView

from webapp.models import Firma, People, OpenBudget, Supliers, Tender


class IndexView(LoginRequiredMixin, ListView):
    model = Firma
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        firms = Firma.objects.count()
        print(firms)
        context['firms'] = Firma.objects.count()
        context['peoples'] = People.objects.count()
        context['budgets'] = OpenBudget.objects.count()
        context['tenders'] = Tender.objects.count()

        return context


class SearchView(LoginRequiredMixin, ListView):
    model = Firma
    template_name = 'search.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        search_str_1 = self.request.GET.get('search_str')
        if search_str_1:
            search_str = " ".join(search_str_1.split())
            if search_str:
                firma_objects = Firma.objects.filter((Q(full_name_ru__icontains=search_str) | Q(full_name_kg__icontains=search_str)
                                                      | Q(director__icontains=search_str) | Q(founders__icontains=search_str) |
                                                      Q(inn__icontains=search_str))).order_by('full_name_kg')

                print(firma_objects)
                paginator = Paginator(firma_objects, 5)
                page = self.request.GET.get('page', 1)
                # firma_objects = paginator.get_page(page)
                context['firmas'] = paginator.get_page(page)
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

        inn = firma.inn
        print(inn)
        inn_objects = []
        if inn is not None:
            inn_object = OpenBudget.objects.filter(Q(inn__icontains=inn))
            inn_objects.append(inn_object)
            print(inn_objects, 'INN')
            print(inn, 'BYYYYY')
        paginator = Paginator(inn_objects, 5)
        page = self.request.GET.get('page', 1)

        # org_name_ru = firma.full_name_kg
        # org_name_kg = firma.full_name_ru
        # org_short_kg = firma.short_name_ru
        # org_short_ru = firma.short_name_kg
        # print(org_short_ru, org_short_kg)
        # tender_objs = Tender.objects.filter(Q(org_name__icontains=org_short_kg) | Q(org_name__icontains=org_short_ru))
        # print(tender_objs, 'tenders')

        # supliers_objects = Supliers.objects.filter(Q(inn__icontains=inn))

        # context['supliers'] = supliers_objects
        # context['tenders'] = tender_objs
        context['budget'] = paginator.get_page(page)
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