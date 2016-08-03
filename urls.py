from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'FrontU.blog.views.home', name='home'),
    url(r'^FrontU/blog/templates/login$', 'FrontU.blog.views.login', name='login'),
    url(r'^FrontU/blog/templates/signup$', 'FrontU.blog.views.signup', name='signup'),
    url(r'^FrontU/blog/templates/about$', 'FrontU.blog.views.about', name='about'),
    url(r'^FrontU/blog/templates/contact$', 'FrontU.blog.views.contact', name='contact'),

    # url(r'^FrontU/', include('FrontU.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
