# _Dataset White Wine Quality_
## Domain Proyek (_Project Domain_)
**Latar Belakang**
_Wine_ adalah salah satu minuman populer di dunia. Industri ini merupakan sektor bisnis yang signifikan. Pasar _wine_ yang paling besar terdapat di Eropa, seperti Portugal, Italia, dan Prancis karena mereka memiliki konsumsi per kapita tertinggi di atas 35 liter/orang/tahun. Konsumsi _wine_ yang semakin meningkat beriringan dengan perlunya industri menghasilkan wine berkualitas baik. Saat ini, pengusaha dapat melihat konsumsi wine di berbagai kesempatan, salah satunya wine yang terkenal adalah _white wine_. Tetapi, melakukan analisis kualitas _wine_ berdasarkan bahan kimia atau bahan lainnya menjadi sangat sulit karena masih kurangnya alat teknis [[1]](https://www.sciencedirect.com/science/article/abs/pii/S221478532101316X). Dengan kata lain, proses _testing wine_ secara manual membutuhkan investasi waktu dan uang.
Selain itu, produksi _white wine_ juga terdiri dari beberapa proses yang kompleks. Untuk mendapatkan _white wine_ yang berkualitas baik, pengujian _white wine_ termasuk dalam tahap akhir produksi [[2]](https://www.scirp.org/journal/paperinformation?paperid=107796). _The Wine & Spirit Education Trust_ (WSET) melakukan evaluasi wine dengan berbagai aspek, seperti tampilan _wine_, aroma _wine_, kandungan oksigen di dalamnya, dan yang terakhir adalah rasa _wine_ [[3]](https://www.researchgate.net/publication/369869028_White_Wine_Quality_Prediction_and_Analysis_with_Machine_Learning_Techniques). Jika kualitasnya tidak bagus, maka semua prosedur harus diimplementasikan kembali dari awal, dan tentunya ini sangat mahal. Selain itu, mengidentifikasi kualitas _wine_ berdasarkan selera seseorang (secara manual) sangat menantang dan cenderung bias mengingat selera setiap orang berbeda-beda.

_Quality wine process_ atau _wine tasting process_ yang panjang dan rumit sangat memakan waktu. Jika proses ini digunakan secara luas, maka akan sangat sulit dan membuang banyak sumber daya. Dengan perkembangan teknologi, mengontrol kualitas _wine_ selama produksi dengan menggunakan berbagai parameter bahan kimia/bahan spesifik dapat menghemat banyak sumber daya dan waktu. Implementasi proyek ini memberi manfaat bagi industri _wine_ tentang aspek spesifik apa saja yang memengaruhi kualitas _wine_ dan aspek apa yang memiliki pengaruh kecil sehingga pengusaha dapat menghemat waktu dalam proses akhir produksi _wine_.

## Pemahaman Bisnis (_Business Understanding_)
**Pernyataan Masalah (_Problem Statements_)**: 
* Bagaimana pelaksanaan _wine quality process_ dapat lebih singkat agar dapat menghemat waktu dan sumber daya (uang dan tenaga)?
* Apa model terbaik yang bisa diterapkan untuk memprediksi kualitas _wine_ pada _dataset_ yang tersedia?

**Tujuan (_Goals_)**:
Dalam rangka meningkatkan kualitas produksi _white wine_, penelitian ini bertujuan untuk:
* Memilih fitur bahan dan karakteristik kimia yang berpengaruh terhadap kualitas _white wine_. Fitur yang tidak perlu dapat menghemat proses _quality wine_.
* Mengembangkan dan menentukan model terbaik untuk memprediksi kualitas _wine_ berdasarkan fitur dan jumlah _dataset_.

**Pernyataan Solusi (_Solution Statements_)**:
* Menguji _dataset_ dengan 3 algoritma yaitu _logistic regression_, SVM, dan _random forest classifier_ kemudian menentukan algoritma mana yang memiliki hasil terbaik.
* Metrik yang digunakan adalah ROC dan AUC. Metrik ini lebih cocok digunakan untuk _dataset_ kualitas _white wine_ yang memiliki jumlah _dataset_ yang tidak seimbang.

## Pemahaman Data (_Data Understanding_)
_Dataset_ yang digunakan adalah _Wine Quality_ dari [UCI Datasets](https://archive.ics.uci.edu/dataset/186/wine+quality). _Dataset white wine quality_ memiliki karakteristik multivariat yang berisi 4898 _instances_ dan 11 fitur untuk tipe _real_ dan 1 fitur dengan tipe objek.

**_Dataset white wine_ memiliki 12 atribut sebagai berikut**:
* _fixed_acidity_: keasaman yang tetap berada dalam cairan saat direbus, tidak mudah menguap.
* _volatile_acidity_: ukuran asam gas _wine_ yang menyebabkan bau dan rasa cuka.
* _citric_acid_: asam pelengkap dengan rasa tertentu untuk meningkatkan kesegaran dan keasaman _wine_ selama proses fermentasi.
* _residual_sugar_: jumlah gula yang tersisa setelah fermentasi berakhir.
* _chlorides_: jumlah garam dalam _wine_ (menambah rasa asin).
* _free_sulfur_dioxide_: berfungsi untuk mencegah oksidasi _wine_ dan pertumbuhan mikroba.
* _total_sulfur_dioxide_: jumlah SO2 yang bebas di dalam _wine_ ditambah dengan bagian yang terikat.
* _density_: massa per satuan volume _wine_ yang menentukan tingkat alkohol pada _final wine_.
* pH: tingkat keasaman.
* _sulphates_: bertindak sebagai bantuan untuk melindungi _wine_ dari potensi oksidasi atau paparan bakteri dalam _wine_.
* _alchohol_: jumlah konsentrat alkohol dalam _wine_.
* _quality_: kualitas _wine_.

Berikut Gambar 3 menunjukkan hasil pengecekan _null values_ pada _dataset white wine quality_. Berdasarkan Gambar 3, semua data terisi dengan lengkap.
![null values](https://github.com/tanaths/dicoding/blob/main/Submission_Belajar_Machine_Learning_Terapan/Submission_1/graph/data_is_null.png "Checking null values")

**Langkah-langkah memahami data**:
Untuk memahami data lebih lanjut, EDA (_Exploratory Data Analysis)_ terdiri atas sejumlah langkah:
* Memeriksa gambaran besar dari kumpulan data (deskripsi kumpulan data, informasi tipe data, dan bentuk data atau _shape_). Gambar 1 menunjukkan deskripsi data _white wine quality_.
![data description](https://github.com/tanaths/dicoding/blob/main/Submission_Belajar_Machine_Learning_Terapan/Submission_1/graph/data_description.png "Description of data")
Gambar 2 menunjukkan bentuk atau _shape_ dari _dataset_. _Dataset_ terdiri dari 4898 baris dan 12 kolom.
![data shape](https://github.com/tanaths/dicoding/blob/main/Submission_Belajar_Machine_Learning_Terapan/Submission_1/graph/shape.png "Shape of data")
Gambar 3 menunjukkan tipe data. Terdapat 11 fitur memiliki tipe data "float" sebagai fitur masukan dan 1 fitur target memiliki tipe data "object".
![data types](https://github.com/tanaths/dicoding/blob/main/Submission_Belajar_Machine_Learning_Terapan/Submission_1/graph/datatypes.png, "Data types")
* Memeriksa nilai _null_. Berdasarkan Gambar 4, semua data terisi dengan lengkap.
![null values](https://github.com/tanaths/dicoding/blob/main/Submission_Belajar_Machine_Learning_Terapan/Submission_1/graph/data_is_null.png "Checking null values")
* Memeriksa distribusi dan korelasi data. Gambar 5 menunjukkan distribusi data.
![distribution](https://github.com/tanaths/dicoding/blob/main/Submission_Belajar_Machine_Learning_Terapan/Submission_1/graph/data_distribution.png "distribution")
Berdasarkan Gambar 5, fitur tersebut mengikuti distribusi normal meskipun ada beberapa yang mengalami _right-skewed_.

## Persiapan Data (_Data Preparation_)
Persiapan data dilakukan dengan beberapa langkah yang meliputi:
* _Feature importances_ atau fitur penting. Ini bertujuan untuk mengetahui fitur mana yang berpengaruh terhadap kualitas _wine_. _Feature importances_ dilakukan dengan identifikasi korelasi fitur masukan terhadap fitur target yaitu _quality_. Berikut Gambar 6 menunjukkan matriks korelasi antar fitur.
![correlation](https://github.com/tanaths/dicoding/blob/main/Submission_Belajar_Machine_Learning_Terapan/Submission_1/graph/data_correlation.png "Correlation each feature")
Berdasarkan hasil korelasi pada Gambar 6, fitur `alcohol` dan `density` memiliki korelasi terbesar dengan fitur target (sekitar 0,44 dan -0,31). Selain itu, fitur `sulphates`, `free sulfur dioxide`, dan `citric acid` memiliki korelasi terkecil (sekitar -0,01 ~ 0,05). Demikian, ketiga fitur ini dihilangkan. Sisanya, fitur pH memiliki korelasi positif yang lemah terhadap kualitas. Korelasi negatif lemah seperti `fixed acidity`, `volatile acidity`, `residual sugar`, `chlorides`, and `total sulfure dioxide`. Demikian, kedua korelasi lemah (positif dan negatif) tetap dimasukkan sebagai fitur penting. Semakin tinggi skor suatu fitur, semakin besar pengaruhnya terhadap model untuk memprediksi suatu variabel tertentu.

* Gambar 7 menunjukkan beberapa hubungan antar fitur:
![pairplot](https://github.com/tanaths/dicoding/blob/main/Submission_Belajar_Machine_Learning_Terapan/Submission_1/graph/data_correlation.png "Correlation each feature")
    - Kualitas wine menurun dengan meningkatnya volatile acidity. Sementara itu, kualitas wine meningkat seiring dengan meningkatnya fixed acidity (keasaman tetap).
    - Kualitas wine meningkat seiring meningkatnya level alkohol.
* _Encoding category_ dengan membuat klasifikasi biner berdasarkan variabel target. Karena '_wine quality_' masih terklasifikasi dalam rentang 3 hingga 9, _encoding category_ biner diperlukan untuk mengelompokkan semua jenis kualitas wine ke dalam 2 kategori, yaitu '_low_' dan '_good_'. Setiap _wine_ yang memiliki kualitas >= 7 akan dikategorikan sebagai kualitas baik (_good_), dan di bawah 7 sebagai kualitas buruk (_low_). Setelah mengkodekan kategori ke dalam klasifikasi biner, dihasilkan 3838 _wine_ berkualitas buruk dan 1060 _wine_ berkualitas baik.
* _Feature engineering_ dengan _StandardScaler()_. _StandardScaler()_ perlu digunakan karena setiap fitur memiliki rentang nilai yang berbeda sehingga normalisasi nilai diperlukan.

Persiapan data yang efektif penting untuk membangun model yang baik pada _dataset white wine_. _Feature importances_ membantu mengidentifikasi fitur-fitur penting yang berpengaruh dalam kualitas _wine_, sementara _encoding category_ menyederhanakan _input_ untuk model. Selain itu, _feature engineering_ seperti _StandardSaler()_ memastikan fitur numerik berada dalam skala yang konsisten, sehingga dapat mencegah bias. Lalu, rasio _training set_ dan _test set_ yang digunakan adalah 80:20. Pembagian ini merupakan rasio yang paling umum digunakan untuk melatih model.

## Pemodelan (_Modelling_)
Setiap algoritma dilakukan dengan sejumlah langkah berikut:
* Menetapkan parameter pada algoritma.
* Melakukan _fit parameter_ terhadap _training set_ dan _test set_.
* Memprediksi model.
* Mengevaluasi model menggunakan kurva ROC dan AUC.

### Logistic Regression
Penggunaan _logistic Regression_ didasari oleh persamaan formula matematika yang menghasilkan _S-shaped curve_, bermanfaat untuk memprediksi klasifikasi biner atau dua kategori (0 dan 1).
Cara kerja formula matematika _logistic regression_ yaitu menemukan prediksi hubungan antara fitur terikat dan fitur independen yang terletak di antara 0 dan 1. Berbeda dengan _linear regression_ yang memiliki fungsi linear, _logistic regression_ memiliki fungsi non-linear (_sigmoid function_) yang menghasilkan hasil prediksi berupa kategori.

The parameter yang diterapkan pada _logistic regression_ sebagai berikut:
* C `0,1`.`0.1` memungkinkan untuk meningkatkan kekuatan regularization, ini dapat mencegah overfitting.
* penalty `l2`. `l2` memungkinkan penambahan _regularization_ pada fungsi _loss function_.
* _solver_ _`liblinear`_. _`liblinear`_ dirancang untuk klasifikasi biner. _`liblinear`_ efisien untuk dataset berukuran kecil hingga menengah.

Keuntungan:
* _Logistic regression_ memberikan hasil yang mudah diinterpretasikan, sehingga mudah untuk memahami dampaknya dari setiap fitur.
* Efisien secara komputasi, terutama untuk dataset besar dengan jumlah fitur yang relatif sedikit.
* _Low variance_, jika jumlah fitur dataset relatif sedikit.

Kekurangan:
* Berpotensi tidak berkinerja baik ketika _decision boundary_ sangat tidak linier.
* Berpotensi tidak dapat menangkap hubungan yang kompleks antara fitur dan variabel respon.
* Berpotensi tidak  dapat bekerja dengan baik jika terdapat terlalu banyak fitur.

### Support Vector Machine
Pada berbagai penelitian, SVM sangat lazim digunakan untuk klasifikasi biner maupun multikelas.
Cara kerja SVM yaitu memisahkan _data points_ menjadi dua kelas dengan mencari nilai _hyperplane_ optimal untuk memaksimalkan margin antar kelas [[4]](https://www.sciencedirect.com/science/article/pii/S1738573323003467). 

Parameter yang diterapkan untuk SVM adalah:
* C `0.1`. Nilai `0.1` mengimplikasikan model yang lebih teratur.
* _Gamma_ `scale`. `scale` adalah nilai default dari parameter _gamma_.
* Kernel `rbf`. `rbf` menangkap hubungan non linier pada variabel.
* Probabilitas diatur ke `True`.

Keuntungan:
* SVM berkinerja baik pada _high dimensional spaces_ sehingga cocok untuk dataset dengan banyak fitur.
* _Kernel Tricks_. Menggunakan fungsi kernel yang berbeda memungkinkan SVM untuk menangani _decision boundary_ secara linier atau nonlinier. Hal ini dapat dilakukan dengan eksperimen secara manual atau menggunakan _GridSearchCV_.

Kekurangan:
* Kurang rentan terhadap _overfitting_.
* Mahal secara komputasi (sangat mahal terutama jika menggunakan _GridSearchCV_).
* Memilih kernel yang sesuai dan mengatur parameter tuning dapat menjadi tantangan tersendiri.

Alasan utama menggunakan kernel rbf karena lebih kompleks dan efisien. Pada saat yang sama SVM dapat menggabungkan beberapa kernel polinomial (nonlinier) untuk memproyeksikan data yang tidak dapat dipisahkan secara linier ke dalam ruang dimensi yang lebih tinggi. Sebelumnya, percobaan lain dilakukan dengan menggunakan kernel linear dan ternyata menghasilkan nilai AUC yang lebih rendah daripada kernel rbf (linear dengan nilai AUC 0,79 dan rbf dengan nilai AUC 0,82).

### Random Forest Classifier
RFC adalah salah satu dari sedikit model yang memiliki _baseline_ atau default parameter model yang baik untuk dilatih. Berbeda dengan _decision tree_, RFC mengembangkan _multi decision trees_ yang menggabung "hasil" dari banyak pohon (_individual models_) untuk menghasilkan prediksi yang lebih baik. 
RFC bekerja dengan menggunakan teknik _bagging_. Teknik _bagging_ merupakan salah satu metode _ensemble learning_ yang menciptakan _subset training_ yang berbeda dari sampel _training set_, sehingga hasil akhir didasarkan pada voting mayoritas (_majority voting_) dari seluruh model.

RFC hanya menggunakan parameter default sehingga belum dibutuhkan penyesuaian eksplisit (_hyperparameter tuning_) untuk menghasilkan hasil prediksi dalam kasus ini.

Keuntungan:
* Metode _ensemble_ memungkinkan penggabungan beberapa _decision trees_ untuk meningkatkan performa secara keseluruhan.
* Mampu menangani nonlinieritas, sangat cocok untuk dataset yang kompleks.
* _Feature importances_, menyediakan ukuran _feature importances_ untuk membantu mengidentifikasi fitur mana yang paling berpengaruh.

Kekurangan:
* Proses RFC terjadi secara _black box_, sehingga kurang dapat diinterpretasikan dibandingkan dengan _logistic regression_.
* Pelatihan dataset dalam jumlah besar dapat menjadi mahal secara komputasi.
* Kurang rentan terhadap _overfitting_, terutama terhadap data yang memiliki banyak _noise_.

### Model Terbaik
Setelah membandingkan ketiga model ini menggunakan kurva ROC dan skor AUC, dapat disimpulkan bahwa _random forest classifier_ memiliki kinerja terbaik dengan nilai skor AUC mencapai 0.92, diikuti oleh SVM (0,81) dan _logistic regression_ (0.79). 
Penjelasan: Tingginya nilai AUC _Random Forest Classifier_ pada kasus ini dapat dikaitkan dengan sifat ensembelnya, yang secara inheren menangani hubungan yang kompleks dan tidak terlalu sensitif terhadap _hyperparameter tuning_. Walaupun begitu, pengaturan default pada RFC sudah cukup efisien untuk dataset kasus ini, sedangkan _logistic regression_ dan SVM sudah dioptimalkan secara efektif dengan _tuning_ yang dipilih.

# Evaluation
Pada Gambar 8 menunjukkan perbandingan evaluasi kinerja model menggunakan ROC Curve dan AUC Score.
![AUC and ROC](https://github.com/tanaths/dicoding/blob/main/Submission_Belajar_Machine_Learning_Terapan/Submission_1/graph/ROC_and_AUC.png "ROC Curve and AUC Score")

Secara umum, kurva ROC adalah representasi grafis dari kinerja model dengan sumbu x mewakili _false positive rate_ (FPR atau invers sensitivitas), dan sumbu y mewakili tingkat _true positive rate_ (TPR atau sensitivitas). Skor AUC adalah nilai skalar yang mewakili kinerja keseluruhan _classifier_.

Penggunaan kurva ROC dan skor AUC relevan dan bermanfaat pada konteks masalah klasifikasi biner. Selain itu, penggunaan kurva ROC dan skor AUC dapat dianggap cocok untuk dataset _white wine_ karena:
* Untuk perbandingan model, kurva ROC memvisualisasikan kinerja, sementara skor AUC memberikan ukuran ringkasan kinerja pengklasifikasi dengan _threshold_ probabilitas yang berbeda untuk penetapan kelas .
* Kurva ROC dan skor AUC tidak terlalu sensitif terhadap ketidakseimbangan kelas (_imbalanced datasets_) dibandingkan dengan metrik seperti _accuracy_. Pada dataset yang tidak seimbang (misalnya, dataset _white wine_), satu kelas dapat secara signifikan melebihi kelas yang lain. _Accuracy_ saja tidak memberikan gambaran yang jelas tentang kinerja model.
* Kurva ROC secara eksplisit menggambarkan pertukaran antara sensitivitas (_true positive rate_) dan spesifisitas (1 - _false positive rate_). Hal ini penting dalam pengaplikasikan di mana biaya (_cost_) _false positive_ dan _false negative_ tidaklah sama.

Berikut cara kerja ROC dan AUC:
* Hasil prediksi model diurutkan berdasarkan probabilitas.
* Mulai dari probabilitas terendah, ambang batas (_threshold_) dinaikkan, dan untuk setiap ambang batas, _true positive rate_ dan _false positive rate_ dihitung.
* Nilai TPR dan FPR ini kemudian digunakan untuk memplot titik-titik pada kurva ROC. Di sinilah AUC digunakan sebagai ukuran ringkasan dari keseluruhan informasi kurva ROC ke dalam satu angka, sehingga memudahkan untuk membandingkan model. _Classifier_ yang sempurna memiliki AUC 1.0.

Walaupun kurva ROC dan skor AUC cocok dipakai pada evaluasi klasifikasi biner, metrik ini tetap memiliki kekurangan, khususnya terletak pada TFR dan TPR Skor AUC:
Meningkatkan _True Positive Rate_ (sensitivity) akan menyebabkan peningkatan _False Positive Rate_ (1-_specificity_), dan sebaliknya. Jika _threshold_ diturunkan untuk mengklasifikasikan suatu sampel sebagai positif, _True Positive Rate_ (TPR) akan meningkat karena lebih banyak sampel positif yang terdeteksi, tetapi hal ini juga dapat meningkatkan _False Positive Rate_ (FPR) karena lebih banyak sampel negatif yang salah diklasifikasikan sebagai positif.
Ketika 0,5<AUC<1, ada kemungkinan besar bahwa _classifier_ akan mampu membedakan nilai kelas positif dari nilai kelas negatif. Ini terjadi karena _classifier_ mampu mendeteksi lebih banyak jumlah _True Positive_ dan _True Negative_ dibandingkan _False Negative_ dan _False Positive_.

Pemilihan _threshold_ harus disesuaikan dengan tujuan bisnis spesifik dan dampak relatif dari _False Positive_ dan _True Positive_ pada setiap kasus. Pada kasus kualitas _white wine_, pemilihan _threshold_ untuk membedakan _wine_ berkualitas bagus atau buruk sangat penting dalam pengambilan keputusan bisnis. Untuk memastikan hanya _wine_ berkualitas bagus yang dianggap sebagai "positif" oleh model, memilih _threshold_ yang tinggi diperlukan sehingga hanya _wine_ yang memenuhi standar tertentu yang akan diklasifikasikan sebagai positif.

## Kesimpulan (_Conclusion_)
Berdasarkan data yang ada, proses pengujian kualitas _wine_ yang manual memakan waktu dan sumber daya yang besar. Namun, dengan penerapan teknologi _machine learning_, industri _wine_ dapat mempersingkat proses tersebut. Melalui pengembangan model yang tepat, hasil kinerja algoritma _random forest classifier_ memperoleh skor AUC yang paling tinggi di antara model yang diuji, yaitu 0.92. Artinya, model _random forest classifier_ memiliki tingkat probabilitas yang tinggi dalam mengklasifikasi kualitas _wine_. Selain itu, identifikasi fitur penting melalui korelasi antar fitur menentukan kualitas _wine_ seperti tingkat alkohol, _density_, _total sulfur dioxide_, pH, _fixed acidity_, _volatile acidity_, _residual sugar_, dan _chlorides_. Dengan demikian, implementasi solusi ini memberikan kemungkinan penghematan waktu dan sumber daya pada tahap produksi akhir _wine_.

### Daftar Pustaka
[1]	M. Koranga, R. Pandey, M. Joshi, and M. Kumar, “Analysis of white wine using machine learning algorithms,” Mater. Today Proc., vol. 46, pp. 11087–11093, 2021, doi: https://doi.org/10.1016/j.matpr.2021.02.229.
[2]	K. R. Dahal, J. N. Dahal, H. Banjade, and S. Gaire, “Prediction of Wine Quality Using Machine Learning Algorithms,” Open J. Stat., vol. 11, no. 2, 2021, doi: 10.4236/ojs.2021.112015.
[3]	X. Jiang, X. Liu, Y. Wu, and D. Yang, “White Wine Quality Prediction and Analysis with Machine Learning Techniques,” Highlights Sci. Eng. Technol., vol. 39, pp. 321–326, Apr. 2023, doi: 10.54097/hset.v39i.6548.
[4]	M. Dongliang, L. Yi, Z. Tao, and H. Yanping, “Research on prediction and analysis of supercritical water heat transfer coefficient based on support vector machine,” Nucl. Eng. Technol., 2023, doi: https://doi.org/10.1016/j.net.2023.07.030.


