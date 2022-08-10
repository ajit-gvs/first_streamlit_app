
import streamlit
streamlit.title("My parents new healthy diner")
streamlit.header("Breakfast Menu")
streamlit.text("idli and sambhar")
streamlit.text("bread and butter")
streamlit.text("🤞dosa and chutney😏")
streamlit.header("Make your own smoothie")
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
