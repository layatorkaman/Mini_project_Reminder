from django import template
from django.utils.timesince import timeuntil
from todo.models import Task
from datetime import datetime

register = template.Library()


# @register.inclusion_tag('diff_time.html')
# def dif_time():
#     tasks = Task.objects.annotate()
#     tt = timeuntil(tasks.expire_date, datetime.now())
#     return {'tt': tt}
# # return {'tasks':tasks}
@register.simple_tag
def dif_time(expire_date):

    return timeuntil(expire_date,)