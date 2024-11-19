import datetime
import json
import os
import matplotlib.pyplot as plt

class GolfProgressTracker:
    def __init__(self, data_file='golf_data.json'):
        self.data_file = data_file
        self.daily_logs = []
        self.milestones = {
            'Break 100': False,
            'Break 90': False,
            'Break 80': False,
            'Handicap < 15': False,
            'Handicap < 10': False,
            'Scratch Golfer': False
        }
        self.practice_days = 0
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    # Try to load JSON data
                    data = json.load(file)
                    self.daily_logs = data.get('daily_logs', [])
                    self.milestones = data.get('milestones', self.milestones)
                    self.practice_days = data.get('practice_days', 0)
            except (json.JSONDecodeError, ValueError) as e:
                print(f"Data file is corrupted or empty: {e}. Reinitializing data...")
                self.reinitialize_data()
        else:
            self.reinitialize_data()

    def reinitialize_data(self):
        # Set default values
        self.daily_logs = []
        self.milestones = {
            'Break 100': False,
            'Break 90': False,
            'Break 80': False,
            'Handicap < 15': False,
            'Handicap < 10': False,
            'Scratch Golfer': False
        }
        self.practice_days = 0
        # Save the initialized data to the file
        self.save_data()

    def save_data(self):
        data = {
            'daily_logs': self.daily_logs,
            'milestones': self.milestones,
            'practice_days': self.practice_days
        }
        with open(self.data_file, 'w') as file:
            json.dump(data, file)

    def log_practice(self):
        date = datetime.date.today()
        range_balls = int(input("Enter the number of range balls hit today: "))
        short_game_hours = float(input("Enter the number of hours spent on short game practice today: "))
        holes_played = int(input("Enter the number of holes played today (0 if none): "))
        score = None
        if holes_played > 0:
            score = int(input(f"Enter your score for the {holes_played}-hole round: "))
        practiced_today = input("Did you practice today? (yes/no): ").strip().lower() == 'yes'

        log_entry = {
            'Date': str(date),
            'Range Balls': range_balls,
            'Short Game Hours': short_game_hours,
            'Holes Played': holes_played,
            'Score': score
        }
        self.daily_logs.append(log_entry)
        if practiced_today:
            self.practice_days += 1
        print(f"Logged practice for {date}.")
        if score is not None:
            self.update_milestones(score)
        self.save_data()

    def update_milestones(self, score):
        if not self.milestones['Break 100'] and score < 100:
            self.milestones['Break 100'] = True
            print("Congratulations! You've broken 100.")
        if not self.milestones['Break 90'] and score < 90:
            self.milestones['Break 90'] = True
            print("Congratulations! You've broken 90.")
        if not self.milestones['Break 80'] and score < 80:
            self.milestones['Break 80'] = True
            print("Congratulations! You've broken 80.")
        if not self.milestones['Handicap < 15'] and score < 85:
            self.milestones['Handicap < 15'] = True
            print("Congratulations! Your estimated handicap is below 15.")
        if not self.milestones['Handicap < 10'] and score < 80:
            self.milestones['Handicap < 10'] = True
            print("Congratulations! Your estimated handicap is below 10.")
        if not self.milestones['Scratch Golfer'] and score == 72:
            self.milestones['Scratch Golfer'] = True
            print("Congratulations! You've achieved a scratch golfer status.")
        self.save_data()

    def calculate_averages(self):
        nine_hole_scores = [log['Score'] for log in self.daily_logs if
                            log['Holes Played'] == 9 and log['Score'] is not None]
        eighteen_hole_scores = [log['Score'] for log in self.daily_logs if
                                log['Holes Played'] == 18 and log['Score'] is not None]

        if nine_hole_scores:
            avg_9_holes = sum(nine_hole_scores) / len(nine_hole_scores)
        else:
            avg_9_holes = None

        if eighteen_hole_scores:
            avg_18_holes = sum(eighteen_hole_scores) / len(eighteen_hole_scores)
        else:
            avg_18_holes = None

        return avg_9_holes, avg_18_holes

    def weekly_summary(self):
        week_logs = self.daily_logs[-7:]
        total_range_balls = sum(log['Range Balls'] for log in week_logs)
        total_short_game_hours = sum(log['Short Game Hours'] for log in week_logs)
        total_holes_played = sum(log['Holes Played'] for log in week_logs)

        print("\nWeekly Summary:")
        print(f"Total Range Balls Hit: {total_range_balls}")
        print(f"Total Short Game Practice Hours: {total_short_game_hours:.2f}")
        print(f"Total Holes Played: {total_holes_played}")
        print(f"Total Practice Days This Week: {len([log for log in week_logs if log['Date'] != ''])}")

        avg_9_holes, avg_18_holes = self.calculate_averages()
        if avg_9_holes is not None:
            print(f"Average 9-Hole Score: {avg_9_holes:.2f}")
        else:
            print("No 9-Hole Rounds Recorded Yet.")

        if avg_18_holes is not None:
            print(f"Average 18-Hole Score: {avg_18_holes:.2f}")
        else:
            print("No 18-Hole Rounds Recorded Yet.")

    def total_summary(self):
        total_range_balls = sum(log['Range Balls'] for log in self.daily_logs)
        total_short_game_hours = sum(log['Short Game Hours'] for log in self.daily_logs)
        total_holes_played = sum(log['Holes Played'] for log in self.daily_logs)

        print("\nTotal Summary:")
        print(f"Total Range Balls Hit: {total_range_balls}")
        print(f"Total Short Game Practice Hours: {total_short_game_hours:.2f}")
        print(f"Total Holes Played: {total_holes_played}")
        print(f"Total Practice Days: {self.practice_days}")

        avg_9_holes, avg_18_holes = self.calculate_averages()
        if avg_9_holes is not None:
            print(f"Average 9-Hole Score: {avg_9_holes:.2f}")
        else:
            print("No 9-Hole Rounds Recorded Yet.")

        if avg_18_holes is not None:
            print(f"Average 18-Hole Score: {avg_18_holes:.2f}")
        else:
            print("No 18-Hole Rounds Recorded Yet.")

    def milestone_status(self):
        print("\nMilestone Status:")
        for milestone, achieved in self.milestones.items():
            status = "Achieved" if achieved else "Not Achieved"
            print(f"{milestone}: {status}")

    def plot_scores(self):
        dates = [log['Date'] for log in self.daily_logs if log['Score'] is not None]
        nine_hole_scores = [log['Score'] for log in self.daily_logs if
                            log['Holes Played'] == 9 and log['Score'] is not None]
        eighteen_hole_scores = [log['Score'] for log in self.daily_logs if
                                log['Holes Played'] == 18 and log['Score'] is not None]

        plt.figure(figsize=(10, 6))

        if nine_hole_scores:
            plt.plot(dates[:len(nine_hole_scores)], nine_hole_scores, label='9-Hole Scores', marker='o')

        if eighteen_hole_scores:
            plt.plot(dates[:len(eighteen_hole_scores)], eighteen_hole_scores, label='18-Hole Scores', marker='o')

        plt.xlabel('Date')
        plt.ylabel('Score')
        plt.title('Golf Score Progression')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def run(self):
        # Log daily practices (will prompt for input)
        self.log_practice()

        # Get a weekly summary
        self.weekly_summary()

        # Get a total summary
        self.total_summary()

        # Check milestone status
        self.milestone_status()

        # Plot the score progression
        self.plot_scores()



# Example Usage
tracker = GolfProgressTracker()
tracker.run()
