from fullcontrol.gcode import Point, Printer, Extruder, ManualGcode, PrinterCommand, Buildplate, Hotend, Fan, StationaryExtrusion
import fullcontrol.gcode.printer_library.singletool.base_settings as base_settings


def set_up(user_overrides: dict):
    ''' DO THIS
    '''

    # overrides for this specific printer relative those defined in base_settings.py
    printer_overrides = {'e_units': 'mm', 'dia_feed': 14.5, 'primer': 'no_primer'}
    # update default initialization settings based on the printer-specific overrides and user-defined overrides
    initialization_data = {**base_settings.default_initial_settings, **printer_overrides}
    initialization_data = {**initialization_data, **user_overrides}

    starting_procedure_steps = []
    starting_procedure_steps.append(ManualGcode(
        text='; Time to print!!!!!\n; GCode created with FullControl\n; Printing silicone we are jiaolao\n; LYX'))
    starting_procedure_steps.append(Buildplate(temp=initialization_data["bed_temp"], wait=False))
    starting_procedure_steps.append(Hotend(temp=initialization_data["nozzle_temp"], wait=False))
    starting_procedure_steps.append(Buildplate(temp=initialization_data["bed_temp"], wait=True))
    starting_procedure_steps.append(Hotend(temp=initialization_data["nozzle_temp"], wait=True))
    starting_procedure_steps.append(PrinterCommand(id='absolute_coords'))
    starting_procedure_steps.append(PrinterCommand(id='units_mm'))
    starting_procedure_steps.append(ManualGcode(text='G90        ;absolute positioning'))
    starting_procedure_steps.append(ManualGcode(text='G1 Z100.0 F1800'))
    starting_procedure_steps.append(ManualGcode(text='G28 X0 Y0  ;move X/Y to min endstops'))
    starting_procedure_steps.append(ManualGcode(text='G28 Z0  ;move Z to min endstops'))
    starting_procedure_steps.append(ManualGcode(text='G1 Z100.0 F1800 ;move the platform down 15mm'))
    starting_procedure_steps.append(ManualGcode(text='G1 X150 Y150  ;go to the center'))
    starting_procedure_steps.append(ManualGcode(text='M117 Printing...'))
    starting_procedure_steps.append(ManualGcode(text='G92 E0\nM107\nM204 S20\nM205 X10 Y10'))
    starting_procedure_steps.append(ManualGcode(text='M82 ;absolute extrusion mode'))
    starting_procedure_steps.append(Extruder(relative_gcode=initialization_data["relative_e"]))
    starting_procedure_steps.append(Fan(speed_percent=initialization_data["fan_percent"]))
    # starting_procedure_steps.append(ManualGcode(
    #     text='M220 S' + str(initialization_data["print_speed_percent"])+' ; set speed factor override percentage'))
    # starting_procedure_steps.append(ManualGcode(
    #     text='M221 S' + str(initialization_data["material_flow_percent"])+' ; set extrude factor override percentage'))
    # starting_procedure_steps.append(Extruder(on=False))
    # starting_procedure_steps.append(Point(x=5, y=5, z=10))
    # starting_procedure_steps.append(Point(x=10.0, y=10.0, z=0.3))
    starting_procedure_steps.append(Extruder(on=True))
    starting_procedure_steps.append(ManualGcode(text=';-----\n; END OF STARTING PROCEDURE\n;-----\n'))

    ending_procedure_steps = []
    ending_procedure_steps.append(ManualGcode(text='\n;-----\n; START OF ENDING PROCEDURE\n;-----'))
    ending_procedure_steps.append(ManualGcode(text='M204 S4000\nM205 X20 Y20'))
    ending_procedure_steps.append(ManualGcode(text='G90     ;absolute positioning'))
    ending_procedure_steps.append(ManualGcode(text='G1 Z100.0 F1000'))
    ending_procedure_steps.append(ManualGcode(text='G28 X0 Y0  ;move X/Y to min endstops'))
    ending_procedure_steps.append(ManualGcode(text='G92 E0\nG1 E0.35 F20'))
    ending_procedure_steps.append(ManualGcode(text='M84      ;steppers off\nM82 ;absolute extrusion mode'))
    ending_procedure_steps.append(ManualGcode(text='\n; This GCode is just padding because some printer firmwares need it'*2))

    initialization_data['starting_procedure_steps'] = starting_procedure_steps
    initialization_data['ending_procedure_steps'] = ending_procedure_steps

    return initialization_data
