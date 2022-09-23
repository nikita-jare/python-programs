# python-programs

This repostiory is for mini python programs.
Below is the list of programs as part of this repository. Please feel free to suggest any code changes, features or a better approach.

### 1. Guess the word:

This program is terminal game which asks user to guess the word by guessing the letters in word in limited chances.

### 2. Choose random episodes to bingewatch

This program chooses an episode randomly from given directory.
The directory structure is assumed to be as follows:

```
shows
  |___ show1
	 |____ season 1
		    |_____ Epsiode 1
		    |_____ Episode 2
		    |_____ Episode 3

         |____ season 2
		    |_____ Epsiode 1

         |____ season 3
                    |_____ Episode 1
		    |_____ Episode 2

  |___ show2
	 |____ season 1
                    |____ Episode 1

         |____ season 2
                    |____ Episode 1
		    |____ Episode 2

```
The dataset folder has the structure defined. I have included txt files for now as a reference.

### 3. Download PDF file from a url provided:

This program reads contents using request module and writes to a PDF file in chunks.
A progress bar is also displayed to denote the download progress. tqdm module is used for this.

For your reference, Downloaded file is stored in the Output folder. 

### 4. Basic Chat application (Client-server):

This is a basic application which enables sending and receiving messages on terminal.
An IPV4 address socket is created and it is bound explicitly to local host.
You can find the screenshot of output of this chat program.

On one machine run server.py

```
python server.py
```

On another terminal/machine run client.py

```
python client.py
```  

These two programs will keep on running infinitely until close manually

### 4. Facebook Graph API 

Using request module, fetch profile pictures of facebook users using Facebook Graph API URL.
If the profile picture is not set, or it is private, it returns a default picture.

```
python3 facebook_graph_api.py
```
