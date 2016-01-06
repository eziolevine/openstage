# Create your views here.
from .models import Inerview

from publisher.views import PublisherDetailView, PublisherListView


class InterviewListView(PublisherListView):
    model = Inerview
    context_object_name = 'interviewes'
    template_name = 'pages/home.html'


class InterviewView(PublisherDetailView):
    model = Inerview
    context_object_name = 'interview'
    template_name = 'pages/interview_detail.html'
