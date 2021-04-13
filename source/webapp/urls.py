from django.urls import path

# from webapp.views import MinjustView, PeopleView
from webapp.views import SearchView, FirmaView, FirmaSecondView, IndexView, BudgetView

app_name = 'webapp'

urlpatterns = [
    # path('minjust/', MinjustView.as_view(), name='min_create'),
    # path('people/', PeopleView.as_view(), name='people_create'),
    path('', IndexView.as_view(), name='firma_main'),
    path('search/', SearchView.as_view(), name='search'),
    path('firma/<int:pk>/', FirmaView.as_view(), name='firma_detail'),
    path('firma/<int:pk>/budget/', BudgetView.as_view(), name='budget'),
    path('firma_2/<int:pk>/', FirmaSecondView.as_view(), name='firma_detail_2'),
]
