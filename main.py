import bluetooth
import time



# def walk(steps):
#   for x in steps:
def message(command, parameters):
    header = b'\xFB\xBF'
    end = b'\xED'
    parameter = b''.join(parameters)
    # len(header + length + command +parameters + check)
    length = bytes([len(parameters) + 5])
    data = [command, length]
    data.extend(parameters)
    check = bytes([sum(ord(x) for x in data)])
    print(check)
    return header + length + command + parameter + check + end




def discover():
    print("searching ...")
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("found %d devices" % len(nearby_devices))

    for addr, name in nearby_devices:
        if name == "Alpha1_C5C4":
            return addr



msg = message(b'\x22', [b'\x03', b'\x5a', b'\x00', b'\x09'])
msg2 = message(b'\x22', [b'\x02', b'\x5a', b'\x00', b'\x09'])
msg3 = message(b'\x22', [b'\x02', b'\xb4', b'\x00', b'\x09'])
msg4 = message(b'\x22', [b'\x02', b'\x00', b'\x00', b'\x09'])
msg5 = message(b'\x22', [b'\x02', b'\x5a', b'\x09', b'\x09'])
msg6 = message(b'\x22', [b'\x02', b'\x00', b'\x00', b'\x09'])
msg7 = message(b'\x22', [b'\x07', b'\xb4', b'\x08', b'\x09'])
msg8 = message(b'\x22', [b'\x08', b'\xb4', b'\x09', b'\x09'])
msg9 = message(b'\x22', [b'\x09', b'\xb4', b'\x09', b'\x09'])
msg10 = message(b'\x04', [b'\x02'])
action = [msg, msg2, msg3, msg4]

#msg11 = message(b'\x01', [b'\x03', bytearray(int())])
msg12 = message(b'\x26', [b'\x02', b'\xb4'])
print(msg)

# bd_addr = discover()
# bd_addr = "88:1B:99:08:C5:C4"
bd_addr = "88:1B:99:06:D1:54"
port = 6
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))
print('Connected')

sock.send(msg)
sock.send(msg2)
print(sock.send(msg10))

print('Sent data')


response = sock.recv(1024)

time.sleep(2)

sock.send(msg2)
response = sock.recv(1024)
 time.sleep(2)

sock.send(msg3)

     response = sock.recv(1024)
     time.sleep(2)
     sock.send(msg4)
    response = sock.recv(1024)
    time.sleep(2)
    sock.send(msg5)
    response = sock.recv(1024)
    time.sleep(2)
    sock.send(msg6)
    response = sock.recv(1024)
