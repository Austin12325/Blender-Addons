import bpy

bl_info = {
    "name": "Austin's Bone Snapping Panel",
    "blender": (3, 0, 0),
    "category": "Armature",
}




class ARMATURE_Apply_Visual_Transform(bpy.types.Operator):
    """This will apply the visual transform of the selected bone"""
    bl_idname = "armature.apply_visual_transform"
    bl_label = "Apply Driver Transforms"
    
    def execute(self, context):
        bpy.ops.pose.visual_transform_apply()
        return {'FINISHED'} 

class Austins_Properties(bpy.types.PropertyGroup):
    
    #User can input their own bones for the desired sliders
    hand_mag_shared_string : bpy.props.StringProperty(name="Hand Magazine Shared", description='Reminder, your bone names need to be seperated by spaces.')
    mag_weapon_shared_string : bpy.props.StringProperty(name="Mag Weapon Shared", description='Reminder, your bone names need to be seperated by spaces.')
    weapon_string : bpy.props.StringProperty(name="Weapon Bones", description='Reminder, your bone names need to be seperated by spaces.')
    mag_string : bpy.props.StringProperty(name="Mag Bones", description='Reminder, your bone names need to be seperated by spaces.')
    hand_string : bpy.props.StringProperty(name="Hand", description='Reminder, your bone names need to be seperated by spaces.')
    
    #Operators for the UI sliders
    hand_barrel_snap : bpy.props.FloatProperty(default=0, min=0, max=1)
    hand_mag_snap : bpy.props.FloatProperty(default=0, min=0, max=1)
    mag_weapon_snap : bpy.props.FloatProperty(default=0, min=0, max=1)
    weapon_snap : bpy.props.FloatProperty(default=0, min=0, max=1)
    hand_snap : bpy.props.FloatProperty(default=0, min=0, max=1)
    hand_mag_shared : bpy.props.FloatProperty(default=0, min=0, max=1)
    mag_weapon_shared : bpy.props.FloatProperty(default=0, min=0, max=1)
    
    show_all_menus : bpy.props.BoolProperty(name="Show all drivers", description='Show all drivers')
    #Exposes settings to define the bones
    show_all_bool : bpy.props.BoolProperty(name="Bone editing", description='Reminder, your bone names need to be seperated by spaces.')

class Austins_tools(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Animation"
    bl_label = "Bone Snapping"

#bpy.data.scenes["Scene.001"].austins_props.mag_string

    def draw(self, context):
        layout = self.layout
        obj = context.object
        bone = context.active_bone
        scene = context.scene
        mytool = scene.austins_props
 
        #Defines and converts the strings into lists for the UI        
        HandMagShared = bpy.data.scenes[scene.name].austins_props.hand_mag_shared_string.split()
#        HandWeapon = bpy.data.scenes[scene.name].austins_props.hand_weapon_string.split() 
        Weapon = bpy.data.scenes[scene.name].austins_props.weapon_string.split() 
        Mag = bpy.data.scenes[scene.name].austins_props.mag_string.split() 
        Handstring = bpy.data.scenes[scene.name].austins_props.hand_string.split()
        MagWeaponShared = bpy.data.scenes[scene.name].austins_props.mag_weapon_shared_string.split()
        
        col = self.layout.column(align=True)
        row = self.layout.row()

        row.prop(mytool, "show_all_bool")
        row.prop(mytool, "show_all_menus")
        
        
        col.label(text="Active bone is: " + bone.name)
        print("working active bone")
        
        
        if bpy.context.scene.austins_props["show_all_menus"] == True:
            box = layout.box()
            
            box.label(text="All Drivers")
            box.prop(mytool, 'weapon_snap', text='Weapon->Rest' )
#            col.label(text="Mag->Weapon")
            box.prop(mytool, 'mag_weapon_snap', text='Mag->Weapon' )
            box.prop(mytool, 'hand_barrel_snap', text='Hand->Barrel' )
            box.prop(mytool, 'hand_mag_snap', text='Hand->Mag' )    
            box.operator('armature.apply_visual_transform', text='Apply Transform')
        
        #Enables the string input box if bool is true
        if bpy.context.scene.austins_props["show_all_bool"] == True: 
            box = layout.box()
            box.label(text='Reminder, your bone names need to be seperated by spaces.')
        

            row = layout.row()
            
            col = self.layout.column(align=True)
            col.prop(mytool, 'hand_mag_shared_string')
            
            row = layout.row()
          
          #String input boxes 
            col = self.layout.column(align=True)
            col.prop(mytool, 'mag_weapon_shared_string')
            row = layout.row()
            
            col = self.layout.column(align=True)
            col.prop(mytool, 'weapon_string')
            print("working hand mag string")
            
            col = self.layout.column(align=True)
            col.prop(mytool, 'mag_string')
            print("working mag string")
            
            col = self.layout.column(align=True)
            col.prop(mytool, 'hand_string')
            print("working hand string")
#        #Gives UI sliders to bones in HandMag list. 
#        if bpy.context.active_bone.name in HandMag:
#            print("Found bones in Hand/mag list")
#            
#                    

#            row = layout.row()
#            col = self.layout.column(align=True)
#            
#        #UI for the sliders 

#            col.label(text="Hand->Barrel")
#            col.prop(mytool, 'hand_barrel_snap', text='' )
#        

#            split = layout.split(factor=0)
#            col = self.layout.column(align=True)

#            
#            col.label(text="Hand->Mag")
#            col.prop(mytool, 'hand_mag_snap', text='' )
#            
#        #Gives UI sliders to bones in HandWeapon list
#        if bpy.context.active_bone.name in HandWeapon:
#            print("Found bones in Hand/Weapon list")
#            
#                    
#        #UI for the sliders 
#            row = layout.row()
#            col = self.layout.column(align=True)
#            
#            col.label(text="Hand->Barrel")
#            col.prop(mytool, 'hand_barrel_snap', text='' )

#        
        
        if bpy.context.active_bone.name in Weapon and bpy.context.scene.austins_props["show_all_menus"] == True:
            print("Found bones in Weapon list")
            
        elif bpy.context.active_bone.name in Weapon:         
        #UI for the sliders 
            row = layout.row()
            col = self.layout.column(align=True)
            box = layout.box()
            split = layout.split(factor=0)
            col = self.layout.column(align=True)
            
            box.label(text="Weapon Drivers")
            box.prop(mytool, 'weapon_snap', text='Weapon->Rest' )
#            col.label(text="Mag->Weapon")
            box.prop(mytool, 'mag_weapon_snap', text='Mag->Weapon' )
#            col.label(text="Hand->Barrel")
            box.prop(mytool, 'hand_barrel_snap', text='Hand->Barrel' )
            box.operator('armature.apply_visual_transform', text='Apply Transform')
                            
        if bpy.context.active_bone.name in Mag and bpy.context.scene.austins_props["show_all_menus"] == True:
            print("Found bones in Mag list")
            
        elif bpy.context.active_bone.name in Mag:           
        #UI for the sliders 
            row = layout.row()
            col = self.layout.column(align=True)
            
            split = layout.split(factor=0)
            col = self.layout.column(align=True)
            box = layout.box()
            
            box.label(text='Mag Drivers')
#            col.label(text="Mag->Weapon")
            box.prop(mytool, 'mag_weapon_snap', text='Mag->Weapon' )
#            col.label(text="Hand->Mag")
            box.prop(mytool, 'hand_mag_snap', text='Hand->Mag' )         
            box.operator('armature.apply_visual_transform', text='Apply Transform')   
        
                
        if bpy.context.active_bone.name in Handstring and bpy.context.scene.austins_props["show_all_menus"] == True:
            print("Found bones in Hand list")
            
        elif bpy.context.active_bone.name in Handstring:            
        #UI for the sliders 
            row = layout.row()
            col = self.layout.column(align=True)
            
            split = layout.split(factor=0)
            col = self.layout.column(align=True)
            box = layout.box()
            
            box.label(text="Hand Drivers")
#            col.label(text="Hand->Rest")
            box.prop(mytool, 'hand_snap', text='Hand->Rest' )
#            col.label(text="Hand->Barrel")
            box.prop(mytool, 'hand_barrel_snap', text='Hand->Barrel' )
#            col.label(text="Hand->Mag")
            box.prop(mytool, 'hand_mag_snap', text='Hand->Mag' )
            box.operator('armature.apply_visual_transform', text='Apply Transform')
        
        
        
        if bpy.context.active_bone.name in HandMagShared:
            print("Found bones in Hand Mag Shared list")
            box = layout.box()
            
            box.label(text="Hand Mag Shared Controls")
            box.prop(mytool, 'hand_mag_snap', text='Hand->Mag')
            box.operator('armature.apply_visual_transform', text='Apply Transform')
                
        if bpy.context.active_bone.name in MagWeaponShared:
            print("Found bones in Mag Weapon Shared list")
            box = layout.box()
            box.label(text="Weapon Mag Shared Controls")
            box.prop(mytool, 'mag_weapon_snap', text='Mag->Weapon')
            box.operator('armature.apply_visual_transform', text='Apply Transform')
            
classes = [Austins_Properties, Austins_tools, ARMATURE_Apply_Visual_Transform]
        
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        bpy.types.Scene.austins_props = bpy.props.PointerProperty(type= Austins_Properties) 
            
    
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        del bpy.types.Scene.austins_props
