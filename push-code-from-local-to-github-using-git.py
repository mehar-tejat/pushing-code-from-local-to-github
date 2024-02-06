Push code 1st time;
1.	Create a new repo in github with some name
2.	Create the python file i.e ur code in laptop
3.	Install git – if done already not required
4.	Open terminal and traverse to the path where ur code is there using cd 
5.	and give the following 3 commands at a time paste them and enter and enter
echo "# pushing-code-from-local-to-github" >> README.md
git init
git add README.md
6.	now enter another command – this will add all the file including read file and hit enter
git add .
7.	enter below 4 commands at a time paste them and hit enter and enter – that’s it it will push github
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/mehar-tejat/pushing-code-from-local-to-github.git
git push -u origin main




'''
after making any changes to the code , how to make the 2nd commit
'''
1. traverse to the same folder using cd
2. use below two commands once after the other 
git add .
git commit -m 'second commit'
3. configure with github if its done skip this , if not done enter ur mail and hit enter it will send code to ur mail enter then u can commit
git config --global user.email 'yourmail@gmail.com'
4. use below command to push the code to github , thats it u can refresh the github u can see the updatated 2nd commit
git push -f origin main



