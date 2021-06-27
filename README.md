# Data 22 Star Wars Project (Josh Blackmore)

## Provided Instructions
The character data in your MongoDB database has been pulled from https://swapi.dev/. As well as 'people', the API has data on starships. Using Python, write code to pull data on all available starships from the API. The "pilots" key contains URLs pointing to the characters who pilot the starship. Use these to replace 'pilots' with a list of ObjectIDs from our characters collection, then insert the starships into their own collection in MongoDB. (Make sure you drop any existing starships collections.)


## How It Works
Program starts by instancing the pymongo client which is used for querying the starwars database. Next the 'starships' collection is created if it does not already exist, if it does it is dropped to avoid duplication in the next stage.
Next, the starships data are inserted into the database from the starwars api.
Finally if the pilots section is not empty then the urls for the pilots are changed for the object ids of the pilots connecting them to the characters collection.

## Testing
Use 'pytest -v' on the parent directory to view the tests conducted during the TDD (Test Driven Development) part of this small project.


## Research
- PyMongo: https://www.w3schools.com/python/python_mongodb_getstarted.asp
- PyMongo Docs: https://pymongo.readthedocs.io/en/stable/


## Other Information
- Trello Board: https://trello.com/b/pwNxR3rf/starwars-mongodb-api-project
- My Git: https://github.com/Kcorb0
