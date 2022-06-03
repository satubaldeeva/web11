from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views import View
import json
from django.contrib import auth
from .forms import AccountForm
from .forms import CreateUserForm
from .models import Recipes
from .models import Account
from .telegram import send_message
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    recipe = Recipes.objects.all()[:2]
    data = {
        'recipe': recipe,
    }
    return render(request, 'main/index.html', data)


def contact(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)

        if form.is_valid():
            form.save()
            forms = Account.objects.last()
            message = "*ЗАЯВКА С САЙТА*:" + "\n" + str({forms})
            send_message(message)
            return redirect('main:contact')
        else:
            """return HttpResponse("Your account is disabled")"""

    form = AccountForm()
    data = {
        'form': form,
    }

    return render(request, 'main/contact.html', data)


def about(request):
    return render(request, 'main/about.html')


def recipes(request):
    recipe = Recipes.objects.all()
    data = {
        'recipe': recipe,
    }
    print(recipes)
    return render(request, 'main/recipes.html', data)


def post_detail(request, slug):
    post = Recipes.objects.get(slug=slug)

    is_favourite = False
    if post.favourite.filter(id=request.user.id).exists():
        is_favourite = True
    context = {
        'post': post,
        'is_favourite': is_favourite
    }

    return render(request, 'main/single.html', context)


class FavouriteView(View):
    # This variable will set the bookmark model to be processed
    model = None
    print("FavouriteView")
    def post(self, request, pk):
        # We need a user
        user = auth.get_user(request)
        # Trying to get a bookmark from the table, or create a new one
        bookmark, created = self.model.objects.get_or_create(user=user, obj_id=pk)
        print()
        # If no new bookmark has been created,
        # Then we believe that the request was to delete the bookmark
        if not created:
            bookmark.delete()

        return HttpResponse(
            json.dumps({
                "result": created,
                "count": self.model.objects.filter(obj_id=pk).count()
            }),
            content_type="application/json"
        )

def member(request):
    form = CreateUserForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user)
                return redirect('main:member')

        elif 'log_in' in request.POST:
            username = request.POST.get('username')

            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main:home')
            else:
                messages.info(request, 'Username or password is incorrect')

    context = {'form': form}

    return render(request, 'main/member.html', context)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def logoutUser(request):
    logout(request)
    return redirect('main:home')


def favourite_post(request):
    post = get_object_or_404(Recipes, id=request.POST.get('id'))
    is_favourite = False
    if post.favourite.filter(id=request.user.id).exists():
        post.favourite.remove(request.user)
        is_favourite = False
        print("remove")

    else:
        post.favourite.add(request.user)
        is_favourite = True
        print("add")
    context={
        'post': post,
        'is_favourite':is_favourite,}
    print(context)
    if is_ajax(request=request):
        html = render_to_string('main/favourite_section.html', context, request=request)
        print("ajax")
        return JsonResponse({'form': html})
#    return HttpResponseRedirect(post.get_absolute_url())


"""
def like_post(request):
    user = request.user

    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = PostsRecipes.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)


        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'
            post_obj.save()
            like.save()

        data = {
            'value': like.value,
            'likes': post_obj.liked.all().count()
        }

        return JsonResponse(data, safe=False)
    return redirect('recipes:recipes_home')
"""