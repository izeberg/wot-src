from enum import Enum

class BanState(Enum):
    PREPICK = 'prepick'
    VOTING = 'voting'
    FINISHED = 'finished'
    NONE = 'none'


class CandidateState(Enum):
    NOSELECTED = 'noSelected'
    DONTBANSELECTED = 'dontBanSelected'
    SINGLECANDIDATE = 'singleCandidate'
    MULTIPLECANDIDATES = 'multipleCandidates'