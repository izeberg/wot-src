from __future__ import absolute_import, division
import CGF
from Math import Matrix
from cgf_script.registration import ComponentProperty, registerComponent
from cgf_demo.demo_category import DEMO_CATEGORY

def createRotationMatrix(rotation):
    result = Matrix()
    result.setRotateYPR(rotation)
    return result


clamp = --- This code section failed: ---

 L.  19         0  LOAD_FAST             2  'val'
                3  LOAD_FAST             0  'minVal'
                6  COMPARE_OP            0  <
                9  POP_JUMP_IF_FALSE    16  'to 16'
               12  LOAD_FAST             0  'minVal'
               15  RETURN_END_IF_LAMBDA
             16_0  COME_FROM             9  '9'
               16  LOAD_FAST             2  'val'
               19  LOAD_FAST             1  'maxVal'
               22  COMPARE_OP            4  >
               25  POP_JUMP_IF_FALSE    32  'to 32'
               28  LOAD_FAST             1  'maxVal'
               31  RETURN_END_IF_LAMBDA
             32_0  COME_FROM            25  '25'
               32  LOAD_FAST             2  'val'
               35  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `None' instruction at offset -1

@registerComponent
class TestScriptAxisRotator(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test Script Axis Rotator'
    domain = CGF.Domain.All
    rotationSpeedYaw = ComponentProperty(type=CGF.PropertyType.Float, editorName='rotation speed yaw', value=1.0)
    rotationSpeedPitch = ComponentProperty(type=CGF.PropertyType.Float, editorName='rotation speed pitch', value=1.0)
    rotationSpeedRoll = ComponentProperty(type=CGF.PropertyType.Float, editorName='rotation speed roll', value=1.0)
    transform = ComponentProperty(type=CGF.PropertyType.Link, editorName='transform', value=CGF.TransformComponent)


@registerComponent
class TestScriptMover(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test Script Mover'
    domain = CGF.Domain.All
    finalPoint = ComponentProperty(type=CGF.PropertyType.Link, editorName='finalPoint', value=CGF.TransformComponent)
    period = ComponentProperty(type=CGF.PropertyType.Float, editorName='period', value=1.0)
    transform = ComponentProperty(type=CGF.PropertyType.Link, editorName='transform', value=CGF.TransformComponent)

    def prepare(self, transform):
        self.startMatrix = transform.transform
        self.simTime = 0.0


class TestAxisRotatorSystem(CGF.System):
    MoverCreated = CGF.CreateReaction(CGF.ReactRw(TestScriptMover))
    MoverActivated = CGF.ActivateReaction(CGF.TransformComponent, CGF.ReactRw(TestScriptMover))
    MoverIterate = CGF.IterateReaction(CGF.ActiveOnly, CGF.TransformComponent, CGF.Rw(TestScriptMover))
    RotatorIterate = CGF.IterateReaction(CGF.ActiveOnly, CGF.Rw(CGF.TransformComponent), CGF.Ro(TestScriptAxisRotator))
    TransformAccess = CGF.AccessReaction(CGF.Rw(CGF.TransformComponent))
    Reactions = CGF.Reactions(MoverCreated, MoverActivated, MoverIterate, RotatorIterate, TransformAccess)

    def update(self):
        for mover in self.reaction(self.MoverCreated):
            mover.simTime = 0.0
            mover.startTransform = Matrix()

        transformAccess = self.reaction(self.TransformAccess)
        for myTransform, mover in self.reaction(self.MoverActivated):
            self._setupMover(myTransform, mover, transformAccess)

        delta = self.clock.updateDelta
        for transformComp, axisrotator in self.reaction(self.RotatorIterate):
            transform = transformComp.transform
            m = createRotationMatrix((clamp(-100, 100, axisrotator.rotationSpeedYaw * delta),
             clamp(-100, 100, axisrotator.rotationSpeedPitch * delta),
             clamp(-100, 100, axisrotator.rotationSpeedRoll * delta)))
            transform.preMultiply(m)
            transformComp.transform = transform

        for transformComp, mover in self.reaction(self.MoverIterate):
            self.__move(transformComp, mover, delta, transformAccess)

    def _setupMover(self, myTransform, mover, transformAccess):
        transform = transformAccess.find(mover.transform)
        if not transform:
            transform = myTransform
        mover.prepare(transform)

    def __move(self, myTransform, mover, delta, transformAccess):
        transform = transformAccess.find(mover.transform)
        if not transform:
            transform = myTransform
        mover.simTime += delta
        if mover.simTime > mover.period:
            mover.simTime -= mover.period
        startPos = mover.startMatrix.applyToOrigin()
        finalPoint = transformAccess.find(mover.finalPoint)
        shift = finalPoint.position - startPos
        t = 2 * mover.simTime / mover.period
        if t > 1.0:
            t = 2 - t
        transform.position = startPos + shift * t# Decompile failed :(