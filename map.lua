require "ground"
require "settings"

Map = {}
Map.__index = Map

function Map:new()
    local map = {}
    setmetatable(map, Map)

    for y = 1, map_height do
        for x = 1, map_width do
            local ground = Ground:new({
                type = "grass",
                x = x * 32,
                y = y * 32,
            })
            table.insert(map, ground)
        end
    end

    return map
end

function Map:draw()
    for _, tile in pairs(self) do
        love.graphics.draw(tile.sprite, tile.x, tile.y)
    end
end
