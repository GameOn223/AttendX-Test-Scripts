# AttendX Test Scripts

Selenium test scripts for the AttendX student attendance app. The whole QA team keeps them here so nothing gets overwritten or lost.

## Scripts

- `login_test.py` logs in with a teacher account and checks that we land on the dashboard.
- `attendance_test.py` logs in, marks a student present and checks that the save message shows up.

## Running

Install selenium with `pip install selenium`, start AttendX on localhost:3000, then run a script:

    python login_test.py
    python attendance_test.py

Each script prints PASS or FAIL.
