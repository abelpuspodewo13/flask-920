import im_wireless as imw
import time
from flask import Flask, render_template

#datalog
FILE_NAME = '/Savelog.txt'

#I2C
SLAVE_ADR = 0x30		#hatのI2Cアドレスは0x30~0x33

#WebServer
app = Flask(__name__)

#Page Ichiran
@app.route('/all')
def index_all():
	iwc = imw.IMWireClass(SLAVE_ADR)
	try:
		while True:
			time.sleep(0.5)
			rx_data_hex = iwc.Read_920()
			#rx_data_hex = "4142454C"
			data = { 'status1' : rx_data_hex}
			'''
			if len(rx_data_hex) >= 1:
				#rx_data_1 = bytes.fromhex(rx_data_hex)
				#rx_data = rx_data_1.decode('utf-8')
				print(rx_data_hex, end='')
				
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

	return render_template('920_index_all.html', **data)

#Main
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, use_reloader=False, debug=True)
