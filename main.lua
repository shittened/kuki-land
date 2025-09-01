require "bunny"
require "map"
local camera = require "lib/camera"
require "world"

function love.load()
    love.graphics.setDefaultFilter("nearest", "nearest")

    world = World:new()
    bunny = Bunny:new(100, 100, world)
    map = Map:new()
    cam = camera()
end

function love.draw()
    love.graphics.push()
        love.graphics.scale(2, 2)
        cam:attach()
            map:draw()
            bunny:draw()
        cam:detach()
    love.graphics.pop()
end

function love.update(dt)
    world:update(dt)
    bunny:update(dt)
    bunny.x = bunny.x + bunny.speed * dt
    --bunny.body:applyForce(500 * dt, 500 * dt)
    cam:lookAt(bunny.body:getX() + screen_width / 6, bunny.body:getY() + screen_height / 4)
end
