require "entity"

Bunny = {}
Bunny.__index = Entity

function Bunny:new()
    local bunny = Entity:new({
        type = "player"
    })
    setmetatable(bunny, Bunny)
    return bunny
end
