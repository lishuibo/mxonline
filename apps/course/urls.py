from django.urls import re_path, path
from course.views import CourseDetailView, CourseInfoView, CommentsView, AddCommentsView, CourseListView, VideoPlayView

__author__ = 'litl'

app_name = "course"

urlpatterns = [
    re_path('detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),
    re_path('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name="course_info"),
    re_path('comment/(?P<course_id>\d+)/', CommentsView.as_view(), name="course_comments"),
    path('add_comment/', AddCommentsView.as_view(), name="add_comment"),
    path('list/', CourseListView.as_view(), name="course_list"),
    re_path('video/(?P<course_id>\d+)/', VideoPlayView.as_view(), name="video_play"),
]
