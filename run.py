import argparse, random, subprocess, time
from datetime import date, timedelta
import calendar

def month(ym_start, ym_end):
    """Yield YYYY-MM strings from start to end inclusive."""
    y0, m0 = map(int, ym_start.split("-"))
    y1, m1 = map(int, ym_end.split("-"))
    cur_y, cur_m = y0, m0
    while (cur_y, cur_m) <= (y1, m1):
        yield f"{cur_y:04d}-{cur_m:02d}"
        if cur_m == 12:
            cur_y += 1
            cur_m = 1
        else:
            cur_m += 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ym0", required=True)  # YYYY-MM
    ap.add_argument("--ym1", required=True)    # YYYY-MM
    args = ap.parse_args()

    ym0 = args.ym0
    ym1 = args.ym1

    for cur in month(ym0, ym1):
        y, m = map(int, cur.split("-"))
        start_date = date(y, m, 1)
        end_date = date(y, m, calendar.monthrange(y, m)[1])
        print(f">>> Running for {cur}")
        cmd = ["scrapy", "crawl", "search", "-s", f"START_DATE={start_date}", "-s", f"END_DATE={end_date}"]
        print (f">>> Command: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)

        if cur < ym1:
            slp = random.randint(600, 1200)
            print(f">>> Sleeping {slp}s...")
            time.sleep(slp)

if __name__ == "__main__":
    main()



