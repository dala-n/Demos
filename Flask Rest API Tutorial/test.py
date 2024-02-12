import requests

BASE = "http://127.0.0.1:5000/"                 # Location of the API, server it is running on

######################## main2.py
### Hello world API: ###

# response = requests.get(BASE + "helloworld")    # 1:
# print(response.json())                          # Do json so its not a response Object, but information

# response = requests.post(BASE + "helloworld") # 2:
# print(response.json())

# response = requests.get(BASE + "helloworld/daniel/19")    # Now with Parameters
# print(response.json())   

######################## main3.py
### Hello world API: ###

# response = requests.get(BASE + "helloworld/bill")    # helloworld/daniel , helloworld/bill
# print(response.json())   

######################## main4.py
### Mock Youtube API: ###

# ### Attempts to add a new video, video/1, with certain args
# response = requests.put(BASE + "video/1", {"likes": 10, "name": "Daniel", "views": 10000})    # Arguments as parameters
# print(response.json())

# input()       # Delay for demonstation purposes

# ### Attempts to get a video that is defined as video/1
# response = requests.get(BASE + "video/1") 
# print(response.json())

### Attempts to add a new video, video/2, with certain args, but it already exists
# response = requests.put(BASE + "video/2", {"likes": 20, "name": "Hello", "views": 500})    # Arguments as parameters
# print(response.json())

# input()       # Delay for demonstation purposes

# response = requests.put(BASE + "video/2", {"likes": 5, "name": "Nice Video", "views": 6000})    # Arguments as parameters
# print(response.json())

# ### Check if abort works if there is no valid video to get
# input()       # Delay for demonstation purposes
# response = requests.get(BASE + "video/6")
# print(response.json())   

######################### main.py
### Mock YouTube API: ###

response = requests.put(BASE + "video/2", {"likes": 20, "name": "Hello", "views": 500})    # Arguments as parameters
print(response.json())

data = [{"likes": 20, "name": "New Video!", "views": 50000},
        {"likes": 1000, "name": "Cats!", "views": 1000000},
        {"likes": 45, "name": "How to make REST API", "views": 1000}] 

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()         # Delay for demonstration purposes
response = requests.get(BASE + "video/2") # Return video/2 data
print(response.json())