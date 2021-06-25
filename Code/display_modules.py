# building display functions 
import streamlit as st 
import altair as alt

def plot_skeleton(df,player_name,start,stop):
	if (stop - start) == 1:
		st.header(player_name)
		st.area_chart(df.loc[player_name].iloc[:,start:stop])
		st.write(df.loc[player_name].iloc[:,start:stop])
	else:
		st.header(player_name)
		st.line_chart(df.loc[player_name].iloc[:,start:stop])
		st.write(df.loc[player_name].iloc[:,start:stop])


def df_skeleton(df,player_name,start,stop):
	st.write(df.loc[player_name].iloc[:,start:stop])