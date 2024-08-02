import eventlet
eventlet.monkey_patch()

import json
from flask import Flask, render_template
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
from time import strftime
import im_wireless as imw
import time

app = Flask(__name__)
#app.config['SECRET'] = 'my scret key'
app.config['TEMPLATES_AUTO_RELOAD'] = False
app.config['MQTT_BROKER_URL'] = 'localhost'
#app.config['MQTT_BROKER_URL'] = 'test.mosquitto.org'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_CLIENT_ID'] = 'flask_MQTT' 
app.config['MQTT_CLEAN_SESSION'] = True
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False

# Parameters for SSL enabled
# app.config['MQTT_BROKER_PORT'] = 8883
# app.config['MQTT_TLS_ENABLED'] = True
# app.config['MQTT_TLS_INSECURE'] = True
# app.config['MQTT_TLS_CA_CERTS'] = 'ca.crt'


mqtt = Mqtt(app)
socketio = SocketIO(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
	#data = {'status':"OK"}
	#socketio.emit('mqtt_message', data=data)
	#return render_template('main.html')
	#return render_template('server.html')
	time = strftime("%Y-%m-%d %H:%M:%S")
	data = {'time':time}
	return render_template('920_test_index.html', **data)
	#return render_template('test_index_dai3_3f_out.html', **data) --> pake textarea, pasti bisa, tapi ga jadi merah

	
@app.route('/all')
def index_all():
	data = {'status':"OK"}
	#socketio.emit('mqtt_message', data=data)
	#return render_template('main.html')
	#return render_template('server.html')
	return render_template('920_test_index_all.html', **data)
	#return render_template('test_index_dai3_3f_out.html', **data) --> pake textarea, pasti bisa, tapi ga jadi merah
	
@app.route("/dai3_5f")
def index_dai3_5f():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "20"
	hum1 = "15"
	data_dai3_5f = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('test_index_dai3_5f.html', **data_dai3_5f)
	
@app.route("/dai3_1f")
def index_dai3_1f():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "20"
	hum1 = "15"
	data_dai3_1f = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('test_index_dai3_1f.html', **data_dai3_1f)
	
@app.route("/dai3_2f_neg_a")
def index_dai3_2f_neg_a():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "20"
	hum1 = "15"
	data_dai3_2f_neg_a = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('test_index_dai3_2f_neg_a.html', **data_dai3_2f_neg_a)

@app.route("/dai3_2f_aa_b")
def index_dai3_2f_aa_b():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "20"
	hum1 = "15"
	data_dai3_2f_aa_b = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('test_index_dai3_2f_aa_b.html', **data_dai3_2f_aa_b)
	
@app.route("/dai3_4f")
def index_dai3_4f():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "20"
	hum1 = "15"
	data_dai3_4f = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('test_index_dai3_4f.html', **data_dai3_4f)

@app.route("/dai3_1f_out")
def index_dai3_1f_out():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "20"
	hum1 = "15"
	data_dai3_1f_out = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('test_index_dai3_1f_out.html', **data_dai3_1f_out)
	
@app.route("/dai3_2f_out")
def index_dai3_2f_out():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "20"
	hum1 = "15"
	data_dai3_2f_out = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('test_index_dai3_2f_out.html', **data_dai3_2f_out)
	
@app.route("/dai3_3f_out")
def index_dai3_3f_out():
	time = strftime("%Y-%m-%d %H:%M:%S")
	temp1 = "20"
	hum1 = "15"
	data_dai3_3f_out = {'time':time, 'temp':temp1, 'hum':hum1,'status':"OK"}
	return render_template('test_index_dai3_3f_out.html', **data_dai3_3f_out)
"""
#MQTT
@socketio.on('publish')
def handle_publish(json_str):
    data = json.loads(json_str)
    mqtt.publish(data['topic'], data['message'], data['qos'])


@socketio.on('subscribe')
def handle_subscribe(json_str):
    data = json.loads(json_str)
    mqtt.subscribe(data['topic'], data['qos'])
"""
#920MHz Lib
def receive():
	#I2C
	SLAVE_ADR = 0x30		#hatのI2Cアドレスは0x30~0x33
	iwc = imw.IMWireClass(SLAVE_ADR)
	try:
		while True:
			time.sleep(0.5)
			rx_data_hex = iwc.Read_920()
			#rx_data_hex = "4142454C"
			if len(rx_data_hex) >= 1:
				#rx_data_1 = bytes.fromhex(rx_data_hex)
				#rx_data = rx_data_1.decode('utf-8')
				print(rx_data_hex, end='')
				'''
				with open(FILE_NAME, 'a') as f:
					f.write(rx_data)
				
				if len(rx_data) >= 11:
					if (rx_data[2]==',' and rx_data[7]==',' and rx_data[10]==':'):
						rxid = rx_data[3:7]
						txbuf = 'TXDA' + rxid
						print('>', txbuf)
						iwc.Write_920(txbuf)
				'''
	except KeyboardInterrupt:
		iwc.gpio_clean()
		print('END')
		
def scheduledsend():
	SLAVE_ADR = 0x30		#hatのI2Cアドレスは0x30~0x33
	iwc = imw.IMWireClass(SLAVE_ADR)
	i = 0
	try:
		while True:
			tx001_buf = "TXDU 0001,AA"
			tx003_buf = "TXDU 0003,BB"
			rx_data = iwc.Read_920()
			if len(rx_data) >= 1:
				print("Read Awal" +rx_data, end='')
			#Send 001
			iwc.Write_920(tx001_buf)
			time.sleep(0.05)
			rx_data = iwc.Read_920()
			i=i+1
			if len(rx_data) >= 1:
				timestamp = str(time.time())
				
				print(timestamp+"From 0001 "+rx_data, end='')
			time.sleep(0.1)
			print(i)
			"""
			#Send 003
			iwc.Write_920(tx003_buf)
			time.sleep(0.1)
			rx_data = iwc.Read_920()
			if len(rx_data) >= 1:
				print("From 0003 "+rx_data, end='')		
			"""	
	except KeyboardInterrupt:
		iwc.gpio_clean()
		print('END')


#920MHZ socketio
@socketio.on('scheduledsend')  #@sockeetio.on('nama_function_yg_di_python'
def handle_publish():
    #data = json.loads(json_str)
    #mqtt.publish(data['topic'], data['message'], data['qos'])
    scheduledsend()


@socketio.on('receive')
def handle_subscribe():
    #data = json.loads(json_str)
    #mqtt.subscribe(data['topic'], data['qos'])
    receive()


@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    #mqtt.unsubscribe_all()
    pass


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode(),
        qos=message.qos,
    )
    socketio.emit('mqtt_message', data=data)


@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    # print(level, buf)
    pass


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3000, use_reloader=False, debug=True)
