-- =============================================================================
-- Authors:		Martin Zabel
-- 
-- Module:              Testing whether generics can be read via VPI
-- 
-- Description:
-- ------------------------------------
-- Just to check whether reading of generic values is possible via VPI.
--
-- License:
-- =============================================================================
-- Copyright 2016 Technische Universitaet Dresden - Germany
--		  Chair for VLSI-Design, Diagnostics and Architecture
-- 
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
-- 
--		http://www.apache.org/licenses/LICENSE-2.0
-- 
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.
-- =============================================================================

library ieee;
use ieee.std_logic_1164.all;

entity generics_test is
  generic (
    N : positive := 5);
  port (
    x : in std_logic_vector(N-1 downto 0);
    y : out std_logic_vector(N-1 downto 0));
end entity generics_test;

architecture rtl of generics_test is
begin
  y <= x;
end architecture rtl;
