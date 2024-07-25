import random
import streamlit as st 
# List of 10 players
#players = ["Jram", "pari", "Valentine", "Siraj", "Ryan",
#           "Praveena", "Caldwell", "Mani", "Rajeev", "Rahul"]
stinput = st.text_input("Enter keyword to search -")


# Shuffle the list to ensure randomness
random.shuffle(players)

# Create 5 teams with 2 players each
teams = [players[i:i + 2] for i in range(0, len(players), 2)]
#teams = [players[i:i + 1] for i in range(0, len(players), 2)]

# Print the teams
for idx, team in enumerate(teams, 1):
    print(f"Team {idx}: {team}")