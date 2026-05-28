import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="StudyMatch – Find Your Study Partner",
    page_icon="📚",
    layout="wide",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* ── Background ── */
.stApp {
    background: linear-gradient(135deg, #0f1624 0%, #1a2438 50%, #0f1624 100%);
    color: #e8eaf0;
}

/* ── Hero header ── */
.hero {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    background: linear-gradient(90deg, #64b5f6, #a78bfa, #f48fb1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.3rem;
}
.hero p {
    color: #9aa3b8;
    font-size: 1.05rem;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: #131c2e !important;
    border-right: 1px solid #2a3550;
}
section[data-testid="stSidebar"] * {
    color: #c9d1e0 !important;
}

/* ── Metric row ── */
.metric-row {
    display: flex;
    gap: 1rem;
    justify-content: center;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
}
.metric-card {
    background: #1e2d47;
    border: 1px solid #2e4070;
    border-radius: 12px;
    padding: 0.8rem 1.6rem;
    text-align: center;
    min-width: 140px;
}
.metric-card .num {
    font-size: 1.6rem;
    font-weight: 700;
    color: #64b5f6;
}
.metric-card .lbl {
    font-size: 0.78rem;
    color: #7888a0;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

/* ── Partner cards ── */
.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(270px, 1fr));
    gap: 1.2rem;
    padding: 0.5rem 0;
}
.partner-card {
    background: #1a2640;
    border: 1px solid #2a3a5c;
    border-radius: 16px;
    padding: 1.4rem;
    transition: transform 0.2s, box-shadow 0.2s;
    position: relative;
    overflow: hidden;
}
.partner-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #64b5f6, #a78bfa);
}
.partner-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.4);
}
.card-header {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin-bottom: 0.9rem;
}
.avatar {
    width: 46px;
    height: 46px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.3rem;
    flex-shrink: 0;
}
.avatar-male   { background: linear-gradient(135deg, #1565c0, #42a5f5); }
.avatar-female { background: linear-gradient(135deg, #880e4f, #f48fb1); }
.card-name {
    font-size: 1.05rem;
    font-weight: 600;
    color: #dde3f0;
}
.card-age {
    font-size: 0.8rem;
    color: #7888a0;
}
.badge {
    display: inline-block;
    padding: 0.2rem 0.65rem;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin-right: 0.3rem;
    margin-bottom: 0.4rem;
}
.badge-course     { background: #1e3a5f; color: #64b5f6; border: 1px solid #2a5080; }
.badge-time       { background: #1e3520; color: #66bb6a; border: 1px solid #2a5030; }
.badge-gender-m   { background: #1a2e50; color: #90caf9; border: 1px solid #2a4070; }
.badge-gender-f   { background: #3e1a30; color: #f48fb1; border: 1px solid #60234a; }
.card-desc {
    font-size: 0.83rem;
    color: #8898b0;
    line-height: 1.55;
    margin-top: 0.6rem;
}
.match-score {
    position: absolute;
    top: 1rem; right: 1rem;
    background: linear-gradient(135deg, #1565c0, #7b1fa2);
    color: #fff;
    font-size: 0.72rem;
    font-weight: 700;
    padding: 0.25rem 0.6rem;
    border-radius: 20px;
}

/* ── No results ── */
.no-results {
    text-align: center;
    padding: 3rem 1rem;
    color: #5a6880;
}
.no-results .icon { font-size: 3rem; margin-bottom: 0.5rem; }

/* ── Section title ── */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.25rem;
    color: #c9d1e0;
    margin-bottom: 1rem;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid #2a3550;
}

/* ── Divider ── */
hr { border-color: #2a3550 !important; }
</style>
""", unsafe_allow_html=True)

# ── Fake user database ────────────────────────────────────────────────────────
USERS = [
    {
        "name": "Aiden Tan",
        "gender": "Male",
        "course": "Engineering",
        "age": 21,
        "available": (9, 12),   # 9 AM – 12 PM
        "description": "Computer engineering student passionate about embedded systems and robotics. Looking for a focused study buddy for circuit analysis and calculus.",
    },
    {
        "name": "Priya Nair",
        "gender": "Female",
        "course": "Engineering",
        "age": 20,
        "available": (13, 17),  # 1 PM – 5 PM
        "description": "Civil engineering sophomore who loves structural design. Prefers afternoon sessions and group problem-solving for thermodynamics and fluid mechanics.",
    },
    {
        "name": "Marcus Lim",
        "gender": "Male",
        "course": "Business",
        "age": 22,
        "available": (10, 14),
        "description": "Business management student with a focus on marketing strategy. Enjoys case-study discussions and is preparing for his internship interviews.",
    },
    {
        "name": "Sofia Chen",
        "gender": "Female",
        "course": "Business",
        "age": 19,
        "available": (9, 13),
        "description": "Finance & business double major who is meticulous with Excel models. Great study partner for accounting, stats, and economics problem sets.",
    },
    {
        "name": "Raj Patel",
        "gender": "Male",
        "course": "Architecture",
        "age": 23,
        "available": (14, 17),
        "description": "Third-year architecture student specialising in sustainable urban design. Looks for a creative partner for design critique sessions and AutoCAD workshops.",
    },
    {
        "name": "Amelia Wong",
        "gender": "Female",
        "course": "Architecture",
        "age": 21,
        "available": (9, 15),
        "description": "Architecture student with a passion for interior spatial planning. Loves long studio sessions and can mentor on hand-rendering and model-making.",
    },
    {
        "name": "Daniel Ooi",
        "gender": "Male",
        "course": "Medicine",
        "age": 24,
        "available": (9, 11),
        "description": "Pre-clinical medical student grinding anatomy and physiology. Prefers Pomodoro-style morning study blocks and quizzing each other with flashcards.",
    },
    {
        "name": "Hannah Yap",
        "gender": "Female",
        "course": "Medicine",
        "age": 23,
        "available": (12, 17),
        "description": "Medical student in her second year, focusing on pathology and pharmacology. Open to forming a study group for OSCE preparation and case discussions.",
    },
    {
        "name": "Ethan Ng",
        "gender": "Male",
        "course": "Finance",
        "age": 20,
        "available": (11, 16),
        "description": "Finance student interested in quantitative investing and derivatives. Looking for a partner to work through Bloomberg terminal exercises and CFA prep materials.",
    },
    {
        "name": "Chloe Rajan",
        "gender": "Female",
        "course": "Finance",
        "age": 22,
        "available": (9, 14),
        "description": "Finance major specialising in corporate valuation. Enjoys whiteboard sessions for DCF models and financial statement analysis. Morning person!",
    },
]

COURSE_COLORS = {
    "Engineering":   "#1565c0",
    "Business":      "#6a1b9a",
    "Architecture":  "#bf360c",
    "Medicine":      "#1b5e20",
    "Finance":       "#e65100",
}

HOUR_LABELS = {h: f"{h if h <= 12 else h-12} {'AM' if h < 12 else 'PM'}" for h in range(9, 18)}

def hours_overlap(user_range, filter_range):
    """Return True if the two (start, end) hour ranges overlap."""
    return user_range[0] <= filter_range[1] and user_range[1] >= filter_range[0]

def match_score(user, gender, course, age, avail):
    """Simple 0–100 compatibility score."""
    score = 0
    if user["gender"] == gender:
        score += 30
    if user["course"] == course:
        score += 40
    if abs(user["age"] - age) <= 1:
        score += 15
    elif abs(user["age"] - age) <= 3:
        score += 8
    overlap_hours = min(user["available"][1], avail[1]) - max(user["available"][0], avail[0])
    if overlap_hours > 0:
        score += min(15, overlap_hours * 5)
    return score

# ── Sidebar filters ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🎓 Your Profile")
    st.markdown("---")

    my_gender = st.selectbox("Gender", ["Male", "Female"])

    my_course = st.selectbox(
        "Course",
        ["Engineering", "Business", "Architecture", "Medicine", "Finance"]
    )

    st.markdown("**Available Time**")
    my_time = st.slider(
        "Available time range",
        min_value=9, max_value=17,
        value=(9, 17),
        format="%d:00",
        label_visibility="collapsed",
    )
    st.caption(f"🕐 {HOUR_LABELS[my_time[0]]} → {HOUR_LABELS[my_time[1]]}")

    my_age = st.slider("Your Age", min_value=18, max_value=25, value=20)

    st.markdown("---")
    st.markdown("**Filter Preferences**")
    filter_same_course  = st.checkbox("Same course only", value=False)
    filter_overlap_time = st.checkbox("Must share available time", value=False)
    st.markdown("---")
    st.caption("StudyMatch v1.0 · Built with Streamlit")

# ── Filter & score users ──────────────────────────────────────────────────────
results = []
for u in USERS:
    if filter_same_course and u["course"] != my_course:
        continue
    if filter_overlap_time and not hours_overlap(u["available"], my_time):
        continue
    score = match_score(u, my_gender, my_course, my_age, my_time)
    results.append({**u, "score": score})

results.sort(key=lambda x: x["score"], reverse=True)

# ── Main content ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>📚 StudyMatch</h1>
  <p>Find your perfect study partner — same course, same schedule, same drive.</p>
</div>
""", unsafe_allow_html=True)

# Metric row
total    = len(results)
same_crs = sum(1 for r in results if r["course"] == my_course)
has_ovlp = sum(1 for r in results if hours_overlap(r["available"], my_time))

st.markdown(f"""
<div class="metric-row">
  <div class="metric-card"><div class="num">{total}</div><div class="lbl">Matches Found</div></div>
  <div class="metric-card"><div class="num">{same_crs}</div><div class="lbl">Same Course</div></div>
  <div class="metric-card"><div class="num">{has_ovlp}</div><div class="lbl">Time Overlap</div></div>
</div>
""", unsafe_allow_html=True)

# Section label
st.markdown(
    f'<div class="section-title">✨ Best Matches for {my_course} · Age {my_age} · '
    f'{HOUR_LABELS[my_time[0]]} – {HOUR_LABELS[my_time[1]]}</div>',
    unsafe_allow_html=True,
)

# ── Cards ─────────────────────────────────────────────────────────────────────
if not results:
    st.markdown("""
    <div class="no-results">
      <div class="icon">🔍</div>
      <p>No partners match your current filters.<br>Try relaxing the filters in the sidebar.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    # Render cards in rows of 3
    cols_per_row = 3
    for i in range(0, len(results), cols_per_row):
        row = results[i:i + cols_per_row]
        cols = st.columns(len(row))
        for col, u in zip(cols, row):
            with col:
                avatar_cls   = "avatar-male" if u["gender"] == "Male" else "avatar-female"
                avatar_icon  = "👨‍💻" if u["gender"] == "Male" else "👩‍💻"
                gender_badge = "badge-gender-m" if u["gender"] == "Male" else "badge-gender-f"
                avail_label  = f"{HOUR_LABELS[u['available'][0]]} – {HOUR_LABELS[u['available'][1]]}"
                overlap_note = "⏰ Time overlap!" if hours_overlap(u["available"], my_time) else ""

                st.markdown(f"""
                <div class="partner-card">
                  <div class="match-score">⭐ {u['score']}%</div>
                  <div class="card-header">
                    <div class="avatar {avatar_cls}">{avatar_icon}</div>
                    <div>
                      <div class="card-name">{u['name']}</div>
                      <div class="card-age">Age {u['age']}</div>
                    </div>
                  </div>
                  <span class="badge badge-course">{u['course']}</span>
                  <span class="badge {gender_badge}">{u['gender']}</span>
                  <br>
                  <span class="badge badge-time">🕐 {avail_label}</span>
                  {f'<span class="badge badge-time">{overlap_note}</span>' if overlap_note else ''}
                  <p class="card-desc">{u['description']}</p>
                </div>
                """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)