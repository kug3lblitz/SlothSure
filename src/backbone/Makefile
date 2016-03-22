CPPFLAGS = -Wall -ansi -g -std=c++11

all: testOut.o
	g++ $(CPPFLAGS) testOut.o -o Driver.out

testOut.o: testOut.cpp
	g++ $(CPPFLAGS) -c testOut.cpp

# to test for memory leaks
val:
	valgrind ./Driver.out

# -f removes any error messages if the file is not present
clean:
	rm -rf *~ *.h.gch *# *.out *.o
	clear
	ls

# compile an executable
run:
	./Driver.out