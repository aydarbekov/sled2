import csv
from itertools import islice

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, render_to_response
from django.views import View
# import bulk_update_or_create
from django.views.generic import DetailView, ListView, TemplateView

from webapp.models import Firma, People, OpenBudget, Supliers, Tender, WinnerDetailed, Tizme, Farm, Bankrupt, \
    TenderBlackList, Gkpen, TenderBuyers, SupplierDetailed

PAGE_NUM_ITEMS = 10


class IndexView(ListView):
    model = Firma
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     firms = Firma.objects.count()
    #     print(firms)
    #     context['firms'] = Firma.objects.count()
    #     context['peoples'] = People.objects.count()
    #     context['budgets'] = OpenBudget.objects.count()
    #     context['supliers'] = Supliers.objects.count()
    #
    #     return context


# class SearchView(ListView):
#     model = Firma
#     template_name = 'search.html'

# def get_context_data(self, *, object_list=None, **kwargs):
#     context = super().get_context_data(object_list=object_list, **kwargs)
#     search_str_1 = self.request.GET.get('search_str')
#     if search_str_1:
#         search_str = " ".join(search_str_1.split())
#         if search_str:
#             firma_objects = Firma.objects.filter((Q(full_name_ru__icontains=search_str) | Q(full_name_kg__icontains=search_str)
#                                                   | Q(director__icontains=search_str) | Q(founders__icontains=search_str) |
#                                                   Q(inn__icontains=search_str))).order_by('full_name_kg')
#
#             # print(firma_objects)
#             paginator = Paginator(firma_objects, 5)
#             page = self.request.GET.get('page', 1)
#             # firma_objects = paginator.get_page(page)
#             context['firmas'] = paginator.get_page(page)
#             context['search_str'] = search_str
#
#         return context


class SearchView(ListView):
    template_name = "search.html"
    # paginate_by = 10
    context_object_name = "firmas"

    def get_queryset(self, *args, **kwargs):
        page = int(self.request.GET.get("page", 1))
        offset = (page - 1) * 10

        search_str_1 = self.request.GET.get("search_str")
        if search_str_1:
            search_str = " ".join(search_str_1.split())
            num_items = offset + PAGE_NUM_ITEMS
            if search_str:
                firma_objects = Firma.objects.filter(
                    (
                            Q(full_name_ru__icontains=search_str)
                            | Q(full_name_kg__icontains=search_str)
                            | Q(director__icontains=search_str)
                            | Q(founders__icontains=search_str)
                            | Q(inn__icontains=search_str)
                    )
                ).order_by("full_name_kg")[offset:num_items]
                return firma_objects

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        search_str = self.request.GET.get("search_str")
        person = search_str.upper().split()
        director_objects = []
        tizme_objects = []
        # print(person)
        page = int(self.request.GET.get("page_fiz", 1))
        offset = (page - 1) * PAGE_NUM_ITEMS
        page2 = int(self.request.GET.get("page_fiz_tizme", 1))
        offset2 = (page2 - 1) * PAGE_NUM_ITEMS
        num_items = offset + PAGE_NUM_ITEMS
        num_items2 = offset2 + PAGE_NUM_ITEMS
        if len(person) == 3:
            director_objects = People.objects.filter(
                (
                        Q(last_name__icontains=person[0])
                        & Q(first_name__icontains=person[1])
                        & Q(middle_name__icontains=person[2])
                )
            ).order_by("last_name", "first_name", "last_name")[offset:num_items]
            tizme_objects = Tizme.objects.filter(
                (
                        Q(last_name__icontains=person[0])
                        & Q(first_name__icontains=person[1])
                        & Q(middle_name__icontains=person[2])
                )
            ).order_by("last_name", "first_name", "last_name")[offset2:num_items2]
            # print(director_objects)
        if len(person) == 2:
            director_objects = People.objects.filter(
                (Q(last_name__icontains=person[0]) & Q(first_name__icontains=person[1]))
            ).order_by("last_name", "first_name", "last_name")[offset:num_items]
            tizme_objects = Tizme.objects.filter(
                (Q(last_name__icontains=person[0]) & Q(first_name__icontains=person[1]))
            ).order_by("last_name", "first_name", "last_name")[offset2:num_items2]
        if len(person) == 1:
            director_objects = People.objects.filter(
                (
                        Q(last_name__icontains=person[0])
                        | Q(first_name__icontains=person[0])
                        | Q(middle_name__icontains=person[0])
                )
            ).order_by("last_name", "first_name", "last_name")[offset:num_items]
            tizme_objects = Tizme.objects.filter(
                (
                        Q(last_name__icontains=person[0])
                        | Q(first_name__icontains=person[0])
                        | Q(middle_name__icontains=person[0])
                )
            ).order_by("last_name", "first_name", "last_name")[offset2:num_items2]
        context["tizmes"] = director_objects
        context["tizmes_2"] = tizme_objects
        context["search_str"] = self.request.GET.get("search_str")
        context["page_actual"] = int(self.request.GET.get("page", 1))
        context["page_actual_sti"] = int(self.request.GET.get("page_fiz", 1))
        context["page_actual_tizme"] = int(self.request.GET.get("page_fiz_tizme", 1))
        return context



# class FirmaView(ListView):
#     model = Firma
#     template_name = 'detail.html'
#     paginate_by = 5
#     paginate_orphans = 0
#
#     def get(self, request, *args, **kwargs):
#         firma_inn = []
#         context = {}
#         firma = Firma.objects.get(pk=kwargs['pk'])
#         firma_inn.append(firma)
#         director = firma.director.upper().split()
#         if len(director) == 3:
#             director_objects = People.objects.filter((Q(last_name__icontains=director[0]) & Q(first_name__icontains=director[1]) & Q(middle_name__icontains=director[2])))
#         else:
#             director_objects = People.objects.filter((Q(last_name__icontains=director[0]) & Q(
#                 first_name__icontains=director[1])))
#         firma_inn.append(director_objects)
#         # print(director_objects,'dfgfdg')
#         # for obj in director_objects:
#         #     print(obj.first_name)
#
#         inn = firma.inn
#         # print(inn)
#         supliers_objects = Supliers.objects.filter(Q(inn__icontains=inn))
#
#         context['supliers'] = supliers_objects
#         # context['budget'] = inn_object
#         context['firma'] = firma_inn
#         # print(context['firma'])
#
#         return render(request=request, template_name=self.template_name, context=context)


class FirmaView(TemplateView):
    template_name = "detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        firma = Firma.objects.get(pk=kwargs["pk"])
        founders = []
        if firma:
            founders_all = firma.founders
            founders_striped = founders_all.strip(" []")
            founders_splitted = founders_striped.split(",")
            for founder in founders_splitted:
                if "Замените на физическое лицо" not in founder:
                    founders.append(founder.strip(" ',"))

        inn = firma.inn
        supliers_objects = []
        buyers_objects = []
        director_objects = []
        gkpen_objects = []
        founders_director = []
        tizme_objects_all = []
        black_list_ojects = []
        bankrupts = []
        farms = []
        if inn:
            supliers_objects = Supliers.objects.filter(Q(inn__icontains=inn))
            buyers_objects = TenderBuyers.objects.filter(Q(inn__icontains=inn))
            gkpen_objects = Gkpen.objects.filter(Q(inn_okpo__icontains=inn))
            black_list_ojects = TenderBlackList.objects.filter(Q(inn__icontains=inn))
            bankrupts = Bankrupt.objects.filter(Q(tin__icontains=inn))
            farms = Farm.objects.filter(Q(inn__icontains=inn))
        director = firma.director
        founders_director.append(director)
        for founder in founders:
            founders_director.append(founder)

        for person in founders_director:
            person = person.upper().split()
            if len(person) == 3:
                nalog_objects = People.objects.filter(
                    (
                            Q(last_name__icontains=person[0])
                            & Q(first_name__icontains=person[1])
                            & Q(middle_name__icontains=person[2])
                    )
                )

                tizme_objects = Tizme.objects.filter(
                    (
                            Q(last_name__icontains=person[0])
                            & Q(first_name__icontains=person[1])
                            & Q(middle_name__icontains=person[2])
                    )
                )
                for query in nalog_objects:
                    if query not in director_objects:
                        director_objects.append(query)
                for query in tizme_objects:
                    if query not in tizme_objects_all:
                        tizme_objects_all.append(query)
            if len(person) == 2:
                nalog_objects = People.objects.filter(
                    (
                            Q(last_name__icontains=person[0])
                            & Q(first_name__icontains=person[1])
                    )
                )
                tizme_objects = Tizme.objects.filter(
                    (
                            Q(last_name__icontains=person[0])
                            & Q(first_name__icontains=person[1])
                    )
                )
                for query in nalog_objects:
                    if query not in director_objects:
                        director_objects.append(query)
                for query in tizme_objects:
                    if query not in tizme_objects_all:
                        tizme_objects_all.append(query)
            if len(director) == 1:
                nalog_objects = People.objects.filter(
                    (
                            Q(last_name__icontains=director[0])
                            | Q(first_name__icontains=director[0])
                            | Q(middle_name__icontains=director[0])
                    )
                )
                tizme_objects = Tizme.objects.filter(
                    (
                            Q(last_name__icontains=director[0])
                            | Q(first_name__icontains=director[0])
                            | Q(middle_name__icontains=director[0])
                    )
                )
                for query in nalog_objects:
                    if query not in director_objects:
                        director_objects.append(query)
                for query in tizme_objects:
                    if query not in tizme_objects_all:
                        tizme_objects_all.append(query)

        # print(director_objects)
        # print(tizme_objects_all)

        context["black_lists"] = black_list_ojects
        context["search_str"] = self.request.GET.get("search_str")
        context["supliers"] = supliers_objects
        context["buyers"] = buyers_objects
        context["tizmes"] = director_objects
        context["tizmes_2"] = tizme_objects_all
        context["firma"] = firma
        context["founders"] = founders
        context["gkpens"] = gkpen_objects
        context["bankrupts"] = bankrupts
        context["farms"] = farms

        return context

#
# class BudgetView(ListView):
#     template_name = 'open_budget.html'
#     model = Firma
#
#     def get(self, request, *args, **kwargs):
#         firma_inn = []
#         context = {}
#         firma = Firma.objects.get(pk=kwargs['pk'])
#         # print(firma, 'ddddd')
#
#         inn = firma.inn
#         # print(inn)
#         # inn_objects = []
#         # if inn is not None:
#         inn_object = OpenBudget.objects.filter(Q(inn__icontains=inn))
#         # inn_objects.append(inn_object)
#         print(inn_object, 'INN')
#         budget_objects = []
#         for bs in inn_object:
#             # for b in bs:
#                 # print(b)
#             budget_objects.append(bs)
#         # print(inn, 'BYYYYY')
#         paginator = Paginator(budget_objects, 10)
#         page = self.request.GET.get('page', 1)
#
#         context['budget'] = paginator.get_page(page)
#         context['firma'] = firma
#
#         return render(request=request, template_name=self.template_name, context=context)


class BudgetView(LoginRequiredMixin, ListView):
    template_name = "open_budget.html"
    model = Firma

    def get(self, request, *args, **kwargs):
        context = {}
        firma = Firma.objects.get(pk=kwargs["pk"])
        # print(firma, 'ddddd')

        inn = firma.inn
        # print(inn)
        # inn_objects = []
        # if inn is not None:
        inn_object = OpenBudget.objects.filter(Q(inn__icontains=inn))
        # inn_objects.append(inn_object)
        print(inn_object, "INN")
        budget_objects = []
        for bs in inn_object:
            # for b in bs:
            # print(b)
            budget_objects.append(bs)
        # print(inn, 'BYYYYY')
        paginator = Paginator(budget_objects, 10)
        page = self.request.GET.get("page", 1)

        context["budget"] = paginator.get_page(page)
        context["firma"] = firma

        return render(
            request=request, template_name=self.template_name, context=context
        )


class TenderView(LoginRequiredMixin, ListView):
    template_name = "tender_winners.html"
    context_object_name = "tenders"
    paginate_by = 50

    def get_queryset(self, *args, **kwargs):
        winned_tenders = WinnerDetailed.objects.filter(
            Q(winner_name__icontains=self.kwargs["firm_name"])
            & Q(winner_place__icontains="Подтверждено")
        )
        return winned_tenders

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        firma = Firma.objects.get(pk=self.kwargs["pk"])
        context["firma"] = firma
        return context


class SupplieredView(LoginRequiredMixin, ListView):
    template_name = "tender_suppliered.html"
    context_object_name = "tenders"
    paginate_by = 50

    def get_queryset(self, *args, **kwargs):
        suppliered_tenders = SupplierDetailed.objects.filter(
            Q(supplier_name__icontains=self.kwargs["firm_name"])
        )
        return suppliered_tenders

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        firma = Firma.objects.get(pk=self.kwargs["pk"])
        context["firma"] = firma
        return context



# class FirmaSecondView(ListView):
#     template_name = 'detail_2.html'
#     model = Firma
#     paginate_by = 5
#     paginate_orphans = 2
#
#     def get(self, request, *args, **kwargs):
#         context = {}
#         firma = Firma.objects.get(pk=kwargs['pk'])
#
#         f = []
#         # print(firma.founders)
#         old_founders = firma.founders.strip('[]').split(',')
#         # print(old_founders,'foundres')
#         founders = []
#         for founder in old_founders:
#             fo = founder.strip("' ")
#             # print(founder, 'цикл')
#             founders.append(fo)
#         # print(founders,'за циклом')
#         founders = founders
#         # print(len(founders))
#         if founders.__contains__('Замените на физическое лицо 1'):
#             pass
#         else:
#             if founders[0] != '':
#                 for founder in founders:
#                     firma_objects_2 = Firma.objects.filter(Q(founders__icontains=founder) | Q(director__icontains=founder))
#                     fff = {
#                         'name': founder,
#                         'firmas': firma_objects_2
#                     }
#                     f.append(fff)
#
#             else:
#                 pass
#             print('none')
#
#         # print(f)
#         # print(len(firma.director))
#         # print(firma.director ,'1111111')
#         context['fir'] = firma.director
#         if len(firma.director) != '':
#             director_objects_2 = Firma.objects.filter(Q(founders__icontains=firma.director) | Q(director__icontains=firma.director))
#             context['firmas_3'] = director_objects_2
#         # print(firma.address_street)
#         if firma.address_street != None and firma.address_street != '':
#             if '.' in firma.address_street:
#                 street = firma.address_street.split('.')[1]
#             else:
#                 street = firma.address_street
#             addresses = Firma.objects.filter(Q(address_street__icontains=street) & Q(house_number__icontains=firma.house_number))
#             # print(addresses)
#             context['addresses'] = addresses
#         else:
#             pass
#         context['firmas_2'] = f
#         print(firma.phone, 'dfgfddfggit ')
#
#         firma_inn = []
#         firma_inn.append(firma)
#         print(firma, 'ddddd')
#
#         print(len(firma.director.upper().split()))
#         director = firma.director.upper().split()
#         print(director[0])
#         print(director[1])
#         if len(director) == 3:
#             director_objects = People.objects.filter((Q(last_name__icontains=director[0]) & Q(
#                 first_name__icontains=director[1]) & Q(middle_name__icontains=director[2])))
#         else:
#             director_objects = People.objects.filter((Q(last_name__icontains=director[0]) & Q(
#                 first_name__icontains=director[1])))
#         firma_inn.append(director_objects)
#         print(director_objects, 'dfgfdg')
#         for obj in director_objects:
#             print(obj.first_name)
#
#         context['firma'] = firma_inn
#         print(context['firma'], 2222222)
#
#         return render(request=request, template_name=self.template_name, context=context)

class FirmaSecondView(ListView):
    template_name = "detail_2.html"
    model = Firma
    paginate_by = 5
    paginate_orphans = 2

    def get(self, request, *args, **kwargs):
        context = {}
        firma = Firma.objects.get(pk=kwargs["pk"])
        f = []
        old_founders = firma.founders.strip("[]").split(",")
        founders = []
        for founder in old_founders:
            fo = founder.strip("' ")
            founders.append(fo)
        # founders = founders
        if "Замените на физическое лицо 1" in founders:
            pass
        else:
            if founders[0] != "":
                for founder in founders:
                    firma_objects_2 = Firma.objects.filter(
                        Q(founders__icontains=founder) | Q(director__icontains=founder)
                    )
                    fff = {"name": founder, "firmas": firma_objects_2}
                    f.append(fff)
            else:
                pass
        context["fir"] = firma.director
        if len(firma.director) != "":
            director_objects_2 = Firma.objects.filter(
                Q(founders__icontains=firma.director)
                | Q(director__icontains=firma.director)
            )
            context["firmas_3"] = director_objects_2
        if firma.address_street is not None and firma.address_street != "":
            if "." in firma.address_street:
                street = firma.address_street.split(".")[1]
            else:
                street = firma.address_street
            addresses = Firma.objects.filter(
                Q(address_street__icontains=street)
                & Q(house_number__icontains=firma.house_number)
            )
            context["addresses"] = addresses
        else:
            pass
        context["firmas_2"] = f

        firma_inn = [firma]
        director = firma.director.upper().split()
        if len(director) == 3:
            director_objects = People.objects.filter(
                (
                    Q(last_name__icontains=director[0])
                    & Q(first_name__icontains=director[1])
                    & Q(middle_name__icontains=director[2])
                )
            )
        else:
            director_objects = People.objects.filter(
                (
                    Q(last_name__icontains=director[0])
                    & Q(first_name__icontains=director[1])
                )
            )
        firma_inn.append(director_objects)

        context["firma"] = firma_inn

        return render(
            request=request, template_name=self.template_name, context=context
        )


class AboutView(TemplateView):
    template_name = "about.html"