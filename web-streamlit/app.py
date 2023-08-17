import streamlit as st

def main():
    st.sidebar.title("Rain Prediction with Logistic Regression Modeling and SVM")
    menu = ["Abstract", "Dataset", "Environment", "Research Step", "Conclusion", "Literature", "Author"]
    choice = st.sidebar.selectbox("Select Menu", menu)
    st.sidebar.write("Final Project Fresh Graduate Academy Digitalent 2023 - Big Data Using Python")
    st.sidebar.image("assets/dts.png", width=250)

    if choice == "Abstract":
        st.title("Abstract")
        st.write("Perkembangan ilmu pengetahuan dan teknologi dalam beberapa dekade terakhir telah membawa dampak signifikan dalam berbagai bidang kehidupan manusia, termasuk dalam pemahaman dan prediksi fenomena alam. Salah satu aspek penting dari fenomena alam adalah cuaca, yang memiliki peran vital dalam aktivitas manusia dan ekosistem. Curah hujan, sebagai salah satu elemen kunci dalam dinamika cuaca, memiliki dampak yang luas pada pertanian, lingkungan, ekonomi, serta kehidupan sehari-hari.")
        st.write("Negara Australia, dengan geografi yang luas dan keragaman ekosistemnya, sering kali menghadapi tantangan dalam mengelola dan merencanakan kegiatan yang terkait dengan curah hujan. Dalam konteks inilah pentingnya pengembangan model prediksi curah hujan yang akurat dan handal menjadi sangat mendasar. Dengan memiliki kemampuan untuk memprediksi curah hujan secara lebih tepat, berbagai sektor di negara Australia dapat mengambil langkah-langkah yang lebih efektif dalam merespons perubahan cuaca yang mungkin terjadi.")
        st.write("Dalam penelitian ini, kami akan fokus pada pengembangan model prediksi curah hujan di negara Australia menggunakan dua metode pemodelan: Logistic Regression dan Support Vector Machine (SVM). Logistic Regression adalah metode statistik yang telah terbukti efektif dalam pemodelan klasifikasi, sedangkan SVM adalah algoritma pembelajaran mesin yang dikenal karena kemampuannya dalam mengatasi masalah klasifikasi yang kompleks.")
        st.write("Tujuan utama dari penelitian ini adalah untuk menghasilkan model prediksi curah hujan yang akurat dan dapat diandalkan untuk negara Australia. Melalui penerapan Logistic Regression dan SVM, kami bertujuan untuk memanfaatkan informasi historis curah hujan dan variabel cuaca terkait lainnya guna mengembangkan model yang mampu mengklasifikasikan kondisi cuaca dengan lebih baik, serta meramalkan intensitas curah hujan dengan akurasi yang lebih tinggi.")
        st.write("Dalam upaya mencapai tujuan tersebut, penelitian ini akan melakukan analisis mendalam terhadap data cuaca historis dari berbagai wilayah di Australia. Hasil dari penelitian ini diharapkan akan memberikan pandangan yang lebih jelas tentang pola cuaca dan variabilitas curah hujan di negara tersebut. Selain itu, model prediksi yang dihasilkan juga dapat digunakan sebagai alat bantu bagi berbagai sektor, seperti pertanian, pengelolaan sumber daya air, serta mitigasi risiko bencana alam yang berkaitan dengan perubahan cuaca.")
        st.write("Dengan merujuk pada konteks studi kasus di negara Australia, penelitian ini diharapkan akan memberikan sumbangan yang berharga dalam pengembangan teknologi prediksi cuaca yang lebih canggih dan akurat. Hasil penelitian ini juga dapat menjadi landasan bagi pengembangan model serupa di wilayah-wilayah lain dengan tantangan serupa dalam menghadapi perubahan cuaca dan curah hujan yang tidak pasti.")

    elif choice == "Dataset":
        st.title("Dataset")
        st.write("Data yang digunakan dalam penelitian ini bernama Rain in Australia dan sumbernya berasal dari https://www.kaggle.com/jsphyg/weather-dataset-rattle-package")
        st.write("Data ini digunakan untuk memprediksi apakah terjadi hujan pada keesokan hari dari tanggal pengamatan. Set data ini mencakup catatan harian curah hujan selama periode 10 tahun di berbagai lokasi di seluruh wilayah Australia. Total, terdapat 145.460 baris data yang terekam dengan 23 atribut yang berbeda.")
        st.write("Salah satu aspek penting dalam data ini adalah atribut yang menjadi fokus utama, yaitu RainTomorrow. Atribut ini berfungsi sebagai label kelas yang menunjukkan apakah besok akan terjadi hujan atau tidak. Terdapat dua kategori dalam atribut ini, yaitu No (tidak akan terjadi hujan dengan curah minimal 1mm pada besok hari) dan Yes (akan terjadi hujan dengan curah minimal 1mm pada besok hari).")
        st.write(" ")
        st.write("Deskripsi Atribut:")
        st.write("Atribut bertipe kategorikal (nominal dan/atau ordinal)")
        st.write("1. Location - lokasi, nama kota di Australia")
        st.write("2. WindGustDir - arah kecepatan angin yang paling tinggi selama 24 jam sebelum jam 12 malam hari itu")
        st.write("3. WindDir9am - arah angin jam 9 pagi")
        st.write("4. WindDir3pm - arah angin jam 3 sore")
        st.write("5. RainToday - apakah hari ini hujan: jika curah hujan 24 jam sebelum jam 9 pagi melebihi 1mm, maka nilai ini adalah 1, jika tidak nilai nya 0")
        st.write("6. RainTomorrow - variable yang mau di prediksi")
        st.write(" ")
        st.write("Atribut bertipe numerikal (int, float)")
        st.write("1. MinTemp - temperatur terendah hari itu dalam celcius")
        st.write("2. MaxTemp - temperatur tertinggi hari itu dalam celcius")
        st.write("3. Rainfall - jumlah curah hujan hari itu dalam mm")
        st.write("4. Evaporation - jumlah evaporasi dalam mm dari Class A pan selama 24 jam sebelum jam 9 pagi hari itu")
        st.write("5. Sunshine - jumlah jam hari itu cerah dengan cahaya matahari")
        st.write("6. WindGustSpeed - kecepatan angin yang paling tinggi dalam km/jam selama 24 jam sebelum jam 12 malam hari itu")
        st.write("7. WindSpeed9am - kecepatan angin jam 9 pagi dalam km/jam dihitung dari rata-rata kecepatan angin 10 menit sebelum jam 3 sore")
        st.write("8. WindSpeed3pm - kecepatan angin jam 3 sore dalam km/jam dihitung dari rata-rata kecepatan angin 10 menit sebelum jam 3 sore")
        st.write("9. Humidity9am - humiditas jam 9 pagi dalam persen")
        st.write("10. Humidity3pm - humiditas jam 3 sore dalam persen")
        st.write("11. Pressure9am - tekanan udara jam 9 pagi dalam hpa")
        st.write("12. Pressure3pm - tekanan udara jam 3 sore dalam hpa")
        st.write("13. Cloud9am - persentase langit yang tertutup awan jam 9 pagi. dihitung dalam oktas, unit ⅛, menghitung berapa unit ⅛ dari langit yang tertutup awan. Jika 0, langit cerah, jika 8, langit sepenuhnya tertutup awan.")
        st.write("14. Cloud3pm - persentase langit yang tertutup awan jam 3 sore")
        st.write("15. Temp9am - temperatur jam 9 pagi dalam celcius")
        st.write("16. Temp3pm - temperatur jam 3 sore dalam celcius")
        st.write(" ")
        st.write("Atribut bertipe date (time series)")
        st.write("1. Date - tanggal hari itu")

    elif choice == "Environment":
        st.title("Environment")
        st.write("- pandas 2.0.3")
        st.write("- numpy 1.25.1")
        st.write("- scipy 1.11.1")
        st.write("- scikit-learn 1.3.0")
        st.write("- matplotlib")
        st.write("- seaborn 3.7.2")
        st.write("- pickleshare 0.7.5")
        st.write("- Flask 2.3.2")
        st.write("- streamlit 1.25.0")

    elif choice == "Research Step":
        st.title("Research Step")
        st.write("Langkah-langkah dalam penelitian ini adalah sebagai berikut:")

        st.write("1. Data Loading")
        st.caption("-- Loading Data yang berasal dari Kaggle")
        st.caption("-- Data dibagi menjadi 2 bagian yaitu 70% Data Latih 30% Data Uji")

        st.write("2. Data Cleaning")
        st.caption("-- Merename nama kolom")
        st.caption("-- Menghapus data yang label kelas ('Hari besok Hujan') mengandung missing values")
        st.caption("-- Mengisi missing values pada atribut kategorikal kecuali label kelas")
        st.caption("-- Mengisi missing values pada atribut numerikal ")
        st.caption("-- Mengisi missing values pada atribut numerikal ")
        st.caption("-- Mengecek rangkuman total missing values untuk setiap kolom")
        st.caption("-- Menghapus kolom yang tidak dipakai")
        st.caption("-- Mengelompokkan atribut berdasarkan tipe datanya")
        
        st.write("3. Explorasi Data")
        st.caption("-- Melakukan Data Query, Grouping, dan Visualisasi")

        st.write("4. Data Preprocessing")
        st.caption("-- Drop data dengan target *missing values*")
        st.caption("-- Train Test Split")
        st.caption("-- Undersampling data latih")
        st.caption("-- Drop columns based on Anova and Mutual Information")
        st.caption("-- Mengelompokkan Atribut berdasarkan tipe datanya")
        st.caption("-- Imputasi missing values")
        st.caption("-- One Hot Encoding Categorical Features")
        st.caption("-- Concat Numerical and Categorical Features")
        st.caption("-- Features Scaling")
        st.caption("-- Menentukan n_best component dengan threshold tertentu")
        st.caption("-- Fit and Transform PCA dengan best_component yang didapat")

        st.write("5. Modelling")
        st.caption("-- Membuat list dari model yang akan digunakan")
        st.caption("-- Fungsi untuk K-fold cross validation setiap model")
        st.caption("-- Tuning model dengan scoring accuracy")
        st.caption("-- Tuning model dengan hyperparameter tuning")
        
        st.write("6. Pelatihan Model")
        st.caption("-- Classification report untuk masing-masing model")

        st.write("7. Evaluasi Model")
        st.caption("-- Tuning model dengan hyperparameter")
        st.caption("-- Tuning model dengan threshold")

        st.write("8. Pengambilan Keputusan")

        st.write("9. Save Models")
        st.caption("-- Menyimpan hasil Modelling")
        st.caption("-- Loading data Modelling")
        st.caption("-- Inisialisasi Variabel yang ada di dalam model")
        st.caption("-- Membuat Predict Function ")

        st.write("10. Deployment")
        st.caption("-- Menggunakan model .PKL untuk diaplikasikan kedalam aplikasi berbasis web dengan framework Flask")
        st.caption("-- Membuat dokumentasi penelitian dengan aplikasi berbasis web dengan framework Streamlit")

    elif choice == "Conclusion":
        st.title("Conclusion")
        st.write("Dalam penelitian ini, kami telah melakukan analisis mendalam terhadap data curah hujan harian di berbagai lokasi di Australia menggunakan metode Regresi Logistik dan Mesin Vector Pendukung (SVM) untuk memprediksi kemungkinan terjadinya hujan pada hari berikutnya. Hasil dari penelitian ini mengungkapkan beberapa temuan dan kesimpulan yang penting:")
        st.write("1. Pemodelan Regresi Logistik dan SVM: Kami berhasil mengembangkan model prediksi curah hujan dengan menggabungkan Regresi Logistik dan SVM. Kedua metode ini membantu dalam mengklasifikasikan apakah akan terjadi hujan pada hari berikutnya berdasarkan data cuaca pada hari sebelumnya. Kombinasi kedua model ini memberikan hasil yang lebih baik daripada menggunakan masing-masing model secara terpisah.")
        st.write("2. Atribut Penting: Kami mengidentifikasi atribut-atribut penting yang signifikan dalam memprediksi curah hujan. Atribut seperti curah hujan pada hari sebelumnya, tekanan atmosfer, kelembaban udara, dan suhu rata-rata memiliki dampak besar terhadap kemungkinan terjadinya hujan pada hari berikutnya.")
        st.write("3. Akurasi Prediksi: Model yang dikembangkan dalam penelitian ini berhasil mencapai tingkat akurasi yang cukup tinggi dalam memprediksi apakah akan terjadi hujan pada hari berikutnya. Penggabungan Regresi Logistik dan SVM memberikan performa prediksi yang lebih baik daripada model tunggal, menunjukkan bahwa pendekatan ini efektif dalam meningkatkan akurasi.")
        st.write("4. Implikasi dan Manfaat: Penelitian ini memiliki implikasi penting dalam berbagai sektor, terutama dalam perencanaan dan pengambilan keputusan. Model prediksi curah hujan yang akurat dapat digunakan untuk mengoptimalkan penggunaan sumber daya air, mengelola pertanian, serta merencanakan aktivitas sosial ekonomi yang bergantung pada cuaca.")
        st.write("5. Perkembangan Selanjutnya: Meskipun model yang dikembangkan telah memberikan hasil yang memuaskan, terdapat potensi untuk pengembangan lebih lanjut. Penelitian selanjutnya dapat mencakup perbaikan pada pengolahan data, eksplorasi metode pemodelan yang lebih kompleks, serta penerapan teknik optimasi untuk meningkatkan performa prediksi.")
        st.write("Secara keseluruhan, penelitian ini memberikan kontribusi penting dalam bidang prediksi cuaca, khususnya dalam hal prediksi curah hujan di Australia. Hasil penelitian ini diharapkan dapat memberikan panduan yang berharga bagi pengambilan keputusan dan pengembangan strategi di berbagai sektor yang terkait dengan cuaca dan lingkungan alam.")

    elif choice == "Literature":
        st.title("Literature")
        st.write("This is the literature page.")
        st.write("[Rainfall Prediction using Machine Learning Python](https://www.geeksforgeeks.org/rainfall-prediction-using-machine-learning-python/)")
        st.write("[Predicting Rain with Machine Learning](https://towardsdatascience.com/predicting-rain-with-machine-learning-2acf80017c44)")
        st.write("[LogisticRegression_on_WeatherDataset](https://www.kaggle.com/code/hesampourrostami/logisticregression-on-weatherdataset)")
        st.write("[Rain prediction for tomorrow in Australia](https://www.kaggle.com/code/igorprikhodko/rain-prediction-for-tomorrow-in-australia#4.Data-Cleaning-and-Feature-Engineering)")

    elif choice == "Author":
        st.title("Rain Prediction Application with Logistic Regression Modeling and SVM")
        st.image("assets/me.jpg", width=200)
        st.write("My name is Taofik Krisdiyanto, and I'm passionate about Web Development, Data Science, and Machine Learning. I have a background in computer science and have worked on various projects involving data analysis, natural language processing, and computer vision. This web app is a showcase of my recent project.")
        st.write("Connect with me on [LinkedIn](https://www.linkedin.com/in/taofikkhris/) | [GitHub](https://github.com/taofikkhris)")

if __name__ == "__main__":
    main()
