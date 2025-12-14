from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product

# دالة تحويل آمنة من string إلى float
def safe_float(value, default=None):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('table')
        else:
            return render(request, 'login.html', {'error': 'اسم مستخدم أو كلمة مرور خاطئة'})
    return render(request, 'login.html')


def table_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    products = Product.objects.all()

    if request.method == 'POST':
        for product in products:
            # تحديث كل الحقول السعرية باستخدام safe_float لتجنب أخطاء القيم الفارغة
            product.regular_price = safe_float(request.POST.get(f'regular_price_{product.id}'), product.regular_price)
            product.dukkan = safe_float(request.POST.get(f'dukkan_{product.id}'), product.dukkan)
            product.kian = safe_float(request.POST.get(f'kian_{product.id}'), product.kian)
            product.competitor = safe_float(request.POST.get(f'competitor_{product.id}'), product.competitor)
            product.othaim = safe_float(request.POST.get(f'othaim_{product.id}'), product.othaim)
            product.amazon = safe_float(request.POST.get(f'amazon_{product.id}'), product.amazon)
            product.save()

    return render(request, 'table.html', {'products': products})
