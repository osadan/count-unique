import streamlit as st

st.set_page_config(page_title="Unique Users App", page_icon="📊", layout="wide")

st.title("📊 Unique Users Estimator")
st.markdown("""
ברוך הבא למחשבון המשתמשים הייחודיים!  
כאן תוכל להעריך את מספר המשתמשים הייחודיים באפליקציה שלך על בסיס:
- בקשות לשנייה (RPS)
- בקשות ממוצעות למשתמש
- משך סשן ממוצע
- יחס רוויה

---
### ⬇️ לעבור לעמוד הגרף:
[לחץ כאן כדי לפתוח את המחשבון והגרף](Unique%20Users%20Graph)
""")
