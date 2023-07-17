# Display Data From Firebase (py-1-4)  
  
___  
  
## Make sure the system is set up properly  
  
1. Make sure you are in the **(venv) Internship-py-1-1 %** directory  
  
2. Create and switch to new branch ***Internship-py-1-4***  
  
`% git branch`  
```
Output:  
Internship-py-1-1  
Internship-py-1-2  
* Internship-py-1-3  
```  
  
`% git checkout -b Internship-py-1-4`  
```
Output:  
‘Switched to branch ‘Internship-py-1-4’  
```  
  
**Make sure you are in branch Internship-py-1-4**  
`% git branch`  
```
Output:  
Internship-py-1-1  
Internship-py-1-2  
Internship-py-1-3  
* Internship-py-1-4  
 ```  
  
3. Import required packages  
  
	a. Update `requirements.txt` file  
	> firebase #firebase REST API's  
	> firebase-admin #allows you to manage users and validate tokens  
	> jsonschema #JSON Schema validation  
  
	b. `% pip install -r requirements.txt`  
  
4. Update `README.md` file  
	> Internship-py-1-4  
	> Display Data From Firebase  
  
___  
  
*Note: Updated firebase async files on the Mac so the app would not throw a syntax error when trying to import the Firebase package*  
- The error looks like this [syntax error](https://stackoverflow.com/questions/52133031/receiving-async-error-when-trying-to-import-the-firebase-package)
- `async` is a keyword in python 3.7 and higher  
- This is a work-around because I did not want to downgrade my project to Python 3.6  
- **DO NOT edit/maintain a 3rd party library in a production environment**  Downgrade Python and/or wait for the library to update  
	>Finder → firebase folder  
	> Change file name `async.py` to `async_.py`  
	>Change `.async` to `.async_` in both  `__init__.py` and `firebase.py`  
  
___  
  
## Create Firebase Realtime Database  
  
1. Go to [Google Firebase](https://firebase.google.com) and click "Get Started"  
  
2. Sign in (or create an account) if not already signed in to use your Google Account)  
  
3. Use your **@gmail.com** email address  
  
4. Name your project: *Simco Financial Analyst Blog*  
  
5. Disable Google Analytics  
  
6. Create project  
  
7. Build → Realtime Database → Create Database → Start in test mode  
  
___  
  
## Connect Flask app to Firebase rtdb  
  
1. Go to your Firebase Project Overview ⚙ → Project Settings → General → Your apps → </> Web apps  
  
    a. Register app - nickname Simco blog  
  
    b. Add Firebase SDK - copy/paste config data to `fbconfig.json` in the Flask app `root` directory  
    
    c. Build → Authentication → Sign-In-Method → enable sign in with email and password  
  
2. Export the Admin SDK private key  
  
    a. Go to your Firebase Project Overview ⚙ → Project Settings → Service Accounts → Firebase Admin SDK → Python → "Generate new private key" 
  
    b. Copy/paste the Firebase Admin SDK in the Flask app `root` directory as `fbserviceconfig.json`  
  
3. Configure and publish Firebase rtdb rules  
Go to Project shortcuts → Realtime Database → Rules → Edit Rules  
```
{  
    "rules": {  
      "blog": {  
        ".indexOn": ["date_posted"]  
      },  
      ".read": true,  
      ".write": false  
    }  
}  
```  
  
4. Update files  
    a. Update `init.py`  
	> #Import firebase_admin  
	> #Fetch service account key JSON file  
	> #Initialize SDK with admin privileges  
  
    b. Update `views.py`  
	> #Import firebase_admin  
	> #Fetch service account key JSON file  
	> #Initialize SDK with admin privileges  
	> #Remove json and use firebase to retrieve data in the routes  
  
   c. Update `blog.json`  
	- Remove array brackets `[ ]` from beginning and end of json data then [Validate](https://jsonformatter.curiousconcept.com/) the json file again  
	-- `[ ]` are not necessary for Firebase json tree  
  
	- Create `schema.py` inside the `root` directory to validate the json data  
		-- Use this [converter](https://www.liquid-technologies.com/online-json-to-schema-converter) to help write a json validation schema  
  
	- [Validate](https://towardsdatascience.com/how-to-use-json-schema-to-validate-json-documents-ae9d8d1db344) the json data in python  
  
	`% python schema.py`
	```
	Output:  
	Given JSON data is Valid  
	```  
	- Import `blog.json` into the Firebase rtdb  
  
    d. Update `posts.html` and `single.html` using jinja to incorporate json data from Firebase rtdb
  
___  
  
## Run the app
`% python main.py`  
```
Output:  
 * Running on http://127.0.0.1:5000  
```  
  
- ***http://<area>127.0.0.1:5000***  
All 10 different articles are retrieved from the Firebase rtdb and displayed on the index page  
  
- ***http://<area>127.0.0.1:5000/article/int:post_id***
Clicking one article's title link or the "Read more" link on the index page retrieves that article's data from the Firebase rtdb based on the post id, then displays the article's specific data on its article_single page  
  
___  
  
## Push to remote repo  
Push current local branch (**Internship-py-1-4**) to remote repo  
`% git add .`  
`% git commit -m ‘created and connected firebase rtdb and added json schema validation’`  
`% git push origin HEAD`  
```
Output:  
. . .  
remote:  
To https://github.com/DebJamA/Internship-py-1-1.git  
* [new branch] HEAD -> Internship-py-1-4    
```  
  
  
