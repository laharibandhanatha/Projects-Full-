def Marks(list1):
    totalMarks = sum(list1)
    avergeMarks = totalMarks / len(list1)
    if avergeMarks >=90:
        return "A+"
    elif avergeMarks >=80:
        return "A"
    elif avergeMarks >=70:
        return "B"
    elif avergeMarks >=60:
        return "C"
    elif avergeMarks >=50:
        return "D"
    elif avergeMarks <=49:
        return "F"
