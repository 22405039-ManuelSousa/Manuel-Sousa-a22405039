from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .forms import RegistoForm
from .models import Perfil
import secrets

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('projetos')
        else:
            return render(request, 'accounts/login.html', {'mensagem': 'Credenciais inválidas'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('projetos')

def registo_view(request):
    form = RegistoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/registo.html', context)

def envia_email(perfil, email):
    send_mail(
        subject='Portfolio: Autenticação',
        message=f'Caro {perfil.user.first_name or perfil.user.username}, clique no link http://127.0.0.1:8000/accounts/autentica/?token={perfil.token} para entrar na aplicação.',
        from_email='manuelbarrososousa@gmail.com',
        recipient_list=[email]
    )

def login_magic_link(request):
    email = request.GET.get('email')
    if email:
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            perfil, _ = Perfil.objects.get_or_create(user=user)
            perfil.token = secrets.token_urlsafe(32)
            perfil.save()
            envia_email(perfil, email)
            return render(request, 'accounts/login.html', {'mensagem_info': 'Link enviado para o teu email.'})
        else:
            return render(request, 'accounts/login.html', {'mensagem': 'Email não encontrado.'})
    return render(request, 'accounts/login.html')

def autentica(request):
    token = request.GET.get('token')
    try:
        perfil = Perfil.objects.get(token=token)
        perfil.token = ''
        perfil.save()
        login(request, perfil.user)
        return redirect('projetos')
    except Perfil.DoesNotExist:
        return render(request, 'accounts/login.html', {'mensagem': 'Link inválido ou expirado.'})