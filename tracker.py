import sqlite3
import datetime

class UserTracker:
    def __init__(self, db_name="tracker.db"):
        self.db_name = db_name
        self._initialize_db()

    def _initialize_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    action_type TEXT NOT NULL,
                    description TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    def log_action(self, action_type, description=""):
        """Logs a user action into the database."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO user_logs (action_type, description) VALUES (?, ?)",
                (action_type, description)
            )
            conn.commit()
        print(f"Logged action: [{action_type}] {description}")

    def get_logs(self, limit=10):
        """Retrieves recent logs."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, action_type, description, timestamp FROM user_logs ORDER BY timestamp DESC LIMIT ?",
                (limit,)
            )
            return cursor.fetchall()

if __name__ == "__main__":
    tracker = UserTracker()
    
    # Example usage
    tracker.log_action("USER_LOGIN", "User admin logged in from 192.168.1.100.")
    tracker.log_action("PAGE_VIEW", "User navigated to the settings page.")
    tracker.log_action("RESOURCE_DOWNLOAD", "Downloaded report_2024.pdf.")
    tracker.log_action("USER_LOGOUT", "User admin logged out.")
    
    print("\n--- Recent Logs ---")
    for log in tracker.get_logs():
        print(f"ID: {log[0]} | Action: {log[1]} | Details: {log[2]} | Time: {log[3]}")
