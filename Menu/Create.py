import maya.cmds as cmds
import maya.mel as mel
import Rig
from Rig.Tools import reference_tools
from Rig.Tools import constructor_tools
from Rig.Tools import rig_root, rig_torso, rig_arm, rig_leg, rig_finger, rig_sdk_finger, rig_neck
from System.file_handle import file_dialog_yaml as fd
from System.file_handle import export_curve, import_curve


def Menu():
    menu_name = 'AutoRigger'
    main_window = mel.eval('$x = $gMainWindow')

    if cmds.menu(menu_name, exists=True):
        cmds.menu(menu_name, e=True, dai=True)
    else:
        cmds.setParent(main_window)
        cmds.menu(menu_name, p=main_window, l=menu_name, tearOff=True, allowOptionBoxes=True)

    cmds.setParent(menu_name, menu=True)

    # Reference Menu
    cmds.menuItem('reference', p=menu_name, l='Reference', subMenu=True, tearOff=True)

    # Reference Menu -- Actions
    cmds.menuItem(p='reference', l='Save Reference Data', stp='python',
                  c=lambda *args: reference_tools.joint_reference_save(),
                  ann='Save Reference Joints into YAML')

    cmds.menuItem(p='reference', l='Load Reference Data', stp='python',
                  c=lambda *args: reference_tools.joint_reference_create(fd("Load joint reference", mode="r")),
                  ann='Load Reference Joints from file')

    cmds.menuItem(p='reference', l='Load Template', stp='python',
                  c=lambda *args: reference_tools.joint_reference_create(reference_tools.load_template_file()),
                  ann='Load a template rig structure')

    # Rig builder
    cmds.menuItem('builder', p=menu_name, l='Builder', subMenu=True, tearOff=True)

    # Rig build -- Main Action
    cmds.menuItem(p='builder', l='Build rig', stp='python',
                  c=lambda *args: build_rig(),
                  ann='Generates the complete rig based on reference joints')

    # Rig build -- Step by step actions
    cmds.menuItem('steps', p='builder', l='Step by step', subMenu=True, tearOff=True)

    cmds.menuItem(p='steps', l='Create deform', stp='python',
                  c=lambda *args: constructor_tools.create_deform_rig(),
                  ann='Creates a complete deformation rig')

    cmds.menuItem(p='steps', l='Create root rig', stp='python',
                  c=lambda *args: rig_root.create_root_rig(reference_tools.joint_dictionary_creator()),
                  ann='Creates the rig controls for the root')

    cmds.menuItem(p='steps', l='Create torso rig', stp='python',
                  c=lambda *args: rig_torso.create_torso_rig(reference_tools.joint_dictionary_creator()),
                  ann='Creates the rig controls for the torso')

    cmds.menuItem(p='steps', l='Create neck rig', stp='python',
                  c=lambda *args: rig_neck.create_neck_rig(reference_tools.joint_dictionary_creator()),
                  ann='Creates the rig controls for the neck')

    cmds.menuItem(p='steps', l='Create arm rig', stp='python',
                  c=lambda *args: rig_arm.create_arm_rig(reference_tools.joint_dictionary_creator()),
                  ann='Creates the rig controls for the arms')

    cmds.menuItem(p='steps', l='Create leg rig', stp='python',
                  c=lambda *args: rig_leg.create_leg_rig(reference_tools.joint_dictionary_creator()),
                  ann='Creates the rig controls for the legs')

    cmds.menuItem(p='steps', l='Create fingers rig', stp='python',
                  c=lambda *args: rig_finger.create_finger_rig(reference_tools.joint_dictionary_creator()),
                  ann='Creates the rig controls for the fingers')

    cmds.menuItem(p='steps', l='Create fingers sdk', stp='python',
                  c=lambda *args: rig_sdk_finger.create_finger_sdk(),
                  ann='Creates the sdk controls for fingers')

    # Tools Menu
    cmds.menuItem('tools', p=menu_name, l='Tools', subMenu=True, tearOff=True)

    # Tools Menu -- Actions
    cmds.menuItem(p='tools', l='Export curve', stp='python',
                  c=lambda *args: export_curve(),
                  ann='Save curve object into YAML')

    cmds.menuItem(p='tools', l='Import curve', stp='python',
                  c=lambda *args: import_curve(),
                  ann='Load curve object into YAML')


def build_rig():
    constructor_tools.create_deform_rig()
    rig_root.create_root_rig(reference_tools.joint_dictionary_creator())
    rig_torso.create_torso_rig(reference_tools.joint_dictionary_creator())
    rig_neck.create_neck_rig(reference_tools.joint_dictionary_creator())
    rig_arm.create_arm_rig(reference_tools.joint_dictionary_creator())
    rig_leg.create_leg_rig(reference_tools.joint_dictionary_creator())
    rig_finger.create_finger_rig(reference_tools.joint_dictionary_creator())
    rig_sdk_finger.create_finger_sdk()
