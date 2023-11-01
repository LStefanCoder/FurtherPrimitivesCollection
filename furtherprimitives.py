import bpy

bl_info = {
    "name": "FurtherPrimitivesCollection",
    "author": "LStefan",
    "version": (1, 0),
    "blender": (3, 6, 5),
    "location": "View3D > Add Menu",
    "description": "Enables the user to add additonal mesh and curve primitives.",
    "category": "Add Mesh"
}

class FurtherPrimitivesMenu(bpy.types.Menu):
    bl_label = "Further primitives"
    bl_idname = "OBJECT_MT_furtherprimitives_menu"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("newmeshes.semisphere32_operator")

        row = layout.row()
        row.operator("newmeshes.semisphere64_operator")

        row = layout.row()
        row.operator("newmeshes.semisphere128_operator")
        layout.separator()

        row = layout.row()
        row.operator("newmeshes.hookedcube_operator")

        row = layout.row()
        row.operator("newmeshes.hookedcubebottom_operator")

        row = layout.row()
        row.operator("newmeshes.hookedplane_operator")
        layout.separator()

        row = layout.row()
        row.operator("newmeshes.cableone_operator")

        row = layout.row()
        row.operator("newmeshes.cabletwo_operator")

        row = layout.row()
        row.operator("newmeshes.cablefive_operator")

class AddSemiSphere32Operator(bpy.types.Operator):
    bl_idname = "newmeshes.semisphere_operator"
    bl_label = "Semisphere on ground (32)"

    def execute(self, context):
        #checking whether the user is in edit mode, otherwise returning a warning popup
        #the first clause is needed for the case that there is no object selected
        if(bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT'):
            
            bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.editmode_toggle()
            #see https://blender.stackexchange.com/questions/36933/efficient-way-to-delete-all-points-below-z-0-on-grid-via-python-script
            for vertex in bpy.context.active_object.data.vertices:
                #selecting all vertices below the ground plane
                vertex.select = vertex.co.z < 0
            bpy.ops.object.mode_set(mode='EDIT')
            #deleting those vertices
            bpy.ops.mesh.delete(type='VERT')
            bpy.ops.object.mode_set(mode='OBJECT')
            for vertex in bpy.context.active_object.data.vertices:
                #selecting all vertices on the ground plane
                vertex.select = vertex.co.z == 0
            bpy.ops.object.mode_set(mode='EDIT')
            #adding a face to the bottom of the semisphere
            bpy.ops.mesh.edge_face_add()
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.mode_set(mode='OBJECT')

            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'You have to be in object mode')

class AddSemiSphere64Operator(bpy.types.Operator):
    bl_idname = "newmeshes.semisphere64_operator"
    bl_label = "Semisphere on ground (64)"

    def execute(self, context):
        #checking whether the user is in edit mode, otherwise returning a warning popup
        #the first clause is needed for the case that there is no object selected
        if(bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT'):
            
            bpy.ops.mesh.primitive_uv_sphere_add(segments=64, ring_count=32, radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.editmode_toggle()
            #see https://blender.stackexchange.com/questions/36933/efficient-way-to-delete-all-points-below-z-0-on-grid-via-python-script
            for vertex in bpy.context.active_object.data.vertices:
                #selecting all vertices below the ground plane
                vertex.select = vertex.co.z < 0
            bpy.ops.object.mode_set(mode='EDIT')
            #deleting those vertices
            bpy.ops.mesh.delete(type='VERT')
            bpy.ops.object.mode_set(mode='OBJECT')
            for vertex in bpy.context.active_object.data.vertices:
                #selecting all vertices on the ground plane
                vertex.select = vertex.co.z == 0
            bpy.ops.object.mode_set(mode='EDIT')
            #adding a face to the bottom of the semisphere
            bpy.ops.mesh.edge_face_add()
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.mode_set(mode='OBJECT')

            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'You have to be in object mode')

class AddSemiSphere128Operator(bpy.types.Operator):
    bl_idname = "newmeshes.semisphere128_operator"
    bl_label = "Semisphere on ground (128)"

    def execute(self, context):
        #checking whether the user is in edit mode, otherwise returning a warning popup
        #the first clause is needed for the case that there is no object selected
        if(bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT'):
            
            bpy.ops.mesh.primitive_uv_sphere_add(segments=128, ring_count=64, radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.editmode_toggle()
            #see https://blender.stackexchange.com/questions/36933/efficient-way-to-delete-all-points-below-z-0-on-grid-via-python-script
            for vertex in bpy.context.active_object.data.vertices:
                #selecting all vertices below the ground plane
                vertex.select = vertex.co.z < 0
            bpy.ops.object.mode_set(mode='EDIT')
            #deleting those vertices
            bpy.ops.mesh.delete(type='VERT')
            bpy.ops.object.mode_set(mode='OBJECT')
            for vertex in bpy.context.active_object.data.vertices:
                #selecting all vertices on the ground plane
                vertex.select = vertex.co.z == 0
            bpy.ops.object.mode_set(mode='EDIT')
            #adding a face to the bottom of the semisphere
            bpy.ops.mesh.edge_face_add()
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.mode_set(mode='OBJECT')

            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'You have to be in object mode')

class AddHookedCubeOperator(bpy.types.Operator):
    bl_idname = "newmeshes.hookedcube_operator"
    bl_label = "Cube with hooked vertices"

    def execute(self, context):
        #checking whether the user is in edit mode, otherwise returning a warning popup
        #the first clause is needed for the case that there is no object selected
        if(bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT'):
            bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    
            bpy.ops.object.editmode_toggle()
            #deselecting every vertex in order to select them later one by one for hooking
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.editmode_toggle()

            for i in range(0, 8):
                #hooking each vertex one after another
                #deselecting after each iteration is important
                bpy.context.active_object.data.vertices[i].select = True
                bpy.ops.object.editmode_toggle()
                bpy.ops.object.hook_add_newob()
                bpy.ops.mesh.select_all(action='DESELECT')
                bpy.ops.object.editmode_toggle()
    
            #deselecting everything at the end
            bpy.ops.object.select_all(action='DESELECT')
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'You have to be in object mode')

class AddHookedCubeBottomOriginOperator(bpy.types.Operator):
    bl_idname = "newmeshes.hookedcubebottom_operator"
    bl_label = "Cube on the ground with hooked vertices"

    def execute(self, context):
        #checking whether the user is in edit mode, otherwise returning a warning popup
        #the first clause is needed for the case that there is no object selected
        if(bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT'):
            bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    
            bpy.ops.object.editmode_toggle()
    
            bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
    
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.editmode_toggle()

            for i in range(0, 8):
                #hooking each vertex one after another
                #deselecting after each iteration is important
                bpy.context.active_object.data.vertices[i].select = True
                bpy.ops.object.editmode_toggle()
                bpy.ops.object.hook_add_newob()
                bpy.ops.mesh.select_all(action='DESELECT')
                bpy.ops.object.editmode_toggle()
    
            #deselecting everything at the end
            bpy.ops.object.select_all(action='DESELECT')
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'You have to be in object mode')

class AddHookedPlaneOperator(bpy.types.Operator):
    bl_idname = "newmeshes.hookedplane_operator"
    bl_label = "Plane with hooked vertices"

    def execute(self, context):
        #checking whether the user is in edit mode, otherwise returning a warning popup
        #the first clause is needed for the case that there is no object selected
        if(bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT'):
            bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    
            bpy.ops.object.editmode_toggle()
            #deselecting every vertex in order to select them later one by one for hooking
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.editmode_toggle()

            for i in range(0, 4):
                #hooking each vertex one after another
                #deselecting after each iteration is important
                bpy.context.active_object.data.vertices[i].select = True
                bpy.ops.object.editmode_toggle()
                bpy.ops.object.hook_add_newob()
                bpy.ops.mesh.select_all(action='DESELECT')
                bpy.ops.object.editmode_toggle()
    
            #deselecting everything at the end
            bpy.ops.object.select_all(action='DESELECT')
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'You have to be in object mode')

class AddOneMillimeterCableOperator(bpy.types.Operator):
    """Add a cable with a thickness of 1mm"""
    bl_idname = "newmeshes.cableone_operator"
    bl_label = "Cable (1 mm)"

    def execute(self, context):
        #checking whether the user is in edit mode, otherwise returning a warning popup
        #the first clause is needed for the case that there is no object selected
        if(bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT'):
            bpy.ops.curve.primitive_bezier_curve_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

            #setting the curve resolution to 24, depth to 1mm and bevel resolution to 8
            bpy.context.object.data.resolution_u = 24
            bpy.context.object.data.bevel_depth = 0.001
            bpy.context.object.data.bevel_resolution = 8

            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'You have to be in object mode')

class AddTwoMillimeterCableOperator(bpy.types.Operator):
    """Add a cable with a thickness of 2mm"""
    bl_idname = "newmeshes.cabletwo_operator"
    bl_label = "Cable (2 mm)"

    def execute(self, context):
        #checking whether the user is in edit mode, otherwise returning a warning popup
        #the first clause is needed for the case that there is no object selected
        if(bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT'):
            bpy.ops.curve.primitive_bezier_curve_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

            #setting the curve resolution to 24, depth to 1mm and bevel resolution to 8
            bpy.context.object.data.resolution_u = 24
            bpy.context.object.data.bevel_depth = 0.002
            bpy.context.object.data.bevel_resolution = 8

            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'You have to be in object mode')

class AddFiveMillimeterCableOperator(bpy.types.Operator):
    """Add a cable with a thickness of 5mm"""
    bl_idname = "newmeshes.cablefive_operator"
    bl_label = "Cable (5 mm)"

    def execute(self, context):
        #checking whether the user is in edit mode, otherwise returning a warning popup
        #the first clause is needed for the case that there is no object selected
        if(bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT'):
            bpy.ops.curve.primitive_bezier_curve_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

            #setting the curve resolution to 24, depth to 1mm and bevel resolution to 8
            bpy.context.object.data.resolution_u = 24
            bpy.context.object.data.bevel_depth = 0.005
            bpy.context.object.data.bevel_resolution = 8

            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'You have to be in object mode')

def draw_menu(self, context):
    self.layout.menu(FurtherPrimitivesMenu.bl_idname)

def register():
    bpy.utils.register_class(FurtherPrimitivesMenu)
    bpy.utils.register_class(AddSemiSphere32Operator)
    bpy.utils.register_class(AddSemiSphere64Operator)
    bpy.utils.register_class(AddSemiSphere128Operator)
    bpy.utils.register_class(AddHookedCubeOperator)
    bpy.utils.register_class(AddHookedCubeBottomOriginOperator)
    bpy.utils.register_class(AddHookedPlaneOperator)
    bpy.utils.register_class(AddOneMillimeterCableOperator)
    bpy.utils.register_class(AddTwoMillimeterCableOperator)
    bpy.utils.register_class(AddFiveMillimeterCableOperator)
    bpy.types.VIEW3D_MT_mesh_add.append(draw_menu)

def unregister():
    bpy.types.VIEW3D_MT_mesh_add.remove(draw_menu)
    bpy.utils.unregister_class(AddSemiSphere32Operator)
    bpy.utils.unregister_class(AddSemiSphere64Operator)
    bpy.utils.unregister_class(AddSemiSphere128Operator)
    bpy.utils.unregister_class(AddHookedCubeOperator)
    bpy.utils.unregister_class(AddHookedCubeBottomOriginOperator)
    bpy.utils.unregister_class(AddHookedPlaneOperator)
    bpy.utils.unregister_class(AddOneMillimeterCableOperator)
    bpy.utils.unregister_class(AddTwoMillimeterCableOperator)
    bpy.utils.unregister_class(AddFiveMillimeterCableOperator)
    bpy.utils.unregister_class(FurtherPrimitivesMenu)

if __name__ == "__main__":
    register()