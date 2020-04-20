from django.urls import path
from . import views
from .views import CompetitionDetailView,QuestionDetailView
urlpatterns = [
    path('', views.home ,name='home'),
    path('contests/',views.contests,name='contests'),
    path('contests/<int:pk>', CompetitionDetailView.as_view(), name='indivcontest'),
    path(r'^contests/problem/<int:param1>/<int:param2>$',views.questionDetail,name='question-detail'),
    path('contests/register/<int:param1>',views.register,name='register'),
    path('ratings/',views.ratings,name='ratings'),
]


