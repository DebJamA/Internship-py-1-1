# Internship-py-1-1  
  
# Deploying my Flask app via Heroku  
All the code and configuration for this app is in the main (defeault) branch of my Internship-py-1-1 repo.  
  
url here  
  
___
  
## Setting Up for Deployment  
1. Ensure app is running properly in local env  
  
2. Update requirements.txt - when app is deployed to Heroku, these dependencies are automatically installed before app startup  
  
3. In the root of the application, create "Procfile" without an extension  
  * Procfile tells Heroku which command(s) to run to start the app  
  * Add this line to it: worker: python main.py  
  
4. Create free Heroku account with payment method  
  
5. Install Heroku CLI
  
___
  
## Creating Heroku App and Deploying App  
1. Log in to Heroku  
`% heroku login`  
  
2. Create a local git repo  
`% git add .`   
`% git commit -m 'make it better'`  
  
3. Create Heroku app  
`% heroku create`  
```
Output:  
Creating app... done, ⬢ vast-beach-54080  
https://vast-beach-54080-9f5133dfc5fa.herokuapp.com/  
https://git.heroku.com/vast-beach-54080.git  
```  
  
4. Refresh the Heroku page to see the app name: vast-beach-54080  
  
5. Rename the Heroku remote  
`% heroku rename simco-blog`  
```
Output:  
Renaming vast-beach-54080 to simco-blog... done  
https://vast-beach-54080-9f5133dfc5fa.herokuapp.com/  
https://git.heroku.com/simco-blog.git  
Git remote heroku updated  
```  
  
6. Refresh the Heroku page to see the app name: simco-blog  
  
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
  
9. Ensure an instance of app is running  
`% heroku ps:scale worker=1`  
```
Output:  
 . . .  
remote: https://simco-blog-8578030f7ade.herokuapp.com/ deployed to Heroku  
```  
  
10. Visit the app at this URL or use code  
`% heroku open`  
