from django import template

register = template.Library()
@register.filter('reportkey')
def reportkey(dict_data, key):
    if key in dict_data:
        return dict_data.get(key)

@register.filter(name='ranges')
def ranges(number):
    return range(len(number))

@register.filter
def get_list_item(lst, i):
    return lst[i]