Ground = {
    width = 64,
    height = 64,
    class = "ground",
    type = "none",
    x = 0,
    y = 0,
    sprite = nil,
}
Ground.__index = Ground

function Ground:new(ground)
    ground = ground or {}
    setmetatable(ground, Ground)
    ground.sprite = love.graphics.newImage("assets/ground/" .. ground.type .. ".png")
    return ground
end
