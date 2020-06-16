import mysql.connector
from spellchecker import SpellChecker

# creates a spellchecker object
spell = SpellChecker()


# mysql.conector.connect(...) establishes a connection to the MySQL serverand returns an object

connect = mysql.connector.connect(
	user="ardit700_student",
	password="ardit700_student",
	host="108.167.140.122",
	database="ardit700_pm1database"
)

cursor = connect.cursor()

# """
# 	replacing * by Definition returns only the definition coloum values for the
# 	expression. No need for using return[1] in the print statement since that is
# 	neccessary only to avoid printing the expression along with the meaning
# 	* returns all including the expression itself
# 	Refer to More SQL Statements section in the Udemy pyhton ARDIT course
# 	for the various statements that could be used within cursor.execute()

while True:
    word = input("\nEnter a word: ")
    if not word == "/end":
        query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(word))
        results = cursor.fetchall()

# 	printing results will print a tuple consisting of the word
# 	and the appropriate meaning stored in the database.
# 	Hence a loop can be used to generate the result in a more
# 	user friendly manner
# 	result[1] ensures that only the meaning from the definition
# 	column and not the expression(word) as well

        if len(results) != 0:
            for result in results:
                print("\n\t",result[1])
        else:
            corrected = spell.correction(word)
            if input("\nDid you mean {}, press y if yes, n if not: ".format(corrected)) == "y":
                query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '{}'".format(corrected))
                results = cursor.fetchall()
                if results:
                    for result in results:
                        print("\n\t",result[0])
                else:
                    print("\n\tThe word doesn't exist in the database!")
            else:
                print("\n\tThe word doesn't exist in the database!")
    else:
       break
