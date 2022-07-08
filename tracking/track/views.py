from django.shortcuts import render, redirect
from .models import Track
from .forms import TrackForm, UpdateTrackForm
from django.contrib import messages
# Create your views here.

def home(request):
    if 'submit' in request.POST:
        track = request.POST.get('track')
        getid = Track.objects.get(track_no=track).id
        return redirect('track',getid)
    return render(request, 'track/index.html')

def about(request):
    return render(request,'track/about.html')

def service(request):
    return render(request,'track/service.html')

def price(request):
    return render(request,'track/price.html')

def contact(request):
    return render(request,'track/contact.html')



def track(request,pk):
    track = Track.objects.filter(id = pk)
    context = {
        'track':track,
    }
    return render(request,'track/track.html',context)

def filler(request):
    form = TrackForm()
    if 'submit' in request.POST:
        form = TrackForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request,f'Added successful')
            return redirect('filler')

    if 'modify' in request.POST:
        track = request.POST.get('track')
        getid = Track.objects.get(track_no=track).id
        return redirect('modify',getid)
    context = {'form':form}
    return render(request,'track/form.html',context)

def modifytrack(request, pk):
    track = Track.objects.get(id=pk)
    gettrack = Track.objects.get(id=pk).id
    form = UpdateTrackForm(instance=track)
    if request.method == 'POST':
        form = UpdateTrackForm(request.POST, instance=track)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successful')
            return redirect('modify',gettrack)
    context = {'form':form}
    return render(request, 'track/modify.html', context)