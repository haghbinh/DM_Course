# جلسه ۲۰ — مبانی طبقه‌بندی و k-NN

## از رگرسیون به طبقه‌بندی

در چهار جلسه گذشته هدف ما پیش‌بینی یک **عدد** بود ← [مبانی یادگیری نظارت‌شده و رگرسیون خطی ساده](../Part%204_Regression/16%20-%20%D9%85%D8%A8%D8%A7%D9%86%DB%8C%20%DB%8C%D8%A7%D8%AF%DA%AF%DB%8C%D8%B1%DB%8C%20%D9%86%D8%B8%D8%A7%D8%B1%D8%AA%E2%80%8C%D8%B4%D8%AF%D9%87%20%D9%88%20%D8%B1%DA%AF%D8%B1%D8%B3%DB%8C%D9%88%D9%86%20%D8%AE%D8%B7%DB%8C%20%D8%B3%D8%A7%D8%AF%D9%87.md). اما بسیاری از پرسش‌های داده‌کاوی درباره **برچسب** هستند: این ایمیل هرزنامه است یا نه؟ این مشتری اشتراکش را لغو می‌کند؟ این مسافر تایتانیک زنده می‌ماند؟

در **طبقه‌بندی** (Classification) متغیر هدف **کیفی** است و مدل هر نمونه را به یکی از **کلاس‌های** از پیش تعریف‌شده نسبت می‌دهد. همه ابزارهایی که تا اینجا ساختیم (تقسیم داده، Pipeline، بیش‌برازش و اعتبارسنجی متقابل) در طبقه‌بندی هم به همان شکل به کار می‌روند ← [رگرسیون چندجمله‌ای، بیش‌برازش و اعتبارسنجی متقابل](../Part%204_Regression/18%20-%20%D8%B1%DA%AF%D8%B1%D8%B3%DB%8C%D9%88%D9%86%20%DA%86%D9%86%D8%AF%D8%AC%D9%85%D9%84%D9%87%E2%80%8C%D8%A7%DB%8C%D8%8C%20%D8%A8%DB%8C%D8%B4%E2%80%8C%D8%A8%D8%B1%D8%A7%D8%B2%D8%B4%20%D9%88%20%D8%A7%D8%B9%D8%AA%D8%A8%D8%A7%D8%B1%D8%B3%D9%86%D8%AC%DB%8C%20%D9%85%D8%AA%D9%82%D8%A7%D8%A8%D9%84.md)

این جلسه به سه پرسش پاسخ می‌دهد:

- مسئله طبقه‌بندی و **مرز تصمیم** چیست؟
- ساده‌ترین طبقه‌بند، یعنی **k-نزدیک‌ترین همسایه**، چگونه کار می‌کند و k را چگونه انتخاب کنیم؟
- چرا **مقیاس‌بندی** برای k-NN حیاتی است و این روش کجا ضعیف عمل می‌کند؟

---

## مسئله طبقه‌بندی

مجموعه آموزش شامل n زوج (بردار ویژگی، برچسب کلاس) است. هدف یادگیری تابعی است که هر بردار ویژگی را به یکی از K کلاس نگاشت دهد. بیشتر طبقه‌بندها **احتمال** هر کلاس را برآورد می‌کنند و کلاسی را برمی‌گزینند که بیشترین احتمال را دارد:

$$
\hat{y} = \arg\max_{k} \; P(y = C_k \mid x)
$$

| نوع مسئله | تعداد کلاس | مثال |
|:---:|:---:|:---:|
| طبقه‌بندی دودویی (Binary) | ۲ | زنده ماندن مسافر، هرزنامه یا عادی؛ یک کلاس «مثبت» (مورد توجه) است |
| طبقه‌بندی چندکلاسه (Multiclass) | بیشتر از ۲ | گونه گل زنبق، رقم دست‌نویس؛ هر نمونه دقیقاً یک کلاس |
| طبقه‌بندی چندبرچسبی (Multilabel) | چند برچسب هم‌زمان | برچسب‌های موضوعی یک مقاله (خارج از بحث این درس) |

طبقه‌بند فضای ویژگی‌ها را به **ناحیه‌هایی** تقسیم می‌کند که در هر کدام یک کلاس پیش‌بینی می‌شود؛ مرز میان ناحیه‌ها **مرز تصمیم** (Decision Boundary) است.

| نوع مرز | مدل‌های نمونه | ویژگی |
|:---:|:---:|:---:|
| خطی (ابرصفحه) | رگرسیون لجستیک، SVM خطی | ساده و کم‌واریانس؛ ممکن است کم‌برازش کند |
| محوری و پله‌ای | درخت تصمیم | خطوط موازی محورها |
| غیرخطی و نامنظم | الگوریتم k-NN، SVM با هسته RBF | انعطاف‌پذیر؛ ممکن است بیش‌برازش کند |

تا جلسه ۲۵ که معیارهای ارزیابی را کامل می‌بینیم، از **دقت** (Accuracy) استفاده می‌کنیم و همیشه آن را با **مدل پایه** «همیشه کلاس اکثریت» مقایسه می‌کنیم:

$$
\text{Accuracy} = \frac{\text{number of correct predictions}}{\text{total number of predictions}}
$$

> [!warning] دقت در داده نامتوازن گمراه‌کننده است
> اگر فقط ۱ درصد تراکنش‌ها تقلب باشد، مدلی که **همیشه** «عادی» بگوید دقت ۹۹ درصد دارد اما بی‌فایده است ← [ارزیابی مدل‌های طبقه‌بندی](25%20-%20%D8%A7%D8%B1%D8%B2%DB%8C%D8%A7%D8%A8%DB%8C%20%D9%85%D8%AF%D9%84%E2%80%8C%D9%87%D8%A7%DB%8C%20%D8%B7%D8%A8%D9%82%D9%87%E2%80%8C%D8%A8%D9%86%D8%AF%DB%8C.md)

---

## الگوریتم k-NN

برای طبقه‌بندی نقطه جدید q:

1. فاصله q را تا **همه** نقاط آموزش حساب کن (معمولاً اقلیدسی ← [معیارهای شباهت و فاصله](../Part%201_Data%20Understanding/%DB%B5%20-%20%D9%85%D8%B9%DB%8C%D8%A7%D8%B1%D9%87%D8%A7%DB%8C%20%D8%B4%D8%A8%D8%A7%D9%87%D8%AA%20%D9%88%20%D9%81%D8%A7%D8%B5%D9%84%D9%87.md)).
2. تعداد k نقطه با کمترین فاصله را انتخاب کن.
3. کلاسی را که میان این k همسایه **بیشترین رأی** را دارد، به q نسبت بده.

احتمال هر کلاس هم نسبت همسایه‌های آن کلاس است (N مجموعه k همسایه و I تابع نشانگر):

$$
\hat{P}(y = c \mid q) = \frac{1}{k} \sum_{i \in N_k(q)} I(y_i = c)
$$

در **رأی وزن‌دار** (`weights="distance"`) وزن هر همسایه عکس فاصله آن است تا همسایه‌های نزدیک‌تر اثر بیشتری داشته باشند:

$$
w_i = \frac{1}{d(q, x_i)}
$$

### مثال حل‌شده: k-NN با شش نقطه

شش نقطه آموزش با دو کلاس A و B داریم و نقطه جدید q با مختصات (۳، ۳) را طبقه‌بندی می‌کنیم.

#### گام ۱ — فاصله تا همه نقاط

| نقطه | ویژگی x1 | ویژگی x2 | کلاس | فاصله اقلیدسی تا q | رتبه |
|:---:|:---:|:---:|:---:|:---:|:---:|
| ۱ | 3 | 4 | B | √1 = 1.000 | ۱ |
| ۲ | 1 | 3 | A | √4 = 2.000 | ۲ |
| ۳ | 4 | 1 | A | √5 ≈ 2.236 | ۳ |
| ۴ | 5 | 5 | B | √8 ≈ 2.828 | ۴ |
| ۵ | 6 | 3 | B | √9 = 3.000 | ۵ |
| ۶ | 1 | 0 | A | √13 ≈ 3.606 | ۶ |

برای نمونه، فاصله نقطه ۳ تا q:

$$
d = \sqrt{(4 - 3)^2 + (1 - 3)^2} = \sqrt{1 + 4} = \sqrt{5} \approx 2.236
$$

#### گام ۲ — رأی ساده برای چند k

| مقدار k | همسایه‌ها | رأی‌ها | پیش‌بینی | احتمال کلاس B |
|:---:|:---:|:---:|:---:|:---:|
| ۱ | نقطه ۱ | یک رأی B | **B** | 1.000 |
| ۳ | نقاط ۱، ۲ و ۳ | دو رأی A، یک رأی B | **A** | 0.333 |
| ۵ | نقاط ۱ تا ۵ | دو رأی A، سه رأی B | **B** | 0.600 |

#### گام ۳ — رأی وزن‌دار با k برابر ۳

وزن‌ها: نقطه ۱ (B) برابر ۱، نقطه ۲ (A) برابر ۰.۵ و نقطه ۳ (A) برابر ۱ تقسیم بر ۲.۲۳۶ یعنی حدود ۰.۴۴۷:

$$
\text{score}(A) = 0.5 + 0.447 = 0.947, \qquad \text{score}(B) = 1.000, \qquad P(B) = \frac{1}{1.947} \approx 0.514
$$

> [!note] بررسی
> پیش‌بینی با تغییر k **عوض می‌شود** (B، A، B)؛ پس انتخاب k بخش مهمی از ساخت مدل است. با رأی وزن‌دار، همسایه بسیار نزدیک B دو همسایه دورتر A را خنثی کرد. در مسئله دودویی k را **فرد** بگیرید تا رأی مساوی پیش نیاید.

کلاس `KNeighborsClassifier` همین اعداد را می‌دهد:

```python
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# 1. Six training points with two classes, and the new point q = (3, 3)
points = pd.DataFrame({"x1": [3, 1, 4, 5, 6, 1],
                       "x2": [4, 3, 1, 5, 3, 0],
                       "label": ["B", "A", "A", "B", "B", "A"]})
X, y = points[["x1", "x2"]], points["label"]
q = pd.DataFrame({"x1": [3], "x2": [3]})

# 2. Simple majority vote for k = 1, 3, 5
for k in [1, 3, 5]:
    knn = KNeighborsClassifier(n_neighbors=k).fit(X, y)
    print(f"k={k}  prediction={knn.predict(q)[0]}  P(B)={knn.predict_proba(q)[0, 1]:.3f}")

# 3. Distance-weighted vote with k = 3
knn_w = KNeighborsClassifier(n_neighbors=3, weights="distance").fit(X, y)
print(f"weighted k=3  prediction={knn_w.predict(q)[0]}  P(B)={knn_w.predict_proba(q)[0, 1]:.3f}")

# 4. Distances and indices of the 3 nearest neighbours (index 0 = point 1)
dist, idx = knn.kneighbors(q, n_neighbors=3)
print(f"neighbours={idx[0] + 1}  distances={dist[0].round(3)}")
```

```
k=1  prediction=B  P(B)=1.000
k=3  prediction=A  P(B)=0.333
k=5  prediction=B  P(B)=0.600
weighted k=3  prediction=B  P(B)=0.514
neighbours=[1 2 3]  distances=[1.    2.    2.236]
```

---

## نقش مقیاس‌بندی

الگوریتم k-NN کاملاً بر پایه **فاصله** است؛ ویژگی با دامنه عددی بزرگ‌تر فاصله را کنترل می‌کند و بقیه ویژگی‌ها عملاً نادیده گرفته می‌شوند.

> [!example] مثال — سن و درآمد
> مشتری جدید ۳۰ ساله با درآمد ۲۰٬۰۰۰ (هزار تومان) را با دو مشتری قبلی مقایسه می‌کنیم: مشتری ۱ (۳۲ ساله، درآمد ۵۰٬۰۰۰، «خرید») و مشتری ۲ (۶۰ ساله، درآمد ۲۲٬۰۰۰، «عدم خرید»).
> $$
> d(q, 1) = \sqrt{2^2 + 30000^2} \approx 30000.0, \qquad d(q, 2) = \sqrt{30^2 + 2000^2} \approx 2000.2
> $$
> بدون مقیاس‌بندی، مشتری ۲ با ۳۰ سال اختلاف سن «نزدیک‌تر» است. با مقیاس‌بندی Min-Max (سن ۲۰ تا ۶۰، درآمد ۱۰٬۰۰۰ تا ۶۰٬۰۰۰)، فاصله‌ها ۰.۶۰۲ و ۰.۷۵۱ می‌شوند و پیش‌بینی 1-NN از «عدم خرید» به «خرید» تغییر می‌کند.

```python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

# 1. Two known customers and a new one (income in thousand tomans)
customers = pd.DataFrame({"age": [32, 60], "income": [50000, 22000], "label": ["buy", "no buy"]})
new = pd.DataFrame({"age": [30], "income": [20000]})
X, y = customers[["age", "income"]], customers["label"]

# 2. Without scaling: income dominates the distance
knn = KNeighborsClassifier(n_neighbors=1).fit(X, y)
print(f"raw:    distances={knn.kneighbors(new, 2)[0][0].round(1)}  prediction={knn.predict(new)[0]}")

# 3. Min-Max scaling with fixed ranges (age 20-60, income 10,000-60,000)
scaler = MinMaxScaler().fit(pd.DataFrame({"age": [20, 60], "income": [10000, 60000]}))
knn_s = KNeighborsClassifier(n_neighbors=1).fit(scaler.transform(X), y)
d = knn_s.kneighbors(scaler.transform(new), 2)[0][0]
print(f"scaled: distances={d.round(3)}  prediction={knn_s.predict(scaler.transform(new))[0]}")
```

```
raw:    distances=[ 2000.2 30000. ]  prediction=no buy
scaled: distances=[0.602 0.751]  prediction=buy
```

### داده واقعی: تایتانیک

داده تایتانیک (۸۹۱ مسافر) را از جلسات پیش‌پردازش می‌شناسیم. در جلسات ۲۰ تا ۲۵ همین داده را با تنظیمات **یکسان** به کار می‌بریم تا مدل‌ها قابل مقایسه باشند:

- هدف: `survived` (زنده ماندن، کلاس مثبت ۱).
- ویژگی‌های عددی: سن، کرایه، تعداد همسر و خواهر و برادر، تعداد والدین و فرزندان، کلاس سفر؛ ویژگی‌های کیفی: جنسیت و بندر سوار شدن.
- تقسیم **طبقه‌بندی‌شده** با ۲۰ درصد آزمون و `random_state=42` ← [طراحی آزمایش و Pipeline](../Part%203_Data%20Preprocessing/%DB%B1%DB%B5%20-%20%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C%20%D8%A2%D8%B2%D9%85%D8%A7%DB%8C%D8%B4%20%D9%88%20Pipeline.md)
- پیش‌پردازش داخل Pipeline: جایگذاری میانه و استانداردسازی برای ستون‌های عددی، جایگذاری مد و One-Hot برای ستون‌های کیفی. همه این گام‌ها **یادگیرنده**‌اند و فقط روی داده آموزش `fit` می‌شوند.
- اعتبارسنجی متقابل **طبقه‌بندی‌شده** پنج بخشی (`StratifiedKFold`) تا نسبت زنده‌ماندگان در هر بخش حفظ شود.

```python
import seaborn as sns
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.dummy import DummyClassifier

# 1. Titanic: predict survival; the test set is locked (stratified split)
titanic = sns.load_dataset("titanic")
num = ["age", "fare", "sibsp", "parch", "pclass"]
cat = ["sex", "embarked"]
X_train, X_test, y_train, y_test = train_test_split(titanic[num + cat], titanic["survived"],
                                                    test_size=0.2, stratify=titanic["survived"],
                                                    random_state=42)
print(f"train={len(X_train)}  test={len(X_test)}  survival rate={y_train.mean():.3f}")

# 2. Preprocessing with or without standardization of the numeric columns
def preprocess(scale):
    num_steps = [SimpleImputer(strategy="median")] + ([StandardScaler()] if scale else [])
    return ColumnTransformer([
        ("num", make_pipeline(*num_steps), num),
        ("cat", make_pipeline(SimpleImputer(strategy="most_frequent"),
                              OneHotEncoder(handle_unknown="ignore")), cat)])

# 3. Stratified 5-fold CV accuracy: baseline, k-NN without and with scaling
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
models = {"Baseline (majority class)": DummyClassifier(strategy="most_frequent"),
          "5-NN, no scaling": make_pipeline(preprocess(False), KNeighborsClassifier(5)),
          "5-NN, standardized": make_pipeline(preprocess(True), KNeighborsClassifier(5))}
for name, model in models.items():
    acc = cross_val_score(model, X_train, y_train, cv=cv, scoring="accuracy")
    print(f"{name:26s} CV accuracy={acc.mean():.3f}")
```

```
train=712  test=179  survival rate=0.383
Baseline (majority class)  CV accuracy=0.617
5-NN, no scaling           CV accuracy=0.706
5-NN, standardized         CV accuracy=0.798
```

مدل پایه دقت ۰.۶۱۷ دارد (نسبت جان‌باختگان). بدون مقیاس‌بندی، کرایه (تا ۵۱۲ پوند) بر فاصله مسلط است و دقت فقط ۰.۷۰۶ است؛ با استانداردسازی به ۰.۷۹۸ می‌رسد: حدود **۹ واحد درصد** بهبود فقط با یک گام پیش‌پردازش.

> [!tip] ویژگی‌های کیفی و معیار فاصله
> ویژگی‌های کیفی ابتدا One-Hot می‌شوند ← [تبدیل و یکپارچه‌سازی داده](../Part%203_Data%20Preprocessing/%DB%B1%DB%B2%20-%20%D8%AA%D8%A8%D8%AF%DB%8C%D9%84%20%D9%88%20%DB%8C%DA%A9%D9%BE%D8%A7%D8%B1%DA%86%D9%87%E2%80%8C%D8%B3%D8%A7%D8%B2%DB%8C%20%D8%AF%D8%A7%D8%AF%D9%87.md). معیار فاصله را متناسب با داده انتخاب کنید: اقلیدسی (پیش‌فرض، `p=2`) برای ویژگی‌های عددی هم‌مقیاس، منهتن (`p=1`) با حساسیت کمتر به اختلاف بزرگ در یک ویژگی، کسینوسی برای متن و همینگ برای ویژگی‌های دودویی.

---

## انتخاب k

| مقدار k | مرز تصمیم | بایاس | واریانس | خطر |
|:---:|:---:|:---:|:---:|:---:|
| برابر ۱ | بسیار نامنظم، جزیره‌های کوچک دور نقاط پرت | کم | زیاد | بیش‌برازش؛ دقت آموزش تقریباً ۱۰۰ درصد |
| متوسط | هموارتر | متوسط | متوسط | — |
| بسیار بزرگ (نزدیک n) | تقریباً ثابت: همیشه کلاس اکثریت | زیاد | کم | کم‌برازش |

پیچیدگی k-NN با افزایش k **کم** می‌شود؛ برعکس درجه چندجمله‌ای. کد زیر مرز تصمیم را روی یک داده شبیه‌سازی‌شده دوبعدی (دو نیم‌ماه درهم با نویز) برای سه مقدار k رسم می‌کند:

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# 1. Two interleaving half-moons with noise (a simulated two-class problem)
X, y = make_moons(n_samples=300, noise=0.3, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

# 2. A grid covering the plane, to colour each region by its predicted class
xx, yy = np.meshgrid(np.linspace(-2, 3, 300), np.linspace(-1.5, 2, 300))
grid = np.c_[xx.ravel(), yy.ravel()]

fig, axes = plt.subplots(1, 3, figsize=(15, 4.2), sharey=True)
for ax, k in zip(axes, [1, 15, 150]):
    knn = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    print(f"k={k:3d}  train accuracy={knn.score(X_train, y_train):.3f}  test accuracy={knn.score(X_test, y_test):.3f}")
    ax.contourf(xx, yy, knn.predict(grid).reshape(xx.shape), alpha=0.3, cmap="coolwarm")
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap="coolwarm", edgecolor="k", s=20)
    ax.set(title=f"k = {k}", xlabel="x1")
axes[0].set_ylabel("x2")
plt.show()
```

```
k=  1  train accuracy=1.000  test accuracy=0.878
k= 15  train accuracy=0.895  test accuracy=0.889
k=150  train accuracy=0.795  test accuracy=0.778
```

![moons knn boundaries](../img/moons_knn_boundaries.png)

با k برابر ۱ دقت آموزش ۱۰۰ درصد است (هر نقطه نزدیک‌ترین همسایه خودش است) و مرز دور نقاط پرت جزیره می‌سازد. با k برابر ۱۵ مرز هموار و دقت آزمون بهترین است (۰.۸۸۹). با k برابر ۱۵۰ (نیمی از داده) مرز تقریباً خط راست است و هر دو دقت افت می‌کنند (کم‌برازش).

روی تایتانیک، k و نوع رأی را با **جست‌وجوی شبکه‌ای** (`GridSearchCV`) و اعتبارسنجی متقابل انتخاب می‌کنیم. این کلاس همه ترکیب‌ها را می‌آزماید، بهترین را برمی‌گزیند و آن را روی کل داده آموزش دوباره آموزش می‌دهد:

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier

# 1. Same Titanic data, split and preprocessing as before
titanic = sns.load_dataset("titanic")
num = ["age", "fare", "sibsp", "parch", "pclass"]
cat = ["sex", "embarked"]
X_train, X_test, y_train, y_test = train_test_split(titanic[num + cat], titanic["survived"],
                                                    test_size=0.2, stratify=titanic["survived"],
                                                    random_state=42)
preprocess = ColumnTransformer([
    ("num", make_pipeline(SimpleImputer(strategy="median"), StandardScaler()), num),
    ("cat", make_pipeline(SimpleImputer(strategy="most_frequent"),
                          OneHotEncoder(handle_unknown="ignore")), cat)])
model = make_pipeline(preprocess, KNeighborsClassifier())

# 2. Grid search over k (odd values) and the voting rule, with stratified 5-fold CV
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
grid = {"kneighborsclassifier__n_neighbors": range(1, 102, 2),
        "kneighborsclassifier__weights": ["uniform", "distance"]}
gs = GridSearchCV(model, grid, cv=cv, scoring="accuracy", return_train_score=True)
gs.fit(X_train, y_train)
print(f"best={gs.best_params_}  CV accuracy={gs.best_score_:.3f}")

# 3. Validation curve for the uniform vote
res = gs.cv_results_
mask = np.array(res["param_kneighborsclassifier__weights"]) == "uniform"
ks = np.array(res["param_kneighborsclassifier__n_neighbors"])[mask].astype(int)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(ks, res["mean_train_score"][mask], "o-", ms=3, label="Training")
ax.plot(ks, res["mean_test_score"][mask], "s-", ms=3, label="Validation (5-fold CV)")
ax.set(xlabel="k (number of neighbours)", ylabel="Accuracy", title="k-NN on Titanic")
ax.legend()
plt.show()

# 4. The best model is refitted on the whole training set; test set used once
print(f"test accuracy={gs.score(X_test, y_test):.3f}")
```

```
best={'kneighborsclassifier__n_neighbors': 17, 'kneighborsclassifier__weights': 'uniform'}  CV accuracy=0.826
test accuracy=0.810
```

![titanic knn validation curve](../img/titanic_knn_validation_curve.png)

با k برابر ۱ دقت آموزش ۰.۹۸ ولی دقت اعتبارسنجی فقط ۰.۷۵ است (بیش‌برازش). بهترین مقدار k برابر **۱۷** با دقت اعتبارسنجی ۰.۸۲۶ است و پس از آن هر دو منحنی به‌تدریج پایین می‌آیند (کم‌برازش). دقت آزمون مدل منتخب ۰.۸۱۰ است، در برابر ۰.۶۱۷ مدل پایه.

> [!important] قاعده
> دقت آموزش k-NN با k کوچک هیچ اطلاعاتی درباره عملکرد واقعی نمی‌دهد. k را **فقط** با اعتبارسنجی متقابل انتخاب کنید؛ مقدار اولیه حدود جذر n پیشنهاد خوبی برای شروع جست‌وجوست.

---

## یادگیری تنبل و نفرین ابعاد

الگوریتم k-NN در آموزش **هیچ کاری** جز ذخیره داده نمی‌کند و همه محاسبات را به زمان پیش‌بینی موکول می‌کند؛ به آن **یادگیری تنبل** (Lazy Learning) می‌گویند.

| جنبه | یادگیری تنبل (k-NN) | یادگیری مشتاق (رگرسیون لجستیک، درخت) |
|:---:|:---:|:---:|
| آموزش | فقط ذخیره داده؛ تقریباً آنی | ساخت مدل؛ ممکن است زمان‌بر باشد |
| پیش‌بینی | کند: فاصله تا همه نقاط، از مرتبه n ضرب در p برای هر نقطه | سریع: اعمال یک فرمول یا پیمایش درخت |
| حافظه | نگهداری **کل** داده آموزش | فقط پارامترهای مدل |
| افزودن داده جدید | فوری | نیاز به آموزش مجدد |

ساختارهایی مانند **KD-Tree** و **Ball-Tree** جست‌وجوی همسایه را در ابعاد کم سریع می‌کنند (`algorithm="auto"` خودکار انتخاب می‌کند).

در ابعاد بالا فاصله‌ها **معنای خود را از دست می‌دهند**: فاصله نزدیک‌ترین و دورترین نقطه تقریباً برابر می‌شود (**نفرین ابعاد** ← [مهندسی و انتخاب ویژگی](../Part%203_Data%20Preprocessing/%DB%B1%DB%B3%20-%20%D9%85%D9%87%D9%86%D8%AF%D8%B3%DB%8C%20%D9%88%20%D8%A7%D9%86%D8%AA%D8%AE%D8%A7%D8%A8%20%D9%88%DB%8C%DA%98%DA%AF%DB%8C.md)). کد زیر ۵۰۰ نقطه تصادفی در مکعب واحد می‌سازد و نسبت دورترین به نزدیک‌ترین فاصله از نقطه اول را حساب می‌کند:

```python
import numpy as np
from sklearn.metrics import pairwise_distances

# Ratio of farthest to nearest distance from one point to 499 random points in a unit cube
rng = np.random.default_rng(42)
for p in [2, 10, 100, 1000]:
    X = rng.uniform(size=(500, p))
    d = pairwise_distances(X[:1], X[1:])[0]
    print(f"dimensions={p:4d}  farthest/nearest={d.max() / d.min():.2f}")
```

```
dimensions=   2  farthest/nearest=46.78
dimensions=  10  farthest/nearest=3.20
dimensions= 100  farthest/nearest=1.41
dimensions=1000  farthest/nearest=1.10
```

در ۱۰۰۰ بعد، دورترین نقطه فقط ۱۰ درصد دورتر از نزدیک‌ترین است. پس پیش از k-NN در داده با ابعاد بالا، **انتخاب ویژگی** یا **کاهش ابعاد** لازم است ← [کاهش ابعاد](../Part%203_Data%20Preprocessing/%DB%B1%DB%B4-%20%DA%A9%D8%A7%D9%87%D8%B4%20%D8%A7%D8%A8%D8%B9%D8%A7%D8%AF.md)

| مزایا | معایب |
|:---:|:---:|
| بسیار ساده و قابل فهم | پیش‌بینی کند برای داده بزرگ |
| بدون فرض درباره شکل توزیع (ناپارامتری) | نگهداری کل داده آموزش |
| مرز تصمیم انعطاف‌پذیر و ذاتاً چندکلاسه | حساس به مقیاس و ویژگی‌های بی‌ربط |
| قابل استفاده برای رگرسیون ← [منظم‌سازی در رگرسیون](../Part%204_Regression/19%20-%20%D9%85%D9%86%D8%B8%D9%85%E2%80%8C%D8%B3%D8%A7%D8%B2%DB%8C%20%D8%AF%D8%B1%20%D8%B1%DA%AF%D8%B1%D8%B3%DB%8C%D9%88%D9%86.md) | ضعیف در ابعاد بالا؛ بدون مدل قابل تفسیر |

> [!note] کارگاه عملی
> دفترچه «۲۰ - کارگاه مبانی طبقه‌بندی و k-NN» مقایسه معیارهای فاصله و تمرین عملی کلاس (طبقه‌بندی گل زنبق با k-NN و رسم مرز تصمیم) را با پاسخ دارد. نحوه نوشتن این کدها در امتحان پرسیده نمی‌شود.

---

## خطاهای رایج

| خطا | چرا نادرست است | روش درست |
|:---:|:---:|:---:|
| اجرای k-NN بدون مقیاس‌بندی | ویژگی با دامنه بزرگ‌تر فاصله را کنترل می‌کند | استانداردسازی داخل Pipeline |
| انتخاب k با دقت آموزش | با k برابر ۱ دقت آموزش تقریباً ۱۰۰ درصد است | انتخاب k با اعتبارسنجی متقابل |
| گزارش دقت بدون مدل پایه | دقت ۷۰ درصد وقتی کلاس اکثریت ۶۲ درصد است چندان خوب نیست | مقایسه با DummyClassifier |
| تقسیم ساده در داده نامتوازن | نسبت کلاس‌ها در آموزش، آزمون و بخش‌ها به هم می‌خورد | تقسیم و اعتبارسنجی طبقه‌بندی‌شده |
| مقدار k زوج در مسئله دودویی | رأی مساوی پیش می‌آید | مقدار k فرد یا رأی وزن‌دار |
| ورود صدها ویژگی بی‌ربط به k-NN | نفرین ابعاد؛ فاصله‌ها بی‌معنا می‌شوند | انتخاب ویژگی یا کاهش ابعاد |

---

## نمونه سؤال‌های امتحانی

### سؤال‌های مفهومی

> [!question]- ۱. تفاوت طبقه‌بندی دودویی، چندکلاسه و چندبرچسبی چیست؟ برای هر کدام مثالی بزنید.
> در دودویی دو کلاس داریم (زنده ماندن یا نماندن). در چندکلاسه بیش از دو کلاس داریم و هر نمونه دقیقاً یک کلاس دارد (گونه گل). در چندبرچسبی هر نمونه می‌تواند هم‌زمان چند برچسب داشته باشد (فیلمی هم «کمدی» و هم «عاشقانه»).

> [!question]- ۲. چرا k-NN با k برابر ۱ روی داده آموزش تقریباً دقت ۱۰۰ درصد دارد؟ این عدد چه چیزی را نشان می‌دهد؟
> چون هر نقطه آموزش نزدیک‌ترین همسایه خودش است (با فاصله صفر). این عدد فقط نشان می‌دهد مدل داده آموزش را **حفظ** کرده و درباره تعمیم اطلاعاتی نمی‌دهد. استثنا، نقاط تکراری با برچسب متفاوت است.

> [!question]- ۳. چرا مقیاس‌بندی برای k-NN حیاتی اما برای درخت تصمیم بی‌اهمیت است؟
> الگوریتم k-NN بر پایه فاصله است و ویژگی با دامنه بزرگ‌تر فاصله را کنترل می‌کند. درخت تصمیم هر ویژگی را **جداگانه** با یک آستانه مقایسه می‌کند؛ تغییر مقیاس فقط مقدار آستانه را عوض می‌کند.

> [!question]- ۴. چرا k-NN «یادگیرنده تنبل» نامیده می‌شود؟ یک مزیت و یک عیب آن را بگویید.
> چون در آموزش مدلی نمی‌سازد و فقط داده را ذخیره می‌کند. مزیت: افزودن داده جدید فوری است. عیب: پیش‌بینی برای داده بزرگ کند است و کل داده باید در حافظه بماند.

> [!question]- ۵. داده‌ای با ۵۰۰ ویژگی دارید که فقط ۱۰ ویژگی آن مرتبط است. آیا k-NN مناسب است؟
> به‌تنهایی خیر. ۴۹۰ ویژگی بی‌ربط در فاصله سهم دارند و نویز آن‌ها فاصله‌ها را بی‌معنا می‌کند (نفرین ابعاد). پیش از k-NN باید **انتخاب ویژگی** یا **کاهش ابعاد** انجام داد.

### سؤال‌های محاسباتی

> [!question]- ۶. در مثال شش نقطه، اگر نقطه جدید (۵، ۳) باشد، پیش‌بینی 1-NN و 3-NN چیست؟
> فاصله‌ها تا (۵، ۳): نقطه ۵ برابر ۱ (B)، نقطه ۴ برابر ۲ (B)، نقطه ۱ و نقطه ۳ هر دو برابر جذر ۵ یعنی حدود ۲.۲۴ (B و A). پیش‌بینی 1-NN کلاس **B** است. برای 3-NN دو همسایه اول B هستند، پس صرف‌نظر از همسایه سوم، اکثریت با **B** است.

> [!question]- ۷. در همان مثال با نقطه جدید (۳، ۳) و k برابر ۵، رأی وزن‌دار چه پیش‌بینی می‌کند؟
> وزن‌ها: نقطه ۱ (B) برابر ۱، نقطه ۲ (A) برابر ۰.۵، نقطه ۳ (A) حدود ۰.۴۴۷، نقطه ۴ (B) برابر ۱ تقسیم بر ۲.۸۲۸ یعنی حدود ۰.۳۵۴ و نقطه ۵ (B) برابر ۱ تقسیم بر ۳ یعنی حدود ۰.۳۳۳.
> $$
> \text{score}(A) = 0.5 + 0.447 = 0.947, \qquad \text{score}(B) = 1 + 0.354 + 0.333 = 1.687
> $$
> پیش‌بینی **B** است.

> [!question]- ۸. داده‌ای ۱۰۰۰ نمونه دارد که ۹۰۰ تای آن کلاس منفی است. مدلی دقت ۸۸ درصد دارد. آیا مدل خوبی است؟
> خیر. مدل پایه «همیشه منفی» دقت ۹۰۰ تقسیم بر ۱۰۰۰، یعنی **۹۰ درصد** دارد؛ این مدل حتی از مدل پایه بدتر است.

### سؤال‌های خواندن کد

> [!question]- ۹. ایراد این کد چیست؟
> ```python
> model = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)
> ```
> اگر ستون‌ها مقیاس‌های متفاوت دارند (مثلاً سن و کرایه)، ویژگی با دامنه بزرگ‌تر فاصله را کنترل می‌کند. باید `make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))` نوشت.

> [!question]- ۱۰. خروجی `knn.predict_proba(q)` برای یک مدل با k برابر ۵ و دو کلاس چه مقادیری می‌تواند داشته باشد؟
> هر احتمال نسبت همسایه‌های آن کلاس است؛ پس فقط مقادیر ۰، ۰.۲، ۰.۴، ۰.۶، ۰.۸ و ۱ ممکن است (با رأی ساده) و مجموع دو احتمال ۱ است.

> [!question]- ۱۱. در `GridSearchCV` با شبکه زیر و `cv=5`، مدل چند بار آموزش می‌بیند؟
> ```python
> grid = {"kneighborsclassifier__n_neighbors": range(1, 102, 2),
>         "kneighborsclassifier__weights": ["uniform", "distance"]}
> ```
> تعداد مقادیر k برابر ۵۱ و دو نوع رأی، یعنی ۱۰۲ ترکیب؛ هر ترکیب ۵ بار، یعنی **۵۱۰** بار، و یک بار دیگر برای آموزش بهترین مدل روی کل داده آموزش.

---

## نکات کلیدی

> [!summary] خلاصه جلسه
> - در **طبقه‌بندی** متغیر هدف کیفی است؛ مسئله **دودویی** یا **چندکلاسه** است و طبقه‌بند فضای ویژگی را با **مرز تصمیم** تقسیم می‌کند.
> - الگوریتم **k-NN**: فاصله تا همه نقاط آموزش، انتخاب k نزدیک‌ترین و رأی اکثریت؛ با **رأی وزن‌دار** همسایه‌های نزدیک‌تر اثر بیشتری دارند.
> - مقدار **k** پیچیدگی را کنترل می‌کند: k کوچک بیش‌برازش و k بزرگ کم‌برازش. روی تایتانیک بهترین k برابر ۱۷ با دقت آزمون ۰.۸۱۰ (در برابر ۰.۶۱۷ مدل پایه) بود.
> - **مقیاس‌بندی** برای k-NN حیاتی است؛ روی تایتانیک دقت را از ۰.۷۰۶ به ۰.۷۹۸ رساند.
> - الگوریتم k-NN **یادگیرنده تنبل** است و در **ابعاد بالا** به دلیل تمرکز فاصله‌ها ضعیف عمل می‌کند.
