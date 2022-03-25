from django.http import HttpResponse
from django.shortcuts import redirect, render
from theapp.models import favorite, scripture, user

def indexPageView(request) :
    list = scripture.objects.all()
    person = request.session.get('person')

    if person > 0 :
        login = user.objects.get(user_id = person)

    fav_list = []
    fav_data = favorite.objects.all()
    for x in fav_data :
        if (person > 0) and (x.userid == login) :
            fav_list.append(x.scriptureid)

    context = {
        "scrips" : list,
        "value" : 1,
        "person" : person,
        "list" : fav_list
    }

    return render(request, 'theapp/index.html', context)

def encouragementPageView(request) :
    list = scripture.objects.all()
    list = list.filter(encouragement=True)
    person = request.session.get('person')

    if person > 0 :
        login = user.objects.get(user_id = person)

    fav_list = []
    fav_data = favorite.objects.all()
    for x in fav_data :
        if (person > 0) and (x.userid == login) :
            fav_list.append(x.scriptureid)

    context = {
        "scrips" : list,
        "value" : 2,
        "person" : person,
        "list" : fav_list
    }

    return render(request, 'theapp/index.html', context)

def testimonyPageView(request) :
    list = scripture.objects.all()
    list = list.filter(testimony=True)
    person = request.session.get('person')

    if person > 0 :
        login = user.objects.get(user_id = person)

    fav_list = []
    fav_data = favorite.objects.all()
    for x in fav_data :
        if (person > 0) and (x.userid == login) :
            fav_list.append(x.scriptureid)

    context = {
        "scrips" : list,
        "value" : 3,
        "person" : person,
        "list" : fav_list
    }

    return render(request, 'theapp/index.html', context)

def lowPageView(request) :
    list = scripture.objects.all()
    list = list.filter(low=True)
    person = request.session.get('person')

    if person > 0 :
        login = user.objects.get(user_id = person)

    fav_list = []
    fav_data = favorite.objects.all()
    for x in fav_data :
        if (person > 0) and (x.userid == login) :
            fav_list.append(x.scriptureid)

    context = {
        "scrips" : list,
        "value" : 4,
        "person" : person,
        "list" : fav_list
    }

    return render(request, 'theapp/index.html', context)

def favoritesPageView(request) :
    person = request.session.get('person')

    if person > 0 :
        login = user.objects.get(user_id = person)

    fav_list = []
    fav_data = favorite.objects.all()
    for x in fav_data :
        if (person > 0) and (x.userid == login) :
            fav_list.append(x.scriptureid)

    context = {
        "scrips" : fav_list,
        "value" : 5,
        "person" : person,
        "list" : fav_list
    }

    return render(request, 'theapp/index.html', context)

def markPageView(request, id) :
    person = request.session.get('person')
    scrip = scripture.objects.get(scripture_id = id)
    peeps = user.objects.get(user_id = person)

    new_fav = favorite()
    new_fav.scriptureid = scrip
    new_fav.userid = peeps
    new_fav.save()

    return redirect('../../fav/')

def unmarkPageView(request, id) :
    obj = favorite.objects.get(scriptureid = id)
    obj.delete()

    return redirect('../../')

def loginPageView(request) :
    person = request.session.get('person')

    context = {
            'person' : person
        }

    return render(request, 'theapp/login.html', context)

def loginUserPageView(request) :
    name = request.POST['name']
    password = request.POST['pass']

    dic = {}
    data = user.objects.all()
    for x in data :
        dic[x.username] = x.password

    if name in dic.keys() and password == dic[name] :
        person = user.objects.get(username = name)
        person = person.user_id
        request.session['person'] = person

        return redirect('../')
    else :
        return redirect('../login')

def logoutPageView(request) :
    request.session['person'] = 0
    return redirect('../')

def createUserPageView(request) :
    person = request.session.get('person')

    context = {
        'skip' : 0,
        'person' : person
    }

    return render(request, 'theapp/create.html', context)

def createTheUserPageView(request) :
    name = request.POST['name']
    password = request.POST['pass']
    skip = 0
    person = request.session.get('person')

    for x in user.objects.all() :
        if x.username == name :
            skip = 1

    if skip == 0:
        new_user = user()
        new_user.username = name
        new_user.password = password
        new_user.save()

        context = {
            'person' : person
        }

        return render(request, 'theapp/login.html', context)
    else :
        context = {
            'skip' : 1,
            'person' : person
        }
        return render(request, 'theapp/create.html', context)

def searchPageView(request) :
    list = scripture.objects.all()
    person = request.session.get('person')
    word = request.POST['word']

    if person > 0 :
        login = user.objects.get(user_id = person)

    fav_list = []
    fav_data = favorite.objects.all()
    for x in fav_data :
        if (person > 0) and (x.userid == login) :
            fav_list.append(x.scriptureid)

    list = list.filter(text__icontains = word)

    context = {
        "scrips" : list,
        "value" : 6,
        "person" : person,
        "list" : fav_list,
        "word" : word
    }

    return render(request, 'theapp/index.html', context)