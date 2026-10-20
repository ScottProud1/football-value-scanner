
import streamlit as st

st.set_page_config(
    page_title="Football Value Scanner",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ Football Value Scanner")
st.write("Player shots on target and fouls committed")

st.warning(
    "Demo version: the calculations use the probability you enter. "
    "They are not live predictions and are not connected to player data yet."
)

st.header("1. Select your market")

player = st.selectbox(
    "Player",
    ["Erling Haaland"]
)

market = st.selectbox(
    "Market",
    ["Shots on target", "Fouls committed"]
)

threshold = st.selectbox(
    "Target",
    [1, 2, 3, 4],
    format_func=lambda x: f"{x}+"
)

st.header("2. Enter historical results")

st.write(
    "Enter how many of the player's last 10 matches had complete "
    "data for this market, and how many of those matches reached "
    "your target."
)

col1, col2 = st.columns(2)

with col1:
    recorded = st.number_input(
        "Matches with recorded data",
        min_value=1,
        max_value=10,
        value=6
    )

with col2:
    hits = st.number_input(
        "Recorded matches that hit the target",
        min_value=0,
        max_value=10,
        value=5
    )

st.header("3. Compare with bookmaker odds")

odds = st.number_input(
    "Bookmaker decimal odds",
    min_value=1.01,
    max_value=1000.0,
    value=1.80,
    step=0.05
)

if hits > recorded:
    st.error("Hits cannot be greater than recorded matches.")
else:
    probability = hits / recorded
    implied_probability = 1 / odds
    expected_return = probability * odds - 1

    st.header("4. Results")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Historical hit rate",
        f"{probability:.1%}",
        f"{hits} of {recorded} matches"
    )

    col2.metric(
        "Bookmaker implied probability",
        f"{implied_probability:.1%}"
    )

    col3.metric(
        "Expected return per £1",
        f"£{expected_return:+.2f}"
    )

    difference = probability - implied_probability

    st.write(
        f"**Historical probability minus implied probability:** "
        f"{difference * 100:+.1f} percentage points"
    )

    if expected_return > 0:
        st.success(
            "The entered historical rate is above the break-even "
            "rate for these odds. This does not establish a real edge."
        )
    else:
        st.info(
            "The entered historical rate does not exceed the "
            "break-even rate for these odds."
        )

    st.caption(
        "Important: this is a basic historical comparison, not a "
        "reliable prediction. Small samples, missing statistics, "
        "opponent strength, player minutes and bookmaker margin can "
        "make the actual probability very different."
    )

