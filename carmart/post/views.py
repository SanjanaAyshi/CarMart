from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView


# @method_decorator(login_required, name='dispatch')
# class AddPostCreateView(CreateView):
#     model = models.Post
#     form_class = forms.PostFrom
#     template_name = 'addPost.html'
#     success_url = reverse_lazy('add_post')

#     def form_valid(self, form):
#         form.instance.account = self.request.user
#         return super().form_valid(form)


class EditCartUpdateView(UpdateView):
    model = models.Post
    form_class = forms.CartForm
    template_name = 'addCart.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')


# @method_decorator(login_required, name='dispatch')
# class deletePostUpdateView(DeleteView):
#     model = models.Post
#     template_name = 'deleteview.html'
#     pk_url_kwarg = 'id'
#     success_url = reverse_lazy('add_post')


class DetailPostView(DetailView):
    model = models.Post
    # pk_url_kwarg = 'id' use kori nai cuz amraurl e pk bolsi pk na bolle eita use hobe
    template_name = 'postdetails.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object  # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(account=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_quantity = sum(item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_quantity': total_quantity,
    }

    return render(request, 'view_cart.html', context)
