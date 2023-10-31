--[[
TIME TO TEXT LAYER
Made by: Ted Charles Brown
Version 1.0.0

HOW TO USE:
 - Drag OUTPUT to INPUT of text layer setText()
 - Action name must be "text()" or changed on line 46
]]--


--User Variables
run = true
is12hour = true

-- This function formats the current time based on is12hour variable
function formatTime(currentTime, is12HourFormat)
    local pattern = "(%d+):(%d+):(%d+)"
    local hour, min, sec = currentTime:match(pattern)
    local timeTable = {
        year = os.date("%Y"),
        month = os.date("%m"),
        day = os.date("%d"),
        hour = tonumber(hour),
        min = tonumber(min),
        sec = tonumber(sec)
    }
    local timestamp = os.time(timeTable)

    if is12HourFormat then
        return os.date("%I:%M:%S %p", timestamp) -- 12-hour format with AM/PM
    else
        return os.date("%H:%M:%S", timestamp) -- 24-hour format
    end
end


current_time = Pixera.Utility.getCurrentTimeAsString()
formatted_time = formatTime(current_time, is12hour)

--pixc.log(formatted_time)

--Connect output to input of setText()
pixc.callRefs(formatted_time)

if run then
	Utils.Timer.sleep(1000)
	self.text() --MUST BE NAME OF ACTION "self.{ACTION}()""
end