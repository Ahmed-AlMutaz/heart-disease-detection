import streamlit as st
import pandas as pd
import joblib
import json

# تحميل الـ pipeline
pipeline = joblib.load("pipeline_model2.joblib")

# تحميل الأعمدة المستخدمة
with open("used_features2.json", "r") as f:
    used_features2 = json.load(f)

# عنوان التطبيق
st.title("تطبيق تشخيص أمراض القلب 🫀")

# إنشاء مدخلات المستخدم (نموذج بسيط)
user_input = {}

# مثال لمدخلات (أضف المزيد بناءً على features.json)
user_input["age"] = st.number_input("السن", min_value=20, max_value=100, value=50)
user_input["trestbps"] = st.number_input("الضغط الرايح", min_value=80, max_value=200, value=120)
user_input["chol"] = st.number_input("الكوليسترول", min_value=100, max_value=600, value=200)
user_input["thalach"] = st.number_input("أقصى معدل ضربات القلب", min_value=50, max_value=250, value=150)
user_input["oldpeak"] = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0)

# إضافة مدخلات للسمات التصنيفية
user_input["sex_1"] = st.selectbox("الجنس", ["ذكر", "أنثى"]) == "ذكر"
user_input["fbs_1"] = st.selectbox("هل السكر صايم > 120؟", ["لا", "نعم"]) == "نعم"
user_input["exang_1"] = st.selectbox("هل فيه إجهاد؟", ["لا", "نعم"]) == "نعم"

# باقي الأعمدة التلقائية (تأكد توافقها مع pipeline)
for feature in used_features2:
    if feature not in user_input:
        user_input[feature] = 0

# عند الضغط على زر التنبؤ
if st.button("🔍 تنبأ"):
    try:
        # تحويل الإدخال لـ DataFrame بنفس الترتيب
        input_df = pd.DataFrame([user_input])[used_features2]

        # التنبؤ
        prediction = pipeline.predict(input_df)[0]
        st.success(f"✅ النتيجة المتوقعة: النوع {prediction}")
    except Exception as e:
        st.error(f"حدث خطأ: {e}")
