import streamlit as st

import utils

def fn_menu_option_2():
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
                 '''\n
                 - Memperluas pasar (target: ibu2 yg mencari jajanan sehat untuk anak & keluarga (teh, susu, madu), suplemen (bukan obat) & Keperluan ibu2 lainnya spt garam himalaya, chia seed, dsb)\n
                 - Menjadi marketplace raksasa & kepercayaan masyarakat untuk belanja jajanan sehat (misal: saat ingin membeli madu yg pertama terbetik adalah Sehato; lebih memilih belanja garam himalaya dari Sehato diyakini lebih higienis)\n
                 - Menjadi brand kebanggaan bagi para pengguna/customernya (ada rasa kesenangan tersendiri spt saat seorang menggunakan produk Apple, dsb)\n
                 - Menjadi salah satu penyumbang pemasukkan terbesar untuk perusahaan\n''',
                 'images/sehato-logo-landscape.webp'
                ),
            ),

            '🔹 Langkah/Kegiatan' :
            (
                ('Mengambil Foto/Video Produk',
                '''\n
                - Untuk keperluan foto/video produk di marketplace\n
                - Untuk membantu menyediakan foto saat ada pesan masuk dari calon customer\n
                - Untuk membuat galeri produk (membantu menyediakan foto2 produk agar tim gudang tidak harus selalu mengambil foto produk saat marketing offline memerlukan foto produk)''',
                ),
                
                ('Aktif Di Sosial Media',
                '''\n
                - Meningkatkan awareness marketplace Sehato\n
                - Edukasi/memberi pengetahuan seputar produk\n
                - Menaikkan tingkat kepercayaan publik ke marketplace Sehato yang baru dibuat\n
                '''),
                
                ('Mengupload/update produk & Mengikuti Event/Promo di Marketplace',
                '''\n
                - Memperbarui deskripsi, harga & foto/video produk\n
                - Mengikuti Program Gratis Ongkir Xtra, Program Termurah, dll\n'''
                ),

                ('Mengupload/update Katalog Whatsapp',
                '''\n
                - Memberikan kesan lebih professional & memudahkan calon customer (via Whatsapp) untuk melihat-lihat produk\n''',
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
                '''\n
                - Perlu banyak mencari tahu seputar pengelolaan & SEO marketplace\n
                - Perlu banyak uji coba\n''',
                ),
                
                ('Kualitas Foto/Video Masih Standar',
                '''\n
                - Perlu belajar membuat design untuk gambar/cover/flyer/video produk\n''',
                ),
                
                ('Toko Dimulai Dari 0 & Tanpa Biaya Iklan',
                '''\n
                - Perlu waktu lebih lama untuk naik/meningkat\n
                - Perlu memperkenalkan toko melalui media sosial untuk meningkatkan traffic & kepercayaan publik\n''',
                ),
            ),

            '🔹 PR' :
            (
                ('Masih Lambat Dalam Proses Input Data ke Odoo',
                '''\n
                - Membuat template/format export dari Shopee yang compatible untuk di import ke Odoo\n''',
                ),
                
                ('Orderan Baru Diterima Gudang Jam 9:30 (Terlalu Siang Untuk Disiapkan Gudang)',
                '''\n
                - Menurunkan raw order dari marketplace untuk diberikan ke gudang agar orderan bisa segera disiapkan\n''',
                ),
                
                ('Tim Gudang Perlu Bulak-Balik Mengambil Produk karena Data yg Diberikan per Pesanan',
                '''\n
                - Penyediaan Lembar ke2 yg sudah di pivot table dari raw order setiap produk bisa langsung diketahui total qtynya\n''',
                ),
                
                ('Tim Delivery Lembur karena Perlu Drop/Mengirimkan Orderan',
                '''\n
                - Orderan di pickup di gudang\n''',
                ),
                
                ('Orderan di Cancel Karena Stok yang Sering Tiba-Tiba Habis',
                '''\n
                - Perlu virtual warehouse di Odoo (mirip spt stok toko2 cabang) agar stok lebih terpantau & tidak ditarik oleh orderan lain\n''',
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

