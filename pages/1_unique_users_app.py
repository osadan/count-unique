import streamlit as st
import pandas as pd

st.set_page_config(page_title="Unique Users Graph", page_icon="📈", layout="wide")

st.title("📊 מחשבון משתמשים ייחודיים + גרף הצטברות עם רוויה")

# Create two columns: left for inputs, right for graph
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📥 קלט נתונים")
    rps = st.number_input("📡 בקשות לשנייה (RPS)", min_value=1, value=3000, step=100)
    req_per_user = st.number_input("👤 בקשות ממוצעות למשתמש לשנייה", min_value=1, value=10, step=1)
    session_length = st.number_input("⏱ משך סשן ממוצע (שניות)", min_value=1, value=60, step=1)
    time_minutes = st.number_input("🕒 טווח זמן לחישוב (דקות)", min_value=1, value=10, step=1)
    saturation_ratio = st.slider(
        "⚖️ יחס רוויה (0 = תמיד משתמשים חדשים, 1 = רוויה מהירה)",
        min_value=0.0, max_value=1.0, value=0.2, step=0.05
    )

# Calculations
concurrent_users = rps / req_per_user
max_possible_unique = concurrent_users * (time_minutes * 60) / session_length

times = list(range(1, time_minutes * 60 + 1))
unique_counts = []
unique_so_far = 0

for _ in times:
    new_users = concurrent_users / session_length
    saturation_factor = 1 - (unique_so_far / max_possible_unique) * saturation_ratio
    new_users *= max(saturation_factor, 0)
    unique_so_far += new_users
    unique_counts.append(unique_so_far)

df = pd.DataFrame({
    "שניות": times,
    "משתמשים ייחודיים מצטברים": unique_counts
})

with col2:
    st.markdown("### 📈 גרף הצטברות")
    st.line_chart(df.set_index("שניות"))

st.markdown("---")
st.subheader("🔍 תוצאה")
st.write(f"**משתמשים בו־זמניים משוערים:** {concurrent_users:,.0f}")
st.write(f"**משתמשים ייחודיים ב-{time_minutes} דקות (עם רוויה):** {unique_so_far:,.0f}")

st.caption("החישוב מבוסס על הנחות ממוצעות ואינו מדויק ב-100%.")
