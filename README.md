# Wht The Phish!!

## Project Large Applications Practicum (Group 4)

>This Project is made to make poeple aware about the phising websites that are increasing at an alarming rate. We have made an education app which will first teach poeple about the various types of phishing URLs which will be followed by an exercise session to ensure that the user actually understood the concepts.

## About Phishing
>The fraudulent practice of creating false websites purporting to be from reputable companies in order to induce individuals to reveal personal information, such as passwords and credit card numbers.
<img src="https://user-images.githubusercontent.com/54496028/141749055-b6f99d4c-9380-4f4b-84b8-a82085ed6567.png" width=800px style="display:inline;"> 



## Technology Stack
1. **Frontend**:- HTML, CSS, Javascript
2. **Backend**:- Flask, Pymongo, Jinja
3. **Language**: Python
4. **Database**: MongoDB
5. **Version Control**: Git
6. **Deployment**: Heroku

## Flow Chart
![WhtThePhish](https://user-images.githubusercontent.com/54496028/141750338-84482ff9-3c68-4bcc-865a-30c3915eafc7.png)

## UML Class Diagram
![UML class](https://user-images.githubusercontent.com/54496028/141750188-8adeb55c-fb77-470e-acde-8ad465b7ca38.png)

## Directory Structure
![Directory_Structure](https://user-images.githubusercontent.com/54496028/141750118-e24c92d7-1fbe-4593-9dce-a17927d101ac.png)

## Datasets

1. [Aalto Phishstrom Dataset](https://research.aalto.fi/en/datasets/phishstorm-phishing-legitimate-url-dataset)
2. [UNB URL Dataset 2016](https://www.unb.ca/cic/datasets/url-2016.html)

## Setting Up the Enviornment

1. Fork The repo
2. Clone it in your local machine using the forked repo
3. Create a virtual enviornment in your local machine in the folder you cloned the repo,

    ```bash
    pip install virtualenv
    virtualenv env
    ```
4. Activate the virtual env<br>
   For Windows run
   ```bash
   .\env\Scripts\activate
   ```
   For Linux run
   ```bash
   source env/bin/activate
   ```
   Follow the instructions given after you create a env successfully .

5. Create a `secrets.py` file in src folder with the follwoing content.
    ```python
    USERNAME="[Your MongoDB Username]"
    PASSWORD="[Your MONGODB Password]"
    SECRET_KEY="[A Secret Key For the App]"
    ```

5. Then run
   ```bash
   pip install -r requirements.txt
   ```
7. Now run the server<br>
     For Windows run
     ```bash
     python -m src.server
     ```
     For Linux run
     ```bash
     python3 -m src.server
     ```
8. If you have reached this step, you are good to go.

## Group Members

1. [Shashwat Singh (B19056)](https://github.com/shashwat0003)
2. [Prashant Kumar (B19101)](https://github.com/prashant280920)
3. [Rohan Raj Kansal (B19108)](https://github.com/BeingHomosapien)
4. [Sourav Sehgal (B19059)](https://github.com/SouravSehgal-3009)
5. [Priyanshu Shubham (B19189)](https://github.com/priyanshu-shubham)
6. [Pritish Chugh (B19187)](https://github.com/Pritishchugh22)
7. [Ravi Kumar (B19191)](https://github.com/RaviKumar7870)

## Mentor
- [Megha Sharma](https://github.com/m36h4)
