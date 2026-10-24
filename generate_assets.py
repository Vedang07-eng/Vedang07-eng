"""
Generates all animated SVG assets for the GitHub profile README.
Run from the repo root:  python tools/generate_assets.py
Edit the CONFIG block below to change text, then re-run and commit assets/.
"""
import random, os
from xml.sax.saxutils import escape as esc

# ───────────────────────── CONFIG ─────────────────────────
NAME = "VEDANG DHURI"
TAGLINE = "AI & AUTOMATION ENGINEER  ·  AGENTIC AI  ·  GENERATIVE AI"
SUBLINE = "Explainable ML  |  LLM Workflows  |  Python · FastAPI · n8n"

TYPING_LINES = [
    "Building LLM-powered workflows & AI agents",
    "Explainable ML  |  Published at ETTS-2026",
    "Python  ·  FastAPI  ·  n8n  ·  LangChain",
    "Turning ideas into practical AI systems",
]

TERMINAL = [
    ("whoami",        "Vedang Dhuri, AI & Automation Engineer"),
    ("cat education", "IT Engineering · University of Mumbai · Honors in Data Science"),
    ("cat focus",     "Agentic AI · Generative AI · Explainable ML · Automation"),
    ("cat research",  "GreenGuide: published at ETTS-2026"),
    ("status",        "open to internships & entry-level AI / Automation roles"),
]

SKILLS_ROW1 = ["LLMs", "Prompt Engineering", "RAG", "AI Agents", "LangChain", "LangGraph",
               "Scikit-learn", "Feature Engineering", "Explainable AI (SHAP)", "Data Preprocessing"]
SKILLS_ROW2 = ["Python", "FastAPI", "SQL", "PostgreSQL", "MySQL", "SQLAlchemy", "n8n",
               "REST APIs", "Webhooks", "OpenAI API", "Gemini API", "React", "Streamlit",
               "Docker", "Git", "Power BI"]

# (title, status, status_color, lines, stack)
PROJECTS = [
    ("GreenGuide", "PUBLISHED · ETTS-2026", "#14B8A6",
     ["Explainable, profit-aware stacking ensemble for", "integrated crop recommendation."],
     "Python · Scikit-learn · Ensemble Learning · SHAP"),
    ("Intelligent Accident Response", "IN PROGRESS", "#F59E0B",
     ["Final-year major project: AI workflow for accident", "detection and structured emergency response."],
     "Python · Computer Vision · FastAPI · LLM analysis"),
    ("Multi-Agent Research Generator", "CONCEPT / DESIGN", "#A78BFA",
     ["Researcher, Analyst and Writer agents producing", "source-cited reports with human review."],
     "Python · Agent orchestration · FastAPI · APIs"),
    ("AURA AI", "REPOSITORY", "#3B82F6",
     ["Chatbot assistant focused on natural-language", "interaction using prompt engineering and LLM APIs."],
     "Python · LLM APIs · Prompt Engineering"),
    ("Heart Disease Prediction", "REPOSITORY", "#3B82F6",
     ["Streamlit app exploring prediction from health", "input features. Educational, not diagnostic."],
     "Python · Streamlit · Machine Learning"),
    ("DataStraw Assignment", "REPOSITORY", "#3B82F6",
     ["Project with frontend and backend components", "connecting a UI to application logic and APIs."],
     "Frontend · Backend · APIs"),
    ("Spearmint", "REPOSITORY", "#3B82F6",
     ["React-based AI product recommendation project.", ""],
     "React · JavaScript · AI recommendations"),
    ("Portfolio Website", "LIVE", "#14B8A6",
     ["Source code for my personal portfolio website,", "deployed online."],
     "HTML · CSS · JavaScript"),
]

SECTIONS = [("about", "01", "ABOUT ME"), ("research", "02", "FEATURED RESEARCH"),
            ("work", "03", "SELECTED WORK"), ("stack", "04", "TECH STACK"),
            ("learning", "05", "CURRENTLY LEARNING"), ("connect", "06", "LET'S CONNECT")]

# ───────────────────────── HELPERS ─────────────────────────
BG, BLUE, TEAL, TEXT, MUTED = "#0B1220", "#1D4ED8", "#14B8A6", "#E2E8F0", "#94A3B8"
SANS = "'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'Courier New', 'Fira Code', monospace"
OUT = "assets"
os.makedirs(OUT, exist_ok=True)

def save(name, svg):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(svg)

def svg_open(w, h, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}">')

# ───────────────────────── BANNER ─────────────────────────
def banner():
    random.seed(7)
    W, H = 1200, 300
    pts = [(random.randint(30, W-30), random.randint(25, H-25)) for _ in range(26)]
    lines, dots = [], []
    for i, (x1, y1) in enumerate(pts):
        for (x2, y2) in pts[i+1:]:
            if (x1-x2)**2 + (y1-y2)**2 < 170**2:
                lines.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#fff" stroke-opacity="0.14"/>')
    for i, (x, y) in enumerate(pts):
        d = round(2 + (i % 5) * 0.7, 1)
        dots.append(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#CCFBF1"><animate attributeName="opacity" '
                    f'values="0.2;1;0.2" dur="{d+2}s" begin="{(i%7)*0.4}s" repeatCount="indefinite"/></circle>')
    return f'''{svg_open(W, H, "Vedang Dhuri banner")}
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{BG}"/><stop offset="0.55" stop-color="{BLUE}"/><stop offset="1" stop-color="{TEAL}"/>
  </linearGradient>
  <linearGradient id="shine" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="420" y2="0" spreadMethod="repeat">
    <stop offset="0" stop-color="#FFFFFF"/><stop offset="0.5" stop-color="#99F6E4"/><stop offset="1" stop-color="#FFFFFF"/>
    <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="420 0" dur="4s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.5" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
  </linearGradient>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0H0V40" fill="none" stroke="#fff" stroke-opacity="0.06"/>
  </pattern>
</defs>
<rect width="{W}" height="{H}" rx="16" fill="url(#bg)"/>
<rect width="{W}" height="{H}" rx="16" fill="url(#grid)"/>
{''.join(lines)}
{''.join(dots)}
<circle cx="1080" cy="40" r="120" fill="#fff" fill-opacity="0.05"><animate attributeName="r" values="105;135;105" dur="7s" repeatCount="indefinite"/></circle>
<text x="600" y="132" text-anchor="middle" font-family="{SANS}" font-size="72" font-weight="800" letter-spacing="8" fill="url(#shine)">{esc(NAME)}</text>
<rect x="360" y="156" width="480" height="3" fill="url(#rule)"/>
<text x="600" y="203" text-anchor="middle" font-family="{SANS}" font-size="23" font-weight="600" letter-spacing="2" fill="{TEXT}">{esc(TAGLINE)}</text>
<text x="600" y="246" text-anchor="middle" font-family="{MONO}" font-size="17" letter-spacing="1" fill="#CCFBF1">{esc(SUBLINE)}</text>
</svg>'''

# ───────────────────────── TYPING LINE ─────────────────────────
def typing():
    W, H, FS = 1200, 56, 26
    cw = FS * 0.6
    n = len(TYPING_LINES)
    slot = 1.0 / n
    total = n * 4.0
    out = [svg_open(W, H, "Typing animation"), "<defs>"]
    for i, t in enumerate(TYPING_LINES):
        tw = len(t) * cw
        x0 = (W - tw) / 2
        s = i * slot
        pts = [(0, 0, 0)]
        if s > 0: pts.append((s, 0, 0))
        pts += [(s + .45*slot, tw + 6, 1), (s + .88*slot, tw + 6, 1), (min(s + .93*slot, .999), tw + 6, 0), (1, 0, 0)]
        kt = ";".join(f"{p[0]:.4f}" for p in pts)
        ws = ";".join(f"{p[1]:.1f}" for p in pts)
        os_ = ";".join(str(p[2]) for p in pts)
        out.append(f'<clipPath id="c{i}"><rect x="{x0:.1f}" y="0" height="{H}" width="0">'
                   f'<animate attributeName="width" values="{ws}" keyTimes="{kt}" dur="{total}s" repeatCount="indefinite"/></rect></clipPath>')
    out.append("</defs>")
    for i, t in enumerate(TYPING_LINES):
        tw = len(t) * cw
        x0 = (W - tw) / 2
        s = i * slot
        pts = [(0, 0)]
        if s > 0: pts.append((s, 0))
        pts += [(s + .05*slot, 1), (s + .88*slot, 1), (min(s + .93*slot, .999), 0), (1, 0)]
        kt = ";".join(f"{p[0]:.4f}" for p in pts)
        ov = ";".join(str(p[1]) for p in pts)
        out.append(f'<g clip-path="url(#c{i})"><text x="{x0:.1f}" y="36" font-family="{MONO}" font-size="{FS}" '
                   f'font-weight="700" fill="{TEAL}" xml:space="preserve">{esc(t)}'
                   f'<animate attributeName="opacity" values="{ov}" keyTimes="{kt}" dur="{total}s" repeatCount="indefinite"/></text></g>')
    out.append("</svg>")
    return "".join(out)

# ───────────────────────── TERMINAL ─────────────────────────
def terminal():
    W = 1100
    rowh, top = 38, 78
    H = top + rowh * len(TERMINAL) + 46
    o = [svg_open(W, H, "Terminal introduction"), f'''<defs>
<linearGradient id="tb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="{TEAL}"/></linearGradient></defs>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="#0F172A" stroke="url(#tb)" stroke-width="2"/>
<path d="M1 15a14 14 0 0 1 14-14h{W-30}a14 14 0 0 1 14 14v34H1z" fill="#111C33"/>
<circle cx="30" cy="26" r="7" fill="#EF4444"/><circle cx="54" cy="26" r="7" fill="#F59E0B"/><circle cx="78" cy="26" r="7" fill="#22C55E"/>
<text x="{W/2}" y="31" text-anchor="middle" font-family="{MONO}" font-size="14" fill="{MUTED}">vedang@ai-lab: ~/profile</text>''']
    for i, (cmd, res) in enumerate(TERMINAL):
        y = top + i * rowh + 14
        b = 0.6 + i * 1.1
        o.append(f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{b}s" dur="0.4s" fill="freeze"/>'
                 f'<text x="32" y="{y}" font-family="{MONO}" font-size="19" fill="{TEAL}" font-weight="700">$</text>'
                 f'<text x="56" y="{y}" font-family="{MONO}" font-size="19" fill="#93C5FD">{esc(cmd)}</text>'
                 f'<text x="{56 + len(cmd)*11.4 + 22:.0f}" y="{y}" font-family="{MONO}" font-size="19" fill="{TEXT}">{esc(res)}</text></g>')
    y = top + len(TERMINAL) * rowh + 14
    o.append(f'<text x="32" y="{y}" font-family="{MONO}" font-size="19" fill="{TEAL}" font-weight="700">$</text>'
             f'<rect x="56" y="{y-16}" width="11" height="21" fill="{TEAL}"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>')
    o.append("</svg>")
    return "".join(o)

# ───────────────────────── SKILLS MARQUEE ─────────────────────────
def marquee(items, reverse, name):
    W, H, gap, ph = 1200, 56, 14, 38
    colors = [TEAL, "#3B82F6", "#A78BFA", "#38BDF8"]
    x, pills = 0, []
    for i, t in enumerate(items):
        w = int(len(t) * 9.8 + 40)
        c = colors[i % len(colors)]
        pills.append(f'<g transform="translate({x},9)"><rect width="{w}" height="{ph}" rx="19" fill="#0F172A" stroke="{c}" stroke-width="1.6"/>'
                     f'<circle cx="18" cy="{ph/2}" r="4" fill="{c}"/>'
                     f'<text x="30" y="{ph/2+5}" font-family="{SANS}" font-size="15" font-weight="600" fill="{TEXT}">{esc(t)}</text></g>')
        x += w + gap
    set_w = x
    reps = max(2, int(W / set_w) + 2)
    body = "".join(f'<g transform="translate({k*set_w},0)">{"".join(pills)}</g>' for k in range(reps))
    frm, to = (-set_w, 0) if reverse else (0, -set_w)
    dur = max(20, int(set_w / 55))
    return (f'{svg_open(W, H, name)}<g><animateTransform attributeName="transform" type="translate" '
            f'from="{frm} 0" to="{to} 0" dur="{dur}s" repeatCount="indefinite"/>{body}</g></svg>')

# ───────────────────────── PROJECT CARD ─────────────────────────
def card(i, title, status, color, lines, stack):
    W, H = 560, 210
    pw = int(len(status) * 7.6 + 26)
    ls = "".join(f'<text x="28" y="{108 + k*24}" font-family="{SANS}" font-size="15" fill="{TEXT}">{esc(l)}</text>'
                 for k, l in enumerate(lines) if l)
    return f'''{svg_open(W, H, title)}
<defs><linearGradient id="b" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{color}"/><stop offset="1" stop-color="{BLUE}"/></linearGradient></defs>
<rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="16" fill="#0F172A" stroke="url(#b)" stroke-width="2"/>
<rect x="1.5" y="1.5" width="8" height="{H-3}" rx="4" fill="url(#b)"/>
<text x="28" y="44" font-family="{MONO}" font-size="14" fill="{MUTED}" font-weight="700">PROJECT {i:02d}</text>
<g transform="translate({W-pw-22},22)"><rect width="{pw}" height="26" rx="13" fill="{color}" fill-opacity="0.16" stroke="{color}"/>
<circle cx="14" cy="13" r="3.5" fill="{color}"><animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/></circle>
<text x="25" y="18" font-family="{SANS}" font-size="11.5" font-weight="700" letter-spacing="0.6" fill="{color}">{esc(status)}</text></g>
<text x="28" y="84" font-family="{SANS}" font-size="23" font-weight="800" fill="#FFFFFF">{esc(title)}</text>
{ls}
<line x1="28" y1="168" x2="{W-28}" y2="168" stroke="#fff" stroke-opacity="0.1"/>
<text x="28" y="192" font-family="{MONO}" font-size="13.5" fill="#5EEAD4">{esc(stack)}</text>
</svg>'''

# ───────────────────────── SECTION HEADER & DIVIDER ─────────────────────────
def header(num, title):
    W, H = 1200, 70
    pw = int(len(title) * 17 + 120)
    return f'''{svg_open(W, H, title)}
<defs><linearGradient id="h" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="{TEAL}"/></linearGradient>
<linearGradient id="l" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{TEAL}"/><stop offset="1" stop-color="{TEAL}" stop-opacity="0"/></linearGradient></defs>
<rect x="2" y="10" width="{pw}" height="48" rx="24" fill="url(#h)"/>
<text x="30" y="42" font-family="{MONO}" font-size="18" font-weight="700" fill="#CCFBF1">{num}</text>
<text x="70" y="42" font-family="{SANS}" font-size="22" font-weight="800" letter-spacing="3" fill="#FFFFFF">{esc(title)}</text>
<rect x="{pw+16}" y="33" width="{W-pw-20}" height="3" rx="1.5" fill="url(#l)"/>
<circle cy="34.5" r="5" fill="{TEAL}"><animate attributeName="cx" values="{pw+16};{W-10}" dur="3.5s" repeatCount="indefinite"/>
<animate attributeName="opacity" values="1;0" dur="3.5s" repeatCount="indefinite"/></circle>
</svg>'''

def footer():
    W, H = 1200, 110
    return f'''{svg_open(W, H, "footer")}
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{TEAL}"/><stop offset="0.5" stop-color="{BLUE}"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs>
<rect width="{W}" height="{H}" rx="16" fill="url(#g)"/>
<path d="M0 70 Q150 40 300 70 T600 70 T900 70 T1200 70 T1500 70 T1800 70 V110 H0Z" fill="#fff" fill-opacity="0.08"><animateTransform attributeName="transform" type="translate" values="0 0;-300 0" dur="8s" repeatCount="indefinite"/></path>
<text x="600" y="52" text-anchor="middle" font-family="{SANS}" font-size="24" font-weight="700" letter-spacing="3" fill="#fff">THANKS FOR VISITING</text>
<text x="600" y="80" text-anchor="middle" font-family="{MONO}" font-size="14" fill="#CCFBF1">let's build something thoughtful</text>
</svg>'''

# ───────────────────────── BUILD ─────────────────────────
save("banner.svg", banner())
save("typing.svg", typing())
save("terminal.svg", terminal())
save("skills-1.svg", marquee(SKILLS_ROW1, False, "AI and ML skills"))
save("skills-2.svg", marquee(SKILLS_ROW2, True, "Backend, automation and tools"))
for i, p in enumerate(PROJECTS, 1):
    save(f"card-{i}.svg", card(i, *p))
for key, num, title in SECTIONS:
    save(f"h-{key}.svg", header(num, title))
save("footer.svg", footer())
print("Generated", len(os.listdir(OUT)), "assets in", OUT)
