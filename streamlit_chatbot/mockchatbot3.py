import streamlit as st
import random

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="StudyMatch",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ──────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700;800&family=DM+Serif+Display:ital@0;1&display=swap');

html, body, [class*="css"] {
    font-family: 'Sora', sans-serif;
}

/* ── Background ── */
.stApp {
    background: linear-gradient(135deg, #0f0c29 0%, #1a1040 40%, #24243e 100%);
    min-height: 100vh;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.04) !important;
    border-right: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(20px);
}
[data-testid="stSidebar"] * {
    color: #e8e0ff !important;
}
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stSlider label,
[data-testid="stSidebar"] .stMultiSelect label,
[data-testid="stSidebar"] .stRadio label {
    font-size: 0.78rem !important;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #a78bfa !important;
    font-weight: 600 !important;
}

/* ── Hero header ── */
.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: 3.2rem;
    background: linear-gradient(90deg, #c084fc, #818cf8, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
    margin-bottom: 0.2rem;
}
.hero-sub {
    color: #94a3b8;
    font-size: 1rem;
    font-weight: 300;
    letter-spacing: 0.04em;
    margin-bottom: 2.5rem;
}

/* ── Match card ── */
.match-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(167,139,250,0.25);
    border-radius: 20px;
    padding: 1.8rem;
    margin-bottom: 1.2rem;
    position: relative;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    backdrop-filter: blur(12px);
}
.match-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(129,140,248,0.2);
}
.match-card.top-match {
    border-color: rgba(192,132,252,0.55);
    background: rgba(167,139,250,0.08);
    box-shadow: 0 0 0 1px rgba(192,132,252,0.3), 0 8px 32px rgba(129,140,248,0.15);
}

/* ── Match badge ── */
.match-badge {
    position: absolute;
    top: 1.2rem;
    right: 1.2rem;
    padding: 0.35rem 0.85rem;
    border-radius: 99px;
    font-size: 0.88rem;
    font-weight: 700;
    letter-spacing: 0.03em;
}
.badge-high   { background: linear-gradient(90deg,#7c3aed,#4f46e5); color:#fff; }
.badge-medium { background: linear-gradient(90deg,#0ea5e9,#6366f1); color:#fff; }
.badge-low    { background: rgba(100,116,139,0.4); color:#cbd5e1; }

/* ── Avatar circle ── */
.avatar {
    width: 56px; height: 56px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.6rem;
    margin-bottom: 0.9rem;
    border: 2px solid rgba(167,139,250,0.4);
}
.avatar-m { background: linear-gradient(135deg,#1e3a5f,#2563eb30); }
.avatar-f { background: linear-gradient(135deg,#4a1a5f,#7c3aed30); }

/* ── Name / meta ── */
.card-name {
    font-size: 1.15rem;
    font-weight: 700;
    color: #f1f5f9;
    margin-bottom: 0.25rem;
}
.card-major {
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #a78bfa;
    font-weight: 600;
    margin-bottom: 0.8rem;
}
.card-detail {
    color: #94a3b8;
    font-size: 0.85rem;
    line-height: 1.7;
}
.tag {
    display: inline-block;
    background: rgba(99,102,241,0.2);
    border: 1px solid rgba(99,102,241,0.35);
    color: #c4b5fd;
    border-radius: 99px;
    padding: 0.15rem 0.6rem;
    font-size: 0.75rem;
    margin: 0.15rem 0.1rem;
}
.top-label {
    display: inline-block;
    background: linear-gradient(90deg,#7c3aed,#4f46e5);
    color: #fff;
    font-size: 0.7rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    font-weight: 700;
    padding: 0.2rem 0.65rem;
    border-radius: 99px;
    margin-bottom: 0.6rem;
}

/* ── Section header ── */
.section-header {
    color: #e2e8f0;
    font-size: 1.15rem;
    font-weight: 700;
    margin: 1.8rem 0 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}
.no-match {
    color: #64748b;
    text-align: center;
    padding: 3rem 1rem;
    font-size: 0.95rem;
}

/* ── Button ── */
.stButton > button {
    background: linear-gradient(90deg,#7c3aed,#4f46e5) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: 0.03em !important;
    padding: 0.55rem 1.4rem !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover { opacity: 0.85 !important; }

/* ── Divider ── */
hr { border-color: rgba(255,255,255,0.07) !important; }
</style>
""", unsafe_allow_html=True)

# ── Data ───────────────────────────────────────────────────────────────────────
MAJORS    = ["Engineering", "Business", "Medicine", "Finance", "Architecture"]
LOCATIONS = ["Library", "Study Hall", "Cafe", "Canteen"]
GENDERS   = ["Male", "Female"]

MAJOR_EMOJIS = {
    "Engineering": "⚙️", "Business": "💼",
    "Medicine": "🩺", "Finance": "📊", "Architecture": "🏛️",
}

FAKE_USERS = [
    # ── Engineering (4) ──────────────────────────────────────────────────────
    {"id":1,  "name":"Aiden Loh",     "gender":"Male",   "age":20, "major":"Engineering",   "time_start":8,  "time_end":14, "locations":["Library","Study Hall"]},
    {"id":2,  "name":"Priya Nair",    "gender":"Female", "age":19, "major":"Engineering",   "time_start":9,  "time_end":17, "locations":["Library","Cafe"]},
    {"id":3,  "name":"Marcus Tan",    "gender":"Male",   "age":22, "major":"Engineering",   "time_start":13, "time_end":19, "locations":["Study Hall","Canteen"]},
    {"id":4,  "name":"Zoe Huang",     "gender":"Female", "age":21, "major":"Engineering",   "time_start":7,  "time_end":13, "locations":["Library","Canteen","Cafe"]},
    # ── Business (4) ─────────────────────────────────────────────────────────
    {"id":5,  "name":"Ryan Chong",    "gender":"Male",   "age":23, "major":"Business",      "time_start":10, "time_end":16, "locations":["Cafe","Canteen"]},
    {"id":6,  "name":"Hana Yusof",    "gender":"Female", "age":20, "major":"Business",      "time_start":8,  "time_end":15, "locations":["Library","Study Hall","Cafe"]},
    {"id":7,  "name":"Darren Kok",    "gender":"Male",   "age":24, "major":"Business",      "time_start":12, "time_end":19, "locations":["Canteen","Cafe"]},
    {"id":8,  "name":"Linh Pham",     "gender":"Female", "age":22, "major":"Business",      "time_start":9,  "time_end":18, "locations":["Study Hall","Library"]},
    # ── Medicine (4) ─────────────────────────────────────────────────────────
    {"id":9,  "name":"Ethan Raj",     "gender":"Male",   "age":21, "major":"Medicine",      "time_start":7,  "time_end":12, "locations":["Library","Study Hall"]},
    {"id":10, "name":"Sofía Méndez",  "gender":"Female", "age":20, "major":"Medicine",      "time_start":8,  "time_end":16, "locations":["Library","Cafe"]},
    {"id":11, "name":"Kai Lim",       "gender":"Male",   "age":23, "major":"Medicine",      "time_start":14, "time_end":19, "locations":["Study Hall","Canteen"]},
    {"id":12, "name":"Amara Osei",    "gender":"Female", "age":22, "major":"Medicine",      "time_start":10, "time_end":18, "locations":["Library","Study Hall","Canteen"]},
    # ── Finance (4) ──────────────────────────────────────────────────────────
    {"id":13, "name":"Jordan Wee",    "gender":"Male",   "age":24, "major":"Finance",       "time_start":9,  "time_end":17, "locations":["Cafe","Library"]},
    {"id":14, "name":"Mei Ling Chen", "gender":"Female", "age":21, "major":"Finance",       "time_start":11, "time_end":19, "locations":["Study Hall","Canteen","Cafe"]},
    {"id":15, "name":"Isaac Fernandez","gender":"Male",  "age":20, "major":"Finance",       "time_start":7,  "time_end":13, "locations":["Library","Study Hall"]},
    {"id":16, "name":"Yuna Park",     "gender":"Female", "age":22, "major":"Finance",       "time_start":8,  "time_end":15, "locations":["Cafe","Canteen"]},
    # ── Architecture (4) ─────────────────────────────────────────────────────
    {"id":17, "name":"Lucas Bautista","gender":"Male",   "age":19, "major":"Architecture",  "time_start":10, "time_end":18, "locations":["Study Hall","Cafe"]},
    {"id":18, "name":"Nadia Syahrul", "gender":"Female", "age":23, "major":"Architecture",  "time_start":8,  "time_end":14, "locations":["Library","Canteen"]},
    {"id":19, "name":"Brennan Ho",    "gender":"Male",   "age":25, "major":"Architecture",  "time_start":13, "time_end":19, "locations":["Canteen","Cafe","Library"]},
    {"id":20, "name":"Clara Abreu",   "gender":"Female", "age":20, "major":"Architecture",  "time_start":7,  "time_end":16, "locations":["Study Hall","Library","Cafe"]},
]

# ── Matching logic ─────────────────────────────────────────────────────────────
def compute_match(user_prefs: dict, fake: dict) -> float:
    """
    Weighted scoring:
      Major     40 pts  (hard match)
      Time overlap  30 pts  (proportional to overlap / user range)
      Location  20 pts  (Jaccard of chosen vs fake locations)
      Gender    10 pts  (same gender bonus)
    """
    score = 0.0

    # 1. Major (40 pts)
    if user_prefs["major"] == fake["major"]:
        score += 40

    # 2. Time overlap (30 pts)
    u_start, u_end = user_prefs["time_start"], user_prefs["time_end"]
    f_start, f_end = fake["time_start"],        fake["time_end"]
    overlap = max(0, min(u_end, f_end) - max(u_start, f_start))
    user_range = max(u_end - u_start, 1)
    score += 30 * (overlap / user_range)

    # 3. Location (20 pts)
    user_locs = set(user_prefs["locations"])
    fake_locs = set(fake["locations"])
    if user_locs or fake_locs:
        jaccard = len(user_locs & fake_locs) / len(user_locs | fake_locs)
        score += 20 * jaccard

    # 4. Gender (10 pts)
    if user_prefs["gender"] == fake["gender"]:
        score += 10

    return round(score, 1)

def badge_class(pct: float) -> str:
    if pct >= 70: return "badge-high"
    if pct >= 40: return "badge-medium"
    return "badge-low"

def fmt_time(h: int) -> str:
    return f"{'12' if h == 12 else h % 12}{'am' if h < 12 else 'pm'}"

def render_card(u: dict, score: float, is_top: bool = False):
    avatar_cls  = "avatar-m" if u["gender"] == "Male" else "avatar-f"
    avatar_icon = "👨‍💻" if u["gender"] == "Male" else "👩‍💻"
    bc          = badge_class(score)
    loc_tags    = "".join(f'<span class="tag">{l}</span>' for l in u["locations"])
    top_pill    = '<div class="top-label">⭐ Best Match</div>' if is_top else ""

    st.markdown(f"""
    <div class="match-card {'top-match' if is_top else ''}">
      {top_pill}
      <span class="match-badge {bc}">{score}%</span>
      <div class="avatar {avatar_cls}">{avatar_icon}</div>
      <div class="card-name">{u['name']}</div>
      <div class="card-major">{MAJOR_EMOJIS.get(u['major'],'')} {u['major']}</div>
      <div class="card-detail">
        🎂 Age: <strong style="color:#e2e8f0">{u['age']}</strong> &nbsp;|&nbsp;
        {'♂' if u['gender']=='Male' else '♀'} <strong style="color:#e2e8f0">{u['gender']}</strong><br>
        🕐 Available: <strong style="color:#e2e8f0">{fmt_time(u['time_start'])} – {fmt_time(u['time_end'])}</strong><br>
        📍 Spots: {loc_tags}
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🎓 Your Profile")
    st.markdown("---")

    gender = st.radio("Gender", GENDERS, horizontal=True)

    age = st.slider("Age", min_value=16, max_value=26, value=20)

    major = st.selectbox("Major", MAJORS)

    time_range = st.slider(
        "Available Time",
        min_value=7, max_value=19, value=(9, 17),
        format="%d:00",
        help="Slide to pick your study window (7 am – 7 pm)",
    )
    st.caption(f"🕐 {fmt_time(time_range[0])} → {fmt_time(time_range[1])}")

    locations = st.multiselect(
        "Preferred Locations",
        LOCATIONS,
        default=["Library"],
    )

    st.markdown("---")
    find_btn = st.button("🔍 Find My Study Partner", use_container_width=True)

# ── Main area ──────────────────────────────────────────────────────────────────
st.markdown('<h1 class="hero-title">StudyMatch</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-sub">Find your perfect study partner — same vibe, same grind.</p>', unsafe_allow_html=True)

# Guard: locations required
if not locations:
    st.warning("👈 Please select at least one preferred location in the sidebar.")
    st.stop()

# Build user prefs
user_prefs = {
    "gender":     gender,
    "age":        age,
    "major":      major,
    "time_start": time_range[0],
    "time_end":   time_range[1],
    "locations":  locations,
}

# Score all fake users
scored = sorted(
    [{"user": u, "score": compute_match(user_prefs, u)} for u in FAKE_USERS],
    key=lambda x: x["score"],
    reverse=True,
)

# ── Session state: how many to show ───────────────────────────────────────────
if "show_count" not in st.session_state:
    st.session_state.show_count = 1

if find_btn:
    st.session_state.show_count = 1   # reset on new search

# ── Results ────────────────────────────────────────────────────────────────────
top = scored[0]
rest = scored[1:]

# Top match
st.markdown('<div class="section-header">🏆 Best Match</div>', unsafe_allow_html=True)
render_card(top["user"], top["score"], is_top=True)

# "Show more" section
max_show = st.session_state.show_count
if max_show > 1:
    st.markdown('<div class="section-header">👥 Other Potential Partners</div>', unsafe_allow_html=True)
    for item in rest[:max_show - 1]:
        render_card(item["user"], item["score"])

# Button to reveal next match
if max_show <= len(rest):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("👀 Not quite right? See another match"):
            st.session_state.show_count += 1
            st.rerun()
else:
    st.markdown(
        '<p class="no-match">🎉 You\'ve seen all available study partners!</p>',
        unsafe_allow_html=True,
    )

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    '<p style="color:#475569;font-size:0.75rem;text-align:center;">StudyMatch • Built with Streamlit • Match smarter, study harder 📚</p>',
    unsafe_allow_html=True,
)