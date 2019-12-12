import pyrebase

config = {
    "apiKey": "AIzaSyBJV9POvfWm2P6FD-RohJGYIM8vj8loFOs",
    "authDomain": "pravince-8ac79.firebaseapp.com",
    "databaseURL": "https://pravince-8ac79.firebaseio.com",
    "projectId": "pravince-8ac79",
    "storageBucket": "pravince-8ac79.appspot.com",
    "messagingSenderId": "832471264141",
    "appId": "1:832471264141:web:685cd44192d88b8fa0abc4",
    "measurementId": "G-692GXPM601"
  }

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# db.child("names").push({"name":"pravince"})
# db.child("names").update({"name":"kjk"})
# db.child("names").remove()


while(1):
    n=int(input())
    if(n==1):
        db.child("Lights").update({"light1":"on"})
    elif(n==0):
        db.child("Lights").update({"light1":"off"})