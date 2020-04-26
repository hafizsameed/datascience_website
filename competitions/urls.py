from django.urls import path
from . import views
from .views import QuestionDetailView
urlpatterns = [
    path('', views.home ,name='home'),
    path('contests/',views.contests,name='contests'),
    path('contests/<int:param1>', views.competitionDetailView, name='indivcontest'),
    path('contests/problem/<int:param1>/<int:param2>',views.questionDetail,name='question-detail'),
    path('contests/<int:param1>/mysubmissions',views.mysubmissions,name='my-submissions'),
    path('contests/register/<int:param1>',views.register,name='register'),
    path('ratings/',views.ratings,name='ratings'),

]


