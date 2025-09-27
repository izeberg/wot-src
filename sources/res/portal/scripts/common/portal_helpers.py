import typing
if typing.TYPE_CHECKING:
    from Math import Vector3

def clampImpulse(impulse, mass, velocity, velocityLimit):
    newVelocity = velocity + impulse / mass
    length = newVelocity.length
    if length <= velocityLimit:
        return impulse
    factor = velocityLimit / length
    return (newVelocity * factor - velocity) * mass