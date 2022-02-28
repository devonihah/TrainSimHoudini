#HOUDINI MAKE TRACK CODE
import hou
import sys
import random as rand

redTrainSpeed = 0.0
redTrainStop = True
frameNum = 1

redTrainNull = hou.node('/obj').createNode('null', 'null1', 0)

def setTrainMovement(movement):
    print(movement)
    global redTrainStop
    print(str(redTrainStop))
    #if movement == -1:
    #    redTrainStop = False
    #else:
    #    redTrainStop = True

def setXY(x, z):
    x *= 10
    z *= 10
    return str(x) + ',0,' + str(z)

def setFrame():
    frame = hou.frame()
    while frame > 200:
        frame -= 200
    frame /= 100
    return frame
    
def setRedTrainSpeed(speed):
    frameNum = float(redTrainNull.parm('rx').eval())
    redTrainSpeed = float(redTrainNull.parm('ry').eval())
    global redTrainSpeed, frameNum, redTrainStop
    if frameNum == hou.frame():
        pass
    elif frameNum > hou.frame():
        while frameNum > hou.frame():
            frameNum -= 1
            #if redtrainStop == False:
            redTrainSpeed -= speed
    elif frameNum < hou.frame():
        while frameNum < hou.frame():
            frameNum += 1
            #if redTrainStop == False:
            redTrainSpeed += speed
    redTrainNull.parm('rx').set(frameNum)
    redTrainNull.parm('ry').set(redTrainSpeed)
    return redTrainSpeed


totalTrainsToCreate = 2
trainColors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'white', 'black']


geo = hou.node('/obj').createNode('geo', 'geo1', 0)

curve = geo.createNode('curve', 'curve1', 0)
curve.parm('coords').set(setXY(0,0) + ' ' + setXY(1,0) + ' ' + setXY(1,1) + ' ' + setXY(2,1) + ' ' + setXY(2,2) + ' ' + setXY(0,2) + ' ' + setXY(0,1))
curve.parm('type').set('nurbs')
curve.parm('close').set(1)

transformCurve = geo.createNode('xform', 'transformCurve', 0)
transformCurve.parm('sx').set('5')
transformCurve.parm('sy').set('5')
transformCurve.parm('sz').set('5')
transformCurve.setInput(0, curve, 0)

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




#boxGeo = geo.createNode('box', 'box1', 0)

trainFilePath = 'C:/Users/devon/OneDrive/Documents/Scripting for Animation/trainCarUpdated(notProcedural).fbx'

#trainFilePath = 'C:/Users/dtennis/Downloads/trainCarUpdated(notProcedural).fbx'

#CREATE TRAIN CARS AND ALL OF THEIR TRANSFORMS
numTrainsToMake = 7
redTrainArray = []
redTrainOffset = 6.3
redTrainPos = 0
redTrainSize = 0.2
for i in range(numTrainsToMake):
    trainCar = geo.createNode('file', 'file' + str(i), 0)
    trainCar.parm('file').set(trainFilePath)
    transform = geo.createNode('xform', 'xform' + str(i), 0)
    transform.parm('sx').set(str(redTrainSize))
    transform.parm('sy').set(str(redTrainSize))
    transform.parm('sz').set(str(redTrainSize))
    transform.parm('tz').set(str(redTrainPos))
    transform.setInput(0, trainCar, 0)
    redTrainArray.append(transform)
    redTrainPos += redTrainOffset

trainCar1 = geo.createNode('file', 'file1', 0)
trainCar1.parm('file').set(trainFilePath)
transform1 = geo.createNode('xform', 'transform1', 0)
transform1.parm('sx').set('0.2')
transform1.parm('sy').set('0.2')
transform1.parm('sz').set('0.2')
transform1.parm('tz').set('31.5')
transform1.setInput(0, trainCar1, 0)

trainCar2 = geo.createNode('file', 'file2', 0)
trainCar2.parm('file').set(trainFilePath)
transform2 = geo.createNode('xform', 'transform2', 0)
transform2.parm('sx').set('0.2')
transform2.parm('sy').set('0.2')
transform2.parm('sz').set('0.2')
transform2.parm('tz').set('25.2')
transform2.setInput(0, trainCar2, 0)

trainCar3 = geo.createNode('file', 'file3', 0)
trainCar3.parm('file').set(trainFilePath)
transform3 = geo.createNode('xform', 'transform3', 0)
transform3.parm('sx').set('0.2')
transform3.parm('sy').set('0.2')
transform3.parm('sz').set('0.2')
transform3.parm('tz').set('12.6')
transform3.setInput(0, trainCar3, 0)

trainCar4 = geo.createNode('file', 'file4', 0)
trainCar4.parm('file').set(trainFilePath)
transform4 = geo.createNode('xform', 'transform4', 0)
transform4.parm('sx').set('0.2')
transform4.parm('sy').set('0.2')
transform4.parm('sz').set('0.2')
transform4.parm('tz').set('6.3')
transform4.setInput(0, trainCar4, 0)

trainCar5 = geo.createNode('file', 'file5', 0)
trainCar5.parm('file').set(trainFilePath)
transform5 = geo.createNode('xform', 'transform5', 0)
transform5.parm('sx').set('0.2')
transform5.parm('sy').set('0.2')
transform5.parm('sz').set('0.2')
transform5.parm('tz').set('0')
transform5.setInput(0, trainCar5, 0)

trainCar6 = geo.createNode('file', 'file6', 0)
trainCar6.parm('file').set(trainFilePath)
transform6 = geo.createNode('xform', 'transform6', 0)
transform6.parm('sx').set('0.2')
transform6.parm('sy').set('0.2')
transform6.parm('sz').set('0.2')
transform6.parm('tz').set('37.8')
transform6.setInput(0, trainCar6, 0)

trainCar7 = geo.createNode('file', 'file7', 0)
trainCar7.parm('file').set(trainFilePath)
transform7 = geo.createNode('xform', 'transform7', 0)
transform7.parm('sx').set('0.2')
transform7.parm('sy').set('0.2')
transform7.parm('sz').set('0.2')
transform7.parm('tz').set('18.9')
transform7.setInput(0, trainCar7, 0)

trainFinderRed = geo.createNode('add', 'add1', 0)
trainFinderRed.parm('points').set('1')
trainFinderRed.parm('usept0').set('1')

trainFinderAttribString = 'i@trainFinder = @ptnum; \ni@stop = 0;'

trainFinderAttrib = geo.createNode('attribwrangle', 'attribwrangle1', 0)
trainFinderAttrib.parm('snippet').setExpression(trainFinderAttribString)
trainFinderAttrib.setInput(0, trainFinderRed, 0)

xformTrainFinder = geo.createNode('xform', 'xformPoint', 0)
xformTrainFinder.parm('tz').set(str(redTrainOffset + 5)
xformTrainFinder.setInput(0, trainFinderAttrib, 0)

trainFinderGroup = geo.createNode('groupcreate', 'stoppingPointRed', 0)
trainFinderGroup.parm('grouptype').set('point')
trainFinderGroup.setInput(0, xformTrainFinder, 0)

merge1 = geo.createNode('merge', 'merge1', 0)
for i in range(numTrainsToMake):
    merge1.setInput(i, redTrainArray[i], 0)
merg1.setInput(numTrainsToMake, trainFinderGroup, 0)

merge1.setInput(0, transform1, 0)
merge1.setInput(1, transform2, 0)
merge1.setInput(2, transform3, 0)
merge1.setInput(3, transform4, 0)
merge1.setInput(4, transform5, 0)
merge1.setInput(5, transform6, 0)
merge1.setInput(6, transform7, 0)
merge1.setInput(7, trainFinderGroup, 0)

trainTypeAttrib = geo.createNode('attribcreate', 'attribcreate1', 0)
trainTypeAttrib.setInput(0, merge1, 0)
trainTypeAttrib.parm('name1').set('trainType')
trainTypeAttrib.parm('type1').set('index')
trainTypeAttrib.parm('string1').set('red')

redTrainGroup = geo.createNode('groupcreate', 'group2', 0)
redTrainGroup.setInput(0, trainTypeAttrib, 0)
redTrainGroup.parm('groupname').set('redTrain')

pathDeform = geo.createNode('pathdeform', 'pathdeform1', 0)
pathDeform.setInput(0, redTrainGroup, 0)
pathDeform.setInput(1, transformCurve, 0)
pathDeform.parm('curve_posoffset').setExpression('speed = .01\nreturn hou.session.setRedTrainSpeed(speed)', language = hou.exprLanguage.Python, replace_expression = True)


#trainTypeAttrib.createPointGroup('blueTrainPoints')

merge2 = geo.createNode('merge', 'merge2', 0)
merge2.setInput(0, pathDeform, 0)
merge2.setInput(1, copyToPoints, 0)
merge2.setDisplayFlag('on')

objectMerge = geo.createNode('object_merge', 'object_merge1', 0)

merge3 = geo.createNode('merge', 'merge3', 0)
merge3.setInput(0, merge2, 0)
merge3.setInput(1, objectMerge, 0)

pointWrangleRedExpression = 'i@newPoint = nearpoint(0, \'blueTrain\', @P, 30); \nsetpointattrib(0, \'stop\', 18116, i@newPoint, \'set\');'
pointWrangleRed = geo.createNode('attribwrangle', 'pointwrangleRed', 0)
pointWrangleRed.parm('group').set('stoppingPointRed')
pointWrangleRed.parm('snippet').setExpression(pointWrangleRedExpression)
pointWrangleRed.setInput(0, merge3, 0)

redTrainPython = geo.createNode('python', 'redTrainPython', 0)
redTrainPython.setInput(0, pointWrangleRed, 0)
redTrainPythonCode = 'node = hou.pwd() \ngeo = node.geometry() \nstopPoint = geo.point(18116) \ntrainMovement = stopPoint.attribValue(\'stop\') \nhou.session.setTrainMovement(trainMovement)'
redTrainPython.parm('python').set(redTrainPythonCode)


geo2 = hou.node('/obj').createNode('geo', 'geo2', 0)


curve = geo2.createNode('curve', 'curve1', 0)
curve.parm('coords').set(setXY(0,0) + ' ' + setXY(1,0) + ' ' + setXY(1,1) + ' ' + setXY(2,1) + ' ' + setXY(2,2) + ' ' + setXY(0,2) + ' ' + setXY(0,1))
curve.parm('type').set('nurbs')
curve.parm('close').set(1)

transformCurve = geo2.createNode('xform', 'transformCurve', 0)
transformCurve.parm('sx').set('5')
transformCurve.parm('sy').set('5')
transformCurve.parm('sz').set('5')
transformCurve.parm('ry').set('90')
transformCurve.parm('tz').set('50')
transformCurve.setInput(0, curve, 0)

resample1 = geo2.createNode('resample', 'resample1', 0)
resample1.parm('length').set('2.7')
resample1.setInput(0, transformCurve, 0)

orientCurve = geo2.createNode('orientalongcurve', 'orientalongcurve1', 0)
orientCurve.setInput(0, resample1, 0)

fileCurve = geo2.createNode('file', 'fileCurve', 0)
fileCurve.parm('file').set('C:/Users/devon/OneDrive/Documents/Scripting for Animation/trainTrack(3units).fbx')

#fileCurve.parm('file').set('C:/Users/dtennis/Downloads/trainTrack(3units).fbx')

trackTransform = geo2.createNode('xform', 'trackTransform', 0)
trackTransform.parm('ty').set('-1.6')
trackTransform.parm('sx').set('0.3')
trackTransform.parm('sy').set('0.3')
trackTransform.parm('sz').set('0.3')
trackTransform.setInput(0, fileCurve, 0)

copyToPoints = geo2.createNode('copytopoints::2.0', 'copyToPoints', 0)
copyToPoints.setInput(0, trackTransform, 0)
copyToPoints.setInput(1, orientCurve, 0)




#boxGeo = geo.createNode('box', 'box1', 0)

trainFilePath = 'C:/Users/devon/OneDrive/Documents/Scripting for Animation/trainCarUpdated(notProcedural).fbx'

#trainFilePath = 'C:/Users/dtennis/Downloads/trainCarUpdated(notProcedural).fbx'


#CREATE TRAIN CARS AND ALL OF THEIR TRANSFORMS

trainCar1 = geo2.createNode('file', 'file1', 0)
trainCar1.parm('file').set(trainFilePath)
transform1 = geo2.createNode('xform', 'transform1', 0)
transform1.parm('sx').set('0.2')
transform1.parm('sy').set('0.2')
transform1.parm('sz').set('0.2')
transform1.parm('tz').set('31.5')
transform1.setInput(0, trainCar1, 0)

trainCar2 = geo2.createNode('file', 'file2', 0)
trainCar2.parm('file').set(trainFilePath)
transform2 = geo2.createNode('xform', 'transform2', 0)
transform2.parm('sx').set('0.2')
transform2.parm('sy').set('0.2')
transform2.parm('sz').set('0.2')
transform2.parm('tz').set('25.2')
transform2.setInput(0, trainCar2, 0)

trainCar3 = geo2.createNode('file', 'file3', 0)
trainCar3.parm('file').set(trainFilePath)
transform3 = geo2.createNode('xform', 'transform3', 0)
transform3.parm('sx').set('0.2')
transform3.parm('sy').set('0.2')
transform3.parm('sz').set('0.2')
transform3.parm('tz').set('12.6')
transform3.setInput(0, trainCar3, 0)

trainCar4 = geo2.createNode('file', 'file4', 0)
trainCar4.parm('file').set(trainFilePath)
transform4 = geo2.createNode('xform', 'transform4', 0)
transform4.parm('sx').set('0.2')
transform4.parm('sy').set('0.2')
transform4.parm('sz').set('0.2')
transform4.parm('tz').set('6.3')
transform4.setInput(0, trainCar4, 0)

trainCar5 = geo2.createNode('file', 'file5', 0)
trainCar5.parm('file').set(trainFilePath)
transform5 = geo2.createNode('xform', 'transform5', 0)
transform5.parm('sx').set('0.2')
transform5.parm('sy').set('0.2')
transform5.parm('sz').set('0.2')
transform5.parm('tz').set('0')
transform5.setInput(0, trainCar5, 0)

trainCar6 = geo2.createNode('file', 'file6', 0)
trainCar6.parm('file').set(trainFilePath)
transform6 = geo2.createNode('xform', 'transform6', 0)
transform6.parm('sx').set('0.2')
transform6.parm('sy').set('0.2')
transform6.parm('sz').set('0.2')
transform6.parm('tz').set('37.8')
transform6.setInput(0, trainCar6, 0)

trainCar7 = geo2.createNode('file', 'file7', 0)
trainCar7.parm('file').set(trainFilePath)
transform7 = geo2.createNode('xform', 'transform7', 0)
transform7.parm('sx').set('0.2')
transform7.parm('sy').set('0.2')
transform7.parm('sz').set('0.2')
transform7.parm('tz').set('18.9')
transform7.setInput(0, trainCar7, 0)


merge1 = geo2.createNode('merge', 'merge1', 0)
merge1.setInput(0, transform1, 0)
merge1.setInput(1, transform2, 0)
merge1.setInput(2, transform3, 0)
merge1.setInput(3, transform4, 0)
merge1.setInput(4, transform5, 0)
merge1.setInput(5, transform6, 0)
merge1.setInput(6, transform7, 0)

trainTypeAttrib = geo2.createNode('attribcreate', 'attribcreate1', 0)
trainTypeAttrib.setInput(0, merge1, 0)

blueTrainGroup = geo2.createNode('groupcreate', 'group2', 0)
blueTrainGroup.setInput(0, trainTypeAttrib, 0)
blueTrainGroup.parm('groupname').set('blueTrain')

pointWrangle = geo2.createNode('pointwrangle', 'pointwrangle1', 0)
pointWrangle.setInput(0, blueTrainGroup, 0)

pathDeform = geo2.createNode('pathdeform', 'pathdeform1', 0)
pathDeform.setInput(0, pointWrangle, 0)
pathDeform.setInput(1, transformCurve, 0)
pathDeform.parm('curve_posoffset').setExpression('speed = .01\nreturn hou.session.setRedTrainSpeed(speed)', language = hou.exprLanguage.Python, replace_expression = True)

trainTypeAttrib.parm('name1').set('trainType')
trainTypeAttrib.parm('type1').set('index')
trainTypeAttrib.parm('string1').set('blue')
#trainTypeAttrib.createPointGroup('blueTrainPoints')



merge2 = geo2.createNode('merge', 'merge2', 0)
merge2.setInput(0, pathDeform, 0)
merge2.setInput(1, copyToPoints, 0)
merge2.setDisplayFlag('on')

#this sets the right kind of filepath for the objectmerge node in the red train
objectMerge.parm('objpath1').set('/obj/geo2')
#C:\Users\devon\OneDrive\Documents\Scripting for Animation

#UP TO THIS POINT IT SETS THE GEOMETRY FOR ONE TRAIN TO MOVE AROUND A CURVE
