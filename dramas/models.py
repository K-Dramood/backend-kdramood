from django.db import models

class Drama(models.Model):
    title = models.CharField(max_length=200)
    mood = models.CharField(max_length=25)
    genre = models.CharField(max_length=100)
    synopsis = models.TextField()
    user = models.ForeignKey(
        'users.User', related_name='dramas', on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to='image/', default='images/default.jpg', blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(
        'users.User', related_name='reviews', on_delete=models.CASCADE)
    drama = models.ForeignKey(
        Drama, on_delete=models.CASCADE, related_name='reviews')
    body = models.TextField()
    mood = models.BooleanField()

    def __str__(self):
        return self.user
