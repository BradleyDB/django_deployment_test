from django import template


register = template.Library()

#using the decorator here means that super_cuts becomes an argument of register.filter()
#and the name parameter is the name parameter from register.filter()
@register.filter(name='super_cuts')
def super_cuts(value,arg):
    """
    This cuts out all values of 'arg' from the string
    """

    return value.replace(arg,"")

#name you want to call the function, then the function itself
#register.filter('super_cuts',super_cuts)
