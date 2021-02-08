bl_info = {
    "name": "Silhouette Shading",
    "blender": (2, 91, 0),
    "category": "Interface",
}
import bpy

#silhoutte shading parametrs
def main(context):
    context.space_data.shading.light = 'FLAT'
    context.space_data.shading.color_type = 'SINGLE'
    context.space_data.shading.single_color = (0, 0, 0)
    context.space_data.overlay.show_overlays = False



class ShadingSilhouette(bpy.types.Operator):
    """Silhouette shading"""
    bl_idname = "shading.silhouette"
    bl_label = "S"

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context): # execute() is called by blender when running the operator.
        if context.space_data.shading.light != 'FLAT':
            main(context)
        else:
            context.space_data.shading.light = 'STUDIO'
            context.space_data.shading.color_type = 'MATERIAL'
            context.space_data.overlay.show_overlays = True
        return {'FINISHED'} # this lets blender know the operator finished successfully.
def draw(self, context):
    self.layout.operator("shading.silhouette")

def register():
    bpy.utils.register_class(ShadingSilhouette)
    bpy.types.VIEW3D_HT_tool_header.append(draw)

def unregister():
    bpy.utils.unregister_class(ShadingSilhouette)


if __name__ == "__main__":
    register()