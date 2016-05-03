from django import template

register = template.Library()


@register.filter
def first_paymet(obj):
    pyaments = obj.payment_set.all().order_by('date')
    return pyaments[0].amount


@register.filter
def first_paymet_date(obj):
    pyaments = obj.payment_set.all().order_by('date')
    return pyaments[0].date
