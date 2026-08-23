import os
import json
import calendar
import urllib.request
from datetime import date

def get_uptime(today=None):
    if today is None:
        today = date.today()
    birth = date(2006, 1, 14)
    years = today.year - birth.year
    months = today.month - birth.month
    days = today.day - birth.day
    
    if days < 0:
        prev_month = today.month - 1 if today.month > 1 else 12
        prev_year = today.year if today.month > 1 else today.year - 1
        _, num_days = calendar.monthrange(prev_year, prev_month)
        days += num_days
        months -= 1
        
    if months < 0:
        months += 12
        years -= 1
        
    parts = []
    if years:
        parts.append(f"{years} years" if years != 1 else f"{years} year")
    if months:
        parts.append(f"{months} months" if months != 1 else f"{months} month")
    if days:
        parts.append(f"{days} days" if days != 1 else f"{days} day")
    return ", ".join(parts) if parts else "0 days"

def fetch_live_stats():
    token = os.environ.get('GITHUB_TOKEN')
    headers = {'User-Agent': 'Mozilla/5.0'}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    
    stars = 45
    forks = 97
    repos_count = 19
    followers = 23
    
    try:
        req = urllib.request.Request('https://api.github.com/users/shouri123', headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            repos_count = data.get('public_repos', repos_count)
            followers = data.get('followers', followers)
            
        req_repos = urllib.request.Request('https://api.github.com/users/shouri123/repos?per_page=100', headers=headers)
        with urllib.request.urlopen(req_repos, timeout=10) as resp:
            repo_data = json.loads(resp.read().decode())
            stars = sum(r.get('stargazers_count', 0) for r in repo_data)
            forks = sum(r.get('forks_count', 0) for r in repo_data)
    except Exception as e:
        print(f"Using default fallback stats: {e}")
        
    return {
        'stars': stars,
        'forks': forks,
        'repos': repos_count,
        'followers': followers
    }

def update_cards():
    uptime_str = get_uptime()
    stats = fetch_live_stats()
    
    # Read existing dark_mode.svg for base ASCII avatar lines
    with open('dark_mode.svg', 'r', encoding='utf-8') as f:
        dark_raw = f.read()

    start_pos = dark_raw.find('<text x="28"')
    end_pos = dark_raw.find('<text x="5')
    ascii_dark_lines = dark_raw[start_pos:end_pos].strip()
    ascii_light_lines = ascii_dark_lines.replace('fill="#c9d1d9"', 'fill="#24292f"')

    width = "1140"
    height = "590"
    x = "525"

    dark_right_text = f"""<text x="{x}" y="30" fill="#c9d1d9" font-family="'Consolas', 'Menlo', 'DejaVu Sans Mono', monospace" xml:space="preserve" font-size="14.5">
<tspan x="{x}" y="28"><tspan class="value">shouri@chakraborty</tspan><tspan class="cc"> -————————————————————————————-—-</tspan></tspan>
<tspan x="{x}" y="48"><tspan class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> ................... </tspan><tspan class="value">Windows, Linux</tspan></tspan>
<tspan x="{x}" y="68"><tspan class="cc">. </tspan><tspan class="key">Uptime</tspan>:<tspan class="cc"> ............... </tspan><tspan class="value">{uptime_str}</tspan></tspan>
<tspan x="{x}" y="88"><tspan class="cc">. </tspan><tspan class="key">Host</tspan>:<tspan class="cc"> ................. </tspan><tspan class="value">Kolkata, India (IEM Kolkata)</tspan></tspan>
<tspan x="{x}" y="108"><tspan class="cc">. </tspan><tspan class="key">Role</tspan>:<tspan class="cc"> ................. </tspan><tspan class="value">AI Developer &amp; Open Source Maintainer</tspan></tspan>
<tspan x="{x}" y="128"><tspan class="cc">. </tspan><tspan class="key">IDE</tspan>:<tspan class="cc"> .................. </tspan><tspan class="value">VS Code, Antigravity, Cursor</tspan></tspan>
<tspan x="{x}" y="148"><tspan class="cc">. </tspan></tspan>
<tspan x="{x}" y="166"><tspan class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Programming</tspan>:<tspan class="cc">  </tspan><tspan class="value">TypeScript, Python, JavaScript, Java, C++</tspan></tspan>
<tspan x="{x}" y="186"><tspan class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Computer</tspan>:<tspan class="cc"> ... </tspan><tspan class="value">SQL, HTML5, CSS3, JSON, YAML, GraphQL</tspan></tspan>
<tspan x="{x}" y="206"><tspan class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Real</tspan>:<tspan class="cc"> ....... </tspan><tspan class="value">English, Bengali, Hindi</tspan></tspan>
<tspan x="{x}" y="226"><tspan class="cc">. </tspan></tspan>
<tspan x="{x}" y="244"><tspan class="cc">. </tspan><tspan class="key">Focus</tspan>.<tspan class="key">AI</tspan>:<tspan class="cc"> ............. </tspan><tspan class="value">Generative AI, Coding Agents, MAMWA, RAG</tspan></tspan>
<tspan x="{x}" y="264"><tspan class="cc">. </tspan><tspan class="key">Focus</tspan>.<tspan class="key">Frameworks</tspan>:<tspan class="cc"> ...... </tspan><tspan class="value">Next.js 16, React 19, OpenAI SDK, LangChain</tspan></tspan>
<tspan x="{x}" y="284"><tspan class="cc">. </tspan><tspan class="key">Focus</tspan>.<tspan class="key">Backend</tspan>:<tspan class="cc"> ......... </tspan><tspan class="value">Node.js, Supabase, PostgreSQL, FastAPI</tspan></tspan>
<tspan x="{x}" y="304"><tspan class="cc">. </tspan></tspan>
<tspan x="{x}" y="322"><tspan class="value">- Contact &amp; Links</tspan><tspan class="cc"> -—————————————————————————————————————-—-</tspan></tspan>
<tspan x="{x}" y="342"><tspan class="cc">. </tspan><tspan class="key">Portfolio</tspan>:<tspan class="cc"> ............ </tspan><tspan class="value">devshouri.in</tspan></tspan>
<tspan x="{x}" y="362"><tspan class="cc">. </tspan><tspan class="key">Email</tspan>:<tspan class="cc"> ................ </tspan><tspan class="value">chakrabortyshouri@gmail.com</tspan></tspan>
<tspan x="{x}" y="382"><tspan class="cc">. </tspan><tspan class="key">LinkedIn</tspan>:<tspan class="cc"> ............. </tspan><tspan class="value">shouri-chakraborty-224b5330b</tspan></tspan>
<tspan x="{x}" y="402"><tspan class="cc">. </tspan><tspan class="key">GitHub</tspan>:<tspan class="cc"> ............... </tspan><tspan class="value">github.com/shouri123</tspan></tspan>
<tspan x="{x}" y="422"><tspan class="cc">. </tspan></tspan>
<tspan x="{x}" y="440"><tspan class="value">- Featured Repos</tspan><tspan class="cc"> -—————————————————————————————————————-—-</tspan></tspan>
<tspan x="{x}" y="460"><tspan class="cc">. </tspan><tspan class="value">Late-Meet</tspan> (<tspan class="key">44★</tspan> | <tspan class="key">97 forks</tspan>): <tspan class="value">AI Chrome Ext with Local LLMs &amp; VAD</tspan></tspan>
<tspan x="{x}" y="480"><tspan class="cc">. </tspan><tspan class="value">Aven</tspan> &amp; <tspan class="value">Chat-Buddy</tspan>: <tspan class="value">Multi-Agent MAMWA &amp; OpenAI Agents SDK</tspan></tspan>
<tspan x="{x}" y="500"><tspan class="cc">. </tspan></tspan>
<tspan x="{x}" y="518"><tspan class="value">- Verified GitHub &amp; OSS Stats</tspan><tspan class="cc"> -————————————————————————-—-</tspan></tspan>
<tspan x="{x}" y="538"><tspan class="cc">. </tspan><tspan class="key">Repos</tspan>: <tspan class="value">{stats['repos']}</tspan> | <tspan class="key">Stars</tspan>: <tspan class="value">{stats['stars']}</tspan> | <tspan class="key">Forks</tspan>: <tspan class="value">{stats['forks']}</tspan> | <tspan class="key">Followers</tspan>: <tspan class="value">{stats['followers']}</tspan></tspan>
<tspan x="{x}" y="558"><tspan class="cc">. </tspan><tspan class="key">Contributions</tspan>: <tspan class="value">1,470+</tspan> | <tspan class="key">PR Reviews</tspan>: <tspan class="value">273+</tspan> (GSSoC Admin)</tspan>
<tspan x="{x}" y="578"><tspan class="cc">. </tspan><tspan class="key">Lines of Code</tspan>: <tspan class="value">384,120</tspan> ( <tspan class="addColor">892,410</tspan><tspan class="addColor">++</tspan>, <tspan class="delColor">508,290</tspan><tspan class="delColor">--</tspan> )</tspan>
</text>"""

    light_right_text = dark_right_text.replace('fill="#c9d1d9"', 'fill="#24292f"')

    dark_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="ASCII GitHub profile card for shouri123">
<style>
.key {{fill: #ffa657;}}
.value {{fill: #a5d6ff;}}
.addColor {{fill: #3fb950;}}
.delColor {{fill: #f85149;}}
.cc {{fill: #616e7f;}}
text, tspan {{white-space: pre;}}
</style>
<rect x="0.5" y="0.5" width="{int(width) - 1}" height="{int(height) - 1}" rx="10" fill="#0d1117" stroke="#30363d"/>
{ascii_dark_lines}
{dark_right_text}
</svg>"""

    light_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="ASCII GitHub profile card for shouri123">
<style>
.key {{fill: #953800;}}
.value {{fill: #0a3069;}}
.addColor {{fill: #1a7f37;}}
.delColor {{fill: #cf222e;}}
.cc {{fill: #8c959f;}}
text, tspan {{white-space: pre;}}
</style>
<rect x="0.5" y="0.5" width="{int(width) - 1}" height="{int(height) - 1}" rx="10" fill="#ffffff" stroke="#d0d7de"/>
{ascii_light_lines}
{light_right_text}
</svg>"""

    with open('dark_mode.svg', 'w', encoding='utf-8') as f:
        f.write(dark_svg)

    with open('light_mode.svg', 'w', encoding='utf-8') as f:
        f.write(light_svg)

    print(f"Cards updated. Uptime: {uptime_str}, Stars: {stats['stars']}, Forks: {stats['forks']}")

if __name__ == '__main__':
    update_cards()
