# def makeTrigger(triggerMap, triggerType, params, name):
#     if triggerType in ['TITLE', 'SUMMARY', 'SUBJECT']:
#         triggerMap[name] = triggerType.capitalize() + 'Trigger' + '("' + params[0] + '")'
#         return "%sTrigger made with word: %s" % (triggerType.capitalize(), params[0])

#     if triggerType == 'PHRASE':
#         s = " "
#         triggerMap[name] = triggerType.capitalize() + 'Trigger' + '("' + s.join(params) + '")'
#         return "%sTrigger made with phrase: %s" % (triggerType.capitalize(), s.join(params))

#     if triggerType == 'NOT':
#         triggerMap[name] = triggerType.capitalize() + 'Trigger' + triggerMap[params[0]]
#         return triggerType.capitalize() + 'Trigger made with trigger: ' + triggerMap[params[0]]
    
#     if triggerType in ['AND','OR']:
#         triggerMap[name] = triggerType.capitalize() + 'Trigger' + triggerMap[params[0]] + ' and ' + triggerMap[params[1]]
#         return triggerType.capitalize() + 'Trigger made with triggers: ' + triggerMap[params[0]] +' and ' + triggerMap[params[1]]


def makeTrigger(triggerMap, triggerType, params, name):
    if triggerType in ['TITLE', 'SUMMARY', 'SUBJECT']:
        triggerMap[name] = triggerType.capitalize() + 'Trigger' + '("' + params[0] + '")'
        return triggerMap[name]

    if triggerType == 'PHRASE':
        s = " "
        triggerMap[name] = triggerType.capitalize() + 'Trigger' + '("' + s.join(params) + '")'
        return triggerMap[name]

    if triggerType == 'NOT':
        triggerMap[name] = triggerType.capitalize() + 'Trigger' + triggerMap[params[0]]
        return triggerMap[name]
    
    if triggerType in ['AND','OR']:
        triggerMap[name] = triggerType.capitalize() + 'Trigger' + triggerMap[params[0]] + ' and ' + triggerMap[params[1]]
        return triggerMap[name]
triggerMap = {}

name = 't1'
triggerType = 'TITLE' 
params = ['NASA']

print makeTrigger(triggerMap, triggerType, params, name)

