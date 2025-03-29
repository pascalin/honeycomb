from pyramid.view import view_config

from ..models import *


@view_config(context=BeeHive, renderer='honeycomb:templates/beehive.jinja2')
def beehive(request):
    if hasattr(request.context, 'title'):
        beehive_title = request.context.title
    else:
        beehive_title = "Wild beehive"
    honeycombs = [(request.context[honeycomb], request.resource_url(request.context, honeycomb)) for honeycomb in request.context]
    return {'project': 'Honeycomb', 'title': beehive_title, 'honeycombs': honeycombs}


@view_config(context=Honeycomb, renderer='honeycomb:templates/honeycomb.jinja2')
def honeycomb(request):
    if hasattr(request.context, 'title'):
        honeycomb_title = request.context.title
    else:
        honeycomb_title = "Wild honeycomb"
    cells = [(request.context[cell], request.resource_url(request.context, cell)) for cell in request.context]
    return {'project': 'Honeycomb', 'title': honeycomb_title, 'cells': cells}

@view_config(context=CellText, renderer='honeycomb:templates/cell.jinja2')
def textcell(request):
    if hasattr(request.context, 'title'):
        cell_title = request.context.title
    else:
        cell_title = "Wild cell"
    return {'project': 'Honeycomb', 'title': cell_title, 'contents': request.context.contents}
