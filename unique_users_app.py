import streamlit as st
import pandas as pd
import math

st.set_page_config(page_title="Unique Users Estimator", page_icon="📊")

st.title("📊 מחשבון משתמשים ייחודיים + גרף הצטברות עם רוויה")

st.markdown("""
הכנס את הנתונים הבאים כדי להעריך את מספר המשתמשים הייחודיים באפליקציה שלך.
""")

# קלט מהמשתמש
rps = st.number_input("📡 בקשות לשנייה (RPS)", min_value=1, value=3000, step=100)
req_per_user = st.number_input("👤 בקשות ממוצעות למשתמש לשנייה", min_value=1, value=10, step=1)
session_length = st.number_input("⏱ משך סשן ממוצע (שניות)", min_value=1, value=60, step=1)
time_minutes = st.number_input("🕒 טווח זמן לחישוב (דקות)", min_value=1, value=10, step=1)

# סליידר רוויה
saturation_ratio = st.slider(
    "⚖️ יחס רוויה (0 = תמיד משתמשים חדשים, 1 = רוויה מהירה)",
    min_value=0.0, max_value=1.0, value=0.2, step=0.05
)

# חישוב משתמשים בו־זמניים
concurrent_users = rps / req_per_user
max_possible_unique = concurrent_users * (time_minutes * 60) / session_length

# סימולציה עם רוויה
times = list(range(1, time_minutes * 60 + 1))  # שניות
unique_counts = []
unique_so_far = 0

for t in times:
    # כמה משתמשים חדשים נכנסים בשנייה הזו
    new_users = concurrent_users / session_length
    # מקטינים לפי הרוויה (ככל שמתקרבים למקסימום – נכנסים פחות חדשים)
    saturation_factor = 1 - (unique_so_far / max_possible_unique) * saturation_ratio
    new_users *= max(saturation_factor, 0)
    unique_so_far += new_users
    unique_counts.append(unique_so_far)

# טבלה ל־Streamlit
df = pd.DataFrame({
    "שניות": times,
    "משתמשים ייחודיים מצטברים": unique_counts
})

# הצגת תוצאות
st.subheader("🔍 תוצאה")
st.write(f"**משתמשים בו־זמניים משוערים:** {concurrent_users:,.0f}")
st.write(f"**משתמשים ייחודיים ב-{time_minutes} דקות (עם רוויה):** {unique_so_far:,.0f}")

# גרף
st.subheader("📈 גרף הצטברות המשתמשים הייחודיים")
st.line_chart(df.set_index("שניות"))

st.caption("החישוב מבוסס על הנחות ממוצעות ואינו מדויק ב-100%.")
