import io
from datetime import datetime
from xlsxwriter.workbook import Workbook
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.utils import timezone
from django.utils.encoding import escape_uri_path
from accounts.models import Department
from ideas.models import Idea
from ideas.views_utils import get_ideas
from common.views_utils import json_response
from common.debug_utils import debug


@login_required(login_url='/accounts/login')
def ajax_list_view(request):
    idea_list = get_ideas(request)
    paginator = Paginator(idea_list, 10)

    page = request.GET.get('page', 1)
    ideas = paginator.get_page(page)
    return json_response({'ideas': ideas})


@login_required(login_url='/accounts/login')
def list_view(request):
    idea_list = get_ideas(request)
    paginator = Paginator(idea_list, 10)

    page = request.GET.get('page', 1)
    ideas = paginator.get_page(page)

    departments = Department.objects.all()

    return render(
        request,
        'ideas/list.html',
        {
            'ideas': ideas,
            'departments': departments,
            'statuses': Idea.STATUSES
        })


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


@login_required(login_url='/accounts/login')
def edit_view(request):
    idea_id = request.POST.get('id', '')
    idea = Idea.objects.get(id=idea_id, user=request.user)
    title = request.POST.get('title', '')
    description = request.POST.get('description', '')
    idea.title = title
    idea.description = description
    idea.save()
    return json_response({'is_success': True})


@login_required(login_url='/accounts/login')
def export_view(request):
    ideas = get_ideas(request)

    output = io.BytesIO()

    workbook = Workbook(output)

    workbook.add_format({'text_wrap': True})

    worksheet = workbook.add_worksheet()

    worksheet.write(0, 0, '主题')
    worksheet.write(0, 1, '描述')
    worksheet.write(0, 2, '部门')
    worksheet.write(0, 3, '提议者')
    worksheet.write(0, 4, '时间')

    row = 1
    for idea in ideas:
        worksheet.write(row, 0, idea.title)
        worksheet.write(row, 1, idea.description)
        worksheet.write(row, 2, idea.user.department.name)
        worksheet.write(row, 3, idea.user.name)
        worksheet.write(
            row, 4, idea.created_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        row += 1

    workbook.close()

    output.seek(0)

    filename = '金点子'

    start_timestamp = request.GET.get('start', '')
    if start_timestamp:
        start_date = datetime.fromtimestamp(int(start_timestamp) / 1000)
        filename += start_date.strftime("%Y%m%d")

    end_timestamp = request.GET.get('end', '')
    if end_timestamp:
        end_date = datetime.fromtimestamp(int(end_timestamp) / 1000)
        filename += '-' + end_date.strftime("%Y%m%d")

    debug(filename)

    response = HttpResponse(
        output.read(),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        charset='utf-8')
    response['Content-Disposition'] = "attachment; filename=%s.xlsx" % escape_uri_path(filename)

    output.close()

    return response


@login_required(login_url='/accounts/login')
def accept_view(request, idea_id):
    response = {}
    user = request.user
    if not user.can_accept:
        debug(user, 'limited permission')
        response['error_message'] = '没有权限采纳建议！'
    elif not Idea.objects.filter(id=idea_id).exists():
        response['error_message'] = '此建议不存在！'
    elif Idea.objects.filter(id=idea_id, status=1).exists():
        response['error_message'] = '此建议已被采纳，请刷新界面！'
    else:
        idea = Idea.objects.get(id=idea_id)
        idea.status = 1
        idea.acceptor = user
        idea.accept_datetime = timezone.now()
        idea.save()
        response['is_success'] = True

    return json_response(response)
