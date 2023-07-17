# Create Page Templates (py-1-3)  
  
---  
  
## Make sure the system is set up properly  
  
1. Make sure you are in the **(venv) Internship-py-1-1 %** directory  
  
2. Create and switch to new branch ***Internship-py-1-3***  
  
`% git branch`  
```
Output:  
Internship-py-1-1  
* Internship-py-1-2  
```  
  
`% git checkout -b Internship-py-1-3`  
```
Output:  
‘Switched to branch ‘Internship-py-1-3’  
```  
  
**Make sure you are in branch Internship-py-1-3**  
`% git branch`  
```
Output:  
Internship-py-1-1  
Internship-py-1-2  
* Internship-py-1-3  
 ```  
  
3. Import required packages  
    a. Update `requirements.txt` file  
    > Jinja2 #template engine  
  
    b. `% pip install -r requirements.txt`  
  
4. Update `README.md` file  
> Internship-py-1-3  
Create Page Templates  
  
___  
  

## Create directories and mock data  
    
1. Create the `static` directory inside the `simcoblog` directory  
  
    a. Use [MockTurtle](https://mockturtle.net/) to create mock data and download the json data  
  
    - [Validate](https://jsonformatter.curiousconcept.com/) the json format  
  
    - Create `blog.json` file in the `static` directory and copy/paste the mock data in this file  
  
    b. Create the `css` directory inside the `static` directory  
  
    c. Create the `custom.css` file in the `css` directory  
  
2.  Create the `templates` directory inside the `simcoblog` directory  
  
    a.  Create base template: `layout.html`  
  
       - Design front-end using [Bootstrap 4.0 CDN](https://getbootstrap.com/docs/4.0/getting-started/introduction/) (Content Delivery Network)  
  
    b. Create child templates: `posts.html` and  `single.html`  
  
    - Child templates must [extend the base template](https://jinja.palletsprojects.com/en/3.0.x/templates/#variables)  
  
    - Use Bootstrap4 cards for articles and posts  
  
    - (`login.html` and `create.html` were created for the navbar)  
  
___  
  
## Ensure routes return a URL pattern  
  
1. Update `views.py`  
  
    a. Import render_template  
  
    b. From flask import json, and [use the json data stub](https://docs.python.org/3.10/library/json.html) for mock data (since app isn’t connected to Firebase yet)  
  
    c. From Jinja2 import Environment and PackageLoader to set up the environment for loading templates  
  
2.   Run the app
`% python main.py`  
```
Output:  
 * Running on http://127.0.0.1:5000  
```  
  
- ***http://<area>127.0.0.1:5000*** is the index page
> Web Output:  
> renders template with 10 cards for each article post  
  
*Note: the json data is not rendered into each card, but the json file is read and displays the exact number of cards for the number of posts in the json file*  
  
- Clicking "Article Title" link or "Read more" link redirects to ***http://<area>127.0.0.1:5000/article***, which is the article_single page
> Web Output:  
> renders template for a single article with analysis 
 
___  
  
## Push to remote repo  
  
Push current local branch (**Internship-py-1-3**) to remote repo  
`% git add .`  
`% git commit -m ‘added templates and json mock data’`  
`% git push origin HEAD`  
```
Output:  
. . .  
remote:  
To https://github.com/DebJamA/Internship-py-1-1.git  
* [new branch] HEAD -> Internship-py-1-3    
```  
  
---  
  
