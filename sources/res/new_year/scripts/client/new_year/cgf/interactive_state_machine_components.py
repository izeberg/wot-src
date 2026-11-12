import CGF
from GenericComponents import AnimatorComponent
from cgf_script.component_meta_class import ComponentProperty, registerComponent, CGFMetaTypes
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery
from helpers import dependency
from new_year.interactive_state_machine.constants import PersonaTypes
from new_year.skeletons.i_sm_queue import IStateMachineQueue

@registerComponent
class NYPersonaComponent(object):
    domain = CGF.DomainOption.DomainClient
    editorTitle = 'NY SM Persona'
    category = 'New Year'
    type = ComponentProperty(type=CGFMetaTypes.STRING, editorName='select persona type', value=PersonaTypes.CELEB_MAN, annotations={'comboBox': {PersonaTypes.CELEB_MAN: PersonaTypes.CELEB_MAN, 
                    PersonaTypes.CELEB_WOMAN: PersonaTypes.CELEB_WOMAN, 
                    PersonaTypes.OLD_MAN: PersonaTypes.OLD_MAN}})


class PersonaStateMachineManager(CGF.ComponentManager):
    __slots__ = ()
    __stateMachineQueue = dependency.descriptor(IStateMachineQueue)

    @onAddedQuery(NYPersonaComponent, AnimatorComponent)
    def onAddedPersona(self, persona, animator):
        self.__stateMachineQueue.bind(persona.type, animator)
        self.__stateMachineQueue.handleLoaded()

    @onRemovedQuery(NYPersonaComponent, AnimatorComponent)
    def onRemovedPersona(self, persona, _):
        self.__stateMachineQueue.unbind(persona.type)