#HOUDINI MAKE TRACK CODE
import hou
import sys
import random as rand

redTrainSpeed = 0.2
redTrainStop = False
redFrameNum = 1

blueTrainSpeed = 0.1
blueTrainStop = False
blueFrameNum = 1

greenTrainSpeed = 0.0
greenTrainStop = False
greenFrameNum = 1

def setRedTrainMovement(movement):
    print(movement)
    global redTrainStop
    if movement == -1:
        redTrainStop = False
    else:
        redTrainStop = True
    #print(str(redTrainStop))
    
def setBlueTrainMovement(movement):
    print(movement)
    global blueTrainStop
    if movement == -1:
        blueTrainStop = False
    else:
        blueTrainStop = True
    #print(str(blueTrainStop))
    
def setGreenTrainMovement(movement):
    print(movement)
    global greenTrainStop
    if movement == -1:
        greenTrainStop = False
    else:
        greenTrainStop = True
    #print(str(greenTrainStop))

def setXY(x, z):
    x *= 5
    z *= 5
    return str(x) + ',0,' + str(z)

def setFrame():
    frame = hou.frame()
    while frame > 200:
        frame -= 200
    frame /= 100
    return frame
    
def setRedTrainSpeed(speed):
    global redTrainSpeed, redFrameNum, redTrainStop, greenTrainStop, blueTrainStop
    if redFrameNum == hou.frame():
        pass
    elif redFrameNum > hou.frame():
        while redFrameNum > hou.frame():
            redFrameNum -= 1
            if redtrainStop == False:
                redTrainSpeed -= speed
            elif greenTrainStop == True and blueTrainStop == True:
                redTrainSpeed -= speed
    elif redFrameNum < hou.frame():
        while redFrameNum < hou.frame():
            redFrameNum += 1
            if redTrainStop == False:
                redTrainSpeed += speed
            elif greenTrainStop == True and blueTrainStop == True:
                redTrainSpeed += speed
    return redTrainSpeed

def setBlueTrainSpeed(speed):
    global blueTrainSpeed, blueFrameNum, blueTrainStop
    if blueFrameNum == hou.frame():
        pass
    elif blueFrameNum > hou.frame():
        while blueFrameNum > hou.frame():
            blueFrameNum -= 1
            if blueTrainStop == False:
                blueTrainSpeed -= speed
    elif blueFrameNum < hou.frame():
        while blueFrameNum < hou.frame():
            blueFrameNum += 1
            if blueTrainStop == False:
                blueTrainSpeed += speed
    return blueTrainSpeed
    
def setGreenTrainSpeed(speed):
    global greenTrainSpeed, greenFrameNum, greenTrainStop
    if greenFrameNum == hou.frame():
        pass
    elif greenFrameNum > hou.frame():
        while greenFrameNum > hou.frame():
            greenFrameNum -= 1
            if greenTrainStop == False:
                greenTrainSpeed -= speed
    elif greenFrameNum < hou.frame():
        while greenFrameNum < hou.frame():
            greenFrameNum += 1
            if greenTrainStop == False:
                greenTrainSpeed += speed
    return greenTrainSpeed

totalTrainsToCreate = 3
trainColors = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple', 'White', 'Black']

for trainNumber in range(totalTrainsToCreate):
    trainColor = trainColors[trainNumber]
    #CREATE THE INITIAL NODE FOR THE TRAIN
    geo = hou.node('/obj').createNode('geo', 'geo1', 0)

    trackCurve = geo.createNode('curve', 'curve1', 0)
    trackCurve.parm('coords').set(setXY(0,0) + ' ' + setXY(1,0) + ' ' + setXY(2,0) + ' ' + setXY(2,1) + ' ' + setXY(2,2) + ' ' + setXY(3,2) + ' ' + setXY(4,2) + ' ' + setXY(4,3) + ' ' + setXY(4,4) + ' ' + setXY(3,4) + ' ' + setXY(1,4) + ' ' + setXY(0,4) + ' ' + setXY(0,3) + ' ' + setXY(0,2) + ' ' + setXY(0,1))
    trackCurve.parm('type').set('nurbs')
    trackCurve.parm('close').set(1)

    transformCurve = geo.createNode('xform', 'transformCurve', 0)
    transformCurve.parm('sx').set('5')
    transformCurve.parm('sy').set('5')
    transformCurve.parm('sz').set('5')
    if trainNumber == 1:
        transformCurve.parm('ry').set('90')
        transformCurve.parm('tz').set('50')
    if trainNumber == 2:
        transformCurve.parm('ry').set('180')
        transformCurve.parm('tz').set('50')
        transformCurve.parm('tx').set('50')
    transformCurve.setInput(0, trackCurve, 0)

    resample1 = geo.createNode('resample', 'resample1', 0)
    resample1.parm('length').set('2.7')
    resample1.setInput(0, transformCurve, 0)

    orientCurve = geo.createNode('orientalongcurve', 'orientalongcurve1', 0)
    orientCurve.setInput(0, resample1, 0)

    fileCurve = geo.createNode('file', 'fileCurve', 0)
    fileCurve.parm('file').set('C:/Users/devon/OneDrive/Documents/Scripting for Animation/trainTrack(3units).fbx')
    #fileCurve.parm('file').set('C:/Users/dtennis/Downloads/trainCarUpdated(notProcedural).fbx')

    trackTransform = geo.createNode('xform', 'trackTransform', 0)
    trackTransform.parm('ty').set('-1.6')
    trackTransform.parm('sx').set('0.3')
    trackTransform.parm('sy').set('0.3')
    trackTransform.parm('sz').set('0.3')
    trackTransform.setInput(0, fileCurve, 0)

    copyToPoints = geo.createNode('copytopoints::2.0', 'copyToPoints', 0)
    copyToPoints.setInput(0, trackTransform, 0)
    copyToPoints.setInput(1, orientCurve, 0)


    trainFilePath = 'C:/Users/devon/OneDrive/Documents/Scripting for Animation/trainCarUpdated(notProcedural).fbx'

    #trainFilePath = 'C:/Users/dtennis/Downloads/trainCarUpdated(notProcedural).fbx'

    #CREATE TRAIN CARS AND ALL OF THEIR TRANSFORMS
    numTrainsToMake = 7
    trainArray = []
    trainOffset = 6.3
    trainPos = 0
    trainSize = 0.2
    for i in range(numTrainsToMake):
        trainCar = geo.createNode('file', 'file' + str(i), 0)
        trainCar.parm('file').set(trainFilePath)
        transform = geo.createNode('xform', 'xform' + str(i), 0)
        transform.parm('sx').set(str(trainSize))
        transform.parm('sy').set(str(trainSize))
        transform.parm('sz').set(str(trainSize))
        transform.parm('tz').set(str(trainPos))
        transform.setInput(0, trainCar, 0)
        trainArray.append(transform)
        trainPos += trainOffset

    #CREATE THE LOCATOR POINT TO FIND THE OTHER TRAINS
    trainFinder = geo.createNode('add', 'add1', 0)
    trainFinder.parm('points').set('1')
    trainFinder.parm('usept0').set('1')

    trainFinderAttribString = 'i@trainFinder = @ptnum; \ni@stop = 0;'

    trainFinderAttrib = geo.createNode('attribwrangle', 'attribwrangle1', 0)
    trainFinderAttrib.parm('snippet').setExpression(trainFinderAttribString)
    trainFinderAttrib.setInput(0, trainFinder, 0)
    
    xformTrainFinder = geo.createNode('xform', 'xformPoint', 0)
    xformTrainFinder.parm('tz').set(str(trainPos + 5))
    xformTrainFinder.setInput(0, trainFinderAttrib, 0)
    
    trainFinderGroup = geo.createNode('groupcreate', 'stoppingPoint' + trainColors[trainNumber], 0)
    trainFinderGroup.parm('grouptype').set('point')
    trainFinderGroup.setInput(0, xformTrainFinder, 0)

    #MERGE ALL OF THE TRAIN GEOMETRY
    trainCarMerge = geo.createNode('merge', trainColors[trainNumber] + 'TrainCarMerge', 0)
    for i in range(numTrainsToMake):
        trainCarMerge.setInput(i, trainArray[i], 0)
    trainCarMerge.setInput(numTrainsToMake, trainFinderGroup, 0)

    #ASSIGN THE TYPE OF TRAIN TO THE TRAIN
    trainTypeAttrib = geo.createNode('attribcreate', 'trainTypeAttrib', 0)
    trainTypeAttrib.setInput(0, trainCarMerge, 0)
    trainTypeAttrib.parm('name1').set('trainType')
    trainTypeAttrib.parm('type1').set('index')
    trainTypeAttrib.parm('string1').set(trainColors[trainNumber])

    #CREATE A GROUP CONTAINING ALL OF THE TRAIN GEOMETRY AND ASSIGN IT A TYPE
    trainGroup = geo.createNode('groupcreate', trainColors[trainNumber] + 'TrainGroup', 0)
    trainGroup.setInput(0, trainTypeAttrib, 0)
    trainGroup.parm('groupname').set(trainColors[trainNumber] + 'Train')
    trainGroup.parm('grouptype').set('point')

    #COLOR THE TRAIN
    trainColor = geo.createNode('color', trainColors[trainNumber], 'TrainColor', 0)
    if trainColors[trainNumber] == 'Blue' or trainColors[trainNumber] == 'Green':
        trainColor.parm('colorr').set('0')
    if trainColors[trainNumber] == 'Red' or trainColors[trainNumber] == 'Blue':
        trainColor.parm('colorg').set('0')
    if trainColors[trainNumber] == 'Red' or trainColors[trainNumber] == 'Green':
        trainColor.parm('colorb').set('0')
    trainColor.setInput(0, trainGroup, 0)

    #COMBINE THE TRAIN GEO WITH THE TRACK CURVE
    speed = 0
    if trainNumber == 0:
        speed = .01
    elif trainNumber == 1:
        speed = .015
    elif trainNumber == 2:
        speed = .02
    pathDeform = geo.createNode('pathdeform', 'pathdeform1', 0)
    pathDeform.setInput(0, trainColor, 0)
    pathDeform.setInput(1, transformCurve, 0)
    pathDeform.parm('curve_posoffset').setExpression('speed = ' + str(speed) + '\nreturn hou.session.set' + trainColors[trainNumber] + 'TrainSpeed(speed)', language = hou.exprLanguage.Python, replace_expression = True)

    #CONNECT THE TRAIN GEOMETRY WITH THE TRACK GEOMETRY
    trainGeoMerge = geo.createNode('merge', 'trainGeoMerge', 0)
    trainGeoMerge.setInput(0, pathDeform, 0)
    trainGeoMerge.setInput(1, copyToPoints, 0)
    trainGeoMerge.setDisplayFlag('on')

    #BRING IN THE OTHER TRAINS TO BE ABLE TO CHECK THEIR POINTS
    objectMerge = geo.createNode('object_merge', 'object_merge1', 0)
    if trainNumber == 0:
        objectMerge.parm('objpath1').set('/obj/geo2/trainGeoMerge')
    else:
        objectMerge.parm('objpath1').set('/obj/geo1/trainGeoMerge')
    #THE PATH IS SET FURTHER DOWN AFTER THE OTHER GEOMETRY NODES ARE CREATED

    #COMBINE THIS TRAIN GEO WITH ALL OTHER TRAIN GEO
    merge3 = geo.createNode('merge', 'merge3', 0)
    merge3.setInput(0, trainGeoMerge, 0)
    merge3.setInput(1, objectMerge, 0)

    #CHECK IF THE OTHER TRAINS ARE NEARBY
    pointWrangleExpression = ''
    if trainColors[trainNumber] == 'Red':
        pointWrangleExpression = 'i@newPoint = nearpoint(0, \'BlueTrain\', @P, 8); \nsetpointattrib(0, \'stop\', 18116, i@newPoint, \'set\');'
    elif trainColors[trainNumber] == 'Blue':
        pointWrangleExpression = 'i@newPoint = nearpoint(0, \'RedTrain\', @P, 8); \nsetpointattrib(0, \'stop\', 18116, i@newPoint, \'set\');'
    pointWrangle = geo.createNode('attribwrangle', 'pointwrangle' + trainColors[trainNumber], 0)
    pointWrangle.parm('group').set('stoppingPoint' + trainColors[trainNumber])
    pointWrangle.parm('snippet').setExpression(pointWrangleExpression)
    pointWrangle.setInput(0, merge3, 0)

    #SEND THE RESULT OF THE PREVIOUS NODE TO THE SOURCE EDITOR CODE
    trainPython = geo.createNode('python', trainColors[trainNumber] + 'TrainPython', 0)
    trainPython.setInput(0, pointWrangle, 0)
    trainPythonCode = 'node = hou.pwd() \ngeo = node.geometry() \nstopPoint = geo.point(18116) \ntrainMovement = stopPoint.attribValue(\'stop\') \nhou.session.set' + trainColors[trainNumber] + 'TrainMovement(trainMovement)'
    trainPython.parm('python').set(trainPythonCode)


#UP TO THIS POINT IT SETS THE GEOMETRY FOR ONE TRAIN TO MOVE AROUND A CURVE

    
