extends CharacterBody2D

var speed:int
var normal_speed:int = 50
var carrying_speed:int = floor(self.normal_speed / 2)
var facing_direction:String = 'down'
var direction:Vector2
var axe_dmg:int = 30
var equipped_tool:String = 'axe'
var axe_distance:int = 60
var pickup_distance:int = 30
var luck:int = 10
var force: int = 30000
var inventory: Dictionary
var carrying: bool = false
var carried_object: String

func Animations():
	var prefix: String
	
	if self.carrying:
		prefix = self.carried_object + '_'
	else:
		prefix = ''
		
	if direction.x > 0:
		$AnimatedSprite2D.animation = prefix + 'walking_right'
		facing_direction = 'right'
	elif direction.x < 0:
		$AnimatedSprite2D.animation = prefix + 'walking_left'
		facing_direction = 'left'
	else:
		if direction.y > 0:
			$AnimatedSprite2D.animation = prefix + 'walking_down'
			facing_direction = 'down'
		elif direction.y < 0:
			$AnimatedSprite2D.animation = prefix + 'walking_up'
			facing_direction = 'up'
		else:
			if self.carrying:
				$AnimatedSprite2D.animation = self.carried_object + '_idle_' + facing_direction
			else:
				$AnimatedSprite2D.animation = 'idle_' + facing_direction

func Movement():
	direction = Input.get_vector("move_left", "move_right", "move_up", "move_down").limit_length()
	velocity = direction * speed
	#move_and_slide()

func ChopTree(selected_tile):
	if equipped_tool != 'axe':
		return
		
	for tree in get_parent().get_node('trees').get_children():
		var position = str([tree.global_position.x / 32, tree.global_position.y / 32])
		
		if self.global_position.distance_to(tree.global_position) > axe_distance:
			continue
		
		if position != selected_tile.position:
			continue
			
		var direction_to_fall
		if self.global_position.x <= tree.global_position.x:
			direction_to_fall = 'right'
		else:
			direction_to_fall = 'left'
			
		tree.Chop(axe_dmg, direction_to_fall)
						
func Interact():
	var selected_tile = Maps.selected_tile
	if Input.is_action_just_pressed("right_click"):
		#print(selected_tile)
		self.get_parent().get_node('Cursor').Click()
		match selected_tile.type:
			'tree':
				ChopTree(selected_tile)

func PickUp():
	for item in self.get_parent().get_node('items').get_children():
		if Input.is_action_just_pressed("e"):
			if not $origin.global_position.distance_to(item.global_position) <= pickup_distance:
				return
			if not item.hovered:
				return
			item.visible = false
			item.queue_free()
			if item.is_big and not self.carrying:
				self.carrying = true
				self.carried_object = item.type
				self.speed = self.carrying_speed
			else:
				if self.inventory.get_or_add(item.type) == null:
					self.inventory[item.type] = 0
				self.inventory[item.type] += 1
func Push():
	if not self.move_and_slide():
		return
	if direction == Vector2(0, 0):
		return
	for i in self.get_slide_collision_count():
		var col = self.get_slide_collision(i)
		if col.get_collider() is RigidBody2D:
			var mass = col.get_collider().mass / 100
			col.get_collider().apply_force(col.get_normal() * -force) #- Vector2(mass, mass))	
	
func _ready():
	$AnimatedSprite2D.animation = 'idle_down'
	$AnimatedSprite2D.play()
	self.speed = self.normal_speed

func _physics_process(delta):
	Animations()
	Movement()
	Interact()
	PickUp()
	Push()
