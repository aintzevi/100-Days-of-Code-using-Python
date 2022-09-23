import pandas

student_dict = {
    "student": ["Kat", "Bob", "Tom", "Raki"],
    "score": [90, 51, 40, 84],

}

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():

    if row.student == "Tom":
        print(row.score)
