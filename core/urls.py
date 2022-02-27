from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView , HomeViewMarketplace, UserProductListView, ProductUpdateView, ProductDetailView , CreateCheckoutSessionView, SuccessView, UserProductInsert,stripe_webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('users/', include('accounts.urls', namespace='users')),
    path('social/', include('social.urls', namespace='social')),
    path('marketplaceurl/', include('marketplace.urls', namespace='marketplace')),
    path('', HomeView.as_view(), name="home"),
    path('marketplace', HomeViewMarketplace.as_view(), name="HomeMarketplace"),
    path('products/', UserProductListView.as_view(), name="product-list"),
    path('products/insert/',  UserProductInsert.as_view(), name="insert-list"),
    path('products/<slug>/', ProductDetailView.as_view(), name="product-detail"),
    path('products/<slug>/update/', ProductUpdateView.as_view(), name="product-update"),
    path('create-checkout-session/<slug>/', CreateCheckoutSessionView.as_view(), name="create-checkout-session"),
    path("success/", SuccessView.as_view(), name="success"),
    path("webhook/stripe/", stripe_webhook, name="stripe-webhook"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)