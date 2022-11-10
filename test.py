import socket

s = socket.socket()

yolo = s.connect(("localhost", 8052))
s.sendall(b"""<?xml version="1.0" encoding="UTF-8"?>
<sigml>
	<hns_sign>
		<hamnosys_nonmanual/>
		<hamnosys_manual>
			<hamsymmlr/>
			<hamfinger2345/>
			<hamthumboutmod/>
			<hamextfingerl/>
			<hambetween/>
			<hamextfingero/>
			<hampalml/>
			<hamparbegin/>
			<hammoved/>
			<hamreplace/>
			<hamfist/>
			<hamthumbacrossmod/>
			<hamextfingeruo/>
			<hampalmu/>
			<hamparend/>
		</hamnosys_manual>
	</hns_sign>
</sigml>""")