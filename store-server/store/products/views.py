from django.shortcuts import render


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                'price': 6090,
                'image': 'Adidas-hoodie.png',
            },
            {
                'name': 'Синяя куртка The North Face',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                'price': 23_725,
                'image': 'Blue-jacket-The-North-Face.png',
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                'price': 3_390,
                'image': 'Brown-sports-oversized-top-ASOS-DESIGN.png',
            },
            {
                'name': 'Черный рюкзак Nike Heritage',
                'description': 'Плотная ткань. Легкий материал.',
                'price': 2_340,
                'image': 'Black-Nike-Heritage-backpack.png',
            },
            {
                'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'description': 'Гладкий кожаный верх. Натуральный материал.',
                'price': 13_590,
                'image': 'Black-Dr-Martens-shoes.png',
            },
            {
                'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                'price': 2_890,
                'image': 'Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
            },
        ],
    }
    return render(request, 'products/products.html', context)
