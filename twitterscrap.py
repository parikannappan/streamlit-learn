from ntscraper import Nitter
import streamlit as st 
st.set_page_config(page_title="Extract tweets", page_icon="twitter", layout="wide")
st.title("  :incoming_enveloper: :blue-background[Twitter Search App ()]")
#st.markdown(MobileMonneyTransfer.png, unsafe_allow_html=True)
#st.title("  :bank: :blue[Bank Statement Search App]")
scraper = Nitter(log_level=1, skip_instance_check=False)
tweets = scraper.get_tweets('Overdose_AI', mode="user", number=5)
tweets1 = scraper.get_tweets('DeFi_Hanzo', mode="user", number=5)
for tweet in tweets['tweets']:
  tweettime = tweet.get('date')
  tweetscomb = tweet.get('text')
  st.write('*Overdose_AI*')
  st.write(tweettime)
  st.write(tweetscomb)
  list_coins = [word for word in tweetscomb.split() if word.startswith('$')]
  st.write(f'{list_coins=}')
for tweet1 in tweets1['tweets']:
  tweettime1 = tweet1.get('date')
  tweetscomb1 = tweet1.get('text')
  list_coins1 = [word for word in tweetscomb1.split() if word.startswith('$')]
  st.write('*DeFi_Hanzo*')
  st.write(tweettime1)
  st.write(tweetscomb1)
  st.write(f'{list_coins1=}')
