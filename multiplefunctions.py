class subfieldsinai():
    def subfields():
        list=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print('subfields in ai are:') 
        for fields in list:
            print(fields)


    def odd_even(num):
        if(num%2==0):
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

    def eligible():
        gender=input('enter the gender').strip().lower()
        age=int(input('enter the age'))
        if(gender=='male'):
                if(age>=21):
                    print("eligible to marry")
                else:
                    print("not eligible to marry")
        elif(gender=='female'):
                if(age>=18):
                    print("eligible to marry")
                else:
                    print("not eligible to marry")
        else:
            print("Invalid gender entered")
        
    def Percentage():
        num_subjects=5
        marks=[]
        for i in range (num_subjects):
             mark = int(input(f'Enter mark for subject {i}: '))
             marks.append(mark)
        print(marks)
        total = sum(marks)
        average = total / num_subjects
        print(average)

    def area(height,breadth):
        area=(height*breadth)/2
        print('Area of triangle:',area)
        
    def perimeter(height1,height2,breadth):
        perimeter=(height1+height2+breadth)
        print('Perimeter of triangle:',perimeter)

    
      
      
