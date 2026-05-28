import streamlit as st
from datetime import date, timedelta, datetime

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

html, body, [class*="css"] { font-family: 'Sora', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #0f0c29 0%, #1a1040 40%, #24243e 100%);
    min-height: 100vh;
}

[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.04) !important;
    border-right: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(20px);
}
[data-testid="stSidebar"] * { color: #e8e0ff !important; }
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stSlider label,
[data-testid="stSidebar"] .stMultiSelect label,
[data-testid="stSidebar"] .stRadio label,
[data-testid="stSidebar"] .stTextInput label {
    font-size: 0.78rem !important;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #a78bfa !important;
    font-weight: 600 !important;
}

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
    margin-bottom: 2rem;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.04);
    border-radius: 12px;
    padding: 4px;
    gap: 4px;
    border: 1px solid rgba(255,255,255,0.08);
}
.stTabs [data-baseweb="tab"] {
    border-radius: 9px !important;
    color: #94a3b8 !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.03em;
    padding: 0.5rem 1.2rem !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(90deg,#7c3aed,#4f46e5) !important;
    color: #fff !important;
}
.stTabs [data-baseweb="tab-highlight"] { display: none !important; }

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
.match-card:hover { transform: translateY(-3px); box-shadow: 0 12px 40px rgba(129,140,248,0.2); }
.match-card.top-match {
    border-color: rgba(192,132,252,0.55);
    background: rgba(167,139,250,0.08);
    box-shadow: 0 0 0 1px rgba(192,132,252,0.3), 0 8px 32px rgba(129,140,248,0.15);
}

.match-badge {
    position: absolute; top: 1.2rem; right: 1.2rem;
    padding: 0.35rem 0.85rem; border-radius: 99px;
    font-size: 0.88rem; font-weight: 700; letter-spacing: 0.03em;
}
.badge-high   { background: linear-gradient(90deg,#7c3aed,#4f46e5); color:#fff; }
.badge-medium { background: linear-gradient(90deg,#0ea5e9,#6366f1); color:#fff; }
.badge-low    { background: rgba(100,116,139,0.4); color:#cbd5e1; }

.avatar {
    width: 56px; height: 56px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.6rem; margin-bottom: 0.9rem;
    border: 2px solid rgba(167,139,250,0.4);
}
.avatar-m { background: linear-gradient(135deg,#1e3a5f,#2563eb30); }
.avatar-f { background: linear-gradient(135deg,#4a1a5f,#7c3aed30); }

.card-name  { font-size: 1.15rem; font-weight: 700; color: #f1f5f9; margin-bottom: 0.25rem; }
.card-major { font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.1em; color: #a78bfa; font-weight: 600; margin-bottom: 0.8rem; }
.card-detail { color: #94a3b8; font-size: 0.85rem; line-height: 1.7; }

.tag {
    display: inline-block;
    background: rgba(99,102,241,0.2); border: 1px solid rgba(99,102,241,0.35);
    color: #c4b5fd; border-radius: 99px; padding: 0.15rem 0.6rem;
    font-size: 0.75rem; margin: 0.15rem 0.1rem;
}
.top-label {
    display: inline-block;
    background: linear-gradient(90deg,#7c3aed,#4f46e5); color: #fff;
    font-size: 0.7rem; letter-spacing: 0.12em; text-transform: uppercase;
    font-weight: 700; padding: 0.2rem 0.65rem; border-radius: 99px; margin-bottom: 0.6rem;
}

.section-header {
    color: #e2e8f0; font-size: 1.15rem; font-weight: 700;
    margin: 1.8rem 0 1rem; padding-bottom: 0.5rem;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}
.no-match { color: #64748b; text-align: center; padding: 3rem 1rem; font-size: 0.95rem; }

/* ── Timetable ── */
.tt-container {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(167,139,250,0.2);
    border-radius: 20px;
    overflow: hidden;
    margin-bottom: 1.5rem;
}
.tt-header-row {
    display: grid;
    background: rgba(124,58,237,0.18);
    border-bottom: 1px solid rgba(167,139,250,0.2);
    padding: 0.7rem 1rem;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #a78bfa;
}
.tt-row {
    display: grid;
    padding: 0.85rem 1rem;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    font-size: 0.85rem;
    color: #cbd5e1;
    align-items: center;
    transition: background 0.15s;
}
.tt-row:last-child { border-bottom: none; }
.tt-row:hover { background: rgba(255,255,255,0.03); }
.tt-pill {
    display: inline-block; border-radius: 99px;
    padding: 0.18rem 0.7rem; font-size: 0.72rem; font-weight: 700;
}
.pill-upcoming { background: rgba(124,58,237,0.25); color: #c084fc; border: 1px solid rgba(192,132,252,0.3); }
.pill-today    { background: rgba(16,185,129,0.2);  color: #34d399; border: 1px solid rgba(52,211,153,0.35); }
.pill-done     { background: rgba(100,116,139,0.2); color: #64748b; border: 1px solid rgba(100,116,139,0.25); }
.tt-partner-name { color: #e2e8f0; font-weight: 600; }
.tt-empty {
    text-align: center; padding: 3rem 1rem;
    color: #475569; font-size: 0.9rem;
}
.tt-form-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(167,139,250,0.2);
    border-radius: 16px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1.2rem;
}
.tt-form-title {
    color: #e2e8f0; font-size: 0.95rem; font-weight: 700; margin-bottom: 1rem;
}
.countdown-chip {
    display: inline-block;
    background: rgba(56,189,248,0.12); border: 1px solid rgba(56,189,248,0.3);
    color: #38bdf8; border-radius: 99px;
    padding: 0.15rem 0.65rem; font-size: 0.72rem; font-weight: 600;
    margin-left: 0.4rem;
}

/* ── Button ── */
.stButton > button {
    background: linear-gradient(90deg,#7c3aed,#4f46e5) !important;
    color: #fff !important; border: none !important;
    border-radius: 10px !important; font-family: 'Sora', sans-serif !important;
    font-weight: 600 !important; letter-spacing: 0.03em !important;
    padding: 0.55rem 1.4rem !important; transition: opacity 0.2s !important;
}
.stButton > button:hover { opacity: 0.85 !important; }

hr { border-color: rgba(255,255,255,0.07) !important; }
</style>
""", unsafe_allow_html=True)

# ── Constants ──────────────────────────────────────────────────────────────────
MAJORS    = ["Engineering", "Business", "Medicine", "Finance", "Architecture"]
LOCATIONS = ["Library", "Study Hall", "Cafe", "Canteen"]
GENDERS   = ["Male", "Female"]
DAYS      = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

MAJOR_EMOJIS = {
    "Engineering": "⚙️", "Business": "💼",
    "Medicine": "🩺", "Finance": "📊", "Architecture": "🏛️",
}

FAKE_USERS = [
    {"id":1,  "name":"Aiden Loh",      "gender":"Male",   "age":20, "major":"Engineering",  "time_start":8,  "time_end":14, "locations":["Library","Study Hall"]},
    {"id":2,  "name":"Priya Nair",     "gender":"Female", "age":19, "major":"Engineering",  "time_start":9,  "time_end":17, "locations":["Library","Cafe"]},
    {"id":3,  "name":"Marcus Tan",     "gender":"Male",   "age":22, "major":"Engineering",  "time_start":13, "time_end":19, "locations":["Study Hall","Canteen"]},
    {"id":4,  "name":"Zoe Huang",      "gender":"Female", "age":21, "major":"Engineering",  "time_start":7,  "time_end":13, "locations":["Library","Canteen","Cafe"]},
    {"id":5,  "name":"Ryan Chong",     "gender":"Male",   "age":23, "major":"Business",     "time_start":10, "time_end":16, "locations":["Cafe","Canteen"]},
    {"id":6,  "name":"Hana Yusof",     "gender":"Female", "age":20, "major":"Business",     "time_start":8,  "time_end":15, "locations":["Library","Study Hall","Cafe"]},
    {"id":7,  "name":"Darren Kok",     "gender":"Male",   "age":24, "major":"Business",     "time_start":12, "time_end":19, "locations":["Canteen","Cafe"]},
    {"id":8,  "name":"Linh Pham",      "gender":"Female", "age":22, "major":"Business",     "time_start":9,  "time_end":18, "locations":["Study Hall","Library"]},
    {"id":9,  "name":"Ethan Raj",      "gender":"Male",   "age":21, "major":"Medicine",     "time_start":7,  "time_end":12, "locations":["Library","Study Hall"]},
    {"id":10, "name":"Sofía Méndez",   "gender":"Female", "age":20, "major":"Medicine",     "time_start":8,  "time_end":16, "locations":["Library","Cafe"]},
    {"id":11, "name":"Kai Lim",        "gender":"Male",   "age":23, "major":"Medicine",     "time_start":14, "time_end":19, "locations":["Study Hall","Canteen"]},
    {"id":12, "name":"Amara Osei",     "gender":"Female", "age":22, "major":"Medicine",     "time_start":10, "time_end":18, "locations":["Library","Study Hall","Canteen"]},
    {"id":13, "name":"Jordan Wee",     "gender":"Male",   "age":24, "major":"Finance",      "time_start":9,  "time_end":17, "locations":["Cafe","Library"]},
    {"id":14, "name":"Mei Ling Chen",  "gender":"Female", "age":21, "major":"Finance",      "time_start":11, "time_end":19, "locations":["Study Hall","Canteen","Cafe"]},
    {"id":15, "name":"Isaac Fernandez","gender":"Male",   "age":20, "major":"Finance",      "time_start":7,  "time_end":13, "locations":["Library","Study Hall"]},
    {"id":16, "name":"Yuna Park",      "gender":"Female", "age":22, "major":"Finance",      "time_start":8,  "time_end":15, "locations":["Cafe","Canteen"]},
    {"id":17, "name":"Lucas Bautista", "gender":"Male",   "age":19, "major":"Architecture", "time_start":10, "time_end":18, "locations":["Study Hall","Cafe"]},
    {"id":18, "name":"Nadia Syahrul",  "gender":"Female", "age":23, "major":"Architecture", "time_start":8,  "time_end":14, "locations":["Library","Canteen"]},
    {"id":19, "name":"Brennan Ho",     "gender":"Male",   "age":25, "major":"Architecture", "time_start":13, "time_end":19, "locations":["Canteen","Cafe","Library"]},
    {"id":20, "name":"Clara Abreu",    "gender":"Female", "age":20, "major":"Architecture", "time_start":7,  "time_end":16, "locations":["Study Hall","Library","Cafe"]},
]

# ── Helpers ────────────────────────────────────────────────────────────────────
def compute_match(user_prefs: dict, fake: dict) -> float:
    score = 0.0
    if user_prefs["major"] == fake["major"]:
        score += 40
    u_start, u_end = user_prefs["time_start"], user_prefs["time_end"]
    f_start, f_end = fake["time_start"], fake["time_end"]
    overlap = max(0, min(u_end, f_end) - max(u_start, f_start))
    score += 30 * (overlap / max(u_end - u_start, 1))
    user_locs, fake_locs = set(user_prefs["locations"]), set(fake["locations"])
    if user_locs or fake_locs:
        score += 20 * len(user_locs & fake_locs) / len(user_locs | fake_locs)
    if user_prefs["gender"] == fake["gender"]:
        score += 10
    return round(score, 1)

def badge_class(pct):
    if pct >= 70: return "badge-high"
    if pct >= 40: return "badge-medium"
    return "badge-low"

def fmt_time(h: int) -> str:
    if h == 12: return "12pm"
    if h == 0:  return "12am"
    return f"{h % 12}{'am' if h < 12 else 'pm'}"

def fmt_time_12(h, m=0):
    suffix = "am" if h < 12 else "pm"
    hh = h % 12 or 12
    return f"{hh}:{m:02d}{suffix}"

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

# ── Session state init ─────────────────────────────────────────────────────────
if "show_count"  not in st.session_state: st.session_state.show_count  = 1
if "sessions"    not in st.session_state: st.session_state.sessions    = []   # list of dicts
if "edit_idx"    not in st.session_state: st.session_state.edit_idx    = None

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🎓 Your Profile")
    st.markdown("---")

    user_name  = st.text_input("Your Name", placeholder="e.g. Alex Tan", max_chars=40)
    gender     = st.radio("Gender", GENDERS, horizontal=True)
    age        = st.slider("Age", min_value=16, max_value=26, value=20)
    major      = st.selectbox("Major", MAJORS)
    time_range = st.slider("Available Time", min_value=7, max_value=19, value=(9, 17),
                           format="%d:00", help="Study window (7am – 7pm)")
    st.caption(f"🕐 {fmt_time(time_range[0])} → {fmt_time(time_range[1])}")
    locations  = st.multiselect("Preferred Locations", LOCATIONS, default=["Library"])

    st.markdown("---")
    find_btn = st.button("🔍 Find My Study Partner", use_container_width=True)

# ── Hero ───────────────────────────────────────────────────────────────────────
st.markdown('<h1 class="hero-title">StudyMatch</h1>', unsafe_allow_html=True)
if user_name.strip():
    greeting = f"Welcome, <strong style='color:#c084fc'>{user_name.strip()}</strong>! Find your perfect study partner — same vibe, same grind."
else:
    greeting = "Find your perfect study partner — same vibe, same grind."
st.markdown(f'<p class="hero-sub">{greeting}</p>', unsafe_allow_html=True)

if not locations:
    st.warning("👈 Please select at least one preferred location in the sidebar.")
    st.stop()

user_prefs = {
    "gender": gender, "age": age, "major": major,
    "time_start": time_range[0], "time_end": time_range[1], "locations": locations,
}
scored = sorted(
    [{"user": u, "score": compute_match(user_prefs, u)} for u in FAKE_USERS],
    key=lambda x: x["score"], reverse=True,
)
if find_btn:
    st.session_state.show_count = 1

# ── Tabs ───────────────────────────────────────────────────────────────────────
tab_match, tab_tt = st.tabs(["🔍 Find a Partner", "📅 My Study Timetable"])

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 1 – MATCHING
# ═══════════════════════════════════════════════════════════════════════════════
with tab_match:
    top  = scored[0]
    rest = scored[1:]

    st.markdown('<div class="section-header">🏆 Best Match</div>', unsafe_allow_html=True)
    render_card(top["user"], top["score"], is_top=True)

    max_show = st.session_state.show_count
    if max_show > 1:
        st.markdown('<div class="section-header">👥 Other Potential Partners</div>', unsafe_allow_html=True)
        for item in rest[:max_show - 1]:
            render_card(item["user"], item["score"])

    if max_show <= len(rest):
        c1, c2, c3 = st.columns([1,2,1])
        with c2:
            if st.button("👀 Not quite right? See another match"):
                st.session_state.show_count += 1
                st.rerun()
    else:
        st.markdown('<p class="no-match">🎉 You\'ve seen all available study partners!</p>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 2 – TIMETABLE
# ═══════════════════════════════════════════════════════════════════════════════
with tab_tt:
    st.markdown('<div class="section-header">📅 My Study Timetable</div>', unsafe_allow_html=True)

    # ── Add / Edit session form ────────────────────────────────────────────────
    editing = st.session_state.edit_idx is not None
    form_title = "✏️ Edit Study Session" if editing else "➕ Schedule a New Study Session"

    with st.expander(form_title, expanded=(len(st.session_state.sessions) == 0 or editing)):
        st.markdown(f'<div class="tt-form-title">{form_title}</div>', unsafe_allow_html=True)

        # Pre-fill when editing
        prefill = st.session_state.sessions[st.session_state.edit_idx] if editing else {}

        # Partner picker — show all fake users with match %
        partner_options = {
            f"{s['user']['name']} ({s['score']}% match) — {MAJOR_EMOJIS.get(s['user']['major'],'')} {s['user']['major']}": s['user']
            for s in scored
        }
        default_partner_key = list(partner_options.keys())[0]
        if editing:
            saved_name = prefill.get("partner_name", "")
            for k, v in partner_options.items():
                if v["name"] == saved_name:
                    default_partner_key = k
                    break
        chosen_key = st.selectbox(
            "Study Partner",
            list(partner_options.keys()),
            index=list(partner_options.keys()).index(default_partner_key),
            key="form_partner",
        )
        chosen_partner = partner_options[chosen_key]

        col_a, col_b = st.columns(2)
        with col_a:
            session_date = st.date_input(
                "Date",
                value=prefill.get("date", date.today() + timedelta(days=1)),
                min_value=date.today(),
                key="form_date",
            )
        with col_b:
            session_day = DAYS[session_date.weekday()]
            st.text_input("Day", value=session_day, disabled=True, key="form_day")

        col_c, col_d = st.columns(2)
        with col_c:
            # Overlap hours between user and chosen partner
            overlap_start = max(time_range[0], chosen_partner["time_start"])
            overlap_end   = min(time_range[1], chosen_partner["time_end"])
            if overlap_end <= overlap_start:
                overlap_start, overlap_end = time_range[0], time_range[1]
            start_h = st.slider("Start Time", min_value=7, max_value=18,
                                value=prefill.get("start_h", overlap_start),
                                format="%d:00", key="form_start")
        with col_d:
            end_h = st.slider("End Time", min_value=8, max_value=19,
                              value=prefill.get("end_h", min(overlap_end, overlap_start + 2)),
                              format="%d:00", key="form_end")

        if end_h <= start_h:
            st.warning("⚠️ End time must be after start time.")

        loc_choices = list(set(locations) & set(chosen_partner["locations"])) or locations
        session_loc = st.selectbox(
            "Location",
            loc_choices,
            index=loc_choices.index(prefill.get("location", loc_choices[0])) if prefill.get("location") in loc_choices else 0,
            key="form_loc",
        )
        session_note = st.text_input(
            "Notes (optional)",
            value=prefill.get("note", ""),
            placeholder="e.g. Bring chapter 5 notes",
            key="form_note",
        )

        col_save, col_cancel = st.columns([1,1])
        with col_save:
            save_label = "💾 Update Session" if editing else "✅ Add to Timetable"
            if st.button(save_label, use_container_width=True, disabled=(end_h <= start_h)):
                entry = {
                    "partner_name": chosen_partner["name"],
                    "partner_major": chosen_partner["major"],
                    "date": session_date,
                    "day": session_day,
                    "start_h": start_h,
                    "end_h": end_h,
                    "location": session_loc,
                    "note": session_note,
                }
                if editing:
                    st.session_state.sessions[st.session_state.edit_idx] = entry
                    st.session_state.edit_idx = None
                    st.success("✅ Session updated!")
                else:
                    st.session_state.sessions.append(entry)
                    st.success(f"📅 Session with {chosen_partner['name']} added!")
                st.rerun()

        with col_cancel:
            if editing:
                if st.button("✖ Cancel Edit", use_container_width=True):
                    st.session_state.edit_idx = None
                    st.rerun()

    # ── Timetable display ──────────────────────────────────────────────────────
    sessions = st.session_state.sessions
    if not sessions:
        st.markdown(
            '<div class="tt-empty">📭 No study sessions yet.<br>Schedule your first one above!</div>',
            unsafe_allow_html=True,
        )
    else:
        today = date.today()

        # Sort by date then start time
        sorted_sessions = sorted(sessions, key=lambda x: (x["date"], x["start_h"]))

        # ── Upcoming reminder banner ───────────────────────────────────────────
        upcoming = [s for s in sorted_sessions if s["date"] >= today]
        if upcoming:
            next_s = upcoming[0]
            delta  = (next_s["date"] - today).days
            if delta == 0:
                when_txt = "🟢 TODAY"
            elif delta == 1:
                when_txt = "🔔 TOMORROW"
            else:
                when_txt = f"📆 in {delta} days"
            st.markdown(f"""
            <div style="background:rgba(124,58,237,0.15);border:1px solid rgba(192,132,252,0.35);
                        border-radius:14px;padding:1rem 1.3rem;margin-bottom:1.2rem;
                        display:flex;align-items:center;gap:0.8rem;flex-wrap:wrap;">
                <span style="font-size:1.4rem;">⏰</span>
                <div>
                    <div style="color:#e2e8f0;font-weight:700;font-size:0.95rem;">
                        Next session {when_txt}
                        <span class="countdown-chip">{next_s['day']}, {next_s['date'].strftime('%d %b')}</span>
                    </div>
                    <div style="color:#94a3b8;font-size:0.82rem;margin-top:0.2rem;">
                        With <strong style="color:#c084fc">{next_s['partner_name']}</strong>
                        &nbsp;·&nbsp; {fmt_time(next_s['start_h'])} – {fmt_time(next_s['end_h'])}
                        &nbsp;·&nbsp; 📍 {next_s['location']}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # ── Grid header ───────────────────────────────────────────────────────
        st.markdown("""
        <div class="tt-container">
          <div class="tt-header-row" style="grid-template-columns:90px 110px 1fr 130px 110px 90px 80px;">
            <span>Status</span><span>Date</span><span>Partner</span>
            <span>Time</span><span>Location</span><span>Notes</span><span>Actions</span>
          </div>
        """, unsafe_allow_html=True)

        for i, s in enumerate(sorted_sessions):
            orig_idx = sessions.index(s)
            is_today   = s["date"] == today
            is_past    = s["date"] < today
            pill_cls   = "pill-done" if is_past else ("pill-today" if is_today else "pill-upcoming")
            pill_label = "Done" if is_past else ("Today" if is_today else "Upcoming")
            note_disp  = s["note"] if s["note"] else "—"
            emoji      = MAJOR_EMOJIS.get(s["partner_major"], "")

            st.markdown(f"""
            <div class="tt-row" style="grid-template-columns:90px 110px 1fr 130px 110px 90px 80px;">
              <span><span class="tt-pill {pill_cls}">{pill_label}</span></span>
              <span style="color:#94a3b8;font-size:0.8rem;">{s['day'][:3]}<br>{s['date'].strftime('%d %b %Y')}</span>
              <span>
                <span class="tt-partner-name">{s['partner_name']}</span><br>
                <span style="color:#64748b;font-size:0.75rem;">{emoji} {s['partner_major']}</span>
              </span>
              <span>🕐 {fmt_time(s['start_h'])} – {fmt_time(s['end_h'])}</span>
              <span>📍 {s['location']}</span>
              <span style="color:#64748b;font-size:0.8rem;">{note_disp}</span>
              <span style="font-size:0.75rem;">
                <span style="color:#a78bfa;cursor:pointer;" title="Edit">✏️</span>
                &nbsp;
                <span style="color:#f87171;cursor:pointer;" title="Delete">🗑️</span>
              </span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # ── Edit / Delete buttons (Streamlit native, per row) ─────────────────
        st.markdown('<div style="margin-top:0.5rem;"></div>', unsafe_allow_html=True)
        for i, s in enumerate(sorted_sessions):
            orig_idx = sessions.index(s)
            col_info, col_edit, col_del = st.columns([6, 1, 1])
            with col_info:
                st.markdown(
                    f"<span style='color:#64748b;font-size:0.78rem;'>"
                    f"Row {i+1}: {s['partner_name']} · {s['date'].strftime('%d %b')} · {fmt_time(s['start_h'])}–{fmt_time(s['end_h'])}"
                    f"</span>",
                    unsafe_allow_html=True,
                )
            with col_edit:
                if st.button("✏️", key=f"edit_{orig_idx}", help="Edit this session"):
                    st.session_state.edit_idx = orig_idx
                    st.rerun()
            with col_del:
                if st.button("🗑️", key=f"del_{orig_idx}", help="Delete this session"):
                    st.session_state.sessions.pop(orig_idx)
                    st.rerun()

        # ── Summary stats ──────────────────────────────────────────────────────
        st.markdown("---")
        total     = len(sessions)
        upcoming_n = sum(1 for s in sessions if s["date"] >= today)
        past_n     = total - upcoming_n
        unique_p   = len(set(s["partner_name"] for s in sessions))

        m1, m2, m3, m4 = st.columns(4)
        for col, label, val, icon in [
            (m1, "Total Sessions",    total,      "📚"),
            (m2, "Upcoming",          upcoming_n, "🗓️"),
            (m3, "Completed",         past_n,     "✅"),
            (m4, "Unique Partners",   unique_p,   "🤝"),
        ]:
            with col:
                st.markdown(f"""
                <div style="background:rgba(255,255,255,0.04);border:1px solid rgba(167,139,250,0.2);
                            border-radius:14px;padding:1rem;text-align:center;">
                    <div style="font-size:1.6rem;">{icon}</div>
                    <div style="font-size:1.4rem;font-weight:800;color:#e2e8f0;">{val}</div>
                    <div style="font-size:0.72rem;color:#64748b;text-transform:uppercase;
                                letter-spacing:0.08em;margin-top:0.2rem;">{label}</div>
                </div>
                """, unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    '<p style="color:#475569;font-size:0.75rem;text-align:center;">'
    'StudyMatch • Built with Streamlit • Match smarter, study harder 📚</p>',
    unsafe_allow_html=True,
)