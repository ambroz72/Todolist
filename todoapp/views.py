from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . models import Task
from . form import TodoForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView

class TaskListView(ListView):
    model=Task
    template_name='home.html'
    context_object_name='task1'
    
class TaskDetailView(DetailView):
    model=Task
    template_name='details.html'
    context_object_name='task'
    
class TaskUpdateView(UpdateView):
    model=Task
    template_name='edit.html'
    fields=('name','priority','date')
    
def get_success_url(self):
    return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model=Task
    template_name='delete.html'
    success_url =reverse_lazy('cbvhome')


def add(request):
    task1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task', '')
        priority=request.POST.get('priority', '')
        date=request.POST.get('date', '')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})

def details(request):
    task=Task.objects.all()
    return render(request,'details.html',{'task':task})

def delete(request,taskid):
    task1=Task.objects.get(id=taskid)
    task1.delete()
    return redirect('add')

    # if request.method=='POST':
    #     task1.delete()
    #     return redirect('/')
    # return render(request,'details.html')
    
def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None ,instance=task)
    if f. is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'f':f,'task':task})

    
        