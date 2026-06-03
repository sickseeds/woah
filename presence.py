import psutil
import time
import os
from datetime import datetime
import pygetwindow as gw

start_time = time.time()

# =========================
# SCREEN CLEAR
# =========================
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# =========================
# TIMER (SESSION TIME)
# =========================
def get_time():
    seconds = int(time.time() - start_time)
    minutes = seconds // 60
    sec = seconds % 60
    return f"{minutes}m {sec}s"


# =========================
# CLOCK (REAL TIME)
# =========================
def get_clock():
    return datetime.now().strftime("%I:%M %p")

def get_active_window():
    try:
        window = gw.getActiveWindow()

        if window:
            return window.title

    except Exception:
        pass

    return "Unknown Window"

# =========================
# ACTIVITY DETECTION
# =========================
def get_activity():
    for proc in psutil.process_iter(['name']):
        name = proc.info['name']

        if not name:
            continue

        name = name.lower()

        if "code" in name:
            return ("ᨳ 𝒻𝓁𝓎 𝓂𝑒 𝒶𝓌𝒶𝓎...", "𝟕 𝟕 𝟕")

        if "fluxer" in name or "element" in name:
            return ("♱ 𝔟𝔢 𝔫𝔬𝔱 𝔞𝔣𝔯𝔞𝔦𝔡", "𓂋 🪽")

        if "vivaldi" in name or "firefox" in name:
            return ("♱ ⁴⁴⁴", "𝔩𝔲𝔠𝔦𝔣𝔢𝔯'𝔰 𝔭𝔢𝔱")

        if "youtube" in name:
            return ("𝒟𝑅𝒪𝒲𝒩𝐼𝒩𝒢", " ׅ 𝄂𝄚𝅦𝄚𝄞𝅄ㅤ")

        if "steam" in name or "vrchat" in name:
            return ("𝘸𝘩𝘺 𝘢𝘳𝘦 𝘺𝘰𝘶 𝘤𝘳𝘺𝘪𝘯𝘨, 𝘭𝘢𝘪𝘯?", " 🇮  🇳    🇹  🇭  🇪    🇼  🇮  🇷  🇪  🇩 ")

    return ("ᶻ 𝗓 𐰁 Idle", "⁇ AFK ⁇")


# =========================
# RENDER UI
# =========================
def render(status, detail, timer, clock, window):
    print(" ♡ 𝓃ℴ𝒷ℴ𝒹𝓎 𝓃ℴ𝒷ℴ𝒹𝓎 𝓃ℴ𝒷ℴ𝒹𝓎 ♡")
    print("   · · ─ ·✶· ─ · ·")
    print(f" 𝕞𝕖𝕟𝕥𝕒𝕝 : {status:<18}")
    print(f" 𝕤𝕒𝕟𝕚𝕥𝕪 : {detail:<18}")
    print(f" 𝕥𝕚𝕞𝕖   : {timer:<18}")
    print(f" 𝕔𝕝𝕠𝕔𝕜  : {clock:<18}")
    print(f" 𝕨𝕚𝕟𝕕𝕠𝕨 : {window}")
    print("   · · ─ ·✶· ─ · ·")


# =========================
# MAIN LOOP
# =========================
def main():
    last = None

    while True:
        status, detail = get_activity()
        timer = get_time()
        clock = get_clock()
        window = get_active_window()

        if (status, detail) != last:
            clear()
            render(status, detail, timer, clock, window)

        time.sleep(2)


if __name__ == "__main__":
    main()