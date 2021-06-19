from flask import Flask,render_template,request,session,redirect,url_for
import json
import os
from werkzeug.utils import secure_filename
from web3 import Web3
app=Flask(__name__)
app.secret_key="Hello"
@app.route('/')
def index():
    return render_template('index.html')

    
@app.route('/login')
def login():
    
    return render_template('login.html')

@app.route('/about')
def about():
    
    return render_template('about.html')


@app.route('/thank_you')
def thank_you():
    name=request.args.get("Username")
    password=request.args.get("Password")
    Type=request.args.get('options')
    print(Type)
    ganache_url="http://127.0.0.1:7545"
    web3=Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    web3.eth.defaultAccount=request.args.get("Key")
    session["key"]=request.args.get("Key")
    print(web3.eth.defaultAccount)
    abi=json.loads('[{"inputs":[{"internalType":"string","name":"IPFS","type":"string"},{"internalType":"string","name":"username","type":"string"},{"internalType":"string","name":"password","type":"string"},{"internalType":"string","name":"email","type":"string"}],"name":"register","outputs":[{"internalType":"string","name":"user_name","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"username","type":"string"},{"internalType":"string","name":"password","type":"string"}],"name":"sign_in","outputs":[{"internalType":"string","name":"user_name","type":"string"}],"stateMutability":"view","type":"function"}]')
    address=web3.toChecksumAddress("0x756A235E7A8B83c09F6d5D8eB12554E66462F069")
    contract=web3.eth.contract(address=address,abi=abi)
    NAME=contract.functions.sign_in(name,password).call()
    print(NAME)
    if(NAME=="Invalid"):
        print("True condition")
        return render_template('login.html',flag=False)
    else:
        if(Type=='User'):
            abi1=json.loads('[{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"add_money","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"string","name":"link","type":"string"}],"name":"bid","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"bidder","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"completed","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"counter","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"create_project","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"request_count","type":"int256"}],"name":"delete_project","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"detail","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"exist","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"uint256","name":"selecte","type":"uint256"}],"name":"select","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
            address1=web3.toChecksumAddress("0x8A6b6c015EDBa50596e2b316cecce99bc6E9291f")
            contract1=web3.eth.contract(address=address1,abi=abi1)
            #print(contract.functions.counter().call())
            counter=(int)(contract1.functions.counter().call())

            #print(type(contract1.functions.detail(2).call()))
            projects=[]
            for i in range (1,counter+1,1):
                tup=contract1.functions.detail(i).call()
                if(tup[0]!=0 and tup[-1]<tup[-4]):
                    projects.append(tup)
            print(projects)
            return render_template('user_name.html', Username=name,type="User", project=projects)
        else:
            
            return render_template('admin_home.html', Username=name,type="Admin")  
    
@app.route('/register_page') 
def register_page():
    return render_template('register.html')

@app.route('/register') 
def register():
    web3=Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    
    web3.eth.defaultAccount=request.args.get("Key")
    session["key"]=request.args.get("Key")
    abi=json.loads('[{"inputs":[{"internalType":"string","name":"IPFS","type":"string"},{"internalType":"string","name":"username","type":"string"},{"internalType":"string","name":"password","type":"string"},{"internalType":"string","name":"email","type":"string"}],"name":"register","outputs":[{"internalType":"string","name":"user_name","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"username","type":"string"},{"internalType":"string","name":"password","type":"string"}],"name":"sign_in","outputs":[{"internalType":"string","name":"user_name","type":"string"}],"stateMutability":"view","type":"function"}]')
    address=web3.toChecksumAddress("0x756A235E7A8B83c09F6d5D8eB12554E66462F069")
    contract=web3.eth.contract(address=address,abi=abi)
    
    name=request.args.get("Username")
    password=request.args.get("Password")
    email=request.args.get("email")
    IPFS=request.args.get("IPFS")
    status=contract.functions.register(IPFS,name,password,email).transact()
    
    return render_template('gologin.html')

@app.route('/upload_project', methods=['GET','POST'])
def upload_project():
    p1= "H:\\sem_project\\static"
    p3= "H:\\sem_project\\static\\"
    if(request.method=='POST'):
        f=request.files['image']
        f.save(os.path.join(p1,secure_filename(f.filename)))
        p1=os.path.join(p1,secure_filename(f.filename))
        print(p1)
    web3=Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    
    web3.eth.defaultAccount=request.form['key']
    
    abi=json.loads('[{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"add_money","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"string","name":"link","type":"string"}],"name":"bid","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"bidder","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"completed","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"counter","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"create_project","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"request_count","type":"int256"}],"name":"delete_project","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"detail","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"exist","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"uint256","name":"selecte","type":"uint256"}],"name":"select","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
    address=web3.toChecksumAddress("0x8A6b6c015EDBa50596e2b316cecce99bc6E9291f")
    contract=web3.eth.contract(address=address,abi=abi)
    place=request.form['place']
    description=request.form['description']
    amount=request.form['amount']
    print(request.form['key'],place,description,amount)
    contract.functions.create_project(place,description,p1,(int)(amount)).transact()
    counter =contract.functions.counter().call()

    x=str(counter)
    path=os.path.join(p3,x)
    print(path)
    os.mkdir(path)

    return redirect(url_for('bid'))

@app.route('/bid')    
def bid(): 
    key=session["key"]
    print(key)   
    web3=Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    
    web3.eth.defaultAccount=key
    abi=json.loads('[{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"add_money","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"string","name":"link","type":"string"}],"name":"bid","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"bidder","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"completed","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"counter","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"create_project","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"request_count","type":"int256"}],"name":"delete_project","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"detail","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"exist","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"uint256","name":"selecte","type":"uint256"}],"name":"select","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
    address=web3.toChecksumAddress("0x8A6b6c015EDBa50596e2b316cecce99bc6E9291f")
    #abi=json.loads('[{"inputs":[],"name":"counter","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"create_project","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"request_count","type":"int256"}],"name":"delete_project","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"detail","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string","name":"selected","type":"string"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"exist","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]')
    #address=web3.toChecksumAddress("0x4F9aF5FdcfF54Ab0864b5ed6cDdA81B7AB61EDd3")
    contract=web3.eth.contract(address=address,abi=abi)
    #print(contract.functions.counter().call())
    counter=(int)(contract.functions.counter().call())

    #print(type(contract.functions.detail(2).call()))
    projects=[]
    for i in range (1,counter+1,1):
        
        tup=contract.functions.detail(i).call()
        if(tup[0]!=0 and tup[-2]==""):
            projects.append(tup)
    print(projects)


    return render_template('bid.html', project=projects)

@app.route('/pay',methods=['GET','POST'])
def pay():
    ID=request.form['id']
    amount=request.form['amount']
    web3=Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    key=request.form['key']
    print(key) 
    web3.eth.defaultAccount=key
    abi=json.loads('[{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"add_money","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"string","name":"link","type":"string"}],"name":"bid","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"bidder","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"completed","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"counter","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"create_project","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"request_count","type":"int256"}],"name":"delete_project","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"detail","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"exist","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"uint256","name":"selecte","type":"uint256"}],"name":"select","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
    address=web3.toChecksumAddress("0x8A6b6c015EDBa50596e2b316cecce99bc6E9291f")
    #abi=json.loads('[{"inputs":[],"name":"counter","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"create_project","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"request_count","type":"int256"}],"name":"delete_project","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"detail","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string","name":"selected","type":"string"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"exist","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]')
    #address=web3.toChecksumAddress("0x4F9aF5FdcfF54Ab0864b5ed6cDdA81B7AB61EDd3")
    contract=web3.eth.contract(address=address,abi=abi)
     
    contract.functions.add_money((int)(ID),(int)(amount)).transact()
    acc1=key
    acc2="0x9c8f72D4C1B402cb9525FEbA1F436a6DD40d1D1C"
    pkey=request.form['private_key']
    nonce= web3.eth.getTransactionCount(acc1)
    tx={
	 'nonce': nonce,
	 'to':acc2,
	 'value': web3.toWei((int)(amount),'ether'),
	 'gas': 2000000,
	 'gasPrice': web3.toWei('50','gwei')
    }
    print(pkey)
    
    signtx=web3.eth.account.signTransaction(tx,pkey)
    txhash=web3.eth.sendRawTransaction(signtx.rawTransaction)
    print(txhash)
    return render_template('transaction.html') 

@app.route('/complete',methods=['GET','POST'])
def cprojects():
    key=session["key"]
    web3=Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    web3.eth.defaultAccount=key
    abi=json.loads('[{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"add_money","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"string","name":"link","type":"string"}],"name":"bid","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"bidder","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"completed","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"counter","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"create_project","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"request_count","type":"int256"}],"name":"delete_project","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"detail","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"exist","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"uint256","name":"selecte","type":"uint256"}],"name":"select","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
    address=web3.toChecksumAddress("0x8A6b6c015EDBa50596e2b316cecce99bc6E9291f")
   
    contract=web3.eth.contract(address=address,abi=abi)
    #print(contract.functions.counter().call())
    counter=(int)(contract.functions.counter().call())

    print(counter)
    projects=[]
    for i in range (1,counter+1,1):
        
        tup=contract.functions.detail(i).call()
        print(tup)
        if(tup[0]!=0 and tup[-1]>=tup[-4]):
            projects.append(tup)
    print(projects)
    
    return render_template('complete.html',project=projects)
    #return render_template('complete.html')#, project=projects)      

@app.route('/bidselect')
def bidselect():
    key=session["key"]
    web3=Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    web3.eth.defaultAccount=key
    abi=json.loads('[{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"add_money","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"string","name":"link","type":"string"}],"name":"bid","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"bidder","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"completed","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"counter","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"create_project","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"request_count","type":"int256"}],"name":"delete_project","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"detail","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"exist","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"uint256","name":"selecte","type":"uint256"}],"name":"select","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
    address=web3.toChecksumAddress("0x8A6b6c015EDBa50596e2b316cecce99bc6E9291f")
   
    contract=web3.eth.contract(address=address,abi=abi)
    #print(contract.functions.counter().call())
    counter=(int)(contract.functions.counter().call())

    print(counter)
    projects=[]
    for i in range (1,counter+1,1):
        
        tup=contract.functions.detail(i).call()
        print(tup)
        if(tup[0]!=0 and tup[-1]<tup[-4]):
            projects.append(tup)
    #print(projects)
    return render_template('bidselect.html',project=projects)

@app.route('/selectedbid',methods=['GET','POST'])
def selectedbid():
    key=session["key"]
    web3=Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    web3.eth.defaultAccount=key
    abi=json.loads('[{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"add_money","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"string","name":"link","type":"string"}],"name":"bid","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"bidder","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"completed","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"counter","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"create_project","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"request_count","type":"int256"}],"name":"delete_project","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"detail","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"exist","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"uint256","name":"selecte","type":"uint256"}],"name":"select","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
    address=web3.toChecksumAddress("0x8A6b6c015EDBa50596e2b316cecce99bc6E9291f")
   
    contract=web3.eth.contract(address=address,abi=abi)
    #print(contract.functions.counter().call())
    id=(int)(request.form['id'])
    number=(int)(request.form['number'])
    contract.functions.select(id,number).transact()
    return redirect( url_for('bidselect')) 

@app.route('/file_upload',methods=['GET','POST'])
def file_upload():
    pro_no=str(request.form['id'])
    p3= "H:\\sem_project\\static\\"+pro_no+"\\"
    if(request.method=='POST'):
        f=request.files['fileing']
        f.save(os.path.join(p3,secure_filename(f.filename)))
        p1=os.path.join(p3,secure_filename(f.filename))
        print(p1)
    web3=Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    
    web3.eth.defaultAccount=session["key"]
    
    abi=json.loads('[{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"add_money","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"string","name":"link","type":"string"}],"name":"bid","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"bidder","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"completed","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"counter","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"create_project","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"request_count","type":"int256"}],"name":"delete_project","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"detail","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"exist","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"uint256","name":"selecte","type":"uint256"}],"name":"select","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
    address=web3.toChecksumAddress("0x8A6b6c015EDBa50596e2b316cecce99bc6E9291f")
    contract=web3.eth.contract(address=address,abi=abi)
    n=request.form['name']
    print(type(n))
    print(type(pro_no))
    contract.functions.bid((int)(pro_no),str(n)).transact()
    
    return redirect( url_for('bid'))

@app.route('/people')
def people():
    web3=Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    
    web3.eth.defaultAccount=session["key"]
    
    
    list=[]
    for i in range(0,9,1):
        l=[]
        
        name=web3.eth.accounts[i]
        balance=web3.eth.getBalance(name)
        be=web3.fromWei(balance,"ether")
        #print(web3.fromWei(balance,"ether"))
        l.append(name)
        l.append(be)
        list.append(l) 
    print(list)
    return render_template('account.html' ,list=list)       

if( __name__ == "__main__"):
    app.run(debug=True)     


# new 0x8A6b6c015EDBa50596e2b316cecce99bc6E9291f
# [{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"add_money","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"string","name":"link","type":"string"}],"name":"bid","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"bidder","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"completed","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"counter","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"create_project","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"request_count","type":"int256"}],"name":"delete_project","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"detail","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"string","name":"place","type":"string"},{"internalType":"string","name":"description","type":"string"},{"internalType":"string","name":"image_address","type":"string"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"string[]","name":"array","type":"string[]"},{"internalType":"string","name":"selected","type":"string"},{"internalType":"int256","name":"current_amount","type":"int256"}],"internalType":"struct Projects.project","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"}],"name":"exist","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"number","type":"int256"},{"internalType":"uint256","name":"selecte","type":"uint256"}],"name":"select","outputs":[],"stateMutability":"nonpayable","type":"function"}]    