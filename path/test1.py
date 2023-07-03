import fullcontrol as fc

steps = []
layer_height = 0.4
steps.append(fc.Extruder(extrusion_rate=0.04))
steps.append(fc.Extruder(relative_gcode=False))
steps.append(fc.Point(x=89.9, y=109.9))
for j in range(5):
    steps.append(fc.Point(x=89.9, y=109.9, z=1 + j * layer_height))
    steps.append((fc.Point(x=210.1, y=109.9)))
    for i in range(17):
        steps.append(fc.Point(x=210.1 - 120.2 * (i % 2), y=109.9 + 0.3 * (i + 1)))
        steps.append(fc.Point(x=89.9 + 120.2 * (i % 2), y=109.9 + 0.3 * (i + 1)))

    steps.append(fc.Point(x=89.9, y=190.1))

    for i in range(16):
        steps.append(fc.Point(x=89.9 + 0.3 * (i + 1), y=190.1 - 75.1 * (i % 2)))
        steps.append(fc.Point(x=89.9 + 0.3 * (i + 1), y=115 + 75.1 * (i % 2)))

    steps.append(fc.Point(x=210.1, y=190.1))

    for i in range(16):
        steps.append(fc.Point(x=210.1 - 115.4 * (i % 2), y=190.1 - 0.3 * (i + 1)))
        steps.append(fc.Point(x=94.7 + 115.4 * (i % 2), y=190.1 - 0.3 * (i + 1)))

    steps.append(fc.Point(x=210.1, y=115))

    for i in range(16):
        steps.append(fc.Point(x=210.1 - 0.3 * (i + 1), y=115 + 70.3 * (i % 2)))
        steps.append(fc.Point(x=210.1 - 0.3 * (i + 1), y=185.3 - 70.3 * (i % 2)))

    if j == 0:
        steps.append(fc.Point(x=205, y=192))
        for i in range(21):
            steps.append(fc.Point(x=205 - 5 * (i + 1), y=192 - 84 * (i % 2)))
            steps.append(fc.Point(x=205 - 5 * (i + 1), y=108 + 84 * (i % 2)))

    steps.extend(fc.travel_to(fc.Point(x=89.9, y=109.9, z=1 + j * layer_height)))

filename = 'my_design'
printer = 'siliconePrinter1'
# printer options: generic, ultimaker2plus, prusa_i3, ender_3, cr_10, bambulab_x1,
# toolchanger_T0, toolchanger_T1, toolchanger_T2, toolchanger_T3
print_settings = {'extrusion_width': 0.3, 'extrusion_height': 0.4, 'nozzle_temp': 0, 'bed_temp': 0, 'fan_percent': 0}

fc.transform(steps, 'gcode',
             fc.GcodeControls(printer_name=printer, save_as=filename, initialization_data=print_settings))
