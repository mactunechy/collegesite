from django.urls import path
from . import views

app_name = 'tutorials'

urlpatterns = [
	path('new', views.TutorialCreateView.as_view(),name='tutorial_create'),
	path('update/<slug:username>/<slug:slug>',views.TutorialUpdateView.as_view(),name='tutorial_update'),
	path('delete/<slug:username>/<slug:slug>',views.TutorialDeleteView.as_view(),name='tutorial_delete'),
	path('delete/<slug:username>/<slug:slug>',views.TutorialDetailView.as_view(),name='tutorial_detail'),
	path('<slug:',views.TutorialListView.as_view(),name='tutorial_list'),




]