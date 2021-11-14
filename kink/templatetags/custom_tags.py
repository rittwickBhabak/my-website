from django import template

register = template.Library()

@register.filter()
def format_time(time):
    time = int(time)
    minute = time/60
    minute = int(minute)
    second = time%60
    return f"{minute}:{second}"

@register.filter()
def order_bkmrks(querySet):
    return querySet.order_by('-time')

@register.filter()
def order_bkmrks_rev(querySet):
    return querySet.order_by('time')