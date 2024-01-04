import hou

# Train settings
train_settings = [
    {"color": "Red", "speed": 0.2},
    {"color": "Blue", "speed": 0.1},
    {"color": "Green", "speed": 0.0}
]

def set_train_movement(color, movement):
    print(movement)
    global train_stop_flags
    train_stop_flags[color] = movement != -1

def set_train_speed(color, speed):
    global train_speeds, train_frame_nums, train_stop_flags
    if train_frame_nums[color] == hou.frame():
        return train_speeds[color]
    elif train_frame_nums[color] > hou.frame():
        while train_frame_nums[color] > hou.frame():
            train_frame_nums[color] -= 1
            if not train_stop_flags[color]:
                train_speeds[color] -= speed
    elif train_frame_nums[color] < hou.frame():
        while train_frame_nums[color] < hou.frame():
            train_frame_nums[color] += 1
            if not train_stop_flags[color]:
                train_speeds[color] += speed
    return train_speeds[color]

def set_xy(x, z):
    return f"{x * 5},0,{z * 5}"

def create_train_geometry(geo, color):
    # (Remaining code for creating train geometry)
    pass

def main():
    global train_speeds, train_frame_nums, train_stop_flags
    train_speeds = {color["color"]: color["speed"] for color in train_settings}
    train_frame_nums = {color["color"]: 1 for color in train_settings}
    train_stop_flags = {color["color"]: False for color in train_settings}

    total_trains_to_create = 3

    for train_number in range(total_trains_to_create):
        train_color = train_settings[train_number]["color"]

        # CREATE THE INITIAL NODE FOR THE TRAIN
        geo = hou.node('/obj').createNode('geo', 'geo1', 0)

        track_curve = geo.createNode('curve', 'curve1', 0)
        track_curve.parm('coords').set(
            set_xy(0, 0) + ' ' + set_xy(1, 0) + ' ' + set_xy(2, 0) + ' ' + set_xy(2, 1) + ' ' + set_xy(2, 2) +
            ' ' + set_xy(3, 2) + ' ' + set_xy(4, 2) + ' ' + set_xy(4, 3) + ' ' + set_xy(4, 4) + ' ' + set_xy(3, 4) +
            ' ' + set_xy(1, 4) + ' ' + set_xy(0, 4) + ' ' + set_xy(0, 3) + ' ' + set_xy(0, 2) + ' ' + set_xy(0, 1)
        )
        track_curve.parm('type').set('nurbs')
        track_curve.parm('close').set(1)

                transform_curve = geo.createNode('xform', 'transformCurve', 0)
        transform_curve.parm('sx').set('5')
        transform_curve.parm('sy').set('5')
        transform_curve.parm('sz').set('5')
        if train_number == 1:
            transform_curve.parm('ry').set('90')
            transform_curve.parm('tz').set('50')
        if train_number == 2:
            transform_curve.parm('ry').set('180')
            transform_curve.parm('tz').set('50')
            transform_curve.parm('tx').set('50')
        transform_curve.setInput(0, track_curve, 0)

        train_file_path = 'C:/Users/devon/OneDrive/Documents/Scripting for Animation/trainCarUpdated(notProcedural).fbx'

        for i in range(num_trains_to_make):
            train_car = geo.createNode('file', 'file' + str(i), 0)
            train_car.parm('file').set(train_file_path)
            transform = geo.createNode('xform', 'xform' + str(i), 0)
            transform.parm('sx').set(str(train_size))
            transform.parm('sy').set(str(train_size))
            transform.parm('sz').set(str(train_size))
            transform.parm('tz').set(str(train_pos))
            transform.setInput(0, train_car, 0)
            train_array.append(transform)
            train_pos += train_offset
        
        # CREATE THE LOCATOR POINT TO FIND THE OTHER TRAINS
        train_finder = geo.createNode('add', 'add1', 0)
        train_finder.parm('points').set('1')
        train_finder.parm('usept0').set('1')

        train_finder_attrib_string = 'i@trainFinder = @ptnum; \ni@stop = 0;'

        train_finder_attrib = geo.createNode('attribwrangle', 'attribwrangle1', 0)
        train_finder_attrib.parm('snippet').setExpression(train_finder_attrib_string)
        train_finder_attrib.setInput(0, train_finder, 0)

        xform_train_finder = geo.createNode('xform', 'xformPoint', 0)
        xform_train_finder.parm('tz').set(str(train_pos + 5))
        xform_train_finder.setInput(0, train_finder_attrib, 0)

        train_finder_group = geo.createNode('groupcreate', 'stoppingPoint' + train_color, 0)
        train_finder_group.parm('grouptype').set('point')
        train_finder_group.setInput(0, xform_train_finder, 0)

        # MERGE ALL OF THE TRAIN GEOMETRY
        train_car_merge = geo.createNode('merge', train_color + 'TrainCarMerge', 0)
        for i in range(num_trains_to_make):
            train_car_merge.setInput(i, train_array[i], 0)
        train_car_merge.setInput(num_trains_to_make, train_finder_group, 0)

        # COLOR THE TRAIN
        train_color_node = geo.createNode('color', train_color, 'TrainColor', 0)
        if train_color == 'Blue' or train_color == 'Green':
            train_color_node.parm('colorr').set('0')
        if train_color == 'Red' or train_color == 'Blue':
            train_color_node.parm('colorg').set('0')
        if train_color == 'Red' or train_color == 'Green':
            train_color_node.parm('colorb').set('0')
        train_color_node.setInput(0, train_group, 0)

        # COMBINE THE TRAIN GEO WITH THE TRACK CURVE
        speed = 0
        if train_number == 0:
            speed = 0.01
        elif train_number == 1:
            speed = 0.015
        elif train_number == 2:
            speed = 0.02
        path_deform = geo.createNode('pathdeform', 'pathdeform1', 0)
        path_deform.setInput(0, train_color_node, 0)
        path_deform.setInput(1, transform_curve, 0)
        path_deform.parm('curve_posoffset').setExpression(
            f'speed = {speed}\nreturn hou.session.set{train_color}TrainSpeed(speed)',
            language=hou.exprLanguage.Python,
            replace_expression=True
        )

        # CONNECT THE TRAIN GEOMETRY WITH THE TRACK GEOMETRY
        train_geo_merge = geo.createNode('merge', 'trainGeoMerge', 0)
        train_geo_merge.setInput(0, path_deform, 0)
        train_geo_merge.setInput(1, copy_to_points, 0)
        train_geo_merge.setDisplayFlag('on')

        # BRING IN THE OTHER TRAINS TO BE ABLE TO CHECK THEIR POINTS
        object_merge = geo.createNode('object_merge', 'object_merge1', 0)
        if train_number == 0:
            object_merge.parm('objpath1').set('/obj/geo2/trainGeoMerge')
        else:
            object_merge.parm('objpath1').set('/obj/geo1/trainGeoMerge')

        # (Remaining code for creating and connecting other nodes)

        # COMBINE THIS TRAIN GEO WITH ALL OTHER TRAIN GEO
        merge3 = geo.createNode('merge', 'merge3', 0)
        merge3.setInput(0, train_geo_merge, 0)
        merge3.setInput(1, object_merge, 0)

        # CHECK IF THE OTHER TRAINS ARE NEARBY
        point_wrangle_expression = ''
        if train_color == 'Red':
            point_wrangle_expression = 'i@newPoint = nearpoint(0, \'BlueTrain\', @P, 8); ' \
                                       '\nsetpointattrib(0, \'stop\', 18116, i@newPoint, \'set\');'
        elif train_color == 'Blue':
            point_wrangle_expression = 'i@newPoint = nearpoint(0, \'RedTrain\', @P, 8); ' \
                                       '\nsetpointattrib(0, \'stop\', 18116, i@newPoint, \'set\');'
        point_wrangle = geo.createNode('attribwrangle', 'pointwrangle' + train_color, 0)
        point_wrangle.parm('group').set('stoppingPoint' + train_color)
        point_wrangle.parm('snippet').setExpression(point_wrangle_expression)
        point_wrangle.setInput(0, merge3, 0)

        # SEND THE RESULT OF THE PREVIOUS NODE TO THE SOURCE EDITOR CODE
        train_python = geo.createNode('python', train_color + 'TrainPython', 0)
        train_python.setInput(0, point_wrangle, 0)
        train_python_code = f'node = hou.pwd() \ngeo = node.geometry() ' \
                            f'\nstopPoint = geo.point(18116) \ntrainMovement = stopPoint.attribValue(\'stop\') ' \
                            f'\nhou.session.set{train_color}TrainMovement(trainMovement)'
        train_python.parm('python').set(train_python_code)

        create_train_geometry(geo, train_color)

if __name__ == "__main__":
    main()
