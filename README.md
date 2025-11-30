# تحلیل RFM ۳۶۰ درجه - داشبورد تعاملی مشتریان

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.38-red)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Live](https://img.shields.io/badge/Live-Online-brightgreen)

تحلیل پیشرفته و **کاملاً آنلاین** رفتار مشتریان با روش RFM + خوشه‌بندی K-Means + قانون پارتو 80/20

### لینک داشبورد زنده (همین الان باز کن!)
https://maryam-rfm.streamlit.app

### اسکرین‌شات از داشبورد

<img width="1269" height="450" alt="newplot (1)" src="https://github.com/user-attachments/assets/202c0a82-b3fe-4581-9d88-4ba16e09db9d" />

<img width="1269" height="500" alt="newplot (2)" src="https://github.com/user-attachments/assets/29adec14-0208-4dfc-a07d-0465757c8bd4" />

<img width="1269" height="450" alt="newplot (5)" src="https://github.com/user-attachments/assets/495966dd-75f6-453a-b4df-1209ecc3ad60" />

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
