--[[
Made by: Ted Charles Brown
Version 1.0.0

HOW TO USE:
 - Add a MIDI module to Control.
 - Add a "NewModule" to Control.
 - Right click in the "newModule" and select "add action" (or add a new action to the MIDI module to get around node counts).
 - Name the module "mscIn(data)" - data is the variable name and must be included.
 - Copy and paste this code into the code section of that new action.
 - In the MIDI module, under Receive, SysEx, drag the output to the input of the new action.
 - Edit the deviceID, cueList, and timelineName variables to match your setup.

NOTES:
 - Currently does not support pause, resume, fader, or macro commands.
]]--

-- ----------------------------- USER VARIABLES ----------------------------- --

local deviceID = "00" --can be set to "all"
local cueList = "1" -- can be set to "0" for all cue lists
local timelineName = "Timeline 1"

-- ----------------------------- OTHER VARIABLES ---------------------------- --
-- --------------------------- DONT CHANGE THESE! --------------------------- --

local timeline = Pixera.Timelines.getTimelineFromName(timelineName)
local commands = {
    ["01"] = "GO",
    ["02"] = "PAUSE",
    ["03"] = "RESUME",
    ["06"] = "FADER",
    ["07"] = "MACRO"
}

local sourceID = ""
local command = ""
local cueNumber = ""
local cueLength = 0
local sourceCueList = ""

-- ------------------------- CONFIRM AND STORE SYSEX ------------------------ --
sysex = {}
--parse the sysex message into an array
for byte in data:gmatch("..") do
	--pixc.log(byte)
	table.insert(sysex,byte)
end

--confirm it is sysex
if (sysex[1] == "f0" and sysex[2] == "7f") then
	--pixc.log("Confirmed SysEx")
else
	--pixc.log("Not SysEx")
	return
end

-- ---------------------------- BEGIN SYSEX PARSE --------------------------- --

--remove first two sysex specific bytes
table.remove(sysex,1)
table.remove(sysex,1)
--remove last sysex specific byte
table.remove(sysex,#sysex)

--get and remove source device ID byte
sourceID = sysex[1]
table.remove(sysex,1)

--remove next two, MSC protocol bytes
table.remove(sysex,1)
table.remove(sysex,1)

--get and remove command byte
command = commands[sysex[1]]
table.remove(sysex,1)

-- ---------------------------- PARSE CUE NUMBER ---------------------------- --

for i, part in ipairs(sysex) do
    if part ~= "00" and part ~= "2e" then -- IF PART IS NOT END OF INT OR DECIMAL DELIMITER
        cueNumber = cueNumber .. part:gsub("^3", "")
        cueLength = cueLength + 1
    elseif part == "2e" then
        cueNumber = cueNumber .. "."
        cueLength = cueLength + 1
    else
        cueLength = cueLength + 1
        break
    end
end

-- Remove the processed parts
for i = 1, cueLength do
    table.remove(sysex, 1)
end

-- ----------------------------- PARSE CUE LIST ----------------------------- --

for i, part in ipairs(sysex) do
    sourceCueList = sourceCueList .. part:gsub("^3", "")
end

-- Print the parsed values
--pixc.log("Device ID:", sourceID)
--pixc.log("Command:", command)
--pixc.log("Cue List:", sourceCueList)
--pixc.log("Cue Number:", cueNumber)

-- ------------------------- HANDLE PIXERA CUE LIST ------------------------- --

--convert deviceID to hex if its not set to "all"
if (type(deviceID) == "number") then
	deviceID = string.format("%02x", deviceID)
end

--
--cueNumber = tonumber(cueNumber)
--local pixeraCueNumber = timeline.getCueFromNumber(cueNumber)
local pixeraCue = timeline.getCueFromName(cueNumber)
if (deviceID == sourceID or deviceID == "all" or sourceID == "7f") then
	if (cueList == sourceCueList or tonumber(cueList) <= 0) then
		if (command == "GO") then
			if pixeraCue ~= nil then
				pixc.log("GO CUE:", cueNumber)
				pixeraCue.apply()
				if(pixeraCue.getOperation()==2)
							then
								timeline.play()
							end
			end
		end
	end
end
