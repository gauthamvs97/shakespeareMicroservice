# Django Microservice to analyse an uploaded Text file

- A simple django web application that allows a user to upload a text file, in this case the entire work of William Shakespeare (textfile found at shakespeareMicroservice-Main/shakespeare/media/shaks.txt). 
- The uploaded text file is analysed and the following is displayed: 
                                - Number of unique words in each work of William Shakespeare
                                - Number of lines in each work
                                - Number of words that begins with each alphabet.

**Tech Stack used:** Python, Django framework, Javascript, HTML and CSS.

INSTRUCTION TO BUILD AND DEPLOY:

The build environment must support Python3

- Make sure you have the latest version and python3. 
(OPTIONAL - To create a Virtual Environment)
- Install Virtual Environment (venv) Module if you would like to test the application in an isolated environment.
    ``` python3 -m pip install --user virtualenv ```
- Go to the folder of your choosing or create a new directory. 
   ```mkdir shakesMicro && cd shakesMicro ```
- Create a new Virtual Environment. ```python3 -m venv env```
- Activate it. ```source env/bin/activate```


- Install django framework.
```pip3 install django```
- Clone code from repository preferably using git.
```git clone https://github.com/gauthamvs97/shakespeareMicroservice.git```
- Go inside the directory.
```cd shakespeareMicroservice-Main```
- Start the server using the command ```python3 manage.py runserver```

- if successful, it will give a message "Starting the developement server at http://127.0.0.1:8000".
-  Type the ip address followed by /shakespeare in your web browser. Example URL would be "http://127.0.0.1:8000/shakespeare/"
   
  


 
