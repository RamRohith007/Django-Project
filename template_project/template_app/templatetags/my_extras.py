from django import template

register = template.Library()

@register.filter(name='cut')
def funcut(value,arg):
    #this cuts out all the vaues of arg from the string!
    return value.replace(arg,'')

# register.filter('cut',funcut)

















