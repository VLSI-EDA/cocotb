# ==============================================================================
# Authors:		Martin Zabel
# 
# Cocotb Testbench:	Testing whether generics can be read via VPI
# 
# Description:
# ------------------------------------
# Just to check whether reading of generic values is possible via VPI.
#
# License:
# ==============================================================================
# Copyright 2016 Technische Universitaet Dresden - Germany
#		 Chair for VLSI-Design, Diagnostics and Architecture
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#		http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import random

import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge, ReadOnly
from cocotb.monitors import Monitor
from cocotb.drivers import BitDriver
from cocotb.binary import BinaryValue
from cocotb.regression import TestFactory
from cocotb.scoreboard import Scoreboard
from cocotb.result import TestFailure, TestSuccess

# ==============================================================================
@cocotb.coroutine
def run_test(dut):
    """Run test."""
    N = dut.N.value # read value of generic 'N' of DUT
    dut._log.info("The type of N is {0!s}.".format(type(N))) # print type in simulator console
    # when using FLI (QuestaSim) then N is of type <int>
    # when using VPI (e.g. GHDL) then N is of type <BinaryValue>
    if isinstance(N, BinaryValue): # convert type to <int> if neccesary
        N = N.integer
    dut._log.info("The value of N is {0!s}.".format(N)) # print value in simulator console

    # The following is just an example why the value of the generic is important.
    input_value = random.randint(0,(2**N)-1) # generate a random integer value 
    dut.x <= BinaryValue(input_value, N, False) # assign value to input 'x'
    yield Timer(1000) # wait for 1000 ps (consider delay within DUT)

    # check output 'y' of DUT and raise corresponding test result
    output_value = dut.y.value.integer
    if output_value == input_value:
        raise TestSuccess()
    else:
        raise TestFailure()

# ==============================================================================
# Register test.
factory = TestFactory(run_test)
factory.generate_tests()
