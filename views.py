from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    path(route='', view=views.CourseListView.as_view(), name='index'),
    path(route='signup/', view=views.registration_request, name='signup'),
    path(route='signin/', view=views.login_request, name='signin'),
    path(route='logout/', view=views.logout_request, name='logout'),
    path(route='<int:pk>/enroll/', view=views.enroll, name='enroll'),
    path(route='<int:pk>/course_details/', view=views.CourseDetailView.as_view(), name='course_details'),
    path(route='<int:course_id>/exam_submission/', view=views.submit, name='exam_submission'),
    path(route='<int:course_id>/submission_result/<int:submission_id>/', view=views.show_exam_result, name='exam_result'),
]
