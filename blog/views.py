from django.shortcuts import render, redirect
from blog.forms import FormularioPost
from django.contrib import messages
from blog.models import Post
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/acceder')
def index(request):
    listado_posts = Post.objects.all()
    paginator = Paginator(listado_posts, 3)
    pagina = request.GET.get("page") or 1
    posts = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, posts.paginator.num_pages + 1)
    return render(request, "blog.html", {"posts": posts, "paginas": paginas, "pagina_actual": pagina_actual})

@login_required(login_url='/accounts/acceder')
def crear_post(request):
    if request.method == "POST":
        form = FormularioPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor_id = request.user.id
            post.save()
            titulo = form.cleaned_data.get("titulo")
            messages.success(request, f"El post {titulo} se ha creado correctamente")
            return redirect("blog")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

    form = FormularioPost()
    return render(request, "crear_post.html", {"form": form})

@login_required(login_url='/accounts/acceder')
def eliminar_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        messages.error(request, "El post que quieres eliminar no existe")
        return redirect("blog")

    if post.autor != request.user:
        messages.error(request, "No eres el autor de este post")
        return redirect("blog")

    post.delete()
    messages.success(request, f"El post '{post.titulo}' ha sido eliminado!")
    return redirect("blog")