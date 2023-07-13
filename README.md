# Internship-py-1-1:  Setup the Development Environment  
  
## Set up system for development  
  
1. Ensure Python is installed:  
`% python3 --version`  
```
Output:  
Python 3.11.3  
```  
  
2. Upgrade pip:  
`% pip install --upgrade pip`  
`% pip -V`  
```
Output:  
pip 23.1.2  
```  
  
3. Create a [GitHub](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home) account  
  
4. Install and configure [Git](https://git-scm.com/download/mac) on Mac (using [Homebrew](https://brew.sh/)):   
`%brew install git`  
`% git --version`  
```
Output:  
% git version 2.41.0  
```  
```
% git config --global user.name "DebJamA"  
% git config --global user.email "debbijameseaigbogun@gmail.com"  
```  
  
5. Install [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/?section=mac) on Mac  
  
___  
  
## Create new project  
  
1. Open PyCharm to [Create a Python project](https://www.jetbrains.com/help/pycharm/creating-empty-project.html):  
***Internship-py-1-1***  
  a. select virtual environment  
  b. configure Python interpreter  
  
2. Using the PyCharm terminal, move into the Internship-py-1-1 directory  
  
___  
  
## Create a GitHub repo  
  
### From GitHub web UI    
  
1. New repository  
  
2. Repository name: ***Internship-py-1-1***  
   
3. Do not initialize the new repository with README, license, or gitignore files  
   
4. Choose repository visibility: "Anyone with a link"  
   
5. Create repository  
   
6. Copy the remote repository URL  
 
### From PyCharm terminal  
  
1. Make sure you are in the **(venv) Internship-py-1-1 %** directory  
  
2. Set the remote by pasting the URL after the git command:  
```
% git remote add origin https://github.com/DebJamA/Internship-py-1-1.git  
```  
  
3. Verify the new remote:  
`% git remote -v`  
```
Output:  
origin  https://github.com/DebJamA/Internship-py-1-1.git (fetch)  
origin  https://github.com/DebJamA/Internship-py-1-1.git (push)  
```  
  
___  
  
## Create files  
  
1. Create `.gitignore` file  
> Copy/paste from [mooowooo repo](https://gist.github.com/MOOOWOOO/3cf91616c9f3bbc3d1339adfc707b08a)  
  
2. create `README.md` file for **Internship-py-1-1** branch  
> Internship-py-1-1:  
> Setup the Development Environment   
  
___  
  
## Push entire project to the remote repo  
  
1. Create and switch to a new branch:  
`% git init`  

```
Output:  
Initialized empty Git repository in /Users/DebJamA/PycharmProjects/Internship-py-1-1/.git/  
```  
`% git checkout -b Internship-py-1-1`
```
Output:  
Switched to a new branch 'Internship-py-1-1'
```  
  
2. Push to GitHub:  
```
% git add .  
% git commit -m ‘added project init’  
```  
  
`% git push --set-upstream origin Internship-py-1-1`  
  
```
Output:  
. . .  
remote:  
To https://github.com/DebJamA/Internship-py-1-1.git  
* [new branch] Internship-py-1-1 -> Internship-py-1-1  
branch 'Internship-py-1-1' set up to track 'origin/Internship-py-1-1'.  
```  
  
  
