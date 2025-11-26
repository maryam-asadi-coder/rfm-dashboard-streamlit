# تحلیل RFM ۳۶۰ درجه - داشبورد تعاملی مشتریان

![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red) ![Plotly](https://img.shields.io/badge/Plotly-Interactive-orange) ![License](https://img.shields.io/badge/License-MIT-green)

تحلیل پیشرفته و تعاملی مشتریان با استفاده از روش **RFM** (Recency, Frequency, Monetary) + خوشه‌بندی K-Means + قانون پارتو 80/20

### لینک داشبورد آنلاین (همین الان بازش کن!)
https://maryam-rfm-360.streamlit.app  
(یا هر اسمی که توی App URL زدی)

### ویژگی‌های داشبورد
- آپلود مستقیم فایل CSV دیتاست Online Retail
- محاسبه خودکار Recency, Frequency, Monetary
- امتیازدهی RFM (۱ تا ۱۵)
- خوشه‌بندی هوشمند مشتریان با K-Means
- نمودار سه‌بعدی تعاملی (Plotly)
- قانون پارتو 80/20 با درصد دقیق
- متریک‌های کلیدی (درآمد کل، تعداد مشتری، قهرمانان و ...)
- کاملاً فارسی و ریسپانسیو (موبایل هم باز میشه)

### تکنولوژی‌ها
- Streamlit – داشبورد وب
- Pandas & NumPy – پردازش داده
- Plotly – نمودارهای تعاملی
- Scikit-learn – خوشه‌بندی K-Means
- StandardScaler – نرمال‌سازی داده

### نحوه اجرا (لوکال)
```bash
git clone https://github.com/maryam-asadi-coder/rfm-dashboard-streamlit.git
cd rfm-dashboard-streamlit
pip install -r requirements.txt
streamlit run app.py
