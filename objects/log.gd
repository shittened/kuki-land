extends RigidBody2D

var hovered:bool = false
var type:String = 'log'
var is_big:bool = true

func _ready() -> void:
	pass # Replace with function body.

func _process(delta: float) -> void:
	self.linear_velocity = Vector2(0, 0)
	#self.rotation_degrees = 0

func _on_mouse_entered() -> void:
	hovered = true

func _on_mouse_exited() -> void:
	hovered = false
