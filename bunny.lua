require "entity"

Bunny = {}
Bunny.__index = Entity

function Bunny:new(x, y, world)
    local bunny = Entity:new({
        type = "player",
        x = x,
        y = y,
        speed = 50,
    }, world)
    setmetatable(bunny, Bunny)
    return bunny
end
