import mysql.connector
from spellchecker import SpellChecker


spell = SpellChecker()


connect = mysql.connector.connect(
	user="ardit700_student",
	password="ardit700_student",
	host="108.167.140.122",
	database="ardit700_pm1database"
)

cursor = connect.cursor()


while True:
    word = input("\nEnter a word: ")
    if not word == "/end":
        query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(word))
        results = cursor.fetchall()



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
