from flask import Flask, render_template, flash , request , redirect, url_for 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import logging
app = Flask(__name__ , template_folder="templates")
uri = "mongodb+srv://imicorp:BNCjJPAswlcwQP93@cluster0.mh1eamh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
def configure_logger(app):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('app.log')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)

configure_logger(app)
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



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
    print("ooooooooooooooooooooo" , mydata)
    mymen = numToName(mydata)
    return render_template("start.html" , mydata=mymen)
    # return render_template('index.html', items=perfect)

# @app.route("/admin" , method=["GET" , "POST"])
# def page_admin():
#     return render_template("index.html")





def numToName(numlist):
    items = []
    for i in numlist :
        mydb = client["test_database"]["posts"]
        myquery = { "state" : i }
        myitem = mydb.find_one(myquery)
        print(myitem)
        items.append(myitem["name"])
        # !!!!!!!!!!!! IMPORTANT Print!!!!!!!!!!!!!!
        # !!!!!!!!!!!! IMPORTANT Print!!!!!!!!!!!!!!
        # !!!!!!!!!!!! IMPORTANT Print!!!!!!!!!!!!!!
        # !!!!!!!!!!!! IMPORTANT Print!!!!!!!!!!!!!!
        # !!!!!!!!!!!! IMPORTANT Print!!!!!!!!!!!!!!
        # !!!!!!!!!!!! IMPORTANT Print!!!!!!!!!!!!!!
        # !!!!!!!!!!!! IMPORTANT Print!!!!!!!!!!!!!!
        # !!!!!!!!!!!! IMPORTANT Print!!!!!!!!!!!!!!
         #print(items , "0000000000000000000000000033333333333333333333333333")
    return items


def hasPath(src , dst):
    mySet = set()
    latone = None
    globsrc = src
    queue = [[src , 0 , src]]
    print(direction)
    arrayLen = len(queue)
    while arrayLen > 0 :
        [src , distance , saheb] = queue.pop()
        direction.append([src , distance , saheb])
        print(direction , "llllllllllllllllllllllllllllllllllllllllllllll")
        print(queue)
        if(src == dst) :
            print(direction)
            fortest = roadfinder(src , saheb , globsrc)
            latone = fortest
            return latone
              
        
        mygraph = graph.find_one()
        neighbors = mygraph[str(src)]
        distance += 1
        for neighbor in neighbors :
            if neighbor not in mySet :
                print( neighbor ,"checked !")
                mySet.add(neighbor)
                mySet.add(src)
                queue.insert(0 , [neighbor , distance , src])
                print(queue , "myQwas")
    print(latone , "5555555555555555555555555555555555555555555555555555555555555555555555555")
    queue = []
    mySet = {}
    return latone  
                
def roadfinder(src , saheb , globsrc ) :
    mypath.append(src)
    print(direction , "this is direction")
    if src != globsrc :
        #print(src , globsrc , "tjosssssssssssssssssssssssssssssssssssssssss")
        for i in direction : 
            if i[0] == saheb :
                newSrc = i[0]
                newSaheb = i[2]
                roadfinder(newSrc , newSaheb , globsrc)
    else:
        print("this is my hole path" , mypath)
    return mypath



            # newSrc = i[0]
            # newSaheb = i[1]
            # print(newSaheb , newSrc)
            # myFinal.append(newSrc)
    # if newSrc != newSaheb :
    #     roadfinder(newSrc , newSaheb)
    # else :
    #     print(myFinal)
    #     return
        


    





