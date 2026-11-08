<div dir="rtl">

<p align="center"><img src="img/pgu_logo.png" alt="دانشگاه خلیج فارس" width="110"></p>

#  داده‌کاوی

این مخزن شامل جزوه‌های درس **داده‌کاوی (Data Mining)** برای مقطع کارشناسی آمار است. جزوه‌ها به زبان فارسی و در قالب Markdown (سازگار با Obsidian) نوشته شده‌اند و مثال‌های عملی با **Python** (`numpy`، `pandas`، `matplotlib`، `seaborn` و `scikit-learn`) ارائه می‌شوند.

- **مدرس:** دکتر حسین حق‌بین
- **دانشگاه:** دانشگاه خلیج فارس
- **وب‌سایت درس:** [haghbinh.github.io/DM_Course](https://haghbinh.github.io/DM_Course/) — همه جزوه‌ها با فرمول‌ها، نمودارها و Callout‌ها، همراه با دکمه دانلود PDF هر جلسه
- **PDF همه جلسه‌ها در یک فایل:** [all-sessions.pdf](https://haghbinh.github.io/DM_Course/pdf/all-sessions.pdf)
- **تعداد واحد:** ۳
- **پیش‌نیاز:** برنامه‌نویسی Python و آمار توصیفی
- **نرم‌افزار اصلی:** Python (نرم‌افزارهای جایگزین: R، MATLAB)
- [طرح درس کامل](Teaching%20Plan.md) — اهداف، سرفصل جلسات، تمرین‌ها و نحوه ارزشیابی

## ساختار درس

| بخش | موضوع | جلسات |
|:-:|--:|:-:|
| ۰ | [مقدمه و فرایند داده‌کاوی](#part-0) | ۱ – ۲ |
| ۱ | [شناخت داده (Data Understanding)](#part-1) | ۳ – ۶ |
| ۲ | [تحلیل اکتشافی داده (EDA)](#part-2) | ۷ – ۹ |
| ۳ | [پیش‌پردازش داده (Data Preprocessing)](#part-3) | ۱۰ – ۱۵ |
| ۴ | [یادگیری نظارت‌شده — رگرسیون (Regression)](#part-4) | ۱۶ – ۱۹ |
| ۵ | [یادگیری نظارت‌شده — طبقه‌بندی (Classification)](#part-5) | ۲۰ – ۲۵ |
| ۶ | [یادگیری بدون نظارت — خوشه‌بندی (Clustering)](#part-6) | ۲۶ – ۳۰ |

## ارزشیابی

| بخش | درصد |
|--:|:-:|
| آزمون میان‌ترم (جلسات ۱ تا ۱۲) | ۲۵٪ |
| پروژه عملی | ۲۵٪ |
| تکالیف و تمرین‌ها | ۱۰٪ |
| آزمون پایانی (جلسات ۱۳ تا ۲۸) | ۴۰٪ |

---

<a id="part-0"></a>

## بخش ۰: مقدمه و فرایند داده‌کاوی

آشنایی با مفهوم داده‌کاوی و کشف دانش (KDD)، کاربردها و وظایف اصلی آن، فرایند استاندارد CRISP-DM و راه‌اندازی محیط کار Python.

📁 پوشه: [Part 0_Introduction](Part%200_Introduction)

| جلسه | عنوان | دانلود PDF |
|:-:|--:|:-:|
| ۱ | [مقدمه‌ای بر داده‌کاوی](Part%200_Introduction/%DB%B1%20-%20%D9%85%D9%82%D8%AF%D9%85%D9%87%E2%80%8C%D8%A7%DB%8C%20%D8%A8%D8%B1%20%D8%AF%D8%A7%D8%AF%D9%87%E2%80%8C%DA%A9%D8%A7%D9%88%DB%8C.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-01.pdf) |
| ۲ | [فرایند CRISP-DM و محیط کار](Part%200_Introduction/2%20-%20%D9%81%D8%B1%D8%A7%DB%8C%D9%86%D8%AF%20CRISP-DM%20%D9%88%20%D9%85%D8%AD%DB%8C%D8%B7%20%DA%A9%D8%A7%D8%B1.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-02.pdf) |

<a id="part-1"></a>

## بخش ۱: شناخت داده (Data Understanding)

انواع داده و ویژگی‌ها، آمار توصیفی، معیارهای شباهت و فاصله و ارزیابی کیفیت داده.

📁 پوشه: [Part 1_Data Understanding](Part%201_Data%20Understanding)

| جلسه | عنوان | دانلود PDF |
|:-:|--:|:-:|
| ۳ | [انواع داده و ویژگی‌ها](Part%201_Data%20Understanding/%DB%B3%20-%20%D8%A7%D9%86%D9%88%D8%A7%D8%B9%20%D8%AF%D8%A7%D8%AF%D9%87%20%D9%88%20%D9%88%DB%8C%DA%98%DA%AF%DB%8C%E2%80%8C%D9%87%D8%A7.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-03.pdf) |
| ۴ | [آمار توصیفی](Part%201_Data%20Understanding/4%20-%20%D8%A2%D9%85%D8%A7%D8%B1%20%D8%AA%D9%88%D8%B5%DB%8C%D9%81%DB%8C.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-04.pdf) |
| ۵ | [معیارهای شباهت و فاصله](Part%201_Data%20Understanding/%DB%B5%20-%20%D9%85%D8%B9%DB%8C%D8%A7%D8%B1%D9%87%D8%A7%DB%8C%20%D8%B4%D8%A8%D8%A7%D9%87%D8%AA%20%D9%88%20%D9%81%D8%A7%D8%B5%D9%84%D9%87.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-05.pdf) |
| ۶ | [کیفیت داده](Part%201_Data%20Understanding/%DB%B6%20-%20%DA%A9%DB%8C%D9%81%DB%8C%D8%AA%20%D8%AF%D8%A7%D8%AF%D9%87.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-06.pdf) |

<a id="part-2"></a>

## بخش ۲: تحلیل اکتشافی داده (EDA)

تحلیل تک‌متغیره، دومتغیره و چندمتغیره با نمودار و آماره‌ها، و یک مطالعه موردی کامل EDA همراه با استخراج بینش و داستان‌گویی با داده.

📁 پوشه: [Part 2_EDA](Part%202_EDA)

| جلسه | عنوان | دانلود PDF |
|:-:|--:|:-:|
| ۷ | [تحلیل تک‌متغیره](Part%202_EDA/%DB%B7%20-%20%D8%AA%D8%AD%D9%84%DB%8C%D9%84%20%D8%AA%DA%A9%E2%80%8C%D9%85%D8%AA%D8%BA%DB%8C%D8%B1%D9%87.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-07.pdf) |
| ۸ | [تحلیل دومتغیره و چندمتغیره](Part%202_EDA/8%20-%20%D8%AA%D8%AD%D9%84%DB%8C%D9%84%20%D8%AF%D9%88%D9%85%D8%AA%D8%BA%DB%8C%D8%B1%D9%87%20%D9%88%20%DA%86%D9%86%D8%AF%D9%85%D8%AA%D8%BA%DB%8C%D8%B1%D9%87.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-08.pdf) |
| ۹ | [مطالعه موردی EDA](Part%202_EDA/9%20-%20%D9%85%D8%B7%D8%A7%D9%84%D8%B9%D9%87%20%D9%85%D9%88%D8%B1%D8%AF%DB%8C%20EDA.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-09.pdf) |

<a id="part-3"></a>

## بخش ۳: پیش‌پردازش داده (Data Preprocessing)

مدیریت داده گمشده، پرت، نویز و تکراری؛ تبدیل و یکپارچه‌سازی داده؛ مهندسی و انتخاب ویژگی؛ کاهش ابعاد؛ و طراحی آزمایش و ساخت Pipeline.

📁 پوشه: [Part 3_Data Preprocessing](Part%203_Data%20Preprocessing)

| جلسه | عنوان | دانلود PDF |
|:-:|--:|:-:|
| ۱۰ | [مدیریت داده گمشده](Part%203_Data%20Preprocessing/%DB%B1%DB%B0%20-%20%D9%85%D8%AF%DB%8C%D8%B1%DB%8C%D8%AA%20%D8%AF%D8%A7%D8%AF%D9%87%20%DA%AF%D9%85%D8%B4%D8%AF%D9%87.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-10.pdf) |
| ۱۱ | [داده پرت، نویز و داده تکراری](Part%203_Data%20Preprocessing/11-%20%D8%AF%D8%A7%D8%AF%D9%87%20%D9%BE%D8%B1%D8%AA%D8%8C%20%D9%86%D9%88%DB%8C%D8%B2%20%D9%88%20%D8%AF%D8%A7%D8%AF%D9%87%20%D8%AA%DA%A9%D8%B1%D8%A7%D8%B1%DB%8C.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-11.pdf) |
| ۱۲ | [تبدیل و یکپارچه‌سازی داده](Part%203_Data%20Preprocessing/%DB%B1%DB%B2%20-%20%D8%AA%D8%A8%D8%AF%DB%8C%D9%84%20%D9%88%20%DB%8C%DA%A9%D9%BE%D8%A7%D8%B1%DA%86%D9%87%E2%80%8C%D8%B3%D8%A7%D8%B2%DB%8C%20%D8%AF%D8%A7%D8%AF%D9%87.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-12.pdf) |
| ۱۳ | [مهندسی و انتخاب ویژگی](Part%203_Data%20Preprocessing/%DB%B1%DB%B3%20-%20%D9%85%D9%87%D9%86%D8%AF%D8%B3%DB%8C%20%D9%88%20%D8%A7%D9%86%D8%AA%D8%AE%D8%A7%D8%A8%20%D9%88%DB%8C%DA%98%DA%AF%DB%8C.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-13.pdf) |
| ۱۴ | [کاهش ابعاد](Part%203_Data%20Preprocessing/%DB%B1%DB%B4-%20%DA%A9%D8%A7%D9%87%D8%B4%20%D8%A7%D8%A8%D8%B9%D8%A7%D8%AF.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-14.pdf) |
| ۱۵ | [طراحی آزمایش و Pipeline](Part%203_Data%20Preprocessing/%DB%B1%DB%B5%20-%20%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C%20%D8%A2%D8%B2%D9%85%D8%A7%DB%8C%D8%B4%20%D9%88%20Pipeline.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-15.pdf) |
| ۱۵ | [کارگاه Pipeline (نوت‌بوک Jupyter)](Part%203_Data%20Preprocessing/%DB%B1%DB%B5%20-%20%DA%A9%D8%A7%D8%B1%DA%AF%D8%A7%D9%87%20Pipeline.ipynb) | — |
| پروژه | [پروژه ۱: کیفیت هوای یک شهر](Part%203_Data%20Preprocessing/%D9%BE%D8%B1%D9%88%DA%98%D9%87%201-%20%DA%A9%DB%8C%D9%81%DB%8C%D8%AA%20%D9%87%D9%88%D8%A7%DB%8C%20%DB%8C%DA%A9%20%D8%B4%D9%87%D8%B1.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/project-1.pdf) |

<a id="part-4"></a>

## بخش ۴: یادگیری نظارت‌شده — رگرسیون (Regression)

مبانی یادگیری نظارت‌شده، رگرسیون خطی ساده و چندگانه، معیارهای ارزیابی، بیش‌برازش و اعتبارسنجی متقابل، و منظم‌سازی (Ridge و Lasso).

📁 پوشه: [Part 4_Regression](Part%204_Regression)

| جلسه | عنوان | دانلود PDF |
|:-:|--:|:-:|
| ۱۶ | [مبانی یادگیری نظارت‌شده و رگرسیون خطی ساده](Part%204_Regression/16%20-%20%D9%85%D8%A8%D8%A7%D9%86%DB%8C%20%DB%8C%D8%A7%D8%AF%DA%AF%DB%8C%D8%B1%DB%8C%20%D9%86%D8%B8%D8%A7%D8%B1%D8%AA%E2%80%8C%D8%B4%D8%AF%D9%87%20%D9%88%20%D8%B1%DA%AF%D8%B1%D8%B3%DB%8C%D9%88%D9%86%20%D8%AE%D8%B7%DB%8C%20%D8%B3%D8%A7%D8%AF%D9%87.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-16.pdf) |
| ۱۷ | [رگرسیون چندگانه، هم‌خطی، رگرسیون غیرخطی و ارزیابی](Part%204_Regression/17%20-%20%D8%B1%DA%AF%D8%B1%D8%B3%DB%8C%D9%88%D9%86%20%DA%86%D9%86%D8%AF%DA%AF%D8%A7%D9%86%D9%87%D8%8C%20%D9%87%D9%85%E2%80%8C%D8%AE%D8%B7%DB%8C%D8%8C%20%D8%B1%DA%AF%D8%B1%D8%B3%DB%8C%D9%88%D9%86%20%D8%BA%DB%8C%D8%B1%D8%AE%D8%B7%DB%8C%20%D9%88%20%D8%A7%D8%B1%D8%B2%DB%8C%D8%A7%D8%A8%DB%8C.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-17.pdf) |
| ۱۸ | [رگرسیون چندجمله‌ای، بیش‌برازش و اعتبارسنجی متقابل](Part%204_Regression/18%20-%20%D8%B1%DA%AF%D8%B1%D8%B3%DB%8C%D9%88%D9%86%20%DA%86%D9%86%D8%AF%D8%AC%D9%85%D9%84%D9%87%E2%80%8C%D8%A7%DB%8C%D8%8C%20%D8%A8%DB%8C%D8%B4%E2%80%8C%D8%A8%D8%B1%D8%A7%D8%B2%D8%B4%20%D9%88%20%D8%A7%D8%B9%D8%AA%D8%A8%D8%A7%D8%B1%D8%B3%D9%86%D8%AC%DB%8C%20%D9%85%D8%AA%D9%82%D8%A7%D8%A8%D9%84.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-18.pdf) |
| ۱۹ | [منظم‌سازی در رگرسیون](Part%204_Regression/19%20-%20%D9%85%D9%86%D8%B8%D9%85%E2%80%8C%D8%B3%D8%A7%D8%B2%DB%8C%20%D8%AF%D8%B1%20%D8%B1%DA%AF%D8%B1%D8%B3%DB%8C%D9%88%D9%86.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-19.pdf) |

<a id="part-5"></a>

## بخش ۵: یادگیری نظارت‌شده — طبقه‌بندی (Classification)

مبانی طبقه‌بندی و k-NN، بیز ساده و رگرسیون لجستیک، درخت تصمیم، روش‌های گروهی (Bagging، Random Forest، Boosting)، ماشین بردار پشتیبان و ارزیابی مدل‌های طبقه‌بندی.

📁 پوشه: [Part 5_Classification](Part%205_Classification)

| جلسه | عنوان | دانلود PDF |
|:-:|--:|:-:|
| ۲۰ | [مبانی طبقه‌بندی و k-NN](Part%205_Classification/20%20-%20%20%D9%85%D8%A8%D8%A7%D9%86%DB%8C%20%D8%B7%D8%A8%D9%82%D9%87%E2%80%8C%D8%A8%D9%86%D8%AF%DB%8C%20%D9%88%20k-NN.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-20.pdf) |
| ۲۱ | [بیز ساده و رگرسیون لجستیک](Part%205_Classification/21%20-%20%D8%A8%DB%8C%D8%B2%20%D8%B3%D8%A7%D8%AF%D9%87%20%D9%88%20%D8%B1%DA%AF%D8%B1%D8%B3%DB%8C%D9%88%D9%86%20%D9%84%D8%AC%D8%B3%D8%AA%DB%8C%DA%A9.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-21.pdf) |
| ۲۲ | [درخت تصمیم](Part%205_Classification/22%20-%20%D8%AF%D8%B1%D8%AE%D8%AA%20%D8%AA%D8%B5%D9%85%DB%8C%D9%85.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-22.pdf) |
| ۲۳ | [روش‌های گروهی](Part%205_Classification/23%20-%20%D8%B1%D9%88%D8%B4%E2%80%8C%D9%87%D8%A7%DB%8C%20%DA%AF%D8%B1%D9%88%D9%87%DB%8C.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-23.pdf) |
| ۲۴ | [ماشین بردار پشتیبان](Part%205_Classification/24%20-%20%20%D9%85%D8%A7%D8%B4%DB%8C%D9%86%20%D8%A8%D8%B1%D8%AF%D8%A7%D8%B1%20%D9%BE%D8%B4%D8%AA%DB%8C%D8%A8%D8%A7%D9%86.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-24.pdf) |
| ۲۵ | [ارزیابی مدل‌های طبقه‌بندی](Part%205_Classification/25%20-%20%D8%A7%D8%B1%D8%B2%DB%8C%D8%A7%D8%A8%DB%8C%20%D9%85%D8%AF%D9%84%E2%80%8C%D9%87%D8%A7%DB%8C%20%D8%B7%D8%A8%D9%82%D9%87%E2%80%8C%D8%A8%D9%86%D8%AF%DB%8C.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-25.pdf) |

<a id="part-6"></a>

## بخش ۶: یادگیری بدون نظارت — خوشه‌بندی (Clustering)

مبانی خوشه‌بندی و k-Means، خوشه‌بندی سلسله‌مراتبی، روش‌های چگالی‌محور (DBSCAN) و مبتنی بر مدل (GMM)، ارزیابی و تفسیر خوشه‌ها، و جمع‌بندی درس.

📁 پوشه: [Part 6_Clustering](Part%206_Clustering)

| جلسه | عنوان | دانلود PDF |
|:-:|--:|:-:|
| ۲۶ | [مبانی خوشه‌بندی و k-Means](Part%206_Clustering/26%20-%20%D9%85%D8%A8%D8%A7%D9%86%DB%8C%20%D8%AE%D9%88%D8%B4%D9%87%E2%80%8C%D8%A8%D9%86%D8%AF%DB%8C%20%D9%88%20k-Means.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-26.pdf) |
| ۲۷ | [خوشه‌بندی سلسله‌مراتبی](Part%206_Clustering/27%20-%20%D8%AE%D9%88%D8%B4%D9%87%E2%80%8C%D8%A8%D9%86%D8%AF%DB%8C%20%D8%B3%D9%84%D8%B3%D9%84%D9%87%E2%80%8C%D9%85%D8%B1%D8%A7%D8%AA%D8%A8%DB%8C.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-27.pdf) |
| ۲۸ | [خوشه‌بندی چگالی‌محور و مبتنی بر مدل](Part%206_Clustering/28%20-%20%D8%AE%D9%88%D8%B4%D9%87%E2%80%8C%D8%A8%D9%86%D8%AF%DB%8C%20%DA%86%DA%AF%D8%A7%D9%84%DB%8C%E2%80%8C%D9%85%D8%AD%D9%88%D8%B1%20%D9%88%20%D9%85%D8%A8%D8%AA%D9%86%DB%8C%20%D8%A8%D8%B1%20%D9%85%D8%AF%D9%84.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-28.pdf) |
| ۲۹ | [ارزیابی و تفسیر خوشه‌ها](Part%206_Clustering/29%20-%20%D8%A7%D8%B1%D8%B2%DB%8C%D8%A7%D8%A8%DB%8C%20%D9%88%20%D8%AA%D9%81%D8%B3%DB%8C%D8%B1%20%D8%AE%D9%88%D8%B4%D9%87%E2%80%8C%D9%87%D8%A7.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-29.pdf) |
| ۳۰ | [جمع‌بندی و ارائه پروژه‌ها](Part%206_Clustering/30%20-%20%D8%AC%D9%85%D8%B9%E2%80%8C%D8%A8%D9%86%D8%AF%DB%8C%20%D9%88%20%D8%A7%D8%B1%D8%A7%D8%A6%D9%87%20%D9%BE%D8%B1%D9%88%DA%98%D9%87%E2%80%8C%D9%87%D8%A7.md) | [PDF](https://haghbinh.github.io/DM_Course/pdf/session-30.pdf) |

---

## نحوه استفاده

- بهترین راه مطالعه، **وب‌سایت درس** است: [haghbinh.github.io/DM_Course](https://haghbinh.github.io/DM_Course/). بالای هر جلسه دکمه دانلود PDF همان جلسه و PDF همه جلسه‌ها قرار دارد.
- روی عنوان هر جلسه در جدول‌های بالا هم می‌توانید کلیک کنید تا جزوه مربوط در GitHub باز شود.
- برای بهترین نمایش (فرمول‌ها، Callout‌ها و پیوندهای داخلی)، مخزن را کلون کرده و پوشه را به‌عنوان یک Vault در **Obsidian** باز کنید:

```bash
git clone https://github.com/haghbinh/DM_Course.git
```

- تصاویر استفاده‌شده در جزوه‌ها در پوشه [img](img) قرار دارند.
- داده‌های درس (به‌جز داده‌هایی که از کتابخانه‌های پایتون مانند seaborn بارگذاری می‌شوند) در پوشه [data](data) قرار دارند. کدها آن‌ها را با مسیر نسبی `../data/...` می‌خوانند؛ پس جزوه یا دفترچه کارگاه را از داخل پوشه جلسه خودش اجرا کنید.

</div>
