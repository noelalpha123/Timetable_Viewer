import json
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

# File to store timetable data
TIMETABLE_FILE = 'timetable_data.json'

# Load timetable data from the file (or use default if file doesn't exist)
def load_timetable():
    try:
        with open(TIMETABLE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Return default data if the file doesn't exist
        return {
            "Monday": [
                {"time": "9:00 AM", "subject": "Math", "venue": "Room 101", "faculty": " Dr. Salvin Saju "},
                {"time": "11:00 AM", "subject": "Physics", "venue": "Room 102", "faculty": " Dr. Noel G.J "},
                {"time": "1:00 PM", "subject": "History", "venue": "Room 103", "faculty": " Ms. Milna "},
            ],
            "Tuesday": [
                {"time": "10:00 AM", "subject": "Chemistry", "venue": "Room 104", "faculty": " Dr. Salvin Saju "},
                {"time": "12:00 PM", "subject": "Biology", "venue": "Room 105", "faculty": " Dr. Noel G.J "},
                {"time": "2:00 PM", "subject": "English", "venue": "Room 106", "faculty": " Ms. Milna "},
            ],
            "Wednesday": [
                {"time": "9:30 AM", "subject": "Computer Science", "venue": "Room 107", "faculty": " Dr. Salvin Saju "},
                {"time": "11:30 AM", "subject": "Math", "venue": "Room 108", "faculty": " Dr. Noel G.J "},
                {"time": "1:30 PM", "subject": "Philosophy", "venue": "Room 109", "faculty": " Ms. Milna "},
            ],
        }

# Save the timetable data to the file
def save_timetable(timetable):
    with open(TIMETABLE_FILE, 'w') as f:
        json.dump(timetable, f, indent=4)

# Admin password
admin_password = "1234"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        entered_password = request.form.get('password')
        if entered_password == admin_password:
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', error="Invalid password, please try again.")
    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    timetable_data = load_timetable()

    if request.method == 'POST':
        # Update timetable with submitted data (both subject and venue)
        for day, sessions in timetable_data.items():
            for i, session in enumerate(sessions):
                # Get the new subject and venue from the form
                new_subject = request.form.get(f"{day}_{session['time']}_subject")
                new_venue = request.form.get(f"{day}_{session['time']}_venue")
                new_Faculty = request.form.get(f"{day}_{session['time']}_faculty")
                
                # Update subject and venue if they were changed
                if new_subject:
                    timetable_data[day][i]["subject"] = new_subject
                if new_venue:
                    timetable_data[day][i]["venue"] = new_venue
                if new_Faculty:
                    timetable_data[day][i]["faculty"] = new_Faculty

        # Save the updated timetable to the file
        save_timetable(timetable_data)
        return render_template('timetable.html', timetable=timetable_data, is_admin=True)

    return render_template('timetable.html', timetable=timetable_data, is_admin=True)

@app.route('/student')
def student():
    timetable_data = load_timetable()
    print(timetable_data)
    return render_template('timetable.html', timetable=timetable_data, is_admin=False)

if __name__ == "__main__":
    app.run(debug=True)
