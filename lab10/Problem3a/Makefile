cc = g++
remove = rm

hello: main.o factorial.o hello.o
	$(cc) -std=c++11 -o hello main.o factorial.o hello.o

main.o: main.cpp
	$(cc) -std=c++11 -c main.cpp -o main.o

factorial.o: factorial.cpp
	$(cc) -std=c++11 -c factorial.cpp -o factorial.o

hello.o: hello.cpp
	$(cc) -std=c++11 -c hello.cpp -o hello.o

clean:
	$(remove) -f factorial.o hello hello.o main.o
