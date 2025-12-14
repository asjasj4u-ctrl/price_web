from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product
import pandas as pd
import os

# ----------------------
# Login view
# ----------------------
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

# ----------------------
# Table view (لوحة الأسعار)
# ----------------------
def table_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    products = Product.objects.all().order_by('name')
    message_text = generate_messages(products)

    if request.method == 'POST':
        # تحديث الأسعار من لوحة التحكم
        for product in products:
            product.dukkan = safe_decimal(request.POST.get(f'dukkan_{product.id}'))
            product.kian = safe_decimal(request.POST.get(f'kian_{product.id}'))
            product.competitor = safe_decimal(request.POST.get(f'competitor_{product.id}'))
            product.othaim = safe_decimal(request.POST.get(f'othaim_{product.id}'))
            product.amazon = safe_decimal(request.POST.get(f'amazon_{product.id}'))
            product.save()
        # تحديث Excel بعد التعديل
        export_to_excel(products)
        message_text = generate_messages(products)

    return render(request, 'table.html', {'products': products, 'messages': message_text})

# ----------------------
# دالة تحويل القيم إلى Decimal
# ----------------------
def safe_decimal(value):
    try:
        if value is None or value == '':
            return None
        return float(value)
    except ValueError:
        return None

# ----------------------
# دالة استيراد Excel
# ----------------------
def import_from_excel():
    excel_path = os.path.join(os.getcwd(), 'prices_excel', 'products.xlsx')
    df = pd.read_excel(excel_path)

    for _, row in df.iterrows():
        Product.objects.update_or_create(
            name=row['المنتج'],
            defaults={
                'regular_price': row.get('السعر العادي', 0),
                'dukkan': row.get('الدكان', None),
                'kian': row.get('كيان', None),
                'competitor': row.get('المنافس', None),
                'othaim': row.get('العثيم', None),
                'amazon': row.get('أمازون', None),
            }
        )

# ----------------------
# دالة تصدير Excel
# ----------------------
def export_to_excel(products):
    excel_path = os.path.join(os.getcwd(), 'prices_excel', 'products.xlsx')
    data = []
    for p in products:
        data.append({
            'المنتج': p.name,
            'السعر العادي': float(p.regular_price),
            'الدكان': float(p.dukkan) if p.dukkan is not None else None,
            'كيان': float(p.kian) if p.kian is not None else None,
            'المنافس': float(p.competitor) if p.competitor is not None else None,
            'العثيم': float(p.othaim) if p.othaim is not None else None,
            'أمازون': float(p.amazon) if p.amazon is not None else None,
        })
    df = pd.DataFrame(data)
    df.to_excel(excel_path, index=False)

# ----------------------
# دالة إنشاء الرسائل التسويقية
# ----------------------
def generate_messages(products):
    messages = []
    sorted_products = []

    for p in products:
        prices = {
            'dukkan': p.dukkan,
            'kian': p.kian,
            'competitor': p.competitor,
            'othaim': p.othaim,
            'amazon': p.amazon
        }
        # إزالة القيم الفارغة
        prices = {k: v for k, v in prices.items() if v is not None}
        if prices:
            min_store = min(prices, key=prices.get)
            min_price = prices[min_store]
            sorted_products.append(f"أرخص سعر لـ {p.name}: {min_price} ريال ({min_store})")

    # تقسيم الرسائل كل 10 منتجات
    chunk_size = 10
    for i in range(0, len(sorted_products), chunk_size):
        messages.append('\n'.join(sorted_products[i:i+chunk_size]))

    return messages
