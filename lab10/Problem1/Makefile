all: peer server

peer: peer.o
	g++ -std=c++11 peer.o -o peer

peer.o: peer.cpp
	g++ -std=c++11 -c peer.cpp -o peer.o

server: server.cpp peerinfo.hpp
	g++ -std=c++11 server.cpp -o server

clean:
	rm -f peer.o peer server