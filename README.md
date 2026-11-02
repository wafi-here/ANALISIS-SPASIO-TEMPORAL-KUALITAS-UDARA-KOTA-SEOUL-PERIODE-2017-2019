# **DAFTAR ISI**

# **BAB 1   PENDAHULUAN**

## **1.1 Latar Belakang**

​	Pertumbuhan kota metropolitan dan industrialisasi yang pesat sering kali membawa dampak turunan yang signifikan terhadap kelestarian lingkungan, di mana salah satu isu paling mendesak adalah penurunan kualitas udara. Kota Seoul, sebagai pusat aktivitas ekonomi dan wilayah padat penduduk di Asia Timur, secara konsisten menghadapi tantangan polusi udara perkotaan yang sangat kompleks. Emisi dari padatnya volume kendaraan bermotor, aktivitas industri di sekitar wilayah metropolitan, hingga fenomena debu musiman lintas batas secara kolektif berkontribusi pada akumulasi berbagai polutan berbahaya di udara terbuka. Fenomena ini tidak lagi sekadar isu ekologis, melainkan telah menjadi ancaman langsung bagi kesehatan masyarakat umum yang beraktivitas sehari-hari di wilayah tersebut.

​	Di dalam mengukur tingkat bahaya polusi udara, *Particulate Matter*—khususnya partikel halus berukuran 2,5 mikrometer (PM2.5) dan 10 mikrometer (PM10)—dijadikan sebagai indikator dan fokus pemantauan utama. PM2.5 memiliki tingkat bahaya yang sangat tinggi karena ukurannya yang mikroskopis memungkinkannya terhirup melewati sistem filtrasi alami tubuh, menembus paru-paru bagian dalam, hingga memasuki sistem peredaran darah. Paparan jangka panjang maupun lonjakan ekstrem jangka pendek dari polutan ini terbukti secara medis dapat memicu penyakit infeksi saluran pernapasan atas (ISPA), asma, hingga risiko komplikasi kardiovaskular. Oleh karena itu, kemampuan untuk memprediksi dan memetakan kapan serta di mana konsentrasi partikel ini mencapai titik kritis sangatlah esensial bagi perlindungan kesehatan publik.

​	Guna memahami dinamika penyebaran polutan tersebut secara objektif dan empiris, analisis yang mendalam terhadap data historis sangat diperlukan. Proyek analisis ini memanfaatkan dataset pemantauan kualitas udara yang direkam dari berbagai stasiun sensor di seluruh distrik kota Seoul selama kurun waktu tahun 2017 hingga 2019. Dataset ini menyajikan informasi yang sangat terperinci, mencakup pengukuran konsentrasi PM2.5 dan polutan lainnya per jam, lokasi stasiun pemantau, serta kategorisasi kelayakan udara. Berbekal data dengan ribuan baris rekaman ini, terdapat peluang besar untuk mengekstraksi wawasan berharga terkait perilaku polusi udara dari dua dimensi utama: tren waktu (kapan polusi paling parah terjadi) dan pemetaan spasial (wilayah mana yang paling tercemar).

​	Proyek ini dilaksanakan untuk mengolah, membersihkan, dan memvisualisasikan kumpulan data tersebut menggunakan perangkat lunak Microsoft Excel, yang merupakan bagian dari pemenuhan kompetensi Tugas Akhir Data Analitik tingkat SMK. Fokus utama dari penyusunan laporan ini adalah merumuskan temuan faktual mengenai tren lonjakan rata-rata PM2.5 berdasarkan Tahun, Kuarter, dan Jam, mengidentifikasi lokasi dengan kualitas udara terburuk, serta melihat persentase status udara tidak sehat. Pada akhirnya, hasil analisis dan *dashboard* yang dibangun tidak hanya akan memenuhi kriteria akademik, tetapi juga diharapkan mampu memberikan rekomendasi berbasis data agar masyarakat dapat mengambil tindakan pencegahan yang tepat—seperti penggunaan masker atau penjadwalan ulang aktivitas luar ruangan—pada wilayah dan waktu dengan risiko polusi tertinggi.


 

## **1.2 Rumusan** **Pertanyaan Analisis**

​	Untuk mencapai tujuan pelaporan dan memberikan arah yang terstruktur pada pengolahan data ini, perumusan masalah difokuskan pada evaluasi temporal (tahun dan kuartal serta jam) serta kerentanan spasial. Berikut adalah pertanyaan analisis yang menjadi landasan utama dalam proyek ini:

1. ​	Bagaimana tren fluktuasi konsentrasi rata-rata PM2.5 jika dievaluasi berdasarkan pergerakan antar-tahun dan per kuartal (Q1–Q4) secara runut selama periode 2017 hingga 2019?
2. ​	Pada kuartal berapakah tingkat pencemaran udara di kota Seoul selalu mencapai titik puncaknya, dan apakah terdapat pola musiman yang konsisten berulang setiap tahunnya?
3. ​	Berdasarkan pemetaan wilayah, stasiun pemantau (alamat) manakah yang mencatat akumulasi polutan PM2.5 tertinggi yang mengindikasikan kualitas udara terburuk secara spasial?
4. ​	Bagaimana proporsi distribusi jam dengan kualitas udara berstatus "Tidak Sehat" dan "Sangat Tidak Sehat" dibandingkan dengan status udara yang tergolong aman selama masa observasi?

​	

## **1.3 Tujuan**

​	Tujuan utama dari proyek analisis data ini adalah untuk mengevaluasi dinamika kualitas udara di kota Seoul selama periode 2017 hingga 2019, dengan berfokus pada pengukuran konsentrasi polutan utama berupa partikel halus (PM2.5 dan PM10). Guna memenuhi standar pelaporan analisis data, penjabaran tujuan khusus dari proyek ini disusun sebagai berikut:

1. Mengevaluasi Tren Waktu Berdasarkan Tahun dan Kuartal serta Jam: Menganalisis fluktuasi tingkat polusi udara melalui perbandingan agregat antar tahun (2017, 2018, dan 2019) dan membedah tren konsentrasi polutan per kuartal (Q1, Q2, Q3, dan Q4) serta mengevaluasi proporsi Konsentrasi polutasn per jam. Evaluasi temporal ini bertujuan untuk mengidentifikasi pola musiman jangka panjang, mendeteksi secara presisi pada kuartal ke berapa lonjakan partikel berbahaya paling sering mencapai titik kritis dan berapa persentase jam dimana polutan bersebaran di lingkungan.
2. Memetakan Tingkat Kerentanan Spasial: Mengidentifikasi dan membandingkan rata-rata paparan PM2.5 yang tercatat di berbagai stasiun pemantauan. Tujuannya adalah untuk menentukan wilayah atau alamat spesifik di Seoul yang memiliki riwayat kualitas udara terburuk, sehingga lokasi dengan tingkat risiko paparan tertinggi dapat dipetakan secara akurat.
3. Menganalisis Distribusi Kategori Kualitas Udara: Menghitung persentase kelayakan udara per jam berdasarkan kategorisasi standar (seperti Baik, Sedang, Tidak Sehat, dan Sangat Tidak Sehat) sepanjang periode observasi. Analisis ini diperlukan untuk mengukur seberapa sering masyarakat Seoul terpapar tingkat udara yang melampaui ambang batas aman.
4. Menyediakan Landasan Mitigasi Berbasis Data: Menghasilkan ringkasan temuan objektif yang divisualisasikan melalui dashboard Microsoft Excel. Hasil analisis ini ditujukan untuk menjadi landasan rekomendasi praktis bagi masyarakat terkait mitigasi risiko kesehatan, seperti imbauan pengurangan aktivitas luar ruangan pada wilayah dan kuartal yang teridentifikasi paling berpolusi


 

# **BAB 2   Metode dan Kebutuhan Teknis**

​	Bagian ini menguraikan tahapan sistematis serta instrumen yang diaplikasikan dalam memproses dataset polusi udara kota Seoul. Sesuai dengan pedoman standar proyek analisis data, keseluruhan alur kerja—mulai dari persiapan data, perhitungan statistik, hingga perancangan visual—dieksekusi sepenuhnya menggunakan perangkat lunak Microsoft Excel. Berikut adalah rincian metodologi teknis yang diterapkan:



## **2.1 Pengumpulan dan Rekayasa Data (Data Preparation):**

​	Dataset kualitas udara historis ini bersumber dari Kaggle [[1\]](https://www.kaggle.com/datasets/bappe/air-pollution-in-seoul) (**Sumber Data Asli:** *Seoul Metropolitan Government (Open Data Plaza))*, dengan proses awal mencakup pemeriksaan kelengkapan kolom, validasi lisensi (**Lisensi Data:** CC BY-SA 4.0 (Creative Commons Attribution-ShareAlike 4.0 International)), serta pembersihan data dari duplikasi atau baris yang kosong (menggunakan Google Spreadsheets dan pustaka pandas. Setelah data dipastikan bersih, langkah krusial berikutnya adalah rekayasa fitur (feature engineering) pada kolom Measurement yang menyimpan informasi waktu mentah. Komponen waktu pada kolom tersebut dipisahkan menjadi dua kolom dimensi waktu yang baru untuk kebutuhan evaluasi jangka panjang, yaitu kolom "Tanggal/Bulan/Tahun” dan kolom “Jam”. Ekstraksi ini melengkapi kolom-kolom utama lainnya yang juga diisolasi untuk analisis, seperti kolom Address (lokasi), PM2.5 (kadar partikel halus), dan Kategori PM2.5, PM10, dan NO2 (status kesehatan udara). Pembersihan data dilakukan menggunakan kode python dengan pustaka pandas dengan kode sebagai berikut:

```python
import argparse
from pathlib import Path
import sys
import pandas as pd


def clean_dataset(input_path, output_path):
    # Konversi string path menjadi objek Path
    input_file = Path(input_path).resolve()

    print(f"=== MEMUAT DATASET ===")
    print(f"Mencoba membaca file dari: {input_file}")

    # Validasi keberadaan file secara dinamis
    if not input_file.exists():
        print(f"[ERROR] File tidak ditemukan di path: {input_file}")
        sys.exit(1)

    if not input_file.is_file():
        print(
            f"[ERROR] Path yang dimasukkan adalah folder, bukan file: {input_file}"
        )
        sys.exit(1)

    try:
        df = pd.read_csv(input_file)
        print(f"[SUKSES] Berhasil memuat {len(df)} baris data.\n")
    except Exception as e:
        print(f"[ERROR] Gagal membaca CSV: {e}")
        sys.exit(1)

    # --- PROSES CLEANING / OLAH DATA DI SINI ---

    # Menentukan lokasi output secara dinamis
    if output_path:
        out_file = Path(output_path).resolve()
    else:
        # Jika output tidak diisi, otomatis buat nama baru di folder yang sama
        out_file = input_file.parent / f"{input_file.stem}_clean.csv"

    # Simpan file hasil
    df.to_csv(out_file, index=False)
    print(f"[SUKSES] File bersih disimpan ke: {out_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Script pembersihan data dengan jalur path dinamis."
    )

    # Argumen dinamis 1: Input Path (Wajib)
    parser.add_argument(
        "input_path",
        type=str,
        help="Path ke file CSV input (bisa relatif seperti ./data.csv atau absolut /home/user/data.csv)",
    )

    # Argumen dinamis 2: Output Path (Opsional)
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="Path tujuan penyimpanan file hasil (opsional)",
    )

    args = parser.parse_args()

    clean_dataset(input_path=args.input_path, output_path=args.output)


if __name__ == "__main__":
    main()

```

atau kode dapat diinstall melalui repositori berikut: https://github.com/wafi-here/ANALISIS-SPASIO-TEMPORAL-KUALITAS-UDARA-KOTA-SEOUL-PERIODE-2017-2019/blob/main/clean_data.py

![img](file:///tmp/lu14234ti1m.tmp/lu14234toau_tmp_fecbb841.gif) 
 **Gambar 1.** Tampilan data kualitas udara pada Microsoft Excel

## **2.2 Teknik Pengolahan dan Agregasi Data**

Guna mengubah ribuan baris data mentah menjadi ringkasan informasi yang bermakna, metode pengolahan utama memanfaatkan fitur PivotTable yang tersedia di Excel. Teknik agregasi difokuskan pada penggunaan fungsi statistik rata-rata (AVERAGE) untuk menghitung konsentrasi polutan secara komprehensif. Pengaturan PivotTable secara khusus dikonfigurasikan untuk menghitung rata-rata nilai PM2.5 per tahun dan di- breakdown lebih lanjut per kuartal (Q1 hingga Q4) serta fungsi COUNT untuk menghitung kategori kondisi kesehatan per jam. Selain dimensi waktu, agregasi rata-rata juga diterapkan pada dimensi keruangan untuk mengkalkulasi tingkat polusi per wilayah/alamat.

![img](file:///tmp/lu14234ti1m.tmp/lu14234toau_tmp_868fb661.gif) **Gambar** **2****.** Tampilan penggunaan AVERAGE sebagai fungsi agregasi
 ![img](file:///tmp/lu14234ti1m.tmp/lu14234toau_tmp_96c1af5f.gif) 
 **Gambar** **3****.** Tampilan penggunaan AVERAGE sebagai fungsi agregasi
 ![img](file:///tmp/lu14234ti1m.tmp/lu14234toau_tmp_db153fa.gif) 
 **Gambar** **4****.** Tampilan penggunaan fungsi COUNT untuuk menghitung kondisi kategori pada polutan PM2.5
 ![img](file:///tmp/lu14234ti1m.tmp/lu14234toau_tmp_b28e928a.gif) 
 **Gambar** **5****.** Tampilan penggunaan AVERAGE sebagai fungsi agregasi

## **2.3 Perancangan Visualisasi Visual dan Dashboard**

Angka-angka agregat yang dihasilkan dari tahap sebelumnya ditransformasikan menjadi bentuk visual melalui PivotChart, yang kemudian disusun menjadi sebuah dashboard analitik terpadu. Metode visualisasi spesifik yang dikembangkan meliputi:

- ​	Grafik Garis (Line Chart): Digunakan secara khusus untuk menganalisis tren waktu (time-series). Grafik ini diproyeksikan untuk menghitung dan menampilkan frekuensi pergerakan fluktuasi rata-rata PM2.5 berdasarkan kombinasi runtut Tahun dan Kuartalnya (misalnya: 2017-Q1, 2017-Q2, dst.), guna mendeteksi pada kuartal ke berapa puncak polusi udara terjadi setiap tahunnya.
   ![img](file:///tmp/lu14234ti1m.tmp/lu14234toau_tmp_4a571f67.gif)

  ​	**Gambar** **6**. Tren Polusi Udara Seiring Waktu periode 2017-2019

- ​	Grafik Batang (Bar Chart): Diterapkan untuk memfasilitasi perbandingan lintas wilayah, di mana grafik ini akan mengurutkan alamat stasiun pemantau dari yang mencatat rekor polusi terendah hingga tertinggi.
   ![img](file:///tmp/lu14234ti1m.tmp/lu14234toau_tmp_c40d3c17.gif)

  ​	**Gambar** **7.** Perbandingan Tingkat Polusi Per Lokasi Periode 2017-2019

- ​	Grafik Lingkaran (Pie Chart): Digunakan untuk merangkum proporsi distribusi persentase dari keseluruhan status kelayakan udara (seperti proporsi jam "Baik" versus "Tidak Sehat").
   ![img](file:///tmp/lu14234ti1m.tmp/lu14234toau_tmp_59a05b32.gif)

  ​	**Gambar** **8**. Proporsi Jam Berdasarkan Kategori Kualitas Udara Periode 2017-2019



Selain PivotChart utama, dashboard ini juga dilengkapi dengan Sparklines (Line dan Column) pada tabel rincian untuk memberikan gambaran mikro mengenai tren dan titik lonjakan polusi (High/Low Points) di setiap lokasi per kuartal.

![img](file:///tmp/lu14234ti1m.tmp/lu14234toau_tmp_9d9aa952.gif)

- ​	**Gambar** **9**. Proporsi Jam Berdasarkan Kategori Kualitas Udara Periode 2017-2019

# **BAB 3   Temuan dan Jawaban Analisis**

1. ​			Berdasarkan proses 	ekstraksi, pembersihan, dan agregasi data historis menggunakan 	teknik *PivotTable* terhadap 50.900 baris data, analisis ini 	menghasilkan temuan-temuan empiris yang secara komprehensif 	menjawab pertanyaan rumusan di atas. Berikut adalah rincian temuan 	yang mendeskripsikan kondisi kualitas udara kota Seoul:

![img](file:///tmp/lu14234ti1m.tmp/lu14234toau_tmp_f23b7012.png)

**Gambar** **10**. Dashboard Analisis Kualitas Udara Kota Seoul Periode 2017-2019	

## **3.1 Pola Tren Tahunan dan Lonjakan Kuartalan (Puncak Polusi)**

1. ​			Evaluasi data time-series 	menunjukkan adanya pola musiman yang sangat konsisten di mana 	polusi udara selalu memburuk pada akhir-awal tahun dan membaik pada 	pertengahan tahun. Kuartal Pertama (Q1) secara absolut menjadi 	periode dengan tingkat polusi terburuk setiap tahunnya, mencatat 	rata-rata PM2.5 sebesar 34,54 µg/m³ (2017), 29,01 µg/m³ (2018), 	dan mencapai rekor tertinggi keseluruhan pada Q1 2019 dengan angka 	35,71 µg/m³. Sebaliknya, Kuartal Ketiga (Q3) secara konsisten 	menjadi periode dengan udara paling bersih, dengan rata-rata 	konsentrasi PM2.5 menyentuh titik terendah hingga 13,42 µg/m³ 	pada tahun 2018. Hal ini mengonfirmasi bahwa periode Desember 	hingga Maret merupakan masa paling kritis bagi kualitas udara di 	Seoul.


   ![image-20261102145231465](/home/wafiannafis/.config/Typora/typora-user-images/image-20261102145231465.png)

   **Gambar** **11**. Line Chart Kualitas Udara Kota Seoul Periode 2017

   ![image-20261102145314145](/home/wafiannafis/.config/Typora/typora-user-images/image-20261102145314145.png)**Gambar** 	**12**	Line Chart Kualitas 	Udara Kota Seoul 	Periode 	2018

   ![image-20261102145400408](/home/wafiannafis/.config/Typora/typora-user-images/image-20261102145400408.png)

   **Gambar** **13**. Line Chart Kualitas 	Udara Kota Seoul 	Periode 	2019

   ## **3.2 Identifikasi Titik Kerentanan Spasial (Lokasi Terburuk)**

   ​	Analisis terhadap variabel 	lokasi menunjukkan bahwa paparan polusi cukup terdistribusi secara 	merata, tidak terpusat pada distrik-distrik tertentu. Stasiun 	pemantau yang berlokasi di Jongno-gu (19, Jong-ro 35ga-gil, 	Jongno-gu) tercatat sebagai wilayah dengan kualitas udara terburuk, 	mengakumulasi rata-rata PM2.5 tertinggi sebesar 22,85 µg/m³ 	selama periode tiga tahun tersebut. Tingkat kerentanan yang hampir 	setara juga ditemukan di wilayah Jung-gu (15, Deoksugung-gil) yang 	mencatat rata-rata 22,63 µg/m³. Angka ini menegaskan perlunya 	intervensi mitigasi yang lebih ketat di kedua titik pusat kota 	tersebut.

   ![image-20261102145604179](/home/wafiannafis/.config/Typora/typora-user-images/image-20261102145604179.png)
   **Gambar** **14**. Bar Chart Analisis Kualitas Udara Pada Dua Lokasi Berbeda Kota Seoul Periode 2017-2019

   ## **3.3 Distribusi Kategorisasi Kelayakan Udara**

   ​	Meskipun terjadi lonjakan 	ekstrem pada kuartal pertama dan keempat setiap tahunnya, kalkulasi 	terhadap proporsi kualitas udara perjam menunjukkan bahwa secara 	umum, warga Seoul masih menikmati udara dalam ambang batas yang 	dapat ditoleransi. Selama kurun waktu 2017–2019, mayoritas waktu 	(54,70%) berada pada kategori "Sedang", diikuti oleh 	kategori "Baik" sebesar 40,11%. Kendati demikian, 	terdapat 5,10% jam di mana udara diklasifikasikan sebagai "Tidak 	Sehat", serta 0,09% jam dengan tingkat "Sangat Tidak 	Sehat" (mayoritas terjadi pada Q1).
   ![image-20261102145631143](/home/wafiannafis/.config/Typora/typora-user-images/image-20261102145631143.png)

   **Gambar** **15**.  Pie Chart Kualitas Udara Kota Seoul Periode 2017-2019

   # **DAFTAR PUSTAKA**

[1]	bappe, "Air Pollution in Seoul," Kaggle, 2019. [Online]. Available: https://www.kaggle.com/datasets/bappekim/air-pollution-in-seoul. [Accessed: Nov. 2, 2026].