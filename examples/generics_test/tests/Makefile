# Copyright (c) 2016 Technische Universitaet Dresden, Germany
# Chair for VLSI-Design, Diagnostic and Architecture
# Author: Martin Zabel
# All rights reserved.

CWD=$(shell pwd)
COCOTB=$(CWD)/../../..

# VHDL only at the moment
TOPLEVEL_LANG ?=vhdl

ifeq ($(TOPLEVEL_LANG),verilog)
  VERILOG_SOURCES =$(CWD)/../hdl/generics_test.v
else ifeq ($(TOPLEVEL_LANG),vhdl)
  VHDL_SOURCES =$(CWD)/../hdl/generics_test.vhdl
else
  $(error "A valid value (verilog or vhdl) was not provided for TOPLEVEL_LANG=$(TOPLEVEL_LANG)")
endif

TOPLEVEL=generics_test
MODULE=$(TOPLEVEL)_cocotb

CUSTOM_SIM_DEPS=$(CWD)/Makefile

VSIM_ARGS=-t 1ps

include $(COCOTB)/makefiles/Makefile.inc
include $(COCOTB)/makefiles/Makefile.sim

# list all required Python files here
sim: $(MODULE).py
