NAME = genera

SOURCES = color.cpp gradient.cpp layer.cpp texture.cpp genera.cpp
OBJECTS = color.o gradient.o layer.o texture.o genera.o

INCLUDE = #-I/usr/include/ -I./
LIBDIR  = #-L/usr/X11R6/lib -L./lib/mfmod/linux

COMPILERFLAGS = -Wall
CC = g++
CFLAGS = $(COMPILERFLAGS) $(INCLUDE)
LIBRARIES = #-lX11 -lXi -lXmu -lglut -lGL -lGLU -lm -lminifmod -lpthread

all : $(SOURCES)
	$(CC) $(SOURCES) $(CFLAGS) -o $(NAME) $(LIBDIR) $(LIBRARIES)

compile : $(SOURCES)
	$(CC) $(SOURCES) $(CFLAGS) -c

debug : $(SOURCES)
	$(CC) $(SOURCES) $(CFLAGS) -ggdb -o $(NAME) $(LIBDIR) $(LIBRARIES)

clean :
	rm *.o

