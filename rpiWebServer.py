from flask import Flask, render_template, request
app = Flask(__name__)

from time import strftime

# Retrieve data from sensor
'''
def sensor1():
	time = 
	return time, temp, hum
'''
# main route 
@app.route("/")
def index():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp = [70, 50, 30, 30]
	hum = [15, 20, 20, 75]
	#temp[1] = 20
	#hum[1] = 15
	#temp[2] = 30
	#hum[2] = 20
	#temp[3] = 30
	#hum[3] = 20
	#temp[4] = 30
	#hum[4] = 20
	dai=[]
	for i in range (4):
		#j = str(i)
		print(temp[i])
		print(hum[i])
		if temp[i] < 40 and hum[i] < 40:
			dai.append("OK")
		else:
			dai.append("NG")
	
	data = {'time':time,'dai1':dai[0], 'dai2':dai[1], 'dai3':dai[2], 'dai4':dai[3]}
	return render_template('index.html', **data)

@app.route("/all")
def index_all():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "60"
	hum1 = "75"
	data_all = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('index_all.html', **data_all)

@app.route("/dai3_5f")
def index_dai3_5f():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "20"
	hum1 = "15"
	data_dai3_5f = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('index_dai3_5f.html', **data_dai3_5f)
	
@app.route("/dai3_1f")
def index_dai3_1f():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "20"
	hum1 = "15"
	data_dai3_1f = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('index_dai3_1f.html', **data_dai3_1f)
	
@app.route("/dai3_2f_neg_a")
def index_dai3_2f_neg_a():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "20"
	hum1 = "15"
	data_dai3_2f_neg_a = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('index_dai3_2f_neg_a.html', **data_dai3_2f_neg_a)

@app.route("/dai3_2f_aa_b")
def index_dai3_2f_aa_b():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "20"
	hum1 = "15"
	data_dai3_2f_aa_b = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('index_dai3_2f_aa_b.html', **data_dai3_2f_aa_b)
	
@app.route("/dai3_4f")
def index_dai3_4f():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "20"
	hum1 = "15"
	data_dai3_4f = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('index_dai3_4f.html', **data_dai3_4f)

@app.route("/dai3_1f_out")
def index_dai3_1f_out():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "20"
	hum1 = "15"
	data_dai3_1f_out = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('index_dai3_1f_out.html', **data_dai3_1f_out)
	
@app.route("/dai3_2f_out")
def index_dai3_2f_out():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "20"
	hum1 = "15"
	data_dai3_2f_out = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('index_dai3_2f_out.html', **data_dai3_2f_out)
	
@app.route("/dai3_3f_out")
def index_dai3_3f_out():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "20"
	hum1 = "15"
	data_dai3_3f_out = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('index_dai3_3f_out.html', **data_dai3_3f_out)
	
# sub factory route 

@app.route("/dai2")
def index2():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp2 = "50"
	hum2 = "20"
	dai2 = {'time':time, 'temp':temp2, 'hum':hum2}
	return render_template('index2.html', **dai2)

@app.route("/dai3")	
def index3():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp3 = "30"
	hum3 = "20"
	dai3 = {'time':time, 'temp':temp3, 'hum':hum3}
	return render_template('index3.html', **dai3)

@app.route("/dai4")	
def index4():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp4 = "30"
	hum4 = "75"
	dai4 = {'time':time, 'temp':temp4, 'hum':hum4}
	return render_template('index4.html', **dai4)
	
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)

