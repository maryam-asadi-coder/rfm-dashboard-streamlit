# تحلیل RFM ۳۶۰ درجه - داشبورد تعاملی مشتریان

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.38-red)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Live](https://img.shields.io/badge/Live-Online-brightgreen)

تحلیل پیشرفته و **کاملاً آنلاین** رفتار مشتریان با روش RFM + خوشه‌بندی K-Means + قانون پارتو 80/20

### لینک داشبورد زنده (همین الان باز کن!)
https://maryam-rfm.streamlit.app

### اسکرین‌شات واقعی از داشبورد
![Dashboard Preview](https://i.imgur.com/0rK8X5j.png)

### ویژگی‌های کلیدی
- آپلود مستقیم فایل CSV (تا 200MB)
- محاسبه خودکار Recency, Frequency, Monetary
- امتیاز RFM (۳ تا ۱۵)
- خوشه‌بندی هوشمند مشتریان (۴ گروه)
- نمودار سه‌بعدی تعاملی با Plotly
- قانون پارتو 80/20 با درصد دقیق (در این دیتاست: **29.3% مشتری = 80% درآمد**)
- متریک‌های زنده: تعداد مشتری، درآمد کل، تعداد قهرمانان
- کاملاً فارسی، ریسپانسیو و موبایل‌فرندلی

### تکنولوژی‌ها
- Streamlit – داشبورد وب
- Pandas & NumPy – پردازش داده
- Plotly – نمودارهای تعاملی
- Scikit-learn – K-Means Clustering

### نحوه اجرا لوکال
```bash
git clone https://github.com/maryam-asadi-coder/rfm-dashboard-streamlit.git
cd rfm-dashboard-streamlit
pip install -r requirements.txt
streamlit run app.py
