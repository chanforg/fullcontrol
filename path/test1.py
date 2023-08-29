import fullcontrol as fc

steps = []
layer_height = 0.4
steps.append(fc.Extruder(extrusion_rate=0.20))
steps.append(fc.Extruder(relative_gcode=False))
steps.append(fc.Printer(print_speed=600, travel_speed=1000))
steps.append(fc.Extruder(on=False))
steps.append(fc.Point(x=105, y=130))
steps.append(fc.Point(x=105, y=130, z=0.5))
steps.append(fc.Extruder(on=True))
for j in range(10):
    steps.append(fc.Point(x=105, y=130, z=0.5 + j * layer_height))
    steps.append((fc.Point(x=105, y=170)))
    for i in range(51):
        steps.append(fc.Point(x=105 + 0.3 * (i + 1), y=170 - 40 * (i % 2)))
        steps.append(fc.Point(x=105 + 0.3 * (i + 1), y=130 + 40 * (i % 2)))

    steps.extend(fc.travel_to(fc.Point(x=105, y=130, z=0.5 + j * layer_height)))
steps.append(fc.Extruder(on=False))
steps.append(fc.Point(x=105, y=130, z=5))
steps.append(fc.Point(x=125, y=130))
steps.append(fc.Point(x=125, y=130, z=0.5))
steps.append(fc.Extruder(on=True))
for j in range(2):
    steps.append(fc.Point(x=125, y=130, z=0.5 + j * layer_height))
    steps.append((fc.Point(x=175, y=130)))
    for i in range(7):
        steps.append(fc.Point(x=175 - 50 * (i % 2), y=130 + 0.3 * (i + 1)))
        steps.append(fc.Point(x=125 + 50 * (i % 2), y=130 + 0.3 * (i + 1)))

    steps.append(fc.Point(x=125, y=170))

    for i in range(6):
        steps.append(fc.Point(x=125 + 0.3 * (i + 1), y=170 - 37.9 * (i % 2)))
        steps.append(fc.Point(x=125 + 0.3 * (i + 1), y=132.1 + 37.9 * (i % 2)))

    steps.append(fc.Point(x=175, y=170))

    for i in range(6):
        steps.append(fc.Point(x=175 - 48.2 * (i % 2), y=170 - 0.3 * (i + 1)))
        steps.append(fc.Point(x=126.8 + 48.2 * (i % 2), y=170 - 0.3 * (i + 1)))

    steps.append(fc.Point(x=175, y=132.1))

    for i in range(6):
        steps.append(fc.Point(x=175 - 0.3 * (i + 1), y=132.1 + 36.1 * (i % 2)))
        steps.append(fc.Point(x=175 - 0.3 * (i + 1), y=168.2 - 36.1 * (i % 2)))

    if j == 0:
        steps.append(fc.Point(x=173.2, y=172))
        for i in range(15):
            steps.append(fc.Point(x=173.2 - 3 * (i + 1), y=172 - 44 * (i % 2)))
            steps.append(fc.Point(x=173.2 - 3 * (i + 1), y=128 + 44 * (i % 2)))

    steps.extend(fc.travel_to(fc.Point(x=125, y=130, z=0.5 + j * layer_height)))

for j in range(2):
    steps.append(fc.Point(x=125, y=130, z=3 + j * layer_height))
    steps.append((fc.Point(x=175, y=130)))
    for i in range(7):
        steps.append(fc.Point(x=175 - 50 * (i % 2), y=130 + 0.3 * (i + 1)))
        steps.append(fc.Point(x=125 + 50 * (i % 2), y=130 + 0.3 * (i + 1)))

    steps.append(fc.Point(x=125, y=170))

    for i in range(6):
        steps.append(fc.Point(x=125 + 0.3 * (i + 1), y=170 - 37.9 * (i % 2)))
        steps.append(fc.Point(x=125 + 0.3 * (i + 1), y=132.1 + 37.9 * (i % 2)))

    steps.append(fc.Point(x=175, y=170))

    for i in range(6):
        steps.append(fc.Point(x=175 - 48.2 * (i % 2), y=170 - 0.3 * (i + 1)))
        steps.append(fc.Point(x=126.8 + 48.2 * (i % 2), y=170 - 0.3 * (i + 1)))

    steps.append(fc.Point(x=175, y=132.1))

    for i in range(6):
        steps.append(fc.Point(x=175 - 0.3 * (i + 1), y=132.1 + 36.1 * (i % 2)))
        steps.append(fc.Point(x=175 - 0.3 * (i + 1), y=168.2 - 36.1 * (i % 2)))

    if j == 0:
        steps.append(fc.Point(x=173.2, y=172))
        for i in range(15):
            steps.append(fc.Point(x=173.2 - 3 * (i + 1), y=172 - 44 * (i % 2)))
            steps.append(fc.Point(x=173.2 - 3 * (i + 1), y=128 + 44 * (i % 2)))

    steps.extend(fc.travel_to(fc.Point(x=125, y=130, z=3 + j * layer_height)))

filename = 'my_design'
printer = 'siliconePrinter1'
# printer options: generic, ultimaker2plus, prusa_i3, ender_3, cr_10, bambulab_x1,
# toolchanger_T0, toolchanger_T1, toolchanger_T2, toolchanger_T3
print_settings = {'extrusion_width': 0.3, 'extrusion_height': 0.4, 'nozzle_temp': 0, 'bed_temp': 0, 'fan_percent': 0}

fc.transform(steps, 'gcode',
             fc.GcodeControls(printer_name=printer, save_as=filename, initialization_data=print_settings))
