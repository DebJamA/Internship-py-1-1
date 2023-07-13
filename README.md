# Create Server and Project Entry Points  
  
---  
  
## Make sure the system is set up properly  
  
1. Make sure you are in the **(venv) Internship-py-1-1 %** directory  
  
2. Create and switch to new branch ***Internship-py-1-2***  
  
`% git branch`  
```
Output:  
* Internship-py-1-1  
```  
  
`% git checkout -b Internship-py-1-2`  
```
Output:  
‘Switched to branch ‘Internship-py-1-2’  
```  
  
**Make sure you are in branch Internship-py-1-2**  
`% git branch`  
```
Output:  
Internship-py-1-1  
* Internship-py-1-2  
 ```  
  
3. Import required packages  
    a. Create `requirements.txt` file  
      > Flask #for building web apps  
  
    b. `% pip install -r requirements.txt`  
  
4. Update `README.md` file  
> Internship-py-1-2  
Create Server and Project Entry Points  
  
___  
  
## Create and configure an instance of the project  
  
1. In the `root` directory:  
  
Create `main.py` file - app entry point  
> `#Import create_app`  
> `#Create a launch point for project`  
  
2. Create `simcoblog` directory in the root directory:  
  
a. Create `__init__.py` file  
> `#Import the Flask package and build app`  
> `#Import blueprints`  
> `#Register blueprints`  
  
b. Create `views.py` inside the simcoblog directory  

- In `views.py` create blueprints of routes for future pages  
  
- define a route for `index` page that lists all the financial news articles posted by the financial analysts  
  
- define a route for `article_single` page that displays the full news article information along with the analysis written by the analyst  
  
___  
  

## Start the app  

1. Run the app  
`% python main.py`  
```
Output:  
 * Running on http://127.0.0.1:5000  
```  
  
2. ***http://<area>127.0.0.1:5000*** is the index page
> Web Output:  
> List of Articles  
> Cant Click Article  
[Click Fake Article](http://127.0.0.1:5000/article)  
Cant Go To Article  
  
3. Clicking "Click Fake Article" link redirects to ***http://<area>127.0.0.1:5000/article/int:post_id***, which is the article_single page
> Web Output:  
> Fake Article  
> Fake Article Analysis  
  
___  
  

## Push to remote repo  
  
Push current local branch (**Internship-py-1-2**) to remote repo  
`% git add .`  
`% git commit -m ‘added main project file and routes’`  
`% git push origin HEAD`  
```
Output:  
. . .  
remote:  
To https://github.com/DebJamA/Internship-py-1-1.git  
* [new branch] HEAD -> Internship-py-1-2    
```  
  
---  
  
