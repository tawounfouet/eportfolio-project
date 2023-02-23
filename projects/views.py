from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,  redirect
from django.urls import reverse

from projects.models import  Project
from projects.forms import ProjectForm, ContactUsForm




def project_list(request):
    projects = Project.objects.all()
    return render(request,
                  'projects/project_list.html',
                  {'projects': projects})


def project_detail(request, id):
    project = Project.objects.get(id=id)
    return render(request,
                  'projects/project_detail.html',
                  {'project': project})



def project_create(request):
    if request.method == 'POST':
        form = projectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/')
    else:
        form = projectForm()

    return render(request,
                  'projects/project_create.html',
                  {'form': form})


def project_update(request, id):
    project = Project.objects.get(id=id)

    if request.method == 'POST':
        form = projectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(f'/projects/{id}/')
            return redirect('project-detail', project.id)
    else:
        form = projectForm(instance=project)

    return render(request,
                  'projects/project_update.html',
                  {'form': form})


def project_delete(request, id):
    project = Project.objects.get(id=id)

    if request.method == 'POST':
        project.delete()
        return HttpResponseRedirect(reverse('project-list'))

    return render(request,
                  'projects/project_delete.html',
                  {'project': project})


def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["nom"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
            )
        return redirect('/email-sent/') 
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
            'projects/contact.html',
            {'form': form})



def email_sent(request):
    return render(request, 'projects/email_sent.html')
