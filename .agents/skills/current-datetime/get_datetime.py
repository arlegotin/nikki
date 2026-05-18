#!/usr/bin/env python3
"""Print current date, day of week, and local time."""

from datetime import datetime


now = datetime.now()

print(f"Date:  {now.strftime('%Y-%m-%d')}")
print(f"Day:   {now.strftime('%A')}")
print(f"Time:  {now.strftime('%H:%M:%S')}")
print(f"ISO:   {now.isoformat()}")

