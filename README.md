# Data 22 Star Wars Project

## Instructions

The character data in the MongoDB database has been pulled from https://swapi.dev/.
As well as 'people', the API has data on starships.
Using Python, code was written to pull data on all available starships from the API.
The "pilots" key contained URLs pointing to the characters who pilot the starship.
Pilots keys with urls were replaced with a list of ObjectIDs from the characterz collection.
Starships were then inserted into their own collection in MongoDB.
(Making sure to drop any existing starships collections.)

## Requirements

- Use good coding principles with appropriate comments, good naming conventions and handling errors gracefully.
- Follow PEP 8
- Create a job board in Trello or similar to keep track of your user stories.
Link to Trello boards: https://trello.com/b/gooxFNRT/project2
- Utilise functional programming OR object-oriented programming
- Use Test Driven Development: write tests first

## Using this repo

- Branch off from main.
- Use your own name for the name of the branch (e.g. mine would be FahimaNakitende - please copy this format).
- Make sure you commit and push to the remote repo frequently to keep your work up-to-date.
- The gitignore should catch most unnecessary project files, but do pay attention to what you are adding to the repo.
- Replace this README with an appropriate README for your project (including a link to your job board).
