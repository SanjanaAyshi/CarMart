from django.db import models
from category.models import Category
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # ekta post multiple category r hoi abar ekta category r modhe multiple post hoite pare
    category = models.ManyToManyField(Category)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='post/media/uploads/', blank=True, null=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart for {self.account.first_name}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Post, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    # jkhn e ei class er object toiri hobe sei time ta rekhe dibe
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self.name}"
