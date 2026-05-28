import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="Study Buddy Matcher",
    page_icon="📚",
    layout="wide"
)

# 2. Mock Data (5 Fake Users)
@st.cache_data
def load_mock_users():
    return [
        {
            "Name": "Ahmad",
            "Gender": "Male",
            "Age": 20,
            "Course": "Engineering",
            "Available Start": 9,
            "Available End": 12,
            "Description": "Hey! I'm a year 2 Mechanical Engineering student. Looking for someone to smash through advanced calculus tutorials with."
        },
        {
            "Name": "Sarah",
            "Gender": "Female",
            "Age": 22,
            "Course": "Business",
            "Available Start": 13,
            "Available End": 16,
            "Description": "Final year Marketing major. Let's study for the upcoming finals and maybe exchange case study notes!"
        },
        {
            "Name": "Chloe",
            "Gender": "Female",
            "Age": 19,
            "Course": "Architecture",
            "Available Start": 10,
            "Available End": 15,
            "Description": "Freshman architecture student here. Spending most of my days in the studio. Looking for a peer to stay motivated during long sketching hours."
        },
        {
            "Name": "Daniel",
            "Gender": "Male",
            "Age": 24,
            "Course": "Medicine",
            "Available Start": 14,
            "Available End": 17,
            "Description": "Med student trying to survive anatomy. Best at studying in quiet library corners. Hit me up if you want a silent study partner."
        },
        {
            "Name": "Emily",
            "Gender": "Female",
            "Age": 21,
            "Course": "Finance",
            "Available Start": 11,
            "Available End": 14,
            "Description": "Corporate finance enthusiast. Love practicing financial modeling. Looking for someone to crack investment analysis problems together."
        }
    ]

users = load_mock_users()

# 3. App Header
st.title("📚 Study Buddy Matcher")
st.subheader("Find your perfect study partner based on your course and availability!")
st.write("Adjust your preferences on the sidebar to filter out potential matches.")

st.markdown("---")

# 4. Sidebar Controls (User Preferences)
st.sidebar.header("Your Preferences & Info")

# Gender Filter
filter_gender = st.sidebar.selectbox(
    "Preferred Partner Gender",
    options=["Any", "Male", "Female"]
)

# Course Filter
filter_course = st.sidebar.selectbox(
    "Select Course / Major",
    options=["Engineering", "Business", "Architecture", "Medicine", "Finance"]
)

# Age Filter (Slider 18 to 25)
filter_age_range = st.sidebar.slider(
    "Age Range",
    min_value=18,
    max_value=25,
    value=(18, 25)  # Default selection range
)

# Time Filter (Slider 9am to 5pm mapped to 9 to 17)
filter_time_range = st.sidebar.slider(
    "Available Time Range",
    min_value=9,
    max_value=17,
    value=(9, 17),
    format="%d:00"
)

# Display user's choice cleanly in the sidebar
def format_time(hour):
    if hour < 12:
        return f"{hour} AM"
    elif hour == 12:
        return "12 PM"
    else:
        return f"{hour - 12} PM"

st.sidebar.markdown(f"**Filtering for:** {format_time(filter_time_range[0])} to {format_time(filter_time_range[1])}")


# 5. Matching Logic & Filtering
matched_users = []

for user in users:
    # Check Gender
    if filter_gender != "Any" and user["Gender"] != filter_gender:
        continue
        
    # Check Course
    if user["Course"] != filter_course:
        continue
        
    # Check Age Range
    if not (filter_age_range[0] <= user["Age"] <= filter_age_range[1]):
        continue
        
    # Check Time Overlap (If they have at least 1 hour of overlapping free time)
    # Filter range: [filter_time_range[0], filter_time_range[1]]
    # User range:   [user["Available Start"], user["Available End"]]
    overlap_start = max(filter_time_range[0], user["Available Start"])
    overlap_end = min(filter_time_range[1], user["Available End"])
    
    if overlap_start < overlap_end:
        matched_users.append(user)


# 6. Displaying Results
st.header(f"🎯 Potential Matches ({len(matched_users)})")

if len(matched_users) > 0:
    # Display matches in a clean grid/card system
    for match in matched_users:
        with st.container():
            st.markdown(f"### 👤 {match['Name']} ({match['Age']}, {match['Gender']})")
            
            # Use columns for metadata
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**📚 Course:** {match['Course']}")
            with col2:
                st.markdown(f"**⏰ Free Time:** {format_time(match['Available Start'])} - {format_time(match['Available End'])}")
            
            st.write(f"*\"{match['Description']}\"*")
            
            if st.button(f"Connect with {match['Name']}", key=match['Name']):
                st.success(f"Request sent! We'll notify {match['Name']} that you want to study together.")
            
            st.markdown("---")
else:
    st.warning("No exact matches found for your current criteria. Try widening your age range, time preferences, or select a different course!")