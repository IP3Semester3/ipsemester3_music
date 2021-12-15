![minions](https://c.tenor.com/PFJV9ICiTTEAAAAC/minions-dance.gif)
# Getting Started
This is the repository for ipsemester3_music. If you are new here be sure to read this readme as it contains helpful information. If you have worked on this project before feel free to continue working on it. Any updates to the readme will be visible in the commit history. If you've worked on other projects within this organisation, you will only need to read the following parts:

- [How to run flask app](#how-to-run-the-flask-app)
- [Coding conventions](#coding-conventions)
- [Docker](#docker)
- [Notes](#notes)

# Overview
Using the Spotify API we can get access to an almost infinite library of music and playlists. This service is designed to make the api easier to use and implement in other applications regardless of coding language used.

#### readme
The Spotify API is a RESTApi use to get data from the Spotify service. We're using this API because Spotify already has a large library of music and millions of users paying for it. With the API we can ask the user to authorize using their own spotify account. This way we have access to the user's information and playlists. 

Currently this project is still under development and many features are subject to change or incomplete. 

# Project Board
The full project board which includes the development process of this service can be found on [Jira](https://semseter3-ip-tomeykholt.atlassian.net/jira/software/projects/SEM3/boards/2). If you're working on this project, you will need to ask for an invite from [me](https://github.com/StijnSchellekens) or [Tom Eykholt](https://github.com/TEykholt)

In order to get the authorization working, we need to verify the app with the spotify developer portal. The verified URL is 127.0.0.1:5000. Any other url will not support Spotify authorization and will therefore not work.

# How to run the flask app
This is mainly aimed towards windows users since python runs a little differently. In order to run the flask app you need to have something called a virtualenv. In this github the virtualenv has been provided and is called SpotifyEnv. In order to run the virtualenv, all you have to do is CD to the root file of this project and type "SpotifyEnv\Scripts\activate". This will activate the virtualenv and you will then be able to run the "python -m flask run" command.

# Coding Conventions
In this project we follow the standard coding conventions for [Python](https://www.python.org/dev/peps/pep-0008) . We also use the standard Python coding conventions in regards to docstring which helps understanding methods easier without having to decipher the whole thing. 
````
def example(string: stringname) -> int
"""This is an example description of a method.
Args: 
    string (stringname): description of string
Returns:
    Int: description of int returned"""
````

# Docker
This project is also being pushed to Dockerhub, https://hub.docker.com/repository/docker/stijnschellekens/spotifylibrary. To pull the Docker project you need to first download [Docker Desktop](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=header). To pull the docker image, open commandprompt and type: ``docker pull stijnschellekens/spotifylibrary``. To run the docker image, start Docker desktop, search for the image and run it. It will run on your localhost with post 5000.

# Notes
#### Development
During development we use the url ``127.0.0.1:5000``. Changing this breaks the Spotify authorization so make sure there are no other applications running on the exact same url.

#### Api

- ``/`` -- Will request the authentication page from Spotify
- ``/user/playlists`` -- Will get/update the authenticated user's Spotify playlists

#### Spotify Developer Mode Limitations
There is a limit of 25 users that can authorize using this service and I have to manually add these users to the list of testers while the program is still under development. This is a limit set by Spotify themselves and I can’t change this. So in order to actually use this service while testing, your email associated with the spotify account you want to use has to be registered for the app. 

#### Microservice
This service is part of a larger application using the MVC principle. Using the data collected from the API in this service we can allow users to create lobbies for them to share their playlists with and host listening parties with their friends. The structure is as follows:
![c2](https://user-images.githubusercontent.com/73947701/143425039-e94d6091-06ed-437c-90ee-2083af29d6e1.png)

#### Integration
Due to the nature of this project, certain functionalities have to be tested using integration tests to avoid testing the spotify api itself while still assuring that the program is working as intented. A good example is [Issue #37](https://github.com/IP3Semester3/ipsemester3_music/issues/37). These tests are still part of the automated workflow so we can make sure everything is working as it should according to the requirements from the stakeholders

# Github setup
## Branches
In this github we work with different branches that correlate to the status of the project. Usually we use the Development branch during development and only push to the main branch after the code has been inspected and tested. 
For new features it is advised to create a new branch from the main branch. The name of this branch has to correspond with the Issue ID found on our JIRA page (SEM3-25, link for the JIRA project is at the top of this document) followed by the feature name. This way we can keep a clean and organized branch setup going.
Pull requests into the main branch will be tested so make sure you have created sufficient unit tests before creating a pull request. 

## Pull requests
The main branch has been locked to avoid accidentally breaking the application with a wrong push and also acts as a backup for if things somewhere else go wrong. It will always host the most up to date stable release.

In order to update and push commits to the main branch, a pull requests has to be made. These will have to be reviewed within 24 hours
