---
name: current-datetime
description: Get the exact current date, day of week, and time from the local machine. Use when a task depends on today, yesterday, deadlines, filenames, journal dates, or current time.
disable-model-invocation: false
user-invocable: false
allowed-tools: Bash
---

# Current Date and Time

Use this skill whenever exact local date or time matters.

Run:

```bash
python3 .agents/skills/current-datetime/get_datetime.py
```

Treat the script output as authoritative for date-sensitive work.
