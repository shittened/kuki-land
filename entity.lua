Entity = {
    hp = 100,
    speed = 100,
    class = "entity",
    type = "none",
    sprite = nil,
    x = 0,
    y = 0,
    body = nil,
    shape = nil,
    fixture = nil,
    weight = 50,
}
Entity.__index = Entity

function Entity:new(entity, world)
    entity = entity or {}
    setmetatable(entity, Entity)
    entity.sprite = love.graphics.newImage("assets/" .. entity.type .. "/idle_down/0.png")
    entity.body = love.physics.newBody(world, entity.x, entity.y, "dynamic")
    entity.body:setMass(entity.weight)
    entity.body:setPosition(entity.x, entity.y)
    entity.shape = love.physics.newRectangleShape(
        entity.sprite:getPixelWidth(),
        entity.sprite:getPixelHeight()
    )
    entity.fixture = love.physics.newFixture(entity.body, entity.shape)
    return entity
end

function Entity:draw()
    love.graphics.draw(self.sprite, self.body:getX(), self.body:getY())
end

function Entity:update(dt)
    self.body:setPosition(self.x, self.y)
end
