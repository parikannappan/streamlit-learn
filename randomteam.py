import random
import streamlit as st 
# List of 10 players
#players = ["Jram", "pari", "Valentine", "Siraj", "Ryan",
#           "Praveena", "Caldwell", "Mani", "Rajeev", "Rahul"]
text1 = st.text_input("Player 1", key="player_1")
text2 = st.text_input("Player 2", key = "player_2")
text3 = st.text_input("Player 3", key="player_3")
text4 = st.text_input("Player 4", key = "player_4")
text5 = st.text_input("Player 5", key="player_5")
text6 = st.text_input("Player 6", key = "player_6")
text7 = st.text_input("Player 7", key="player_7")
text8 = st.text_input("Player 8", key = "player_8")
text9 = st.text_input("Player 7", key="player_9")
text10 = st.text_input("Player 8", key = "player_10")

players = [text1, text2, text3, text4, text5,
           text6, text7, text8, text9, text10]

# Shuffle the list to ensure randomness
random.shuffle(players)

# Create 5 teams with 2 players each
teams = [players[i:i + 2] for i in range(0, len(players), 2)]
#teams = [players[i:i + 1] for i in range(0, len(players), 2)]

# Print the teams
for idx, team in enumerate(teams, 1):
    print(f"Team {idx}: {team}")