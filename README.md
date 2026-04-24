# SQLite Action Tracker

A lightweight Python utility designed to track and log user actions securely within a local SQLite database. It provides an efficient and isolated way to maintain audit logs or capture usage analytics without requiring an external database server.

## Features

- **Local Storage:** Utilizes SQLite for fast, local, and file-based data persistence.
- **Intuitive Interface:** Easily log actions with distinct types and supplementary context..
- **Automated Timestamping:** The system automatically captures the exact moment an action is saved to the database.

## Database Structure & Logs Explanation :

The logs are stored in a database file named `tracker.db`, containing a main table called `user_logs`. This helps in systematically addressing *what* action took place and *when* it occurred.

| Column        | Type     | Purpose                                                                             |
|---------------|----------|-------------------------------------------------------------------------------------|
| `id`          | INTEGER  | Primary key. Automatically increments with each new log entry.                        |
| `action_type` | TEXT     | A high-level category of the action (e.g., "USER_LOGIN", "PAGE_VIEW").               |
| `description` | TEXT     | Detailed human-readable context concerning the action (e.g., user IP, file names).  |
| `timestamp`   | DATETIME | An automatically assigned UTC timestamp corresponding to when the log was recorded. |

## Usage Tracking

To test the basic functionality:

```bash
python tracker.py
```

This will run the example block, logging a few mock user actions and printing out the most recent ones. You can integrate the `UserTracker` class into any existing Python application to begin recording events.
