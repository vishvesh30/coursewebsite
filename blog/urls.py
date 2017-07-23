from django.conf.urls import include, url
from blog.views import PostsFeed
from django.views.generic import ListView
from blog.models import Category, Post
from blog import views
from django_comments.models import Comment
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
url(r'^admin/', include(admin.site.urls)),

    # Home page
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(
        model=Post,
        paginate_by=5,
        )),

    # Blog posts
    url(r'^\d{4}/\d{1,2}/(?P<postSlug>[-a-zA-Z0-9]+)/?$', views.getPost),

    # Categories
    url(r'^categories/?$', ListView.as_view(
        model=Category,
        )),
    url(r'^categories/(?P<categorySlug>\w+)/?$', views.getCategory),
    url(r'^categories/(?P<categorySlug>\w+)/(?P<selected_page>\d+)/?$', views.getCategory),

    # Comments
    url(r'^comments/', include('django_comments.urls')),

    # RSS feeds
    url(r'^feeds/posts/$', PostsFeed()),

    # Flat pages
    url(r'', include('django.contrib.flatpages.urls')),
        ]