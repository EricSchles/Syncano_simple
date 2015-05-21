import syncano
import pickle
from flask import Flask,render_template,url_for, request
import json
import random

class Voting:
    def __init__(self):
        creds = pickle.load(open("creds","rb"))
        self.con = syncano.connect(email=creds["email"],password=creds["password"])
        instance = self.con.Instance
        self.instance = list(instance.please.all())[0]
        self.voting = self.instance.classes.get(name="voting")
    def create_schema(self):
        self.instance.classes.create(name="voting",schema='[{"name":"vote","type":"string"}]')
    def save_vote(self,vote):
        obj = self.voting.objects.create(vote=vote)
        obj.save()
    def get_all_votes(self):
        return [elem.vote for elem in list(self.voting.objects.all())]


class RandomData:
    def __init__(self):
        creds = pickle.load(open("creds","rb"))
        self.con = syncano.connect(email=creds["email"],password=creds["password"])
        instance = self.con.Instance
        self.instance = list(instance.please.all())[1]
        self.random_data = self.instance.classes.get(name="random_data")    
    def create_schema(self):
        self.instance.classes.create(name="random_data",schema='[{"name":"data","type":"integer"}]')
    def create_data_set(self):
        for i in xrange(10): 
            data = random.randint(10,100)
            obj = self.random_data.objects.create(data=data)
            obj.save()
    def get_all_data(self):
        return [elem.data for elem in list(self.random_data.objects.all())]

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    vote_obj = Voting()
    if request.method == "POST":
        vote = request.form.get("vote") 
        if vote:
            vote_obj.save_vote(vote)
        return render_template("index.html",votes=vote_obj.get_all_votes())
    return render_template("index.html",votes=vote_obj.get_all_votes())


@app.route("/viz",methods=["GET","POST"])
def viz():
    rando = RandomData()
    rando.create_data_set()
    data = rando.get_all_data()
    return render_template("viz.html",data=json.dumps(data))


if __name__ == '__main__':
    
    app.run(debug=True)
