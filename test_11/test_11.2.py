import pickle

student_scores = {
    "张三": 85,
    "李四": 92,
    "王二": 78,
    "麻子": 90
}

with open('student_scores.pkl', 'wb') as file:
    pickle.dump(student_scores, file)
print("Student scores have been saved to student_scores.pkl")
with open('student_scores.pkl', 'rb') as file:
    loaded_scores = pickle.load(file)
print("Loaded student scores:")
for student, score in loaded_scores.items():
    print(f"{student}: {score}")
