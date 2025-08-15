# HACKING WORLD™ — TikTok Like Booster (Y)
# ROOT-ONLY • VIP Neon Edition • Heavy Animations

import os, sys, time, random

# Colors
K = '\033[30m'; R = '\033[1;31m'; G = '\033[1;32m'; Y = '\033[1;33m'
B = '\033[1;34m'; C = '\033[1;36m'; M = '\033[1;35m'; W = '\033[1;37m'
RESET = '\033[0m'

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def typewrite(text, delay=0.01):
    for ch in text:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(delay)
    print()

def spinner_line(text, secs=3):
    spin = ['|','/','-','\\']
    sys.stdout.write(Y + text + " ")
    t0 = time.time(); i=0
    while time.time() - t0 < secs:
        sys.stdout.write(spin[i%4]); sys.stdout.flush()
        time.sleep(0.1); sys.stdout.write('\b'); i+=1
    print(G + "✓" + RESET)

def pulse_bar(title, steps=30, speed=0.03):
    sys.stdout.write(C + title + "\n")
    for i in range(steps+1):
        filled = "█" * i
        empty  = "░" * (steps - i)
        sys.stdout.write(f"{M}[{filled}{empty}] {int(i/steps*100)}%   \r")
        sys.stdout.flush()
        time.sleep(speed + (0.002 * (i%5)))
    print(RESET)

def banner():
    clear()
    neon = [
        f"{M}████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗",
        f"{C}╚══██╔══╝██║██║  ██║╚══██╔══╝██╔═══██╗██║ ██╔╝",
        f"{B}   ██║   ██║███████║   ██║   ██║   ██║█████╔╝ ",
        f"{G}   ██║   ██║██╔══██║   ██║   ██║   ██║██╔═██╗ ",
        f"{Y}   ██║   ██║██║  ██║   ██║   ╚██████╔╝██║  ██╗",
        f"{R}   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝{RESET}"
    ]
    for line in neon:
        print(line); time.sleep(0.03)
    print(f"{W}               H A C K I N G   W O R L D™")
    print(f"{C}    TikTok Like Booster • ROOT-ONLY (WORK){RESET}")
    print(f"{W}────────────────────────────────────────────────────────\n")

def require_root():
    # Unix-like root check
    if hasattr(os, "geteuid"):
        if os.geteuid() != 0:
            print(R + "\n[✘] Root Access Not Found!" + RESET)
            print(Y + "[!] This tool requires ROOT. Open a root shell (e.g., 'tsu') and run again." + RESET)
            input(W + "\nPress Enter to exit…" + RESET)
            sys.exit(1)
    else:
        # On non-Unix platforms, force root-only behavior
        print(R + "\n[✘] Unsupported environment for root check." + RESET)
        input(W + "Press Enter to exit…" + RESET)
        sys.exit(1)

def fake_cluster_logs(username, target, batch):
    clusters = ["ap-sg-1","us-east-2","eu-central-1","in-mum-3","jp-tokyo-2","sa-bhr-1"]
    lines = [
        f"[{random.choice(clusters)}] Elevating privileges … OK",
        f"[{random.choice(clusters)}] Kernel hooks patched … OK",
        f"[{random.choice(clusters)}] Session key: {hex(random.getrandbits(48))}",
        f"[{random.choice(clusters)}] Username: @{username} • Quota window open",
        f"[{random.choice(clusters)}] Allocating {batch} ghost-likes",
        f"[{random.choice(clusters)}] Anti-bot heuristic bypass … OK",
        f"[{random.choice(clusters)}] Rate limit bucket: {random.randint(60,95)}%"
    ]
    for ln in lines:
        typewrite(C + ln + RESET, 0.005); time.sleep(0.1)

def confetti(lines=3, width=48):
    syms = ['*','+','x','•','✦','✧']
    cols = [R,G,Y,B,C,M,W]
    for _ in range(lines):
        row = "".join(random.choice(cols)+random.choice(syms)+RESET for _ in range(width))
        print(row); time.sleep(0.03)

def save_log(username, added):
    try:
        os.makedirs("logs", exist_ok=True)
        path = f"logs/tiktok_like_prank_root_{int(time.time())}.log"
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"HACKING WORLD — TikTok Like Booster (FAKE / ROOT)\n")
            f.write(f"User: @{username}\nAdded Likes (fake): {added}\nTimestamp: {time.ctime()}\n")
        return path
    except Exception:
        return None

def main():
    banner()
    require_root()  # ← Root না থাকলে এখানেই Exit

    spinner_line("[✓] Verifying root privileges", 2)
    spinner_line("[✓] Mounting protected namespaces", 2)
    print()

    username = input(f"{Y}[+] Enter TikTok Username (without @): {W}").strip().lstrip('@') or "unknown_user"
    video = input(f"{Y}[+] Enter Video URL (optional): {W}").strip()
    print()

    spinner_line("[✓] Connecting to TikTok Edge Network", 3)
    spinner_line("[✓] Syncing device fingerprint", 2)
    pulse_bar("[#] Establishing secure tunnel", 34, 0.02)

    print(f"{W}\nSelect Like Package:{RESET}")
    pkgs = [("Lite", 250), ("Boost", 1000), ("Turbo", 5000), ("Ultra", 10000)]
    for i,(n,v) in enumerate(pkgs,1):
        print(f"{C}[{i}] {n:<6} → ~{v} likes{RESET}")
    choice = input(f"{Y}Choose (1-4): {W}").strip()
    try:
        idx = max(1, min(4, int(choice)))
    except:
        idx = 2
    target = pkgs[idx-1][1]
    batch = random.choice([25,50,75,100,125])

    print()
    fake_cluster_logs(username, target, batch)
    print()
    pulse_bar("[#] Preparing like stream", 40, 0.02)

    total = 0
    print(f"{M}\n[*] Streaming ghost-likes to @{username} …{RESET}")
    while total < target:
        step = random.randint(int(batch*0.6), batch)
        total = min(target, total + step)
        bar_len = 40
        filled = int(total/target*bar_len)
        bar = G + "█"*filled + RESET + "░"*(bar_len-filled)
        sys.stdout.write(f"{C}Delivered: {W}{total:>5}/{target:<5}  {bar}\r")
        sys.stdout.flush()
        time.sleep(random.uniform(0.05,0.12))
        if random.random() < 0.07:
            sys.stdout.write(f"\n{Y}[!] Minor rate-limit encountered … smoothing traffic\n")
            time.sleep(0.6)
        if random.random() < 0.05:
            sys.stdout.write(f"{B}[i] Rotating proxy … done\n")

    print()
    pulse_bar("[#] Verifying delivery receipts", 28, 0.02)
    spinner_line("[✓] Clearing temporary fingerprints", 2)

    clear(); banner(); confetti(4, 60)
    print(f"{G}✅ SUCCESS!{RESET} {W}Approximate likes delivered to @{username}: {G}{target}{RESET}")
    if video:
        print(f"{C}Target Video: {W}{video}{RESET}")
    print(f"{Y}Note:{W} This is a simulation for entertainment only.\n")

    log = save_log(username, target)
    if log:
        print(f"{C}[log saved] → {W}{log}{RESET}")
    print()
    input(f"{W}Press Enter to exit…{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RESET+"\n\nInterrupted by user.\n")