CXX := g++

override INCLUDES = \
	-I.

override CXXFLAGS += \
	-O3 \
	-std=c++17 \
	-fpermissive

TARGETS = write_to_file
OBJS = write_to_file.o

.PHONY: all
all: $(TARGETS)
 
write_to_file: write_to_file.o
	$(CXX) -o $@ $^

.PHONY: clean
clean:
	@echo "Cleaning..."
	@rm -f *.o
	@rm -f *.csv
	@rm -f $(TARGETS)
