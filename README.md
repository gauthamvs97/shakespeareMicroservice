# Django Microservice to analyse an uploaded Text file

- A simple django web application that allows a user to upload a text file, in this case the entire work of William Shakespeare (textfile is shaks.txt). 
- The uploaded text file is analysed and the following is displayed: 
                                - Number of unique words in each work of William Shakespeare
                                - Number of lines in each work
                                - Number of words that begins with each alphabet.

**Tech Stack used:** Docker, Python, Django framework, Javascript, HTML and CSS.

INSTRUCTION TO BUILD AND DEPLOY:

Method 1 (Recommended): Using Docker (Must have Docker installed)
- Go to a directory of your choosing.
- Clone code from repository preferably using git.
```git clone https://github.com/gauthamvs97/shakespeareMicroservice.git```
- cd into the directory
- Run ```docker-compose up``` to start the server
- If successful, it will give a message "Starting the developement server at http://'ip address':8000.
- Type the ip address followed by /shakespeare in your web browser. Example URL would be "http://localhost:8000/shakespeare".
- Upload the text file found in the root directory and click the Submit button.
- You will be redirected to the output page.


Method 2: Using Python3 (Must have Python3 installed)

- Make sure you have the latest version of python3. 
- (OPTIONAL - To create a Virtual Environment)
Install Virtual Environment (venv) Module if you would like to test the application in an isolated environment using
    ``` python3 -m pip install --user virtualenv ```. 
 Go to the folder of your choosing or create a new directory using
   ```mkdir shakesMicro && cd shakesMicro ```
Create a new Virtual Environment using```python3 -m venv env``` and Activate it using ```source env/bin/activate```

- Install django framework.
```pip3 install django```
- Clone code from repository preferably using git.
```git clone https://github.com/gauthamvs97/shakespeareMicroservice.git```
- cd inside the directory.
```cd shakespeareMicroservice-Main```
- Start the server using the command ```python3 manage.py runserver```
- If successful, it will give a message "Starting the developement server at http://'ip address':8000".
- Type the ip address followed by /shakespeare in your web browser. URL would be "http://localhost:8000/shakespeare/"
- Upload the text file found in the root directory and click the Submit button.
- You will be redirected to the output page.
   
  


 
