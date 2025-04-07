require "bunny"
require "map"

function love.load()
    love.graphics.setDefaultFilter("nearest", "nearest")

    bunny = Bunny:new()
    map = Map:new()
end

function love.draw()
    love.graphics.push()

    love.graphics.scale(2, 2)
    map:draw()
    bunny:draw(100, 100)

    love.graphics.pop()
end

function love.update()

end
