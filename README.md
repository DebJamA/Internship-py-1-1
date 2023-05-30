# Internship-py-1-1
financial analyst research blog

# Internship-py-1-1
financial analyst research blog

# Setting up the Development Environment for this Python Project  

## Set up your system for development  
DebJamA@MacBook ~ % python3 --version  
Python 3.11.3  
DebJamA@MacBook ~ % pip3 install --upgrade pip  
Requirement already satisfied: pip in /Library/Frameworks  
/Python.framework/Versions/3.11/lib/python3.11/site-packages (23.1.2)  
DebJamA@MacBook ~ % pip -V  
pip 23.1.2 from /Library/Frameworks/Python.framework  
/Versions/3.11/lib/python3.11/site-packages/pip (python 3.11)  
DebJamA@MacBook ~ % python3 -m django --version  
4.2.1  

Install PyCharm on MacBook  

## Create new project
/Users/DebJamA/PycharmProjects/**Internship-py-1-1**  

Move into the correct directory  
DebJamA@MacBook ~ % pwd  
/Users/DebJamA  
DebJamA@MacBook ~ % ls  

-Applications -Downloads -Music -**PycharmProjects**  
-Desktop -Library -Pictures -cd  
-Documents -Movies -Public -sudo  
DebJamA@MacBook ~ % cd PycharmProjects  
DebJamA@MacBook PycharmProjects % ls  
**Internship-py-1-1**  
DebJamA@MacBook PycharmProjects % cd Internship-py-1-1  
DebJamA@MacBook Internship-py-1-1 %  

## Create a GitHub Repo  
Name: **Internship-py-1-1**  

Code → Local → Clone HTTPS then copy/paste the URL after the git clone command  
DebJamA@MacBook Internship-py-1-1 % git clone https://github.com/DebJamA/Internship-py-1-1.git  
Cloning into 'Internship-py-1-1'...  
remote: Enumerating objects: 3, done.  
remote: Counting objects: 100% (3/3), done.  
remote: Compressing objects: 100% (2/2), done.  
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0  
Receiving objects: 100% (3/3), done.  

Create a new branch from the master  
DebJamA@MacBook Internship-py-1-1 % git init  
Initialized empty Git repository in /Users/DebJamA/PycharmProjects  
/Internship-py-1-1/.git/  
DebJamA@MacBook Internship-py-1-1 % ls -a  
-**.git** -main.py -Internship-py-1-1 -venv  
DebJamA@MacBook Internship-py-1-1 % git checkout -b Internship-py-1-1  
Switched to a new branch 'Internship-py-1-1'  

## Create a virtual environment  
DebJamA@MacBook Internship-py-1-1 % python3 -m venv .venv  

## Create a .gitignore file  
Add to the readme.md file  

## Push entire project to the remote repo  
DebJamA@MacBook Internship-py-1-1 % git add .  
DebJamA@MacBook Internship-py-1-1 % git commit -m ‘added project init’  
DebJamA@MacBook Internship-py-1-1 % git remote add origin https://github.com/DebJamA/Internship-py-1-1.git  
DebJamA@MacBook Internship-py-1-1 % git remote -v  
origin	https://github.com/DebJamA/Internship-py-1-1.git (fetch)  
origin	https://github.com/DebJamA/Internship-py-1-1.git (push)  
DebJamA@MacBook Internship-py-1-1 %  git push --set-upstream origin Internship-py-1-1  
remote:   
To https://github.com/DebJamA/Internship-py-1-1.git  
-[new branch] -Internship-py-1-1 -> Internship-py-1-1  
branch 'Internship-py-1-1' set up to track 'origin/Internship-py-1-1'.  
DebJamA@MacBook Internship-py-1-1 % git push  
Everything up-to-date  
