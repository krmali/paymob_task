from django import template
from ..models import Message

register = template.Library()

@register.simple_tag
def pub_date_strftime(message):
    return message.pub_date.strftime("%d/%m/%Y %H:%M:%S")