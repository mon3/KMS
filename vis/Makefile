CC=g++
CFLAGS=-Wall
LIBS= -lGL -lGLU -lglut
all:    program
program:    main.o  
	$(CC) -o program main.o $(CFLAGS) $(LIBS)
main.o: main.cpp
	$(CC) -o main.o -c main.cpp $(CFLAGS)
clean:
	rm -f *.o