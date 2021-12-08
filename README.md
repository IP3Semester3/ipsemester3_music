# ipsemester3_music
Using the Spotify API we can get access to an almost infinite library of music and playlists. This service is designed to make the api easier to use and implement in other applications regardless of coding language used.
Currently this project is still under development and many features are subject to change or incomplete. 
The full project board which includes the development process of this service can be found here: https://semseter3-ip-tomeykholt.atlassian.net/jira/software/projects/SEM3/boards/2

# research
The Spotify API is a RESTApi use to get data from the Spotify service. We're using this API because Spotify already has a large library of music and millions of users paying for it. With the API we can ask the user to authorize using their own spotify account. This way we have access to the user's information and playlists. 

In order to get the authorization working, we need to verify the app with the spotify developer portal. The verified URL is 127.0.0.1:4000. Any other url will not support Spotify authorization and will therefore not work.

# Notes

During development we use the url 127.0.0.1:4000. Changing this breaks the Spotify authorization so make sure there are no other applications running on the exact same url. 
There is a limit of 25 users that can authorize using this service and I have to manually add these users to the list of testers while the program is still under development. This is a limit set by Spotify themselves and I can’t change this. So in order to actually use this service while testing, your email associated with the spotify account you want to use has to be registered for the app. 

# Coding Conventions
In this project we follow the standard coding conventions for Python (https://www.python.org/dev/peps/pep-0008) . We also use the standard Python coding conventions in regards to docstring which helps understanding methods easier without having to decipher the whole thing. 
````
def example(string: stringname) -> int
"""This is an example description of a method.
Args: 
    string (stringname): description of string
Returns:
    Int: description of int returned"""
````

# Github setup
## Branches
In this github we work with different branches that correlate to the status of the project. Usually we use the Development branch during development and only push to the main branch after the code has been inspected and tested. 
For new features it is advised to create a new branch from the main branch. The name of this branch has to correspond with the Issue ID found on our JIRA page (SEM3-25, link for the JIRA project is at the top of this document) followed by the feature name. This way we can keep a clean and organized branch setup going.
Pull requests into the main branch will be tested so make sure you have created sufficient unit tests before creating a pull request. 


