from datetime import datetime
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from accounts.models import Department
from ideas.models import Idea
from common.views_utils import json_response
from common.debug_utils import debug


@login_required(login_url='/accounts/login')
def list_view(request):
    debug(request.GET)
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

    paginator = Paginator(idea_list, 10)

    page = request.GET.get('page', 1)
    ideas = paginator.get_page(page)

    departments = Department.objects.all()

    return render(
        request,
        'ideas/list.html',
        {'ideas': ideas, 'departments': departments})


@login_required(login_url='/accounts/login')
def detail_view(request, idea_id):
    return render(request, 'ideas/detail.html')


@login_required(login_url='/accounts/login')
def create_view(request):
    idea = Idea()
    title = request.POST.get('title', '')
    description = request.POST.get('description', '')
    idea.title = title
    idea.description = description
    idea.user = request.user
    idea.save()
    return json_response({'is_success': True})
