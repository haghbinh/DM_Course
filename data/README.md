<div dir="rtl">

# داده‌های درس

داده‌هایی که در جزوه‌ها و دفترچه‌های کارگاه به کار می‌روند و از کتابخانه‌های پایتون (مانند `seaborn` و `scikit-learn`) نمی‌آیند، در این پوشه‌اند تا کدها بدون وابستگی به سایت‌های دیگر اجرا شوند. کدها داده را با مسیر نسبی `../data/...` می‌خوانند؛ پس جزوه یا دفترچه را از داخل پوشه جلسه خودش (مثلاً `Part 6_Clustering`) اجرا کنید.

| فایل | داده | جلسه‌ها | منبع اصلی |
|:-:|:-:|:-:|:-:|
| `housing.csv` | مسکن کالیفرنیا (سرشماری ۱۹۹۰، ۲۰٬۶۴۰ بلوک) | ۱۷، کارگاه ۱۹ | [ageron/handson-ml2](https://github.com/ageron/handson-ml2/tree/master/datasets/housing)، برگرفته از StatLib |
| `sms.tsv` | پیامک‌های هرزنامه (۵٬۵۷۲ پیامک) | کارگاه ۲۱ | [justmarkham/DAT8](https://github.com/justmarkham/DAT8)، برگرفته از SMS Spam Collection در UCI |
| `Telco-Customer-Churn.csv` | ریزش مشتری مخابرات (۷٬۰۴۳ مشتری) | ۲۵ و کارگاه ۲۵ | [IBM/telco-customer-churn-on-icp4d](https://github.com/IBM/telco-customer-churn-on-icp4d) |
| `Mall_Customers.csv` | مشتریان مرکز خرید (۲۰۰ مشتری) | ۲۶ تا ۲۹ و کارگاه‌های آن‌ها | [tirthajyoti/Machine-Learning-with-Python](https://github.com/tirthajyoti/Machine-Learning-with-Python)، منتشرشده در Kaggle |
| `online-retail-dataset.csv.gz` | تراکنش‌های یک فروشگاه اینترنتی (۵۴۱٬۹۰۹ سطر، فشرده) | ۲۹ و کارگاه‌های ۲۹ و ۳۰ | [databricks/Spark-The-Definitive-Guide](https://github.com/databricks/Spark-The-Definitive-Guide)، برگرفته از Online Retail در UCI |

فایل فروشگاه اینترنتی برای کم کردن حجم مخزن با gzip فشرده شده است (۴۵ مگابایت ← ۷ مگابایت)؛ `pd.read_csv` آن را مستقیم و بدون تغییر در نتیجه‌ها می‌خواند. برای شرایط استفاده از هر داده به منبع اصلی آن مراجعه کنید.

</div>
