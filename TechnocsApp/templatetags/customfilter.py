from django import template

register = template.Library()


@register.filter('split')
def split(features, separator):
    ''' Split strings into list '''
    flist = list(features.split(separator))
    return flist

@register.filter('modulus')
def modulus(number):
    ''' return modulus % '''
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
