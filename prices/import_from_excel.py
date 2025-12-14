import os
import sys
import django
import pandas as pd

# إضافة مجلد المشروع للمسار
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# تحديد إعدادات Django الجديدة
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'price_web.settings')
django.setup()

from prices.models import Product

# قراءة ملف الإكسل
file_path = r'/mnt/data/024df0ff-fda5-42ae-9022-be0f287b3049.xlsx'
df = pd.read_excel(file_path)

# التأكد من وجود عمود المنتج
if 'المنتج' not in df.columns:
    raise Exception('❌ عمود (المنتج) غير موجود في ملف الإكسل')

# تحويل القيم الفارغة أو nan إلى None أو 0
for col in ['السعر العادي', 'الدكان', 'كيان', 'المنافس', 'العثيم', 'أمازون']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df[col] = df[col].fillna(0)

# تكرار السعر العادي لجميع الصفوف إذا كان العمود موجود
if 'السعر العادي' in df.columns:
    df['السعر العادي'] = df['السعر العادي'].fillna(0)

# تحديث أو إنشاء المنتجات في قاعدة البيانات
for index, row in df.iterrows():
    name = row['المنتج']
    defaults = {
        'regular_price': row.get('السعر العادي', 0),
        'dukkan': row.get('الدكان', 0),
        'kian': row.get('كيان', 0),
        'competitor': row.get('المنافس', 0),
        'othaim': row.get('العثيم', 0),
        'amazon': row.get('أمازون', 0)
    }

    product, created = Product.objects.update_or_create(
        name=name,
        defaults=defaults
    )

    if created:
        print(f'✅ تم إنشاء المنتج: {name}')
    else:
        print(f'♻️ تم تحديث المنتج: {name}')

print('🎉 تم استيراد جميع البيانات بنجاح')
