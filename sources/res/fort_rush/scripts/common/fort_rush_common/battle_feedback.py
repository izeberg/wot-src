from __future__ import absolute_import

def packPersonalScoreFeedback(score, totalScore):
    return (score & 4294967295) << 32 | totalScore & 4294967295


def unpackPersonalScoreFeedback(packedData):
    score = packedData >> 32 & 4294967295
    totalScore = packedData & 4294967295
    return (score, totalScore)