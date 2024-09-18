CC = gcc
ODIR = build
IDIR = .
TDIR = $(abspath $(dir $(PWD)))
CFLAGS = -Wextra -pthread -I$(IDIR)

_OBJ = sv_task.o sv_utils.o
#OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))
OBJ = $(addprefix $(ODIR)/, $(_OBJ))
TEMP =
ifeq ($(TOPDIR),)
	TOPDIR = $(TDIR)
endif

.PHONY: all
all: build $(TOPDIR)/server.out

build: 
	mkdir -p $(ODIR)

$(ODIR)/%.o: %.c %.h
	$(CC) -o $@ -g -c $<

$(TOPDIR)/server.out: mt_server.c $(OBJ)
	$(CC) -o $@ -g $^ $(CFLAGS)

.PHONY: clean
clean:
	@rm -rf $(ODIR) 
	@rm -f $(TOPDIR)/server.out

.PHONY: run
run: all
	$(TOPDIR)/server.out 8080
