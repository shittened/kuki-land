Entity = {
    hp = 100,
    class = "entity",
    type = "none",
    sprite = nil,
}
Entity.__index = Entity

function Entity:new(entity)
    entity = entity or {}
    setmetatable(entity, Entity)
    entity.sprite = love.graphics.newImage("assets/" .. entity.type .. "/idle_down/0.png")
    return entity
end

function Entity:draw(x, y)
    love.graphics.draw(self.sprite, x, y)
end
