import json

testMethodsSet = set()

with open('logForClient.txt') as logFile:
    for line in logFile:
        line = line.strip()
        if not line:
            continue
        method = line.split(',')[1]
        methodName = method[:method.find('(')]
        methodPath = method[method.find('(')+1:method.find(')')]
        fullPath = methodPath + "#" + methodName
        testMethodsSet.add(fullPath)



json_string = json.dumps(list(testMethodsSet))
print(json_string)


with open("test_method_list.json", "w") as file:
        file.write(json_string)
