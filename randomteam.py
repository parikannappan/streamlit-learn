import random
import streamlit as st 
# List of 10 players
st.set_page_config(page_title="Make random team", page_icon=":game_die:")
st.title("  :game_die: :blue[Random team creation]")
col1, col2 ,col3, col4 = st.columns(4)
with col1: 
      text1 = st.text_input("Player 1")
      text2 = st.text_input("Player 2")      
      text3 = st.text_input("Player 3", key="player_3")
with col2:      
      text4 = st.text_input("Player 4", key = "player_4")
      text5 = st.text_input("Player 5", key="player_5") 
      text6 = st.text_input("Player 6", key = "player_6")
with col3:            
      text7 = st.text_input("Player 7", key="player_7")      
      text8 = st.text_input("Player 8", key = "player_8")
      text9 = st.text_input("Player 9", key="player_9")
with col4:      
      
      text10 = st.text_input("Player 10", key = "player_10")
      text11 = st.text_input("Player 11", key = "player_11")
      text12 = st.text_input("Player 12", key = "player_12")

#players = [text1, text2, text3, text4, text5,
#           text6, text7, text8, text9, text10]
players = [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10,
           text11, text12]

print(players)
# Shuffle the list to ensure randomness
random.shuffle(players)

# Create 5 teams with 2 players each
teamnames = []
if len(text12) > 0:
    teams = [players[i:i + 2] for i in range(0, len(players), 2)]
    print(f'{teams=}')
    #teams = [players[i:i + 1] for i in range(0, len(players), 2)]

    # Print the team dict
    teamd = {}
    for idx, team in enumerate(teams, 1):
     #st.text(team)
     #st.write(f"Team {idx}: {team}")
      teamd['team' + str(idx)] = team
    print(teamd)
    st.table(teamd)
    st.dataframe(teamd)
    #with open(teamd, "rb") as template_file:
    #    template_byte = template_file.read()
    #st.download_button(label="Click to Download Template File",
    #                    data=template_byte,
    #                    file_name="temd.xlsx")
    teamnames = list(teamd.keys())
    print(teamnames)    
from itertools import combinations
#teamnames
#players = ['player1', 'player2', 'player3', 'player4']
comb_set = combinations(teamnames, 2)
#print(comb_set)
game_dict = {}

for idx, team in enumerate(comb_set, 1):
    #print(f"Game {gamd}: {team[0]+ 'vs' +team[1]}")
    game_dict['game' + str(idx)] = [team[0]+ ' ' + 'vs' + ' ' +team[1]]
print(game_dict)
st.dataframe(game_dict)
#st.write(game_dict)