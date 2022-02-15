import streamlit as st
from datetime import date, timedelta

st.title("Maiar Farm Calculator")

# userDF = pd.DataFrame({"Username":[0]})
# username = st.text_input("Create a username").lower()
#
# if submitbutton := st.button("Submit"):
#     login = pd.read_csv(r"C:\Users\sabzu\Documents\MaiarFarming\Usernames.csv")
#     for i in login["Username"]:
#         if i == username:
#             st.write("Member!")
#         else:
#             print(login["Username"].convert_dtypes())
#             print(login)
#             login.to_csv("Usernames.csv", header=True)

mexPrice = st.number_input("Price of Mex")
st.write("Price you entered:", mexPrice)

col1, col2 = st.columns(2)
with col1:
    oneMin = 36.56
    st.write(f"{oneMin} Mex/minute =", "$", (mexPrice * oneMin).__round__(2))

    halfhour = (oneMin*30).__round__(2)
    st.write(f"{halfhour} Mex/30mins =", "$", (mexPrice * halfhour).__round__(2))

    hour = (halfhour*2).__round__(2)
    st.write(f"{hour} Mex/hours =", "$", (mexPrice * hour).__round__(2))

    sixHour = (hour * 6).__round__(2)
    st.write(f"{sixHour} Mex/6hours =", "$", (mexPrice * sixHour).__round__(2))

    halfDay = (sixHour * 2).__round__(2)
    st.write(f"{halfDay} Mex/12hours =", "$", (mexPrice * halfDay).__round__(2))

    day = (halfDay * 2).__round__(2)
    st.write(f"{day} Mex/Day =", "$", (mexPrice * day).__round__(2))

    week = (day * 7).__round__(2)
    st.write(f"{week} Mex/Week =", "$", (mexPrice * week).__round__(2))

    month = (week * 4).__round__(2)
    st.write(f"{month} Mex/Month =", "$", (mexPrice * month).__round__(2))

    three_month = (month * 3).__round__(2)
    st.write(f"{three_month} Mex/3Months =", "$", (mexPrice * three_month).__round__(2))

    halfYear = (three_month * 2).__round__(2)
    st.write(f"{halfYear} Mex/6Months =", "$", (mexPrice * halfYear).__round__(2))

    year = (halfYear * 2).__round__(2)
    st.write(f"{year} Mex/Year =", "$", (mexPrice * year).__round__(2))

with col2:
    mexten = ((10/mexPrice).__round__(2))
    st.write(f"Mex/$10 = {mexten}")

    hoursten = ((mexten/oneMin) / 60).__round__(2)
    st.write(f"hours/$10 = {hoursten}")

    st.write("Time for 100% ROI:")
    rewards = st.number_input("Rewards earned in $", value=0)

    days = ((3150.16 - rewards) / (mexPrice*day))
    st.write(f"Days until 100% ROI: {days}")

    first100 = date.today() + timedelta(days=days)
    st.write("Expected Date of 100% ROI:", first100)

    secondhundred = first100 + timedelta(days = (3150.16 / (mexPrice*day)))
    st.write("Expected Date of 200% ROI:", secondhundred)