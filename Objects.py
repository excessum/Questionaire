

#######################################################
## The user class is the parent class to both the    ##
## student class and professor class. It contains    ##
## the attributes user ID which is automatically     ##
## given upon creation of a instance. It also has    ##
## attributes e-mail address and name of the user.   ##
#######################################################

def User():
	id_to_give = 1
	
	#######################################################
	## This is the basic constructor for the user class  ##
	## that takes in the name and email of a user and    ##
	## which will be strings and then automatically      ##
	## gives them a ID number.                           ##
	#######################################################
	
	def __init__(name_in, email_in, student_id_in):
		self.name = name_in
		self.email = email_in
		if (id_to_give == 1):
			id_to_give = check_current_highest_id()			
		self.id = id_to_give
		id_to_give += 1
	
	#######################################################
	## This method checks against all current users to   ##
	## get the current highest ID assigned to get the    ##
	## new id to give to users being created. If there   ##
	## are no users in the system it will return 1, if   ##
	## there are users it will return the highest user   ##
	## id+1.											 ##
	#######################################################
	
	def check_current_highest_id():
		#TODO : read filesystem and get all users in an array
		if(len(users) < 1):
			return 1
		else:
			#TODO : Grab highest user id in users
			return highest_id+1
			
			
#######################################################	
## The student class is a child class of user and    ##
## contains the attributes previous tests which hold ##
## all the tests the student has taken as well as    ##
## the tests that the proffesor(s) have set for the  ##
## individual student.                               ##
#######################################################

def Student(User):

		#######################################################
		## The init takes no values as it is only called     ##
		## when creating a new student. The variables        ##
		## set_tests and previous_tests are initialised as   ##
		## empty but will hold an array of tests.            ##
		#######################################################
		
		def __init__():
			self.previous_tests = []
			self.set_tests = []
		
		#######################################################
		## The take_practice_test method allows a student    ##
		## take a practice test that is avaliable to all     ##
		## users. It takes a category as a string input      ##
		## and difficulty as a integer and will return a     ##
		## random test that fits both the category and       ##
		## difficulty. 										 ##
		#######################################################
		
		def take_practice_test(category, difficulty):
			#TODO: Grab all the tests that are practice tests and filter to meet requirements
			return tests[random.randint(0, len(tests)-1]
		
		#######################################################
		## The take_test method allows the student to take   ##
		## a test that has been set for them. The parameter  ##
		## is the test that is to be taken by the user.      ##
		#######################################################
		
		def take_test(test):
			#TODO : display the test on screen, when user submits, get mark, supply feedback, add to previous tests
			self.previous_tests += test
def Professor(User):
                #######################################################
		## The init takes no values as it is only called     ##
		## when creating a new Professor. The variable       ##
                ## students is initialised as empty initially but    ##
		## will hold an array of students the proffesor is   ##
                ## responsible for.                                  ##
		#######################################################
                def __init__():
                        self.students = []

                #######################################################
                ## The setTest method sets the test determined by    ##
                ## the type specified to all the students specified. ##
                #######################################################
                def setTest(self, test_type, student[]):
                        # For each student in the array
                        # Grab a test at random with the specified type and set it

                #######################################################
                ## The viewResults method grabs all of the tests     ##
                ## taken by his students and views the results       ##
                #######################################################                   
                def viewResults(self):
                        for Student in self.students:
                                     for Test in Student.previousTests:
                                             #Display the results of the test

                #######################################################
                ## The viewResult(Student) method grabs the results  ##
                ## of a specified student and displays them.         ##
                #######################################################
                def viewResult(self, Student):
                        for Test in Student.previousTests:
                                     #Display the test
                
                        
                                
                                
	
	

		
