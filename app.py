from flask import Flask , render_template , request , redirect , jsonify



app = Flask(__name__)




organic ={"a":2.4 , "b":1.05 , "c":2.5 , "d":0.38}
semidetached ={"a":3.0 , "b":1.12 , "c":2.5 , "d":0.35}
embedded ={"a":3.6 , "b":1.20 , "c":2.5 , "d":0.32}

projecttypes={"organic":"organic", "semidetached":"semidetached" ,"embedded":"embedded"}




rely ={"VeryLow":0.75 , "Low":0.88 , "Nominal":1.00 , "High":1.15 , "VeryHigh":1.40 , "ExtraHigh":1.00,"Fake":1.00}
data ={"VeryLow":1.00 , "Low":0.94 , "Nominal":1.00 , "High":1.08 , "VeryHigh":1.16 , "ExtraHigh":1.00 ,"Fake":1.00}
cplx ={"VeryLow":0.70 , "Low":0.88 , "Nominal":1.00 , "High":1.15 , "VeryHigh":1.40 , "ExtraHigh":0.38 ,"Fake":1.00}

time ={"VeryLow":1.00 , "Low":1.00 , "Nominal":1.00 , "High":1.11 , "VeryHigh":1.30 , "ExtraHigh":1.66 ,"Fake":1.00}
stor ={"VeryLow":1.00 , "Low":1.00 , "Nominal":1.00 , "High":1.06 , "VeryHigh":1.21 , "ExtraHigh":1.56 ,"Fake":1.00}
virt ={"VeryLow":1.00 , "Low":0.87 , "Nominal":1.00 , "High":1.15 , "VeryHigh":1.30 , "ExtraHigh":1.00 ,"Fake":1.00}
turn ={"VeryLow":1.00 , "Low":0.87 , "Nominal":1.00 , "High":1.07 , "VeryHigh":1.15 , "ExtraHigh":1.00 ,"Fake":1.00}

acap ={"VeryLow":1.46 , "Low":1.19 , "Nominal":1.00 , "High":0.86 , "VeryHigh":0.71 , "ExtraHigh":1.00 ,"Fake":1.00}
axep ={"VeryLow":1.29 , "Low":1.13 , "Nominal":1.00 , "High":0.91 , "VeryHigh":0.82 , "ExtraHigh":1.00 ,"Fake":1.00}
pcap ={"VeryLow":1.42 , "Low":1.17 , "Nominal":1.00 , "High":0.86 , "VeryHigh":0.70 , "ExtraHigh":1.00 ,"Fake":1.00}
vexp ={"VeryLow":1.21 , "Low":1.10 , "Nominal":1.00 , "High":0.90 , "VeryHigh":1.00 , "ExtraHigh":1.00 ,"Fake":1.00}
lexp ={"VeryLow":1.14 , "Low":1.07 , "Nominal":1.00 , "High":0.95 , "VeryHigh":1.00 , "ExtraHigh":1.00 ,"Fake":1.00}

modp ={"VeryLow":1.24 , "Low":1.10 , "Nominal":1.00 , "High":0.91 , "VeryHigh":0.82 , "ExtraHigh":1.00 ,"Fake":1.00}
tool ={"VeryLow":1.24 , "Low":1.10 , "Nominal":1.00 , "High":0.91 , "VeryHigh":0.83 , "ExtraHigh":1.00 ,"Fake":1.00}
sced ={"VeryLow":1.23 , "Low":1.08 , "Nominal":1.00 , "High":0.04 , "VeryHigh":1.10 , "ExtraHigh":1.00 ,"Fake":1.00}

alldict = {"rely","data","cplx","time","stor","virt","turn","acap","axep", "pcap","vexp","lexp","modp", "tool", "sced"}
allval = ["VeryLow","Low","Nominal","High","VeryHigh","ExtraHigh"]




@app.route('/basic', methods=['GET', 'POST'])
def basic():
    if request.method == 'GET':
        return render_template("basicmodel.html")
    if request.method == 'POST':
        projectmodel=request.form['type']
        kloc= int(request.form['loc'])
        if projectmodel in projecttypes:
            convertdict = eval(projectmodel)
            if isinstance(convertdict, dict):
                effort = round(convertdict.get("a") * (kloc ** convertdict.get("b")),3)
                developmenttime = round(convertdict.get("c") * (effort ** convertdict.get("d")),3)
                personsrequired = round(effort / developmenttime)
                productivity= round(kloc/effort,4)
                return jsonify(kloc=kloc ,effort=effort ,time=developmenttime,persons=personsrequired , productivity=productivity )


@app.route('/intermediate', methods=['GET', 'POST'])
def intermediate():
    if request.method == 'GET':
        return render_template("intermediatemodel.html" , alldict=alldict , allval=allval)
    if request.method == 'POST':
        dataform = request.form
        projectmodel = projecttypes.get(dataform['radio'])
        kloc = int(dataform['kloc'])
        eaf = 1.0;
        for key in dataform.keys():
            if key in alldict:
                value = eval(key).get(dataform[key])
                eaf = eaf * value
        if projectmodel in projecttypes:
            convertdict = eval(projectmodel)
            if isinstance(convertdict, dict):
                effort = round(convertdict.get("a") * (kloc ** convertdict.get("b")) * eaf , 3)
                developmenttime = round(convertdict.get("c") * (effort ** convertdict.get("d")) , 3)
                personsrequired = round(effort / developmenttime)
                productivity = round(kloc / effort , 4)
                return jsonify(kloc=kloc, eaf=eaf ,effort=effort ,time=developmenttime,persons=personsrequired , productivity=productivity )





@app.route('/')
def Home():
    return render_template("homepage.html")



if __name__ == "__main__":
    app.run(debug=True)