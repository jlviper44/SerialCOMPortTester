import serial
import time
# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='COM20',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

print(ser)
ser.isOpen()

# print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

while 1 :
    # get keyboard input
    # input = raw_input(">> ")
        # Python 3 users
    i = input(">>")
    if i == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        st = i + '\r\n'
        ser.write(str.encode(st))
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
        	# print("")
            out += ser.read(1)
        #     pass
            
        if out != '':

            print (">>" + out)