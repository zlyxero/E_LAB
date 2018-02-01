# E_LAB

The app on heroku. Find it here; https://e-lab-app.herokuapp.com/


<h3>LOGIN CREDENTIALS:</h3>

<b> For doctor:</b>

        username:  doctor

        password: mypassword2


<b>For lab technician:</b>

        username: technician

        password: mypassword1


<h3>SAMPLE SEARCH FIELDS DETAILS FOR AN ALREADY REGISTERED USER:</h3>

        first name: jeff

        mobile: 0711276275

<br> 

<h3>How it works;</h3>


A doctor logs in and is redirected to a page to search for a patient (by username, mobile and insurance member ID(optional)).

If a match is found from the search, the doctor
can proceed to make a lab test request for the patient. The doctor can add several tests on the same page by searching for a test in the database and selecting it. Once the doctor has all the tests selected and other information entered, he/she can
proceed to submit the lab request. The doctor can view the list of lab requests submitted, details of a lab request and results for a test (if any).

By switching users and logging in as a lab technician you will get an extra column in the lab requests list table. Here you can add results to lab test requests submitted.


<b>Kindly Note:</b>

1. In the page to make a lab request, the search function to add tests makes use of ajax. Lab tests are suggested according to the text typed in the search field. The app searches the database in real time and provides options for the doctor to select a test in the database. Only tests in the database can be selected - Trying to add a test not in the database will not work.

   You can select multiple tests here by making more searches and clicking on the add test button. There is an option to remove selected tests as well.

2. There are two groups of users; doctors and lab technicians. The only difference here is that a lab technician can add results to a lab test request submitted. If you log  in as a lab technician, you will notice an extra column added to the list of lab requests table. 

3. If you log in as a doctor and enter credentials for a patient that doesn't exist. This will allow you to register a new patient in the system, and proceed to make a lab report.

4. A doctor can update lab results recieved.
