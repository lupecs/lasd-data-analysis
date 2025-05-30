import pandas as pd
import numpy as np

# Simulate realistic LAUSD-style attendance and performance dataset
np.random.seed(42)

schools = ['Lincoln HS', 'Roosevelt HS', 'Jefferson HS', 'Hamilton HS']
grades = ['9th', '10th', '11th', '12th']
num_students = 200

data = {
    'StudentID': [f"S{i:04d}" for i in range(1, num_students + 1)],
    'School': np.random.choice(schools, size=num_students),
    'Grade': np.random.choice(grades, size=num_students),
    'Days_Enrolled': np.random.randint(150, 181, size=num_students),
    'Days_Absent': np.random.randint(0, 20, size=num_students),
    'GPA': np.round(np.random.uniform(1.0, 4.0, size=num_students), 2),
    'Math_Score': np.random.randint(50, 100, size=num_students),
    'English_Score': np.random.randint(50, 100, size=num_students),
    'Socioeconomic_Status': np.random.choice(['Low', 'Middle', 'High'], size=num_students, p=[0.5, 0.3, 0.2])
}

lausd_df = pd.DataFrame(data)
lausd_df['Attendance_Rate'] = ((lausd_df['Days_Enrolled'] - lausd_df['Days_Absent']) / lausd_df['Days_Enrolled']).round(2)

# Save to Excel for Excel/Tableau exercises
excel_path = "lausd_attendance_data.xlsx"
lausd_df.to_excel(excel_path, index=False)

lausd_df.head()
