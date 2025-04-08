from pyramid.view import view_config
from pyramid.httpexceptions import HTTPSeeOther
from pyramid_storage.exceptions import FileNotAllowed
from pyramid_storage import extensions

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
    if hasattr(request.context, 'map'):
        map = request.context.map
    else:
        map = None
    cells = [(request.context[cell], request.resource_url(request.context, cell)) for cell in request.context]
    return {'project': 'Honeycomb', 'title': honeycomb_title, 'map': map, 'cells': cells}


@view_config(context=Honeycomb, request_method='POST')
def honeycomb_update(request):
    filename = None
    try:
        filename = request.storage.save(request.POST['honeycomb_map'], folder="maps", randomize=True, extensions=extensions.DATA+extensions.IMAGES)
    except FileNotAllowed:
        request.session.flash('Sorry, this file is not allowed')
    if filename:
        prev_filename = request.context.map and request.context.map.filename
        request.context.set_map(HoneyStaticMap(request.storage.url(filename)))
        if prev_filename:
            request.storage.delete(prev_filename)
    return HTTPSeeOther(request.resource_url(request.context))


@view_config(context=CellText, renderer='honeycomb:templates/cell.jinja2')
def textcell(request):
    if hasattr(request.context, 'title'):
        cell_title = request.context.title
    else:
        cell_title = "Wild cell"
    return {'project': 'Honeycomb', 'title': cell_title, 'contents': request.context.contents}
