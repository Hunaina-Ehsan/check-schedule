from datetime import datetime

def main():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"✅ GitHub Actions test run at {now}")

if __name__ == "__main__":
    main()
