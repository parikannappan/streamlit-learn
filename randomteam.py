import random
import streamlit as st 
# List of 10 players
st.set_page_config(page_title="Make random team", page_icon=":game_die:")
st.title("  :game_die: :blue[Random team creation]")
col1, col2 = st.columns(2)
with col1: 
      text1 = st.text_input("Player 1")
      print('text1 -', text1)
      text2 = st.text_input("Player 2")
      text3 = st.text_input("Player 3", key="player_3")
      text4 = st.text_input("Player 4", key = "player_4")
      text5 = st.text_input("Player 5", key="player_5")
with col2: 
      text6 = st.text_input("Player 6", key = "player_6")
      text7 = st.text_input("Player 7", key="player_7")
      text8 = st.text_input("Player 8", key = "player_8")
      text9 = st.text_input("Player 9", key="player_9")
      text10 = st.text_input("Player 10", key = "player_10")

players = [text1, text2, text3, text4, text5,
           text6, text7, text8, text9, text10]
print(players)
# Shuffle the list to ensure randomness
random.shuffle(players)

# Create 5 teams with 2 players each
if len(text10) > 0:
    teams = [players[i:i + 2] for i in range(0, len(players), 2)]
    #teams = [players[i:i + 1] for i in range(0, len(players), 2)]

    # Print the teams
    for idx, team in enumerate(teams, 1):
     st.write("Team {idx}: {team}")