from flask import Flask, render_template, flash , request , redirect, url_for 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import config
# creating flask app
app = Flask(__name__ , template_folder="templates")
# MONGODB database uri for connection
uri = config.uri
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# Routes
@app.route("/")
def hello_world():
    app.logger.info('Index page accessed')
    return render_template("start.html")
@app.route("/start" , methods=["POST"])
def start():
    global mypath
    global myFinal
    global direction
    global globsrc
    global graph
    direction = []
    myFinal = []
    mypath = []
    src = request.form.get("src")
    dst = request.form.get("dst")

    mydb = client["test_database"]["posts"]
    graph = client["roads"]["posts"]
    srcquery = { "name": src }
    dstquery = { "name": dst }
    mysrc = mydb.find_one(srcquery)
    mydst = mydb.find_one(dstquery)

    mygraph = graph.find_one()
    globsrc = mysrc["state"]
    myglobsrc = globsrc
    mydata = hasPath(mysrc["state"] , mydst["state"])
    mymen = numToName(mydata)
    return render_template("start.html" , mydata=mymen)



# Functions
def numToName(numlist):
    lineColors = {1 : "redline" , 2 : "blueline" , 3 : "skyblueline" , 4 :"yellowline" , 5 : "greenline" , 6 : "pinkline", 7 : "purpleline"}
    items = []
    for i in numlist :
        mydb = client["test_database"]["posts"]
        myquery = { "state" : i }
        myitem = mydb.find_one(myquery)
        myTuple = (myitem["name"] , lineColors[myitem["line"]])
        items.append(myTuple)
    return items


def hasPath(src , dst):
    mySet = set()
    latone = None
    globsrc = src
    queue = [[src , 0 , src]]
   
    arrayLen = len(queue)
    while arrayLen > 0 :
        [src , distance , saheb] = queue.pop()
        direction.append([src , distance , saheb])
        if(src == dst) :
            fortest = roadfinder(src , saheb , globsrc)
            latone = fortest
            return latone
              
        
        mygraph = graph.find_one()
        neighbors = mygraph[str(src)]
        distance += 1
        for neighbor in neighbors :
            if neighbor not in mySet :
                mySet.add(neighbor)
                mySet.add(src)
                queue.insert(0 , [neighbor , distance , src])
    queue = []
    mySet = {}
    return latone  


def roadfinder(src , saheb , globsrc ) :
    mypath.insert(0,src)
    print(direction , "this is direction")
    if src != globsrc :
        for i in direction : 
            if i[0] == saheb :
                newSrc = i[0]
                newSaheb = i[2]
                roadfinder(newSrc , newSaheb , globsrc)
    else:
        print("this is my hole path" , mypath)
    return mypath



        


    





