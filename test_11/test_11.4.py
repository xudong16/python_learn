import pandas as pd
import numpy as np


def generate_mock_data(input_file):
    np.random.seed(0)
    students = ['王伟', '刘科', '梅冲', '王未', '田如']
    courses = ['数学', '语文', '英语']
    data = []

    for student in students:
        for course in courses:
            num_scores = np.random.randint(1, 10)
            scores = np.random.randint(60, 101, num_scores)
            for score in scores:
                data.append([student, course, score])

    df = pd.DataFrame(data, columns=['姓名', '课程', '分数'])

    df.to_excel(input_file, index=False)
    print(f"模拟成绩数据已写入 {input_file}")


def calculate_max_scores(input_file, output_file):
    df = pd.read_excel(input_file)
    max_scores = df.groupby(['姓名', '课程'], as_index=False)['分数'].max()
    max_scores.to_excel(output_file, index=False)
    print(f"所有学生每门课程的最高成绩已写入 {output_file}")


input_file = 'student_scores.xlsx'
output_file = 'max_student_scores.xlsx'

generate_mock_data(input_file)
calculate_max_scores(input_file, output_file)
