# Data Analysis - Database Bank Marketing Campaign
## Introduction
Project2 ini terkait dengan pembuatan model menggunakan machine learning. Pemodelan didasarkan pada data bank_marketing_campaign.csv. Dilakukan pemodelan untuk dapat memprediksi customer yang akan memilih produk long term deposit dari bank. Selain itu dilakukan analisis data untuk dapat memberikan rekomedasi perihal solusi yang mungkin dapat dilakukan oleh bank dalam menarik customer untuk menggunakan produknya.

## Source
### Data Info - Data_bank_marketing_campaign.csv
Data diambil dari : https://drive.google.com/file/d/1PQTTWgITANg5Av-1Ot28KCIHVyFaCmUK/view?usp=sharing
yang merupakan adaptasi dari Kaggle : Bank Marketing Dataset (https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset?datasetId=4471&sortBy=voteCount), dengan sedikit penyesuaian pada komponen data.
### Native Data Info - Bank Marketing Dataset
Author : S.Moro, P.Cortez & P.Rita
Year : 2014, June
Source : [Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31, June 2014
### Data Attribute Information
Data data_bank_marketing_campaign.csv terdiri atas beberapa atribut, dan atribut-atribut ini dapat digunakan dalam proses analisis lebih lanjut terhadap behaviour dari customer dalam melakukan deposit. Detail dari atributnya adalah sebagai berikut :
| Attribute | Data Numeric/Categorical | Description |
| --- | --- | --- |
| age | Numeric | Umur dari customer |
| job | Categorical | Pekerjaan dari customer |
| balance | Numeric | Jumlah tabungan yang dimiliki individual |
| housing | Categorical | Apakah customer memiliki cicilan rumah ? <YES/NO> |
| loan | Categorical | Apakah customer memiliki cicilan rumah ? <YES/NO> |
| contact | Categorical | Tipe komunikasi yang dilakukan |
| month | Categorical | Bulan terakhir kontak dalam tahun terkait |
| campaign | Numeric | Jumlah kontak yang dilakukan selama campaign terhadap customer terkait |
| pdays | Numeric | Jumlah hari yang telah berlalu setelah klien terakhir dihubungi dari campaign sebelumnya <br><-1, berarti client belum pernah dikontak sebelumnya> |
| poutcome | Categorical | Hasil dari marketing campaign sebelumnya |
| deposit | Categorical | Apakah customer melakukan deposit ? <YES/NO> |

## DB 
    ![Alt](/image/erd .png "Title")

## Analysis Perform by
Monika Pangestu - monikapangestu20@gmail.com
