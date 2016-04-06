'''
Program:    a2.py
Name:       
Date:
Desc:
'''

# Initialize the database of student grades
database = [
    ['ICS4U', 'Assignment 1', 'Luke Skywalker', '3+'],
    ['ICS4U', 'Assignment 1', 'Han Solo', '4-'],
    ['SPH3U', 'Unit 1 Test', 'Leia Organa', '4'],
    ['SPH3U', 'Unit 1 Test', 'Luke Skywalker', '3-'],
    ['SPH4U', 'Unit 1 Test', 'Yoda', '4+'],
    ['SPH4U', 'Unit 1 Test', 'Anakin Skywalker', '3'],
    ['MHF4U', 'Unit 1 Test', 'Boba Fett', '2+'],
    ['MHF4U', 'Unit 1 Test', 'Kylo Ren', '3'],
    ['MHF4U', 'Unit 1 Test', 'Chewbacca', '4']
    ]

def tfInput(string):
    ''' Prompt the user for a yes/no question and return True/False '''
    # Display the question and returns an answer
    answer = input(string)
    return answer[0].lower() == 'y'


# ICS4U:
# PUT ALL OF YOUR FUNCTIONS HERE

def level2Percent(level):
    '''
    This function takes a grade level and returns an integer representing the corresponding percent grade.
    '''
    # This 'if' statements are returning a percentage according to the different level of grade that the user writes.
    if level == ('4+'):
        return 100
    if level == ('4'):
        return 94
    if level == ('4-'):
        return 86
    if level == ('3+'):
        return 79
    if level == ('3'):
        return 76
    if level == ('3-'):
        return 72
    if level == ('2+'):
        return 69
    if level == ('2'):
        return 66
    if level == ('2-'):
        return 62
    if level == ('1+'):
        return 59
    if level == ('1'):
        return 56
    if level == ('1-'):
        return 52
    if level == ('<1') or ('< 1'):
        return 40

def percent2Level(percent):
    '''
    This function takes a percent grade and returns a string representing the corresponding grade level.
    '''
    # This if statements.
    if percent in range(95,101) :
        return ('4+')
    if percent in range(87,95) :
        return ('4')
    if percent in range(80,87) :
        return ('4-')
    if percent in range(77,80) :
        return ('3+')
    if percent in range(73,77) :
        return ('3')
    if percent in range(70,73) :
        return ('3-')
    if percent in range(67,70) :
        return ('2+')
    if percent in range(63,67) :
        return ('2')
    if percent in range(60,63) :
        return ('2+')
    if percent in range(57,60) :
        return ('1+')
    if percent in range(53,57) :
        return ('1')
    if percent in range(50,53) :
        return ('1-')
    if percent in range(0,51) :
        return ('< 1')

def stringCompare (string1,string2):
    '''
    This function compares two strings, and returns True if the strings are the same, and False if they are not.
    '''
#Compares the two strings and return True if they match or False if they dont.
    return string1.lower().strip()  == string2.lower().strip()

def addGrade(database,course,assignment,student,grade):
    '''
    This function adds a single row to the database, with the specified course, assignment, student, and grade.
    '''
    #By using append is adding a row into database.
    database.append ([course,assignment,student,grade])
    #Return the updated data base with the extra row.
    return database

def inputGrades (database):
    '''
    This function allows the user to imput more grades into your database.
    '''
    #Its giving the user the following prompts to answer.
    course = input ('What is the name of the class?\n')
    assignment = input ('What is the name of the assignment?\n')

    #Loop the following prompt only.
    while True:
        student = input ('Student name:\n')
        grade = input ('Level:\n')

        #It is updating the database with the new answers from the user and putting it into a new row.
        database = database + [[course,assignment,student,grade]]
        response = tfInput('Would you like to input another grade?\n')
        #This statement will allow the user to prompt more information if they answer yes/true.
        if response == True:
            pass
        #This statement will break if answer is False/no, meaning it wont ask anymore questions but instead give you the updated list with new information added.
        elif response == False:
            break
    #Returns the updated database.
    return database


def studentAverage(database,student):
    '''
    This function returns the average percent grade for the specified STUDENT.
    '''

    #The creation of different variables with the equality of a list '[]'
    level = []
    percent = []
    #Variable equal '0' created to take the average.
    total = 0

    #This for loop will find the 'len' of elements of the database.
    for d in range(len(database)):
        #This if statement will check wether ll the elements of the database have the right student.
        if stringCompare(database[d][2],student)== True:
            level  .append(database [d][3])
    #This for loop will turn the grade levels in the array into porcentage grades.
    for l in range(len(level)):
        percent. append (level2Percent(level[l]))
    #This for loop is taking the average of the porcentage grades.
    for p in range (len(percent)):
        total = (total+percent[p])
    #It is returning the result, which is a float representing the student's average percent grade
    return total/len (percent)

def courseAverage (database,course):
    '''
    This function will return the average percent grade for the specified COURSE.
    '''

    #This variables are equal to a list [].
    level = []
    percent = []
    #The variable 'total' is equal '0' in order ot use it later in the code to get the course's average percent grade.
    total = 0

    #This for loop is finding all the element of the databse that have the right COURSE.
    for d in range (len(database)):
        if stringCompare(database[d][0],course)==True:
                level. append(database[d][3])
    #This if statement is storing the matching grade levels into an array.
    for l in range(len(level)):
        percent. append(level2Percent(level[l]))
    #If statement that turns the grade levels in the array into percentage grades.
    for p in range(len(percent)):
        total = (total+percent[p])
    #This variable is equal the formula to take the average of the array of the percentage grades to return the result (average).
    average =total/len(percent)
    #Returns a float representing the COURSE'S average percent grade.
    return average



if __name__=="__main__":
    pass
    # ICS4U:
    # PUT ANY EXTRA CODE (TESTING, ETC) HERE

    #print (level2Percent('4'))
    #print (level2Percent('<1'))

    #print (percent2Level(95))
    #print (percent2Level(52))

    #print (stringCompare('  Hello','hello'))

    #print (addGrade(database,'SPH3U','Catapult project','Jar Jar Binks','2'))

    #print (inputGrades(database))

    
