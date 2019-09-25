from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from ..views.oj import SubmissionAPI, DebugSubmissionAPI, SubmissionListAPI, ContestSubmissionListAPI, SubmissionExistsAPI

urlpatterns = [
    url(r"^submission/?$", SubmissionAPI.as_view(), name="submission_api"),
    url(r"^debug_submission/?$", csrf_exempt(DebugSubmissionAPI.as_view()), name="debug_submission_api"),
    url(r"^submissions/?$", SubmissionListAPI.as_view(), name="submission_list_api"),
    url(r"^submission_exists/?$", SubmissionExistsAPI.as_view(), name="submission_exists"),
    url(r"^contest_submissions/?$", ContestSubmissionListAPI.as_view(), name="contest_submission_list_api"),
]
