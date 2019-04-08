#views for the 'kids' django app

from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, _get_queryset
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Kids, Events

# Create your views here.
def index(request):
    return render(request, 'kids/kids-index.html')

def add(request, kid):
    if request.method == 'POST':
        this_kid = get_object_or_404(Kids, pk=kid)

        new_event = Events()
        new_event.eventsKidID = this_kid
        new_event.eventsDate = timezone.now()
        new_event.eventsTime = timezone.localtime(timezone.now())
        new_event.eventsGenNote = request.POST['gen_note']
        new_event.eventsExtendedNote = request.POST['ext_note']

        new_event.save(force_insert=True)

        return HttpResponseRedirect('/kids')
    else:
        current_kid = get_object_or_404(Kids, pk=kid)
        context = {'kidpk': kid, 'current_kid': current_kid}
        return render(request, 'kids/kids-add-event.html', context)

def detail(request, kid):
    pick_kid = get_object_or_404(Kids, pk=kid)
    kid_events = Events.objects.filter(eventsKidID=pick_kid).order_by('-eventsDate', '-eventsTime')
    context = {'kpk': kid, 'pick_kid': pick_kid, 'kid_events': kid_events}
    return render(request, 'kids/kids-detail.html', context)

def edit(request, event):
    if request.method == 'POST':
        working_event = get_object_or_404(Events, pk=event)

        update_event = Events()

        update_event.eventsID = working_event.eventsID
        update_event.eventsDate = working_event.eventsDate
        update_event.eventsTime = working_event.eventsTime
        update_event.eventsKidID = working_event.eventsKidID
        update_event.eventsGenNote = request.POST['edit_gen_note']
        update_event.eventsExtendedNote = request.POST['edit_ext_note']

        update_event.save(force_update=True)

        return HttpResponseRedirect('/kids')
    else:
        get_event = get_object_or_404(Events, pk=event)
        context = {'get_event': get_event}
        return render(request, 'kids/kids-edit.html', context)


#moving away from class-based views for the moment
#class IndexView(generic.TemplateView):
#    template_name='kids/index.html'