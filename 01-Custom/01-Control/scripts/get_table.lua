--[[
Made by: Ted Charles Brown
Version 1.0.0

HOW TO USE:
 - Drag INPUT to OUTPUT of value query
]]--

result = pixc.callRefs()

function logTable(t, indent)
    indent = indent or ""  -- default value for indent
    for k, v in pairs(t) do
        if type(v) == "table" then
            pixc.log(indent .. tostring(k) .. ":")
            logTable(v, indent .. "  ")  -- Recursively log table with an increased indent
        else
            pixc.log(indent .. tostring(k) .. ": " .. tostring(v))
        end
    end
end