~   clone the repository using git command
~   change derictory to sample_proj file
~   run a virtual environment for python
        python3 -m venv myvenv
        cd myvenv
        cd bin
        source activate
~    exit the directory /myvenv/bin
~   run the following commands in the same order
        python manage.py makemigrations
        python manage.py migrate
        python manage.py runserver

    the server will be launched on 127.0.0.1:8000, browse to the address and all the options   will be visible that can be used

~   Accessing the endpoints
        create a python file and import requests library:
            import requests
        
        Accessing /home endpoint:
            
            import requests

            response = requests.get('http://yourdomain.com/home')
            print(response.text)  # Assuming you're expecting HTML content
        
        Accessing /signup endpoint:
        
            import requests

            data = {
            'username': 'example_user',
            'password': 'example_password'
            # Add other required fields as needed
            }

            response = requests.post('http://yourdomain.com/signup', json=data)
            print(response.json())  # Assuming the response contains JSON data
        
        Accessing /login endpoint:

            URL: http://yourdomain.com/login
            Method: POST (for logging in a user)
            Example: Similar to the signup endpoint, send the appropriate credentials in the request body.
            
        
        Accessing /create_note endpoint:
            
            import requests

            data = {
             'title': 'Example Note',
            'content': 'This is an example note content'
            # Add other required fields as needed
            }

            response = requests.post('http://yourdomain.com/create_note', json=data)
            print(response.json())  # Assuming the response contains JSON data
            
        
        Accessing /get_note/{id} endpoint:
            import requests

            response = requests.get('http://yourdomain.com/get_note/1')
            print(response.json())  # Assuming the response contains JSON data representing the note
            
        
        Accessing /share_note endpoint:

            URL: http://yourdomain.com/share_note
            Method: POST (for sharing a note)
            Example: Similar to the /create_note endpoint, send the necessary data in the request body.
            
            
        Accessing /update_note/{id} endpoint:

            Replace {id} with the actual ID of the note you want to update.
            URL: http://yourdomain.com/update_note/1 (Replace 1 with the actual note ID)
            Method: PUT (for updating an existing note)
            Example: Similar to the /create_note endpoint, send the updated data in the request body.
            
            
        Accessing /get_note_version_history/{id} endpoint:
            
            import requests

            response = requests.get('http://yourdomain.com/get_note_version_history/1')
            print(response.json())  # Assuming the response contains JSON data representing the version history
