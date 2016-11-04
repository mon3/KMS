SOURCES = animateAr.cpp
CC = g++
CFLAGS = -pedantic
CLINK = -lglut -lGL -lGLU 

all: $(SOURCES)
	$(CC) $(CFLAGS) $(SOURCES) $(CLINK) -o animateAr
	
clean:
	rm -f *.o animateAr