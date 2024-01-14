from products.models import Basket


def baskets(request):
    return {
        'basket': request.user.basket_set.all() if request.user.is_authenticated else [],
    }
