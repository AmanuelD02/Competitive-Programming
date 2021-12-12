
def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        grade = grades[i]
            
        if grade <= 37:
            continue
        else:
            if (5- grade%5) <=2:
                grades[i] = grade + (5- grade%5)
    return grades
            
                
                
                
                 
    