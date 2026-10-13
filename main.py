import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load student data
df = pd.read_csv("students.csv")

# Calculate total and average marks
df["Total"] = df["Math"] + df["Python"]
df["Average"] = np.round(df["Total"] / 2, 2)

# Assign grades
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(calculate_grade)

# Check pass or fail
df["Result"] = np.where(
    (df["Math"] >= 40) &
    (df["Python"] >= 40) &
    (df["Attendance"] >= 75),
    "Pass",
    "Fail"
)

# Display complete student report
print("\n===== STUDENT PERFORMANCE ANALYTICS SYSTEM =====")
print(df.to_string(index=False))

# Calculate class statistics
print("\n===== CLASS STATISTICS =====")
print("Total Students:", len(df))
print("Class Average:", round(df["Average"].mean(), 2))
print("Highest Average:", df["Average"].max())
print("Lowest Average:", df["Average"].min())

# Find the top student
top_student = df.loc[df["Average"].idxmax()]

print("\n===== TOP STUDENT =====")
print("Name:", top_student["Name"])
print("Department:", top_student["Department"])
print("Average:", top_student["Average"])

# Subject-wise analysis
print("\n===== SUBJECT-WISE ANALYSIS =====")
print("Math Average:", round(df["Math"].mean(), 2))
print("Python Average:", round(df["Python"].mean(), 2))

# Pass and fail statistics
print("\n===== RESULT SUMMARY =====")
print("Students Passed:", (df["Result"] == "Pass").sum())
print("Students Failed:", (df["Result"] == "Fail").sum())

# Department-wise analysis
print("\n===== DEPARTMENT-WISE AVERAGE =====")
print(df.groupby("Department")[["Math", "Python", "Average"]].mean().round(2))
# Department-wise performance chart
dept_avg = df.groupby("Department")["Average"].mean()

plt.bar(dept_avg.index, dept_avg.values)
plt.title("Department-wise Student Performance")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.savefig("department_chart.png")
plt.show()
# Subject-wise comparison chart
subjects = ["Math", "Python"]
subject_avg = [df["Math"].mean(), df["Python"].mean()]

plt.figure()
plt.bar(subjects, subject_avg)
plt.title("Subject-wise Average Marks")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.savefig("subject_chart.png")
plt.show()
# ===== ADVANCED STUDENT SEARCH SYSTEM =====

def search_student():
    student_id = input("Enter Student ID to search: ")

    result = df[df["Student_ID"].astype(str) == student_id]

    if not result.empty:
        print("\n===== STUDENT FOUND =====")
        print(result.to_string(index=False))
    else:
        print("Student ID not found!")

search_student()
# ===== ADVANCED RESULT SUMMARY =====

print("\n===== ADVANCED RESULT SUMMARY =====")

total_students = len(df)
pass_students = (df["Result"] == "Pass").sum()
fail_students = (df["Result"] == "Fail").sum()

pass_percentage = (pass_students / total_students) * 100

print("Total Students:", total_students)
print("Pass Students:", pass_students)
print("Fail Students:", fail_students)
print("Pass Percentage:", round(pass_percentage, 2), "%")
# ===== TOP 5 STUDENTS REPORT =====

print("\n===== TOP 5 STUDENTS =====")

top_students = df.sort_values(
    by="Total",
    ascending=False
).head(5)

print(top_students.to_string(index=False))
# ===== DEPARTMENT-WISE STUDENT COUNT =====

print("\n===== DEPARTMENT-WISE STUDENT COUNT =====")

department_count = df["Department"].value_counts()

print(department_count.to_string())
# ===== DEPARTMENT-WISE AVERAGE MARKS =====

print("\n===== DEPARTMENT-WISE AVERAGE MARKS =====")

dept_avg = df.groupby("Department")["Average"].mean()

print(dept_avg.round(2).to_string())
print("\n===== STUDENT PERFORMANCE USING LOOP =====")

for index, row in df.iterrows():
    print(row["Name"], "-", row["Average"], "-", row["Grade"])