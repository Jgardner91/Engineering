# making streamlit app 

import pandas as pd 
import streamlit as st 
import altair as alt
from PIL import Image 


from sqlalchemy import create_engine
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

import display_modules as dsp
from sqlalchemy import create_engine


sns.set_context("talk")
sns.set_style('dark')


def plot_map():
	variables = ['Age', 'Team', 'League', 'POS', 'G', 'MP', 'PER', 'TS%', '3PAr', 'FTr',
       'ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS',
       'DWS', 'WS', 'WS_48', 'OBPM', 'DBPM', 'BPM', 'VORP']
	plt_map = {variables[i]:i for i in range(len(variables))}
	return plt_map

def read_data():

	# instantiating engine
	cnx1 = create_engine('sqlite:///NBA.db').connect()
	cnx2 = create_engine('sqlite:///wnba.db').connect()

	

	# reading data from SQLite database 
	NBA = pd.read_sql('AdvStats', cnx1)

	# reindexing data 
	NBA.rename(columns={'level_0': 'PlayerName', 'level_1': 'Year'}, inplace=True)
	NBA.set_index(keys=['PlayerName','Year'], drop=True, append=False, inplace=True, verify_integrity=False)
	
	# reading data from SQLite database 
	WNBA = pd.read_sql('AdvStatsW', cnx2)

	# reindexing data 
	WNBA.rename(columns={'level_0': 'PlayerName', 'level_1': 'Year'}, inplace=True)
	WNBA.set_index(keys=['PlayerName','Year'], drop=True, append=False, inplace=True, verify_integrity=False)
	
	return NBA,WNBA

def get_names_NBA(Stats_DF):
	stats_df = Stats_DF.copy()
	stats_df.reset_index(inplace=True)
	names = list(stats_df['PlayerName'])
	NAMES = []
	for i in range(len(names)):
		if names[i] not in NAMES:
			NAMES.append(names[i])
	return NAMES

def get_names_WNBA(Stats_DF):
	stats_df = Stats_DF.copy()
	stats_df.reset_index(inplace=True)
	names = list(stats_df['PlayerName'])
	NAMES = []
	for i in range(len(names)):
		if names[i] not in NAMES:
			NAMES.append(names[i])
	return NAMES



def streamlit(Stats_DF,WNBA,NAMES,NAMESwnba,plot_map):
	pick_league = st.sidebar.selectbox("League",['NBA','WNBA'])
	if pick_league == 'NBA':
		drop_down = st.sidebar.selectbox("Explore",['Home Page','Player Plots','Definitions','Player Comparisons'])
		if drop_down == 'Home Page':
			st.markdown("# NBA Avanced Player Statistics")
			st.write("")
			image = Image.open('WMCJ.jpeg')
			st.image(image)
			st.markdown("            *Woody Harrelson and Wesley Snipes in 'White Man Cant Jump'*")

		if drop_down == 'Definitions':
			stat_type = st.sidebar.selectbox('Definitions',['Age', 'Team', 'League', 'POS', 'G', 'MP', 'PER', 'TS%', '3PAr', 'FTr',
       		'ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS',
       		'DWS', 'WS', 'WS_48', 'OBPM', 'DBPM', 'BPM', 'VORP'])
			if stat_type == 'OWS':
				image = Image.open('offense2.jpeg')
				st.image(image)
				st.write("Offensive Win Shares")
				st.write("Offensive Win Shares is a metric that estimates the number of wins a player produces for their team due to their offensive ability")
				link = 'https://www.basketball-reference.com/about/ws.html'
				st.markdown(link, unsafe_allow_html=True)
				st.write("More Info here ^^^")
			
			if stat_type == 'DWS':
				image = Image.open('defense.jpeg')
				st.image(image)
				st.write("Defensive Win Shares")
				st.write("A player’s DWS is calculated by estimating the number of points allowed per 100 defensive possessions.")
				link = 'https://www.basketball-reference.com/about/ws.html'
				st.markdown(link,unsafe_allow_html=True)
				st.write("More Info here^^^")

		


		if drop_down == 'Player Plots':
			st.write("PLAYER STATS ")
			stats_1 = st.checkbox("Win Share Stats")
			stats_2 = st.checkbox("Traditional Stats")
			stats_3 = st.checkbox("All Time PER")
			stats_4 = st.checkbox("All time WS/48")
		
			if stats_1:
			
				st.write(" ")
				st.write("Win Share Stats")
				player_name = st.sidebar.selectbox("Player List",NAMES)
				type_display = st.sidebar.selectbox("Display Type",['Single','All'])

				if type_display == 'All':

					dsp.plot_skeleton(Stats_DF,player_name,18,21)
					
			
				if type_display == 'Single':
				
					OWS = st.checkbox('OWS')
					DWS = st.checkbox('DWS')
					WS = st.checkbox('WS')
					WS_48 = st.checkbox('WS/48')
				
					if OWS:
						dsp.plot_skeleton(Stats_DF,player_name,18,19)
				
					if DWS:
						dsp.plot_skeleton(Stats_DF,player_name,19,20)
						
					if WS:
						dsp.plot_skeleton(Stats_DF,player_name,20,21)

					if WS_48:
						dsp.plot_skeleton(Stats_DF,player_name,21,22)



			if stats_2:
				st.write(" ")
				st.write("Traditional Stats")
				player_name = st.sidebar.selectbox("Player List",NAMES)
				type_display = st.sidebar.selectbox("TypeDisplay",['Single','All'])
			
				if type_display == 'All':
					dsp.plot_skeleton(Stats_DF,player_name,10,18)
					

				if type_display == 'Single':
					ORB_ = st.checkbox('ORB%')
					DRB_ = st.checkbox('DRB%')
					TRB_ = st.checkbox('TRB%')
					AST_ = st.checkbox('AST%')
					STL_ = st.checkbox('STL%')
					BLK_ = st.checkbox('BLK%')
					TOV_ = st.checkbox('TOV%')
					USG_ = st.checkbox('USG%')

					if ORB_:
						dsp.plot_skeleton(Stats_DF,player_name,10,11)
					
					if DRB_:
						dsp.plot_skeleton(Stats_DF,player_name,11,12)
						
					if TRB_:
						dsp.plot_skeleton(Stats_DF,player_name,12,13)
						
					if AST_:
						dsp.plot_skeleton(Stats_DF,player_name,13,14)
						
					if STL_:
						dsp.plot_skeleton(Stats_DF,player_name,14,15)
						
					if BLK_:
						dsp.plot_skeleton(Stats_DF,player_name,15,16)
						
					if TOV_:
						dsp.plot_skeleton(Stats_DF,player_name,16,17)
						
					if USG_:
						dsp.plot_skeleton(Stats_DF,player_name,17,18)
			

			if stats_3:
				cnx3 = create_engine('sqlite:///NBA.db').connect()
				NBAPER = pd.read_sql('MAXPER', cnx3)

				NBAPER.rename(columns={'level_0': 'PlayerName', 'level_1': 'Year'}, inplace=True)
				NBAPER.set_index(keys=['PlayerName','Year'], drop=True, append=False, inplace=True, verify_integrity=False)
				st.write(NBAPER)
				#st.bar_chart(NBAPER)


			if stats_4:
				cnx4 = create_engine('sqlite:///NBA.db').connect()
				NBAWSFE = pd.read_sql('WSPG', cnx4)
				NBAWSFE.rename(columns={'level_0': 'PlayerName', 'level_1': 'Year'}, inplace=True)
				NBAWSFE.set_index(keys=['PlayerName','Year'], drop=True, append=False, inplace=True, verify_integrity=False)
				st.write(NBAWSFE)
				


					

	if pick_league == 'WNBA':
		
		drop_down = st.sidebar.selectbox("Explore",['Home Page','Player Plots','Definitions','Player Comparisons'])
		if drop_down == 'Home Page':
			st.markdown("# WNBA Advanced Player Statistics")
			st.write("")
			image = Image.open('wnbapic.jpeg')
			st.image(image)
			st.markdown('*Sidra (Erika Ringor) and Monica become friends when they compete professionally overseas. (Screen shot from “Love & Basketball”)*')

		if drop_down == 'Definitions':
			stat_type = st.sidebar.selectbox('Definitions',['Age', 'Team', 'League', 'POS', 'G', 'MP', 'PER', 'TS%', '3PAr', 'FTr',
       		'ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS',
       		'DWS', 'WS', 'WS_48', 'OBPM', 'DBPM', 'BPM', 'VORP'])
			if stat_type == 'OWS':

				image = Image.open('offense2.jpeg')
				st.image(image)
				st.write("Offensive Win Shares")
				st.write("Offensive Win Shares is a metric that estimates the number of wins a player produces for their team due to their offensive ability")
				link = 'https://www.basketball-reference.com/about/ws.html'
				st.markdown(link, unsafe_allow_html=True)
				st.write("More Info here ^^^")
			if stat_type == 'DWS':
				image = Image.open('defense.jpeg')
				st.image(image)
				st.write("Defensive Win Shares")
				st.write("A player’s DWS is calculated by estimating the number of points allowed per 100 defensive possessions.")
				link = 'https://www.basketball-reference.com/about/ws.html'
				st.markdown(link,unsafe_allow_html=True)
				st.write("More Info here^^^")

		if drop_down == 'Player Plots':
			st.write("PLAYER STATS ")
			stats_1 = st.checkbox("Win Share Stats")
			stats_2 = st.checkbox("Traditional Stats")
			
		
			if stats_1:
			
				st.write(" ")
				st.write("Win Share Stats")
				player_name = st.sidebar.selectbox("Player List",NAMESwnba)
				type_display = st.sidebar.selectbox("Display Type",['Single','All'])

				if type_display == 'All':
					dsp.plot_skeleton(WNBA,player_name,16,19)
			
				if type_display == 'Single':
				
					OWS = st.checkbox('OWS')
					DWS = st.checkbox('DWS')
					WS = st.checkbox('WS')
					WS_48 = st.checkbox('WS/48')
				
					if OWS:
						dsp.plot_skeleton(WNBA,player_name,16,17)
				
					if DWS:
						dsp.plot_skeleton(WNBA,player_name,17,18)
						
				
					if WS:
						dsp.plot_skeleton(WNBA,player_name,18,19)



			if stats_2:
				st.write(" ")
				st.write("Traditional Stats")
				player_name = st.sidebar.selectbox("Player List",NAMESwnba)
				type_display = st.sidebar.selectbox("TypeDisplay",['Single','All'])
			
				if type_display == 'All':
					dsp.plot_skeleton(WNBA,player_name,8,16)

				if type_display == 'Single':
					ORB_ = st.checkbox('ORB%')
					DRB_ = st.checkbox('DRB%')
					TRB_ = st.checkbox('TRB%')
					AST_ = st.checkbox('AST%')
					STL_ = st.checkbox('STL%')
					BLK_ = st.checkbox('BLK%')
					TOV_ = st.checkbox('TOV%')
					USG_ = st.checkbox('USG%')

					if ORB_:
						dsp.plot_skeleton(WNBA,player_name,8,9)
					
					if DRB_:
						dsp.plot_skeleton(WNBA,player_name,9,10)

					if TRB_:
						dsp.plot_skeleton(WNBA,player_name,10,11)

					if AST_:
						dsp.plot_skeleton(WNBA,player_name,11,12)

					if STL_:
						dsp.plot_skeleton(WNBA,player_name,12,13)

					if BLK_:
						dsp.plot_skeleton(WNBA,player_name,13,14)

					if TOV_:
						dsp.plot_skeleton(WNBA,player_name,14,15)

					if USG_:
						dsp.plot_skeleton(WNBA,player_name,15,16)

					

			if stats_3:
				cnx3 = create_engine('sqlite:///NBA.db').connect()
				NBA = pd.read_sql('MAXPER', cnx1)
				st.bar_chart(NBA)




	
	


def main():

	plt_map = plot_map()
	NBA,WNBA= read_data()
	NAMES = get_names_NBA(NBA)
	NAMESwnba = get_names_WNBA(WNBA)
	streamlit(NBA,WNBA,NAMES,NAMESwnba,plt_map)

if __name__ == '__main__':
	main()



