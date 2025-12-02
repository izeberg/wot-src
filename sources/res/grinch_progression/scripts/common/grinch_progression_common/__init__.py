import typing
if typing.TYPE_CHECKING:
    from typing import Dict, List

def getAvailableForClaimingSteps(activeChaptersConfig, progression, tokensCount):
    chaptersOrder = activeChaptersConfig.values()
    chaptersOrder.sort(key=lambda item: item['chapterStart'])
    result = {}
    for chapter in chaptersOrder:
        chapterID = chapter['id']
        dataInt = progression.get(chapterID, 0)
        for i, step in enumerate(chapter['steps']):
            if 1 << i + 1 & dataInt == 0:
                tokensCount -= step['price']
                if tokensCount < 0:
                    return result
                result.setdefault(chapterID, []).append(i + 1)

    return result


def isProgressionCompleted(activeChaptersConf, progression):
    for chapterID, chapter in activeChaptersConf.iteritems():
        chapterPData = progression.get(chapterID, 0)
        for i in range(1, len(chapter['steps']) + 1):
            if 1 << i & chapterPData == 0:
                return False

    return True