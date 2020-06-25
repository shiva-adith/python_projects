# python_projects
 These are my collection of simple python projects that I create while simultaneously learning the language
## Dictionary App:
  - I have created an English dictionary using two methods:
    * The first type makes use of data stored locally on a **JSON** file. The required data is in the data folder.
    
    * The other connects to an online database containing all the required data. Uses very basic SQL commands to retrieve information from the database.
      - Note: This requires the installation of 'mysql connector' in order to be executed. Use the following code in the cmd terminal to install:  
      
        ```pip install mysql-connector-python```
   
  - #### Handling typing errors:
    * One program uses the `get_close_matches` ***method*** from the `difflib` library and returns the closest match to a misspelt word.
    
    * The database version uses the `SpellChecker` ***class*** from the spellchecker library.
      - Note: `spellchekcer` library needs to be installed seperately in order to be executed. Use the following code in the cmd terminal:
      
        ```pip install spellchecker```
         

