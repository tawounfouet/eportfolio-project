from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.db import models
from django.urls import reverse

User = get_user_model()

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")
    thumbnail = models.ImageField(blank=True, upload_to='blog')

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    def __str__(self):
        return self.title

    """
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
    """
    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = BlogPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        # if self.published:
        #     try:
        #         temp = BlogPost.objects.get(published=True)
        #         if self != temp:
        #             temp.published = False
        #             temp.save()
        #     except BlogPost.DoesNotExist:
        #         pass
        
        super(BlogPost, self).save(*args, **kwargs)


    @property
    def author_or_default(self):
        return self.author.username if self.author else  "Auteur inconnu"


    def get_absolute_url(self):
        return reverse('posts:home')


class AboutMe(models.Model):
    name = models.CharField(max_length=255)
    #author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    img_perfil = models.ImageField(null=True, blank=True)
    about = models.TextField()
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    youtube_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "AboutMe"

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse("AboutMe_detail", kwargs={"pk": self.pk})