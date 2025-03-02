import streamlit as st

import utils

def fn_menu_option_2():
    # utils.fn_markdown_text_1(
    #     'Catatan Kerja',
    #     'Center',
    #     size=31,
    #     color= '#FF0000',
    #     header='h1'
    # )
    # st.divider()

    options = (
        'Membuat Marketplace',
        'Kendala & PR',
        'Lainnya'
    )

    selected_option = st.sidebar.selectbox('Topik', options)

    utils.fn_markdown_text_1(
        selected_option,
        'Center',
        size=21,
        color= '#FF0000',
        header='h2'
    )
    st.divider()
    

    if selected_option == options[0]:
        headers = {
            '🔹 Mimpi/Tujuan' :
            (
                ('Marketplace Campuran',
                 '''\n
                - Menjadi marketplace raksasa yang menjual produk-produk herbal yang sudah umum/banyak dicari dipasaran\n
                - Menjadi salah satu penyumbang pemasukkan terbesar untuk perusahaan\n'''
                ),
                
                ('Marketplace Sehato',
                 '''\n- Memperluas pasar (target: ibu2 yg mencari jajanan sehat untuk anak & keluarga (teh, susu, madu), suplemen (bukan obat) & Keperluan ibu2 lainnya spt garam himalaya, chia seed, dsb)\n
                 - Menjadi marketplace raksasa & kepercayaan masyarakat untuk belanja jajanan sehat (misal: saat ingin membeli madu yg pertama terbetik adalah Sehato; lebih memilih belanja garam himalaya dari Sehato diyakini lebih higienis)\n
                 - Menjadi brand kebanggaan bagi para pengguna/customernya (ada rasa kesenangan tersendiri spt saat seorang menggunakan produk Apple, dsb)\n
                 - Menjadi salah satu penyumbang pemasukkan terbesar untuk perusahaan\n''',
                 'images/sehato-logo-landscape.webp'
                ),
            ),

            '🔹 Langkah/Kegiatan' :
            (
                ('Mengambil Foto/Video Produk',
                '''\n- Untuk keperluan foto/video produk di marketplace\n
                - Untuk membantu menyediakan foto saat ada pesan masuk dari calon customer\n
                - Untuk membuat galeri produk (membantu menyediakan foto2 produk agar tim gudang tidak harus selalu mengambil foto produk saat marketing offline memerlukan foto produk)''',
                ),
                
                ('Aktif Di Sosial Media',
                '''\n- Meningkatkan awareness marketplace Sehato\n
                - Edukasi/memberi pengetahuan seputar produk\n
                - Menaikkan tingkat kepercayaan publik ke marketplace Sehato yang baru dibuat\n
                '''),
                
                ('Mengupload/update produk & Mengikuti Event/Promo di Marketplace',
                '''\n- Memperbarui deskripsi, harga & foto/video produk\n
                - Mengikuti Program Gratis Ongkir Xtra, Program Termurah, dll\n'''
                ),

                ('Mengupload/update Katalog Whatsapp',
                '''\n- Memberikan kesan lebih professional & memudahkan calon customer (via Whatsapp) untuk melihat-lihat produk\n''',
                ),
            ),
        }

        for header in headers:
            st.write('\n')
            st.subheader(header)
            st.write('\n')
            for t in headers[header]:
                with st.expander(t[0]):
                    if len(t) > 2:
                        col1, col2, col3 = st.columns(3)
                        with col2:
                            st.image(t[2])
                    st.text(f'{t[1]}')
            st.divider()
                
    
    elif selected_option == options[1]:
        headers = {
            '🔹 Kendala' :
            (
                ('Masih Baru Dalam Mengelola MP',
                '''\n- Perlu banyak mencari tahu seputar pengelolaan & SEO marketplace\n
                - Perlu banyak uji coba\n''',
                ),
                
                ('Kualitas Foto/Video Masih Standar',
                '''\n- Perlu belajar membuat design untuk gambar/cover/flyer/video produk\n''',
                ),
                
                ('Toko Dimulai Dari 0 & Tanpa Biaya Iklan',
                '''\n- Perlu waktu lebih lama untuk naik/meningkat\n
                - Perlu memperkenalkan toko melalui media sosial untuk meningkatkan traffic & kepercayaan publik\n''',
                ),
            ),

            '🔹 PR' :
            (
                ('Masih Lambat Dalam Proses Input Data ke Odoo',
                '''\n- Membuat template/format export dari Shopee yang compatible untuk di import ke Odoo\n''',
                ),
                
                ('Orderan Baru Diterima Gudang Jam 9:30 (Terlalu Siang Untuk Disiapkan Gudang)',
                '''\n- Menurunkan raw order dari marketplace untuk diberikan ke gudang agar orderan bisa segera disiapkan\n''',
                ),
                
                ('Tim Gudang Perlu Bulak-Balik Mengambil Produk karena Data yg Diberikan per Pesanan',
                '''\n- Penyediaan Lembar ke2 yg sudah di pivot table dari raw order setiap produk bisa langsung diketahui total qtynya\n''',
                ),
                
                ('Tim Delivery Lembur karena Perlu Drop/Mengirimkan Orderan',
                '''\n- Orderan di pickup di gudang\n''',
                ),
                
                ('Orderan di Cancel Karena Stok yang Sering Tiba-Tiba Habis',
                '''\n- Perlu virtual warehouse di Odoo (mirip spt stok toko2 cabang) agar stok lebih terpantau & tidak ditarik oleh orderan lain\n''',
                'images/sentra-herbal-logo.png'
                ),
            ),
        }
        
        for header in headers:
            st.write('\n')
            st.subheader(header)
            st.write('\n')
            for t in headers[header]:
                with st.expander(t[0]):
                    st.text(f'{t[1]}')
                    if len(t) > 2:
                        col1, col2, col3 = st.columns(3)
                        with col2:
                            st.image(t[2])
            st.divider()


'''
## Kegiatan Jan-Feb 2025
1. Membuat Marketplace
Mimpi/Tujuan
Marketplace campuran
Menyumbang omset tertinggi untuk pemasukkan perusahaan dengan cara menjual produk-produk yg sudah umum di pasar herbal

Langkah:
Menjual produk-produk yang ramai/banyak dicari di pasar herbal
Menjual produk dengan harga terendan di pasar online

Marketplace premium (Sehato Official)
Membuka pasar baru (bukan hanya menjual produk2 ke existing customer/pasar herbal)
Menjadi marketplace pusat belanja jajanan sehat (susu, madu, teh) & suplement
Membuka pasar di marketplace internasional (Amazon, Ebay, dsb)

Progress
4 marketplace sudah dibuat, namun masih kecil (omset masih dibawah 10jt)
Perlu menambah/mengubah foto, video & deskripsi produk yg lebih menarik (tidak copy-paste)
Perkembangan Marketplace berbeda-beda (pola/sebabnya belum ketahuan), 1 marketplace (Afwah Herbal, produk campuran) cukup cepat perkembangannya.

Notes
Banyak leads masuk via Whatsapp, namun customer checkout di toko lain sekalipun sudah diberi link produk




2. Mengambil Foto & Video Produk2
Tujuan:
Membantu divisi Marketing Pusat saat memerlukan foto/flyer produk, sehingga tidak perlu berulangkali meminta divisi Warehouse untuk mengambil foto produk.
Memudahkan komunikasi & membuat customer lebih tertarik (dengan menunjukkan foto produk) saat ada pesan masuk baik via Whatsapp, marketplace ataupun sosial media
Upload di Marketplace & posting sosial media


Progress:
Baru terkumpul 30-an produk yg sudah dibuat foto-video
3. Memperbarui katalog whatsapp
Progress:
Masih sedikit produk yg sudah diupload & foto dirasa belum cukup pro

Target:
Semua produk premium
50 produk umum/yg sering dicari dipasaran herbal


4. Diskusi & Membaca-Baca Artikel Seputar Marketplace

Kendala
    1. kepercayaan publik masih kurang - rating toko masih sangat sedikit
        A. Langkah yg memungkinkan - Semi-fake order
            - Orderan/Penjualan produk untuk karyawan dialihkan via marketplace
            - ada 1 akun shopee untuk melakukan checkout
            - fisik produk bisa langsung berikan ke karyawan (pembeli)
            - paket yg dikirim ke kurir hanya bubble wrap + resi pengiriman
            - alamat penerima ke gudang selang (agar bubble wrap bisa dipakai kembali & hanya perlu dipasang resi baru jika ada karyawan yg belanja lagi)
            - harga jual = produk cost + 11% (administrasi marketplace non star seller)
        
        B. Langkah lain - Social Media:
            - aktif sosial media
                - rajin memposting di media sosial (sehari minimal 1x)
                - aktif di group/komunitas/akun2 yg memiliki banyak follower yg berkaitan dengan 'Obat/Suplemen Herbal', 'Kesehatan', atau produk2 yg dijual
	
	- Aktif di akun2 orang/tokoh yg memiliki banyak follower (dengan harapan banyak follower tokoh tsb yg melihat 

    2. masih terkendala untuk proses pengambilan foto, video & pembuatan flyer/gambar yg menarik
        - kemampuan kami dalam mengedit & design yg masih minim
        - produk agak lama untuk disiapkan saat ingin diambil foto | prioritas utama penyiapan untuk orderan agen

    3. skill/pengetahuan/pengalaman yg masih sedikit seputar marketplace
        - 

    








    
# A. Marketplace produk campuran
    Langkah yg bisa/sedang diambil:
    1. meningkatkan kepercayaan publik
        - membuat foto/video yg menarik (dan tidak/belum dipajang di toko lain) | pengerjaan utama saat ini
        - rating/ulasan positif di marketplace
            - (bisa dibantu dengan poin 'kendala' no.1 diatas)
    
    2. mencari tau produk yg ramai dipasaran / sedang momen untuk dijual
        - melihat trend (misal: iklan, penjualan agen pusat, berita)
        - mengunjugi toko2 di marketplace yang menjual produk2 herbal (yg stoknya tersedia di gudang) & menampilkan produk2 terlalis di toko tsb
        - menggunakan keyword/kata kunci yg umum (misal: Cuka Apel) untuk mencari produk di marketplace
        - melalui iklan yg sering muncul

    3. aktif di media sosial
        - membuat & rajin memposting di media sosial (sehari minimal 1x)
        - aktif berkomentar di akun2 yg memiliki banyak follower yg berpotensi tertarik untuk membeli
        
    4. memasang harga dibawah marketplace2 lain (namun tetap diatas harga modal + admin/pajak marketplace)


# B. Sehato | Memasarkan produk2 premium
    1. Sehato Menjadi Brand Kepercayaan
        A1. Sehingga saat mencari 'Madu', 'Susu', 'Teh', 'Obat/Suplemen', masyarakat umum akan terfikir/terbetik 'Sehato'
            - Langkah yg bisa dilakukan:
                - Membuat tulisan/artikel/konten berkualitas/profesional (yg tidak terlalu menunjukkan sedang berjualan) | misal spt: ust zaidul akbar, sekalipun tidak berjualan, namun saat menyebutkan obat tertentu (misal cuka apel), orang2 akan mencari/mau membeli
                - Lebih aktif di media sosial
                    - aktif group/komunitas yg berkaitan dengan 'Obat/Suplemen Herbal', 'Kesehatan', dsb
                    - aktif di akun orang2 yg berpengaruh/memiliki banyak follower yg berpotensi tertarik dengan produk2 Sehato
        
        A2. Verified Account (checklist biru)
        
        A3. Mendapatkan follower lebih banyak / brand awareness yg lebih tinggi
            - give away
                - dengan syarat memfollow & share postingan Sehato Official
            - meningkatkan interaksi
                - tanya-jawab/quiz/pooling
                - 

    2. Brand Sehato dapat dipasarkan di Amazon, Ebay / Marketplace berskala Internasional

    - Langkah yg belum bisa dilakukan - Sehato Official:
        - affiliate
        - ads
        - menyebar flyer


- langkah yg belum bisa diambil
    1. menekan cost / mencari supplier produk2 tsb yg bisa memberi harga termurah
    2. 

## Target
    - menjadi Star Seller dalam waktu 3 bulan (akhir April 2025) | 





## Kegiatan - Jan 2025

- Belajar membuat foto & video produk untuk di marketplace
    - tujuan: membuat kesan yang lebih menarik, agar customer lebih tertarik (setidaknya untuk meng-klik)

- Membaca-baca seputar SEO (search engine optimization), LSI (Latent Semantic Indexing) untuk di shopee
    - tujuan: agar produk di shopee lebih berpotensi tampil di pencarian

- Mencari -secara online- komunitas/group herbal, kesehatan, obat2-an dari penyakit tertentu yg berpeluang untuk memperkenalkan produk2 sentra herbal
    - membuat postingan/share artikel seputar kesehatan | tujuan: meningkatkan kepercayaan/membuat publik 

- Memposting-posting produk di media sosial
    - tujuan: memperkenalkan produk2 via sosial media

- Memperbarui Catalog Produk di Whatsapp
    - 
- Broadcast pesan berisi flyer ke karyawan

- Menjawab pesan2/pertanyaan yg masuk (kebanyakan menanyakan produk yg tidak dijual di Sentra Herbal)

- Broadcast/memberikan penawaran produk ke calon customer


## Yg perlu ditingkatkan

1. Rating/Review Toko

    Langkah:
    - Penjualan produk ke karyawan dialihkan via marketplace
        - ada 1 akun shopee untuk melakukan checkout
        - fisik produk bisa langsung berikan ke karyawan (pembeli)
        - resi/paket yg dikirim ke kurir hanya bubble wrap
        - alamat penerima ke gudang selang (agar bubble wrap bisa dipakai kembali & hanya perlu dipasang resi baru jika ada karyawan yg belanja lagi)
        - harga jual produk cost + 12% (administrasi marketplace)

2. Foto & Video Produk
    Langkah:
    1. Dapat mengambil foto yg berkualitas sehingga nama/brand lebih terlihat menarik bagi calon customers | currently: low
    2. Dapat membuat gambar & video yg menarik  | currently: low
        - Video:
            - singkat (durasi tidak lebih dari 30 detik)
            - menyampaikan isi produk
                - manfaat
                - komposisi
                - izin edar
                - cara/aturan pakai

'''

'''

'''


'''
## 
Target MP brand/produk umum

Target MP produk premium
Target utama


## Yang perlu dipenuhi/dicapai dibulan berikutnya
1. Omset lebih tinggi dari bulan sebelumnya
2. Dapat mengambil foto yg berkualitas sehingga nama/brand lebih menarik bagi para calon customer | now: low
3. Dapat membuat gambar & video yg menarik  | now: low
    - Video:
        - singkat (durasi tidak lebih dari 30 detik)
        - menyampaikan isi produk
            - manfaat
            - komposisi
            - izin edar
            - cara/aturan pakai

4. 
'''


'''
## Jan 2025

1. Membuat Marketplace
    progress:
        - sudah dibuat namun masih kecil
        - perlu foto2, video & deskripsi produk yg lebih menarik (tidak copy-paste)
    
    target: omset 5jt | belum tercapai, baru tercapai 3jt-an (bulan januari)

2. mengambil foto & video produk2 untuk di marketplace & sosial media
    progress: baru terkumpul 30-an produk yg sudah dibuat foto-video
    target: 100 foto-video produk (yg ramai/sering dicari) & semua produk premium | belum tercapai
        
3. Memperbarui katalog whatsapp
    progress: masih sedikit produk yg sudah diupload & foto belum dirasa cukup pro
    target: semua produk premium | belum tercapai

4 diskusi / mengobrol dengan beberapa orang & membaca2 artikel seputar tips di marketplace
    progress:
        - SEO (search engine optimization), memilih kata kunci yang   & LSI (latent semantic indexing), menambahkan keyword yg berkaitan dengan produk, misal 'EtawaFresh' menjadi 'Sehato EtawaFresh 500gr - Susu Etawa Kesehatan Tulang'
            - hasilnya: belum terlihat 
        - Berdasarkan manual/panduan Shopee & info dari Ridwan, penggunaan hashtag secara teori berpengaruh
            - hasilnya:  belum terlihat (Ridwan sendiri menginfokan jarang menggunakan hashtag karena hasilnya tidak terlihat)
        - info dari ridwan, peranan paling utama/paling kuat di algoritma pencarian//penjualan adalah dari iklan, rating & penjualan
        - Membuat promo/event di shopee
            - mendaftar gratis ongkir
            - mendaftar cashback extra
            - event 2.2
            - 

## kendala (secara umum):
    1. kepercayaan publik masih kurang - rating toko masih sangat sedikit
        A. langkah yg memungkinkan:
            - Orderan/Penjualan produk untuk karyawan dialihkan via marketplace
            - ada 1 akun shopee untuk melakukan checkout
            - fisik produk bisa langsung berikan ke karyawan (pembeli)
            - paket yg dikirim ke kurir hanya bubble wrap + resi pengiriman
            - alamat penerima ke gudang selang (agar bubble wrap bisa dipakai kembali & hanya perlu dipasang resi baru jika ada karyawan yg belanja lagi)
            - harga jual produk cost + 11% (administrasi marketplace non star seller)
        
        B. langkah lain:
            - aktif sosial media
                - rajin memposting di media sosial (sehari minimal 1x)
                - aktif di group/komunitas/akun2 yg memiliki banyak follower yg berkaitan dengan 'Obat/Suplemen Herbal', 'Kesehatan', atau produk2 yg dijual

    2. masih terkendala untuk proses pengambilan foto, video & pembuatan flyer/gambar yg menarik
        - kemampuan kami dalam mengedit & design yg masih minim
        - produk agak lama untuk disiapkan saat ingin diambil foto | prioritas utama penyiapan untuk orderan agen

    3. skill/pengetahuan/pengalaman yg masih sedikit seputar marketplace
        - 

    








    
# A. Marketplace produk campuran
    Langkah yg bisa/sedang diambil:
    1. meningkatkan kepercayaan publik
        - membuat foto/video yg menarik (dan tidak/belum dipajang di toko lain) | pengerjaan utama saat ini
        - rating/ulasan positif di marketplace
            - (bisa dibantu dengan poin 'kendala' no.1 diatas)
    
    2. mencari tau produk yg ramai dipasaran / sedang momen untuk dijual
        - melihat trend (misal: iklan, penjualan agen pusat, berita)
        - mengunjugi toko2 di marketplace yang menjual produk2 herbal (yg stoknya tersedia di gudang) & menampilkan produk2 terlalis di toko tsb
        - menggunakan keyword/kata kunci yg umum (misal: Cuka Apel) untuk mencari produk di marketplace
        - melalui iklan yg sering muncul

    3. aktif di media sosial
        - membuat & rajin memposting di media sosial (sehari minimal 1x)
        - aktif berkomentar di akun2 yg memiliki banyak follower yg berpotensi tertarik untuk membeli
        
    4. memasang harga dibawah marketplace2 lain (namun tetap diatas harga modal + admin/pajak marketplace)


# B. Sehato | Memasarkan produk2 premium
    1. Sehato Menjadi Brand Kepercayaan
        A1. Sehingga saat mencari 'Madu', 'Susu', 'Teh', 'Obat/Suplemen', masyarakat umum akan terfikir/terbetik 'Sehato'
            - Langkah yg bisa dilakukan:
                - Membuat tulisan/artikel/konten berkualitas/profesional (yg tidak terlalu menunjukkan sedang berjualan) | misal spt: ust zaidul akbar, sekalipun tidak berjualan, namun saat menyebutkan obat tertentu (misal cuka apel), orang2 akan mencari/mau membeli
                - Lebih aktif di media sosial
                    - aktif group/komunitas yg berkaitan dengan 'Obat/Suplemen Herbal', 'Kesehatan', dsb
                    - aktif di akun orang2 yg berpengaruh/memiliki banyak follower yg berpotensi tertarik dengan produk2 Sehato
        
        A2. Verified Account (checklist biru)
        
        A3. Mendapatkan follower lebih banyak / brand awareness yg lebih tinggi
            - give away
                - dengan syarat memfollow & share postingan Sehato Official
            - meningkatkan interaksi
                - tanya-jawab/quiz/pooling
                - 

    2. Brand Sehato dapat dipasarkan di Amazon, Ebay / Marketplace berskala Internasional

    - Langkah yg belum bisa dilakukan - Sehato Official:
        - affiliate
        - ads
        - menyebar flyer


- langkah yg belum bisa diambil
    1. menekan cost / mencari supplier produk2 tsb yg bisa memberi harga termurah
    2. 

## Target
    - menjadi Star Seller dalam waktu 3 bulan (akhir April 2025) | 





## Kegiatan - Jan 2025

- Belajar membuat foto & video produk untuk di marketplace
    - tujuan: membuat kesan yang lebih menarik, agar customer lebih tertarik (setidaknya untuk meng-klik)

- Membaca-baca seputar SEO (search engine optimization), LSI (Latent Semantic Indexing) untuk di shopee
    - tujuan: agar produk di shopee lebih berpotensi tampil di pencarian

- Mencari -secara online- komunitas/group herbal, kesehatan, obat2-an dari penyakit tertentu yg berpeluang untuk memperkenalkan produk2 sentra herbal
    - membuat postingan/share artikel seputar kesehatan | tujuan: meningkatkan kepercayaan/membuat publik 

- Memposting-posting produk di media sosial
    - tujuan: memperkenalkan produk2 via sosial media

- Memperbarui Catalog Produk di Whatsapp
    - 
- Broadcast pesan berisi flyer ke karyawan

- Menjawab pesan2/pertanyaan yg masuk (kebanyakan menanyakan produk yg tidak dijual di Sentra Herbal)

- Broadcast/memberikan penawaran produk ke calon customer


## Yg perlu ditingkatkan

1. Rating/Review Toko

    Langkah:
    - Penjualan produk ke karyawan dialihkan via marketplace
        - ada 1 akun shopee untuk melakukan checkout
        - fisik produk bisa langsung berikan ke karyawan (pembeli)
        - resi/paket yg dikirim ke kurir hanya bubble wrap
        - alamat penerima ke gudang selang (agar bubble wrap bisa dipakai kembali & hanya perlu dipasang resi baru jika ada karyawan yg belanja lagi)
        - harga jual produk cost + 12% (administrasi marketplace)

2. Foto & Video Produk
    Langkah:
    1. Dapat mengambil foto yg berkualitas sehingga nama/brand lebih terlihat menarik bagi calon customers | currently: low
    2. Dapat membuat gambar & video yg menarik  | currently: low
        - Video:
            - singkat (durasi tidak lebih dari 30 detik)
            - menyampaikan isi produk
                - manfaat
                - komposisi
                - izin edar
                - cara/aturan pakai

'''

'''

'''


'''
## 
Target MP brand/produk umum

Target MP produk premium
Target utama


## Yang perlu dipenuhi/dicapai dibulan berikutnya
1. Omset lebih tinggi dari bulan sebelumnya
2. Dapat mengambil foto yg berkualitas sehingga nama/brand lebih menarik bagi para calon customer | now: low
3. Dapat membuat gambar & video yg menarik  | now: low
    - Video:
        - singkat (durasi tidak lebih dari 30 detik)
        - menyampaikan isi produk
            - manfaat
            - komposisi
            - izin edar
            - cara/aturan pakai

4. 
'''