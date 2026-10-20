
import streamlit as st

st.set_page_config(
    page_title="Football Value Scanner",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Football Value Scanner")
st.write("Your player-prop analysis dashboard")

st.info(
    "This is the first version. We will add player statistics, "
    "shots on target, fouls committed, bookmaker odds and value "
    "calculations next."
)

st.header("Analyse a market")

player = st.selectbox(
    "Select player",
    ["Erling Haaland"]
)

market = st.selectbox(
    "Select market",
    ["Shots on target", "Fouls committed"]
)

threshold = st.selectbox(
    "Select target",
    [1, 2, 3, 4]
)

odds = st.number_input(
    "Bookmaker decimal odds",
    min_value=1.01,
    value=1.80,
    step=0.05
)

st.write("### Your selection")
st.write(f"Player: {player}")
st.write(f"Market: {threshold}+ {market}")
st.write(f"Bookmaker odds: {odds:.2f}")

st.caption(
    "This prototype does not yet calculate predictions or "
    "recommend bets. Those features will be added after setup."
)
