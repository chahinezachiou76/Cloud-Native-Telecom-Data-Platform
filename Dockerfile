# 1. البدء بنسخة بايثون جاهزة
FROM python:3.9-slim

# 2. إنشاء مجلد داخل "الحاوية" لنضع فيه شغلنا
WORKDIR /app

# 3. نسخ ملف المكتبات وتثبيتها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. نسخ الكود الخاص بنا داخل الحاوية
COPY app.py .

# 5. الأمر الذي يشغل الكود بمجرد تشغيل الحاوية
CMD ["python", "app.py"]