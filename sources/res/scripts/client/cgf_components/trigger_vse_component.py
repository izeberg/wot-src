from __future__ import absolute_import
import CGF, Event
from GenericComponents import VSEComponent
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class TriggerVSEComponent(object):
    editorTitle = 'Trigger VSE'
    domain = CGF.Domain.ClientEditor
    eventName = ComponentProperty(type=CGF.PropertyType.String, editorName='event name', value='event')

    def __init__(self):
        super(TriggerVSEComponent, self).__init__()
        self.triggerEvent = Event.Event()


class TriggerVisualScriptComponentsSystem(CGF.System):
    TriggerActivated = CGF.ActivateReaction(CGF.ReactRw(TriggerVSEComponent), VSEComponent)
    TriggerDeactivated = CGF.DeactivateReaction(CGF.ReactRw(TriggerVSEComponent), VSEComponent)
    Reactions = CGF.Reactions(TriggerActivated, TriggerDeactivated)

    def update(self):
        for trigger, vse in self.reaction(self.TriggerDeactivated):
            trigger.triggerEvent -= vse.context.onTriggerEvent

        for trigger, vse in self.reaction(self.TriggerActivated):
            self.doAction(trigger.eventName)
            trigger.triggerEvent += vse.context.onTriggerEvent