from django import template
from covidapp.models import Availability

register = template.Library()

@register.simple_tag
def get_table_class(value):
    if value:
        return 'bg-info text-light'
    return 'bg-primary text-light'



@register.simple_tag
def get_availabilities(hospital):
    return Availability.objects.filter(hospital=hospital).order_by('facility_id')


@register.simple_tag
def is_option_selected(selected_option, pk):
    if selected_option == str(pk):
        return 'selected'
    return ''


#@register.simple_tag
#def is_city_selected(selected_city_id, pk):
  #  if selected_city_id == str(pk):
  #      return 'selected'
  #  return ''