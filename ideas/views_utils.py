from accounts.models import Department
from datetime import datetime
from django.db.models import Q
from ideas.models import Idea


def get_ideas(request):
    keywords = request.GET.get('keywords', '')
    department_id = request.GET.get('department', '')
    start_timestamp = request.GET.get('start', '')
    end_timestamp = request.GET.get('end', '')

    idea_list = Idea.objects.all()
    if keywords:
        idea_list = idea_list.filter(
            Q(title__icontains=keywords) | Q(description__icontains=keywords))

    if department_id:
        department = Department.objects.get(id=department_id)
        idea_list = idea_list.filter(user__department=department)

    if start_timestamp:
        start_date = datetime.fromtimestamp(int(start_timestamp) / 1000)
        idea_list = idea_list.filter(created_datetime__gte=start_date)

    if end_timestamp:
        end_date = datetime.fromtimestamp(int(end_timestamp) / 1000)
        idea_list = idea_list.filter(created_datetime__lte=end_date)

    return idea_list
