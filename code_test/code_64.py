def subject_marks(subjectmarks):
 """
 Write a function to sort a list of tuples using lambda.
 """
#subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
 subjectmarks.sort(key = lambda x: x[1])
 return subjectmarks
