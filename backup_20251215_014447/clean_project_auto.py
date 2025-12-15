# clean_project_auto.py
import os
import shutil
import datetime

# مسار مشروعك
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# مجلد النسخ الاحتياطية
BACKUP_DIR = os.path.join(BASE_DIR, "backup_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))

# مجلدات وملفات أساسية لا يتم حذفها
REQUIRED_DIRS = ["price_web", "prices", "venv"]
REQUIRED_FILES = ["manage.py"]
REQUIRED_TEMPLATE_FILES = ["base.html", "table.html"]

PROTECTED_DIRS = ['.git', '__pycache__']

def backup_and_remove_file(path):
    try:
        rel_path = os.path.relpath(path, BASE_DIR)
        backup_path = os.path.join(BACKUP_DIR, rel_path)
        os.makedirs(os.path.dirname(backup_path), exist_ok=True)
        shutil.copy2(path, backup_path)
        os.remove(path)
        print(f"نسخة احتياطية وحذف الملف: {path}")
    except Exception as e:
        print(f"تجاهل الملف (غير قابل للحذف): {path} - {e}")

def backup_and_remove_dir(path):
    try:
        rel_path = os.path.relpath(path, BASE_DIR)
        backup_path = os.path.join(BACKUP_DIR, rel_path)
        shutil.copytree(path, backup_path)
        shutil.rmtree(path)
        print(f"نسخة احتياطية وحذف المجلد: {path}")
    except Exception as e:
        print(f"تجاهل المجلد (غير قابل للحذف): {path} - {e}")

def clean_dir(base_path):
    for item in os.listdir(base_path):
        full_path = os.path.join(base_path, item)
        if os.path.isdir(full_path):
            if item not in REQUIRED_DIRS and item not in PROTECTED_DIRS:
                backup_and_remove_dir(full_path)
        elif os.path.isfile(full_path):
            if item not in REQUIRED_FILES:
                backup_and_remove_file(full_path)

    # تنظيف قوالب Django
    templates_dir = os.path.join(base_path, "prices", "templates")
    if os.path.exists(templates_dir):
        for file in os.listdir(templates_dir):
            full_path = os.path.join(templates_dir, file)
            if file not in REQUIRED_TEMPLATE_FILES:
                if os.path.isdir(full_path):
                    backup_and_remove_dir(full_path)
                else:
                    backup_and_remove_file(full_path)

if __name__ == "__main__":
    os.makedirs(BACKUP_DIR, exist_ok=True)
    clean_dir(BASE_DIR)
    print(f"\nتم تنظيف المشروع وإنشاء النسخ الاحتياطية في: {BACKUP_DIR}")
