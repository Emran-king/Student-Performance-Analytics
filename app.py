from flask import Flask, render_template, request
import pandas as pd

print("Starting Student Analytics App...")

app = Flask(__name__)

df = pd.read_csv("students.csv")
print("CSV loaded successfully!")
print("Total students:", len(df))

@app.route("/")
def home():
    total_students = len(df)
    departments = df["Department"].nunique()
    average_marks = round(df[["Math", "Python"]].mean().mean(), 2)

    department_averages = df.groupby("Department")[["Math", "Python"]].mean().mean(axis=1).round(2)

    return render_template(
        "index.html",
        total_students=total_students,
        departments=departments,
        average_marks=average_marks,
        department_averages=department_averages
    )

if True:
    print("Starting Flask server...")
    app.run(debug=True)