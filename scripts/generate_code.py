from datetime import datetime
import random

# Generate a 6-digit code
code = random.randint(100000, 999999)

# Timestamp
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

# Output format for cron log
print(f"{timestamp} - 2FA Code: {code}")
