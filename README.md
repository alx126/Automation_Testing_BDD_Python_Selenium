# BDD Automation testing project with Python / Selenium <br>
# Proiect de testare automata BDD cu Python / Selenium <br>
<br>

## Implement automated tests for an online store <br>
## Implementare teste automate pentru magazin online <br>
<br>


**Site:** https://demo.nopcommerce.com/

**Language:** Python (https://www.python.org/downloads/)<br>
**Limbaj:** Python (https://www.python.org/downloads/)


**Methodology:** Behavior Driven Design (BDD)<br>
**Metodologie:** Behavior Driven Design (BDD)

**Design pattern:** Page object model (POM)

**IDE:** PyCharm Community Edition 2023.2.3  (https://www.jetbrains.com/pycharm/download/?section=windows)
___

**The necessary libraries can be installed using the following commands in the terminal:** <br>
**Instalarea librariilor necesare se poate face folosind urmatoarele comenzi in terminal:** <br>

**Selenium:**   _pip install selenium_

**Webdrive-manager:** _pip install webdriver-manager_

**Behave:** _pip install behave_

**Behave-html-formatter:** _pip install behave-html-formatter_
___

**Instructions for cloning the project** <br>
**Instructiuni clonare proiect** <br>


1. Copy the project link: https://github.com/alx126/Automation_Testing_BDD_Python_Selenium.git <br>
   Copiaza linkul proiectului: https://github.com/alx126/Automation_Testing_BDD_Python_Selenium.git <br>

2. Create a new local folder where the project will be installed <br>
   Creeaza un folder nou local, aici se va instala proiectul <br>

3. Open Git BASH inside the folder using the "Git Bash Here" command: Right-click inside the folder and select "Git Bash Here" from the context menu <br>
   In folder se deschide Git BASH cu comanda "Git Bash Here": Click dreapta in folder si selectezi "Git Bash Here" din context menu  <br>
![image](https://github.com/alx126/TA_FinalProject/assets/93679540/f50ca661-f78c-4533-81ff-2b9d10b6ad1c)

4. In the open window insert: git clone + project link (right-click - Paste) + Enter <br>
   In fereastra deschisa se introduce: git clone + link proiect (click dreapta - Paste) + Enter   <br>
![image](https://github.com/alx126/Automation_Testing_BDD_Python_Selenium/assets/93679540/c58c2b11-b2f2-4c66-9af7-d73535e64e5a)

___

**Instructions for running the project** <br>
**Instructiuni rulare proiect** <br>

1. Open the project in PyCharm: <br>
   Deschide proiectul in PyCharm: <br>
![image](https://github.com/alx126/TA_FinalProject/assets/93679540/1345a113-919d-4d74-bbe8-0e7b69366128)

2. Install the libraries mentioned above <br>
   Instaleaza librariile mentionate mai sus <br>

In the PyCharm terminal enter the installation commands for the mentioned libraries. <br>
In terminalul PyCharm se introduc comenzile de instalare pentru librariile mentionate. <br>

(I used _pip install -U selenium_ to install the latest selenium updates) <br>
(am folosit comanda _pip install -U selenium_ pentru a instala ultimele update-uri selenium) <br>

![image](https://github.com/alx126/TA_FinalProject/assets/93679540/324e7b36-8464-4f69-9a33-bfeb96e707e8)

___   



**Examples of commands to run tests with tags:** <br>
**Exemple de comenzi pentru a rula teste cu tag-uri:** <br>

  _behave --tags=register_

  _behave --tags=smoke,simple_  (no space between the tags / fara spatiu intre taguri in acest caz!)
  
  _behave -f html -o behave-report_smoke.html --tags=smoke_
