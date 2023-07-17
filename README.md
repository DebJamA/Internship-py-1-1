# Deploy web application on Heroku (py-1-5)  
  
___  
  
## Setting Up for Deployment  
  
1. Ensure app is running properly in local env  
`% python main.py`  
  
2. Update requirements.txt to include `guicorn` - when app is deployed to Heroku, these dependencies are automatically installed before app startup  
  
3. In the root of the application, create `Procfile` without an extension  
  * Procfile tells Heroku which command(s) to run to start the app  
	  > web: gunicorn -w 4 main  
  
4. Create `runtime.txt` to tell Heroku to use the same Python version used locally during development  
  
5. Create free Heroku account with payment method  
  
6. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) on Mac:  
```
% brew tap heroku/brew && brew install heroku
```  
Verify installation:  
`% heroku --version`   
  
___  
  
## Creating Heroku App and Deploying App  
  
1. Log in to Heroku  
`% heroku login`  
  
2. Create a main branch in the local git repo  
`% git branch -c main`  
`% git branch`  
`% git checkout main`  
`% git branch`  
`% git add .`   
`% git commit -m 'make it better'`  
  
3. Create Heroku app  
`% heroku create`  
```
Output:  
Creating app... done, ⬢ historic-haleakala-49710  
https://historic-haleakala-49710-c674e93d8219.herokuapp.com/  
https://git.heroku.com/historic-haleakala-49710.git  
```  
  
4. Refresh the Heroku page to see the app name:  
***historic-haleakala-49710***  
  
5. Rename the Heroku remote  
`% heroku rename simco-blog`  
```
Output:  
Renaming historic-haleakala-49710 to simco-blog... done  
https://historic-haleakala-49710-c674e93d8219.herokuapp.com/  
https://git.heroku.com/simco-blog.git  
Git remote heroku updated  
```  
  
6. Refresh the Heroku page to see the app name:  
***simco-blog***  
  
7. Confirm Heroku remote has been set for app  
`% git remote -v`  
```
Output:  
heroku  https://git.heroku.com/simco-blog.git (fetch)  
heroku  https://git.heroku.com/simco-blog.git (push)  
origin  https://github.com/DebJamA/Internship-py-1-1.git (fetch)  
origin  https://github.com/DebJamA/Internship-py-1-1.git (push)  
```  
  
8. Deploy app: push code from local repo main branch to the Heroku remote repo  
`% git push heroku main`  
```
Output:  
. . .  
remote: https://simco-blog-db547b91756b.herokuapp.com/ deployed to Heroku
. . .  
remote: Verifying deploy... done.  
To https://git.heroku.com/simco-blog.git  
 * [new branch]      main -> main  
```  
  
9. Ensure an instance of app is running  
`% heroku ps:scale web=1`  
```
Output:  
Scaling dynos... done, now running web at 1:Basic  
```  
  
10. Visit the app at URL or use CLI  
`% heroku open`  
  
  
