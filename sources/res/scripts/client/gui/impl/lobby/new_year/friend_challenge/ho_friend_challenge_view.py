import typing
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.new_year.views.friend_challenge.friend_challenge_card_model import FriendChallengeType, FriendChallengeCardModel
from gui.impl.lobby.new_year.ho_selectable_logic_presenter import HOSelectableLogicPresenter
from gui.impl.lobby.new_year.scene_rotatable_view import SceneRotatableView
from helpers import dependency
from items.components.ny_constants import NYFriendServiceDataTokens
from new_year.celebrity.celebrity_quests_helpers import GuestsQuestsConfigHelper
from skeletons.new_year import ICelebritySceneController, IFriendServiceController
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.new_year.views.friend_challenge.ny_friend_challenge_view_model import NyFriendChallengeViewModel
TYPE_TO_TOKEN_MAP = {FriendChallengeType.TOURNAMENT: NYFriendServiceDataTokens.CELEBRITY_QUEST_COMPLETED, 
   FriendChallengeType.GUESTA: NYFriendServiceDataTokens.GUEST_A_QUEST_COMPLETED, 
   FriendChallengeType.GUESTC: NYFriendServiceDataTokens.GUEST_CAT_QUEST_COMPLETED}

class HOFriendChallengeView(SceneRotatableView, HOSelectableLogicPresenter):
    __celebrityController = dependency.descriptor(ICelebritySceneController)
    __friendsService = dependency.descriptor(IFriendServiceController)

    def __init__(self, model, parent, *args, **kwargs):
        super(HOFriendChallengeView, self).__init__(model, parentView=parent)

    @property
    def viewModel(self):
        return self.getViewModel()

    def initialize(self, *args, **kwargs):
        super(HOFriendChallengeView, self).initialize(*args, **kwargs)
        self.isMoveSpaceEnable(False)
        challengeTypes = [FriendChallengeType.TOURNAMENT, FriendChallengeType.GUESTA]
        friendTokens = self.__friendsService.getFriendTokens()
        if friendTokens and friendTokens.get(NYFriendServiceDataTokens.CAT_UNLOCK, 0) > 0:
            challengeTypes.append(FriendChallengeType.GUESTC)
        with self.viewModel.transaction() as (tx):
            tx.setFriendName(self.__friendsService.getFriendName(self.__friendsService.friendHangarSpaId))
            challengeList = Array()
            challengeList.reserve(len(challengeTypes))
            for challengeType in challengeTypes:
                challengeItem = FriendChallengeCardModel()
                challengeItem.setChallengeType(challengeType)
                challengeItem.setCurrentQuantity(friendTokens.get(TYPE_TO_TOKEN_MAP.get(challengeType), 0))
                if challengeType is FriendChallengeType.TOURNAMENT:
                    challengeItem.setTotalQuantity(self.__celebrityController.questsCount)
                else:
                    questsHolder = GuestsQuestsConfigHelper.getNYQuestsByGuest(challengeType.value)
                    challengeItem.setTotalQuantity(len(questsHolder.getQuests()))
                challengeList.addViewModel(challengeItem)

            tx.setChallengeList(challengeList)