
def calculate_average(marks):
    return sum(marks) / len(marks)

def main():
    print("Fundamentals of AI & ML - Basic Python Program")
    
    # Sample student marks dataset
    marks = [85, 90, 78, 92, 88]
    
    average = calculate_average(marks)
    
    print("Student Marks:", marks)
    print("Average Marks:", average)

if __name__ == "__main__":
    main()
