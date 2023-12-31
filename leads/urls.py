from django.urls import path
from .views import (
    LeadListView, 
    LeadDetailView, 
    LeadCreateView, 
    LeadDeleteView, 
    LeadUpdateView,
    AssignAgentView,
    CategoryListView,
    CategoryDetailView,
    LeadCategoryUpdateView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView
)
#from .views import (lead_list, lead_detail, lead_create, lead_update,
#lead_delete, LeadListView, LeadDetailView, LeadCreateView, LeadDeleteView, 
#LeadUpdateView)

#from .views import lead_list

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='assign-agent'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('create-category/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('<int:pk>/category/', LeadCategoryUpdateView.as_view(), name='lead-category-update')
]