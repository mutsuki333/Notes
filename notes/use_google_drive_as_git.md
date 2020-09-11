# Use Google Drive as Git Server

> Works when google drive are installed locally, 
> and set it to sync properly with Google Drive.

## Initialize a local git folder

Go to the folder you wish to initailize as a git folder,
and init the folder, if you haven't already.

```bash
git init
git add .
git commit -m "first commit"
```

(folder with 0 commit can not be pushed)

## Initialize a git repo in google drive

Navigate to the Google Drive folder you wish to store the repo.

```bash
cd PATH_TO_GOOGLE_DRIVE/REPO_FOLDER
git init --bare PROJECT_NAME.git
```

## Set remote to track google drive

In the local git folder.

```bash
git remote add origin PATH_TO_REPO_FOLDER/PROJECT_NAME.git 
git push -u origin master
```

## Clone from other machines

```bash
git clone PATH_TO_REPO_FOLDER/PROJECT_NAME.git
```
