# Andrew's README

## Trello Board Link: https://trello.com/b/wpmmxatO/data22-starwars

Application Info

	starship_pull_request.py
		
		status_code()
		# Returns the HTTP status code from the website to ensure the resource is open
		# to requests.
	
		transform_starship_data()
		# Pulls all starship data from the swapi, loads it into a usable format, and
		# returns it as a list.
	
	starship_connect_objectID_characters.py

		starship_connect_url_characters()
		# Further formats the data sent from the swapi by replacing all urls in the
		# "pilots" field with their respective names.
		
		starship_connect_objectID_characters()
		# Uses the formatted "pilots" field from starship_connect_url_characters() to
		# cross reference the "characters" mongoDB database and assign the respective
		# objectID.
		
	starship_collection_insert.py
		
		collection_insert()
		# Inserts the fully formatted swapi starship data into a MongoDB collection.


Testing Info
	
	test_starship_pull_request.py
	
		test_starship_pull_request()
		# Tests that the "status_code" function in the "starship_pull_request.py"
		# file is correctly returning the status_code "200"

		# Test that asserts whether the data pulled from the swapi website has
		# been correctly pulled and formatted in a 36 length list of dictionaries.
	
	test_starship_connect_objectID_characters.py
	
		test_starship_connect_url_characters()
		# Tests that all urls have been replaced with valid character names from the
		# swapi.
		
		test_starship_connect_objectID_characters()
		# Tests that the pilot object ids are in the list of object ids from the
		# characters database.
	
	test_starship_collection_insert.py
	
		test_starship_collection_length()
		# Tests if the collection inserted into MongoDB is 36 fields long.

	run_all_tests.py
	#debugging file used to run pytest.main() outside of the commandline.



	
# Data 22 Star Wars Project

## Instructions

The character data in your MongoDB database has been pulled from https://swapi.dev/.
As well as 'people', the API has data on starships.
Using Python, write code to pull data on all available starships from the API.
The "pilots" key contains URLs pointing to the characters who pilot the starship.
Use these to replace 'pilots' with a list of ObjectIDs from our characters collection, then insert the starships into their own collection in MongoDB.
(Make sure you drop any existing starships collections.)

You have until 9am on Tuesday.

## Requirements

- Use good coding principles.  That means testing, appropriate comments, good naming conventions and handling errors gracefully.
- Follow PEP 8
- Create a job board in Trello or similar to keep track of your user stories.  Provide a link to that job board in your version of this README.
- Your code should utilise functional programming OR object-oriented programming
- Use Test Driven Development: write your tests first

## Using this repo

- Branch off from main.
- Use your own name for the name of the branch (e.g. mine would be DavidHarvey - please copy this format).
- Make sure you commit and push to the remote repo frequently to keep your work up-to-date.
- The gitignore should catch most unnecessary project files, but do pay attention to what you are adding to the repo.
- Replace this README with an appropriate README for your project (including a link to your job board).