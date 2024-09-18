CC = gcc
ODIR = build
IDIR = .
TDIR = $(abspath $(dir $(PWD)))
CFLAGS = -Wall -pthread -I$(IDIR)
NUMOFCLIENTS = 5

_OBJ = cl_task.o cl_utils.o
#OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))
OBJ = $(addprefix $(ODIR)/, $(_OBJ))
TEMP =
ifeq ($(TOPDIR),)
	TOPDIR = $(TDIR)
endif

.PHONY: all
all: build $(TOPDIR)/client.out

build:
	mkdir -p $(ODIR)

$(ODIR)/%.o: %.c %.h
	$(CC) -o $@ -g -c $<

$(TOPDIR)/client.out: mt_client.c $(OBJ)
	$(CC) -o $@ -g $^ $(CFLAGS)

.PHONY: clean
clean:
	@rm -rf $(ODIR) 
	@rm -f $(TOPDIR)/client.out

.PHONY: run
run: all
	$(TOPDIR)/client.out localhost 8080
	$(TOPDIR)/client.out localhost 8080 $(NUMOFCLIENTS)
