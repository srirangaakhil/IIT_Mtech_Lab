
%.o: %.c hellomake.h
	gcc -c -o $@ $<

hellomake: hellomake.o hellofunc.o
	gcc -o $@ $^
