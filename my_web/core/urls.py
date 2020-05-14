from django.urls import path
from .views import ( ItemDetailView,
    #HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    CheckoutView,
    AddCouponView,
    RequestRefundView,
    sizefilter,
    search,
    items_list,
    reviews,
    contact_form_view,
  
    )
from django.conf.urls.static import static
from django.conf import settings


app_name = 'core'


urlpatterns = [
                  path('', items_list, name='home'),
                  path('checkout/', CheckoutView.as_view(), name='checkout'),
                  path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
                  path('help/',sizefilter, name='help'),
                  path('reviews/',reviews, name='reviews'),
                  path('contact',contact_form_view, name='contact'),
                  path('search/',search, name='search'),
                  path('product/<slug>/', ItemDetailView.as_view(), name='product'),
                  path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
                  path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
                  path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
                  path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
                       name='remove-single-item-from-cart'),
                  path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)