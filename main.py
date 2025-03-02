import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas

from streamlit_option_menu import option_menu  # pip install streamlit-option-menu

import utils
from menu_option_0 import fn_menu_option_0
from menu_option_1 import fn_menu_option_1
from menu_option_2 import fn_menu_option_2

def login():
	password = st.text_input("Enter your password:", type="password")
	# print(password)
	# if password == default_passwd:
	# 	st.session_state.logged_in = password
	st.write(password)
	return password

def main():
	## inital page config
	st.set_page_config(
		page_title="Sentra Herbal | Menjaga Arti Sehat Kita",
		page_icon=":leaves:",
		layout="wide",
		initial_sidebar_state="expanded"
	)

	## hide streamlit header & footer styles
	utils.fn_hide_streamlit_styles()

	# Initialize session state variables
	DEFAULT_PASSWORD = 'sentraherbal'
	if "authenticated" not in st.session_state:
		st.session_state["authenticated"] = False

	# Login section
	if not st.session_state["authenticated"]:
		# st.title("Login Page")

		# Password input field
		password = st.text_input("Password:", type="password", key="password")
		
		if st.button("Login"):
			# st.session_state["password"] = password
			if st.session_state["password"] == DEFAULT_PASSWORD:
				st.session_state["authenticated"] = True
				st.success("Selamat, silahkan click tombol Login sekali lagi")
			else:
				st.session_state["authenticated"] = False
				st.error("Password tidak benar")

		st.stop()

	## load the raw data into pandas dataframe
	df_raw = utils.csv_to_df("raw_data/sales_data.csv")
	
	df_raw_2 = utils.fn_split_datetime_column(df_raw, "Order Lines/Created on")
	df_raw_2 = utils.fn_rename_columns(df_raw_2)
	df_raw_2 = utils.fn_add_week_index(df_raw_2)

	## horizontal nav menu ##
	menu_options = (
		"Home",
		"Penjualan",
		"Catatan Kerja",
		"Ringkasan",
		'---',
	)

	with st.sidebar:
		picked_option = option_menu(
			"Index",
			menu_options,
			icons=None,
			menu_icon="cast",
			default_index=0,
			orientation="vertical")
		st.write('---')

	if picked_option == menu_options[0]:
		fn_menu_option_0(df_raw_2)

	elif picked_option == menu_options[1]:
		fn_menu_option_1(df_raw_2)

	elif picked_option == menu_options[2]:
		fn_menu_option_2()

	elif picked_option == menu_options[3]:
		pass

	# st.write(st.session_state.logged_in)	
	
if __name__ == '__main__':
	main()