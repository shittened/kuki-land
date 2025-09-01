World = {}
World.__index = World

function World:new()
    local world = love.physics.newWorld(0, 0, false)
    love.physics.setMeter(64)
    return world
end
