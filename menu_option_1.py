import streamlit as st

import utils

def fn_menu_option_1(df):
    # title / header
    utils.fn_markdown_text_1(
        "Data Penjualan",
        "Center",
        size=25,
        color= "#ff0000",
        header="h2"
        )
    st.write('---')

    # Filter options
    filtered_df = df

    # buat opsi tamilan tabel: by marketplace: omzet (subtotal); by product: qty terjual; by salesperson: omzet

    radio_options = ['Rinci', 'By Product', 'By Marketplace/Partner']
    radio_option = st.sidebar.radio('Tampilan', radio_options)
    st.sidebar.write('---')

    # filter options

    col1, col2, col3 = st.columns([4.75, 0.5, 4.75])
    
    with col1:
        filter_year_index = st.multiselect('Tahun:', df['Tahun'].unique())
        if filter_year_index:
            filtered_df = filtered_df[df['Tahun'].isin(filter_year_index)]

        filter_month_index = st.multiselect('Bulan Ke:', df['Bulan'].unique())
        if filter_month_index:
            filtered_df = filtered_df[df['Bulan'].isin(filter_month_index)]

        filter_week_index = st.multiselect('Pekan Ke:', df['Index Pekan'].unique())
        if filter_week_index:
            filtered_df = filtered_df[df['Index Pekan'].isin(filter_week_index)]

    with col3:    
        filter_order_status = st.multiselect('Status Orderan', df['Status Order'].unique(), default='sale')
        if filter_order_status:
            filtered_df = filtered_df[df['Status Order'].isin(filter_order_status)]
        
        filter_mp_name = st.multiselect('Marketplace/Partner', df['Nama MP'].unique())
        if filter_mp_name:
            filtered_df = filtered_df[~df['Nama MP'].isin(filter_mp_name)]
        
        filter_product_category = st.multiselect('Kategori Produk', df['Kategori Produk'].unique())
        if filter_product_category:
            filtered_df = filtered_df[df['Kategori Produk'].isin(filter_product_category)]

    if radio_option == radio_options[0]:
        if filter_order_status == ['cancel']:
            display_df = filtered_df[[
                'No SO',
                'Tanggal',
                'Bulan',
                # 'Nama MP',
                'Nama Produk',
                'Qty Order',
            ]]

        else:
            display_df = filtered_df[[
                'No SO',
                'Tanggal',
                'Bulan',
                # 'Nama MP',
                'Nama Produk',
                'Qty Order',
                'Harga Jual',
                'Discount (%)',
                'Subtotal',
                ]]
        
        display_df = display_df.set_index('No SO')
    
    elif radio_option == radio_options[1]:
        display_df = filtered_df.groupby('Nama Produk', as_index=True)['Qty Order'].sum()
    
    elif radio_option == radio_options[2]:
        display_df = filtered_df.groupby('Nama MP', as_index=True)['Subtotal'].sum()

    st.write('---')

    # Visualise the data
    st.dataframe(display_df, use_container_width=True)

    # show the total omzet
    with st.sidebar:
        total_values = filtered_df['Subtotal'].sum()
        total_non_premium = filtered_df.loc[filtered_df['Kategori Produk'] == 'Produk Non Premium', 'Subtotal'].sum()
        total_premium = filtered_df.loc[filtered_df['Kategori Produk'] == 'Produk Premium', 'Subtotal'].sum()
        st.write('Omset')
        st.write(f'`Premium: Rp. {int(total_premium):,}`')
        st.write(f'`Non Premium: Rp. {int(total_non_premium):,}`')
        st.write(f'`Total: Rp. {int(total_values):,}`')
    
