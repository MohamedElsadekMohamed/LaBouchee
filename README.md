# LaBouchee — Branch Sales Automation | أتمتة مبيعات الفروع

أداة ويب لأتمتة تقرير مبيعات الفروع (لابوشيه / ليفانا): بتاخد شيت أسطر الفواتير، بتصنّف
(صواني/بوكسات ليفانا ← **ليفانا**، وأي حاجة تانية ← **لابوشيه**)، بتفلتر على تطبيقات التوصيل بس،
بتشيل «مبيعات الجملة»، بتعمل Pivot لكل فرع، بتدمج النتيجة في تقرير الفروع، بترتّب الفروع،
بتنسّق الألوان (بتتغيّر كل مرة)، وبتطلّع Excel منسّق. وكمان بتدوّر على **رد العربون** و**العربون**.

> كل المعالجة بتحصل **في المتصفح** (مكتبة Excel مدمجة داخل الصفحة) — يعني خصوصي، سريع،
> وبيشتغل حتى أوفلاين. دور Flask هنا إنه يقدّم الصفحة ويديك لينك ثابت للنشر.

---

## 🚀 التشغيل محليًا (Local)

```bash
git clone https://github.com/<username>/labouchee-branch-sales.git
cd labouchee-branch-sales
pip install -r requirements.txt
python app.py
```
افتح المتصفح على: http://localhost:5000

---

## ☁️ النشر (Deploy) — تفضل شغّالة على لينك ثابت

### الطريقة (أ) — Render.com (مجاني)
1. ارفع المشروع على GitHub.
2. ادخل https://render.com ← **New +** ← **Web Service** ← اربط الريبو.
3. Render هيقرأ ملف `render.yaml` تلقائيًا (أو اضبط يدوي):
   - **Build:** `pip install -r requirements.txt`
   - **Start:** `gunicorn app:app --workers 2 --bind 0.0.0.0:$PORT`
   - **Plan:** Free
4. اضغط **Create** ← هيديك لينك زي `https://labouchee-branch-sales.onrender.com`.

### الطريقة (ب) — Railway.app
1. ارفع على GitHub ← https://railway.app ← **New Project** ← **Deploy from GitHub repo**.
2. Railway هيكتشف Python + `Procfile` تلقائيًا ويطلّع لينك.

### الطريقة (ج) — الأبسط: GitHub Pages (استضافة ثابتة مجانية وبتشتغل دايمًا)
بما إن الأداة كلها في المتصفح، تقدر تستضيفها من غير سيرفر خالص:
1. في إعدادات الريبو ← **Settings** ← **Pages**.
2. Source: `Deploy from a branch` ← Branch: `main` ← Folder: `/ (root)`.
3. Save ← بعد دقيقة هيديك لينك زي `https://<username>.github.io/labouchee-branch-sales/`
   (الصفحة الرئيسية هي `index.html` مباشرة).

> ملاحظة عن Render المجاني: الخدمة بتنام بعد فترة خمول وبتصحى في أول زيارة (تأخير بسيط).
> لو عايز لينك دايمًا فوري بدون أي انتظار → **GitHub Pages** هو الأنسب لأن الأداة client-side.

---

## 🗂️ محتويات المشروع
```
app.py            # سيرفر Flask (يقدّم الصفحة + /health)
index.html        # الأداة كاملة (مستقلة، مكتبة Excel مدمجة)
requirements.txt  # Flask + gunicorn
Procfile          # أمر التشغيل للنشر
render.yaml       # إعداد نشر Render
runtime.txt       # نسخة بايثون
```

## 📄 المدخلات
1. **شيت أسطر الفواتير** (مطلوب) — منه بيتعمل الـ Pivot.
2. **شيت مبيعات الفروع** (اختياري) — بيتدمج فيه.
3. **تقرير نقاط البيع** (اختياري) — لاكتشاف العربون/التأمين.

## 🔒 الخصوصية
الملفات مابتترفعش على أي سيرفر — كله بيتعالج جوّه متصفحك.
