from django.urls import path

# from webapp.views import MinjustView, PeopleView
from webapp.views import SearchView, FirmaView, FirmaSecondView

app_name = 'webapp'

urlpatterns = [
    # path('minjust/', MinjustView.as_view(), name='min_create'),
    # path('people/', PeopleView.as_view(), name='people_create'),
    path('', SearchView.as_view(), name='search'),
    path('firma/<int:pk>/', FirmaView.as_view(), name='firma_detail'),
    path('firma_2/<int:pk>/', FirmaSecondView.as_view(), name='firma_detail_2'),
]
