import CGF
from GenericComponents import VSEComponent
from cgf_components.rocket_acceleration_component import SoundEvents
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent

@registerComponent
class RocketAccelerationAbilityStateListener(object):
    editorTitle = 'Rocket Accelerator Ability State Listener'
    category = 'Rocket Accelerator Ability'
    domain = CGF.DomainOption.DomainClient
    vseComponent = ComponentProperty(type=CGFMetaTypes.LINK, editorName='VS Plan', value=VSEComponent)
    start = ComponentProperty(type=CGFMetaTypes.LINK, editorName='Start Object', value=CGF.GameObject)
    idle = ComponentProperty(type=CGFMetaTypes.LINK, editorName='Idle Object', value=CGF.GameObject)
    end = ComponentProperty(type=CGFMetaTypes.LINK, editorName='Stop Object', value=CGF.GameObject)
    sound_l = ComponentProperty(type=CGFMetaTypes.LINK, editorName='Left Sound', value=CGF.GameObject)
    sound_r = ComponentProperty(type=CGFMetaTypes.LINK, editorName='Right Sound', value=CGF.GameObject)
    startDuration = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName='Start Duration', value=0.2)
    endDuration = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName='End Duration', value=0.2)
    soundReady = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Ready sound', value=SoundEvents.ROCKET_ACCELERATION_READY)
    soundActivePC = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Active PC sound', value=SoundEvents.ROCKET_ACCELERATION_ACTIVE_PC)
    soundActiveNPC = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Active NPC sound', value=SoundEvents.ROCKET_ACCELERATION_ACTIVE_NPC)
    soundStopPC = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Stop PC sound', value=SoundEvents.ROCKET_ACCELERATION_STOP_PC)
    soundStopNPC = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Stop NPC sound', value=SoundEvents.ROCKET_ACCELERATION_STOP_NPC)
    soundDisable = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Disable sound', value=SoundEvents.ROCKET_ACCELERATION_DISABLE)
    soundEmpty = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Empty sound', value=SoundEvents.ROCKET_ACCELERATION_EMPTY)