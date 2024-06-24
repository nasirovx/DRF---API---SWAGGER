from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Person
from .serializer import PersonSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsAdminOrReadOnly
from .forms import PersonForm
from django.contrib.auth.decorators import login_required


def home(request):
    people = Person.objects.all()
    return render(request, 'main/home.html', {'people': people})


@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)  # Получить объект без сохранения в БД
            person.user = request.user  # Присвоить текущего пользователя
            person.save()  # Теперь сохраняем объект
            return redirect('home')
        else:
            error = "Форма была неверной"

    form = PersonForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)


class WomenAPIListPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100

class PersonAPIList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = WomenAPIListPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
class PersonAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticated,)
    
class PersonAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAdminOrReadOnly,)