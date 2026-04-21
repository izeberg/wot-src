from gui.server_events.bonuses import getNonQuestBonuses

def parseBonusData(data):
    groups = data.get('groups')
    if groups is None or not groups:
        return {}
    oneOfSection = groups[0].get('oneof')
    if oneOfSection is None:
        return {}
    result = {}
    if len(oneOfSection) == 2:
        _, items = oneOfSection
        for item in items:
            if item and len(item) == 4:
                probability, _, _, rawData = item
                if rawData:
                    name = (rawData.get('properties') or {}).get('name') or ''
                    if name:
                        cell = result.setdefault(name, {})
                        cell['probability'] = probability[0]
                        cell['bonuses'] = []
                        for k, v in rawData.iteritems():
                            cell['bonuses'].extend(getNonQuestBonuses(k, v))

    return result