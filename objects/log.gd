extends RigidBody2D

func _ready() -> void:
	pass # Replace with function body.

func _process(delta: float) -> void:
	self.linear_velocity = Vector2(0, 0)
	#self.rotation_degrees = 0
