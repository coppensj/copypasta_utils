CXX := g++

override INCLUDES = \
	-I.

override CXXFLAGS += \
	$(INCLUDES) \
	-O3 \
	-std=c++17 \
	-fpermissive 

override LDFLAGS += \
	-lstdc++fs \
	-lz \
	-lm

TARGETS = write_to_file create_dir random_nums
OBJS = write_to_file.o create_dir.o random_nums.o

.PHONY: all
all: $(TARGETS)
 
write_to_file: write_to_file.o
	$(CXX) -o $@ $^

create_dir: create_dir.o
	$(CXX) -o $@ $^ $(LDFLAGS)

random_nums: random_nums.o
	$(CXX) -o $@ $^

.PHONY: clean
clean:
	@echo "Cleaning..."
	@rm -f *.o
	@rm -f *.csv
	@rm -rf test_folder/
	@rm -f $(TARGETS)
