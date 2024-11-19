Golf Progress Tracker

This project is a Golf Progress Tracker aimed at helping users monitor and improve their golf skills over time. The tracker logs daily practice details, records milestones, and provides insights into practice frequency and game progress.

Files

1. main.py
The main Python file containing the code to track golf practices, update milestones, and analyze the progress recorded in the golf data.

2. golf_data.json
This JSON file stores all golf practice data and milestones, structured as follows:

daily_logs: Records daily practice information, including:
Date: Date of the practice session.
Range Balls: Number of range balls hit.
Short Game Hours: Time (in hours) spent on the short game.
Holes Played: Number of holes played.
Score: Score recorded for the session (if applicable).
milestones: Tracks golfing milestones, such as breaking certain score thresholds or achieving handicap goals.
practice_days: Counts the total number of unique practice days.
Functionality
The Golf Progress Tracker performs the following functions:

Logging Daily Practice:
Allows users to log daily practice sessions, recording balls hit, short game hours, and holes played.
Milestone Tracking:
Checks for milestone achievements based on user scores and updates the milestones section.
Practice Analysis:
Analyzes total practice days, scores, and other metrics to track improvement and provide feedback.
Requirements

To run this project, you will need:

Python 3.x
json library (usually pre-installed with Python)
Usage

Load Data:
Load golf_data.json to access historical practice data and milestones.
Record New Session:
Use the functions in main.py to add a new session, update milestones, or print a summary of the current progress.
Analyze Progress:
Run specific functions to display milestone achievements, practice frequency, and session breakdowns.
Example

Run the following to start logging sessions:

# Load and initialize data
with open('golf_data.json') as f:
    golf_data = json.load(f)

# Example usage
log_practice_session(golf_data, date="2024-08-21", range_balls=100, short_game_hours=0, holes_played=0, score=None)
Future Improvements

Handicap Calculation: Automate handicap calculation based on scores.
Graphical Analysis: Visualize progress over time with graphs for scores, practice frequency, and milestones.
