# Important plugin info for Blender
from mathutils import Quaternion

bl_info = {
    'name': 'Rokoko Studio Live for Blender',
    'author': 'Rokoko',
    'category': 'Animation',
    'location': 'View 3D > Tool Shelf > Rokoko',
    'description': 'Stream your Rokoko Studio animations directly into Blender',
    'version': (0, 1),
    'blender': (2, 80, 0),
}

# If first startup of this plugin, load all modules normally
# If reloading the plugin, use importlib to reload modules
# This lets you do adjustments to the plugin on the fly without having to restart Blender
if "bpy" not in locals():
    import bpy
    from . import core
    from . import panels
    from . import operators
    from . import properties
else:
    import importlib
    importlib.reload(core)
    importlib.reload(panels)
    importlib.reload(operators)
    importlib.reload(properties)


# List of all buttons and panels
classes = [
    panels.main.ReceiverPanel,
    panels.objects.ObjectsPanel,
    operators.receiver.ReceiverStart,
    operators.receiver.ReceiverStop,
    operators.recorder.RecorderStart,
    operators.recorder.RecorderStop,
    operators.detector.DetectFaceShapes,
    operators.detector.DetectActorBones,
    operators.actor.InitTPose,
    operators.actor.ResetTPose,
    operators.actor.PrintCurrentPose,
    operators.actor.SaveTargetPose,
]


# register and unregister all classes
def register():
    print("\n### Loading Rokoko Studio Live...")

    # Register all classes
    for cls in classes:
        bpy.utils.register_class(cls)

    properties.register()

    print("### Loaded Rokoko Studio Live successfully!\n")

    # test_from1 = Quaternion((-0.707, 0.707, 0, 0))
    # test_to1   = Quaternion((0.707, 0, 0, 0.707))
    #
    # test_from = Quaternion((0.7038, -0.7022, 0.0276, 0.1046))
    # test_to   = Quaternion((0.7038, 0.1046, 0.0276, 0.7022))
    #
    # result = test_from @ Quaternion((0, 0, 0, -1))
    #
    # diff = test_from.inverted() @ test_to
    #
    # print(result)
    # print(diff)
    # print(Quaternion((-1, 1, 0, 0)) @ diff)
    # print(test_from @ Quaternion((0.5, 0.5, -0.5, 0.5)))


def unregister():
    print("### Unloading Rokoko Studio Live...")

    # Shut down receiver if the plugin is disabled while it is running
    if operators.receiver.receiver_enabled:
        operators.receiver.ReceiverStart.force_disable()

    # Unregister all classes
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    print("### Unloaded Rokoko Studio Live successfully!\n")


if __name__ == '__main__':
    register()