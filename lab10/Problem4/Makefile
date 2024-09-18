TOPDIR = $(PWD)
export TOPDIR

all: server.out client.out

server.out:
	cd mt_server && $(MAKE)

client.out:
	cd mt_client && $(MAKE)

.PHONY: clean
clean:
	@cd mt_server && $(MAKE) clean --no-print-directory
	@cd mt_client && $(MAKE) clean --no-print-directory

.PHONY: run_server
run_server: server.out
	@cd mt_server && $(MAKE) run

.PHONY: run_client
run_client: client.out
	@cd mt_client && $(MAKE) run

