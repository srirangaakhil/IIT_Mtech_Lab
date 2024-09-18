hello: main.o factorial.o hello.o
	g++ -std=c++11 -o hello main.o factorial.o hello.o

main.o: main.cpp
	g++ -std=c++11 -c main.cpp -o main.o

factorial.o: factorial.cpp
	g++ -std=c++11 -c factorial.cpp -o factorial.o

hello.o: hello.cpp
	g++ -std=c++11 -c hello.cpp -o hello.o

clean:
	rm -f factorial.o hello hello.o main.o