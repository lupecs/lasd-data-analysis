import pandas as pd
import numpy as np

np.random.seed(42)

# Student Attendance Data
attendance_data = pd.DataFrame({
    'StudentID': np.arange(1001, 1051),
    'School': np.random.choice(['Central High', 'Lincoln High', 'Jefferson High'], 50),
    'Grade': np.random.choice([9, 10, 11, 12], 50),
    'DaysPresent': np.random.randint(120, 180, 50),
    'DaysAbsent': np.random.randint(0, 30, 50),
    'Semester': np.random.choice(['Fall 2024', 'Spring 2025'], 50)
})

# Student Assessment Scores
assessment_data = pd.DataFrame({
    'StudentID': np.arange(1001, 1051),
    'MathScore': np.random.randint(50, 100, 50),
    'ReadingScore': np.random.randint(50, 100, 50),
    'ScienceScore': np.random.randint(50, 100, 50),
    'TestDate': pd.to_datetime(np.random.choice(pd.date_range('2025-02-01', "2025-05-01"), 50))
})

# Teacher Roster and Coourse Assignments
teacher_data = pd.DataFrame({
    'TeacherID': np.arange(2001, 2021),
    'Name': ['Teacher_' + str(i) for i in range(1, 21)],
    'Subject': np.random.choice(['Math', 'Science', 'English', 'History'], 20),
    'School': np.random.choice(['Central High', 'Lincoln High', 'Jefferson High'], 20),
    'GradeLevel': np.random.choice([9, 10, 11, 12], 20),
    'FullTime': np.random.choice([True, False], 20)
})

# Save to excel files
attendance_data.to_excel("lausd_attendance_data.xlsx", index=False)
assessment_data.to_excel("lausd_assessment_data.xlsx", index=False)
teacher_data.to_excel("lausd_teacher_data.xlsx", index=False)

print("Files generated successfully!")