bl_info = {
    "name": "DevolasReincarnation",
    "author": "DevolasRevenge",
    "version": (1, 0, 7),
    "blender": (2, 80, 0),
    "category": "Interface",
}

import bpy
import os
import json
from math import radians


class Devola_PT_Panel(bpy.types.Panel):
    bl_idname = "ARMATURE_PT_panel"
    bl_label = "Reincarnation Weights Manager"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Devola'
    
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        cvalue = scene.custom_values
        
        row = layout.row()
        row.label(text= "Character Selector")
        row = layout.row()
        row.label(text= "Character", icon= 'USER')
        row.prop(cvalue, "character_select")
        
        row = layout.row()
        row.label(text= "Armature Selector")
        row = layout.row()
        row.label(text= "Rein Armature", icon= 'OUTLINER_DATA_ARMATURE')
        row.prop_search(cvalue, "reinobjectname", bpy.data, "objects", text="")
        
        row = layout.row()
        row.label(text= "NieR Armature", icon= 'OUTLINER_DATA_ARMATURE')
        row.prop_search(cvalue, "nierobjectname", bpy.data, "objects", text="")        
        
        
        row = layout.row()
        row.label(text= "Automatic operators")
        row = layout.row()
        
        row.label(text= "Armature", icon= 'OUTLINER_DATA_ARMATURE')
        row.operator("open.scalemesh")
        row = layout.row()
        
        row.label(text= "Body Mesh", icon= 'OUTLINER_OB_MESH')                                    
        row.operator("open.weightmix")        


        row = layout.row()
        row.label(text= "Armature", icon= 'OUTLINER_DATA_ARMATURE')                                    
        row.operator("open.posebones")
        row = layout.row()
        row.prop(cvalue, "apply_constraints_check") 
        
        
        row = layout.row()
        row.label(text= "Body Mesh", icon= 'OUTLINER_OB_MESH')                            
        row.operator("open.applymod")              
        row = layout.row()
        row.prop(cvalue, "add_armature_check")
        
        row = layout.row()
        row.label(text= "Armature", icon= 'OUTLINER_DATA_ARMATURE')                            
        row.operator("open.bonerename")
        
        row = layout.row()
        row.label(text= "Fix Rein Materials")
     
        row = layout.row()
        row.label(text= "", icon= 'FILE_FOLDER')          
        row.prop(cvalue, 'rein_path')
        
        row = layout.row()        
        row.label(text= "Scene", icon= 'BLENDER')                            
        row.operator("open.fixmats")
        
        #row = layout.row()                                  
        #row.operator("open.test")

        
        row = layout.row()        
        row.label(text= "Test Script DevolasRevenge")
        row.label(text= "", icon= 'FUND')  
        
        
class DevolaOpen_PT_Panel(bpy.types.Panel):
    bl_idname = "WEIGHTS_PT_panel"
    bl_label = "Custom Weights Manager"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Devola'
    
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        cvalue = scene.custom_values
 
        layout = self.layout
        

        
        col = layout.column()
        
        col.prop(cvalue, 'json_path')
        
        row = layout.row()
        
        row.label(text= "*Not Supported Yet*")
        
        
##----------------------------------------------------------------
                        
class OPEN_OT_ScaleNIER(bpy.types.Operator):
    """Scales Rein mesh to Nier Dimensions"""
    bl_label = "Scale Rein Objects"
    bl_idname = "open.scalemesh"
    
    def execute(self, context):
         
         scene = context.scene        
         cvalue = scene.custom_values

         arm_object = cvalue.reinobjectname
         armature_name = bpy.data.objects[arm_object]
              
         armature_name.scale[0] = 1
         armature_name.scale[1] = 1
         armature_name.scale[2] = 1
         
         print (':: Rein armature scale set to 1')   
                
         return {'FINISHED'} 
         
##----------------------------------------------------------------
                        
class OPEN_OT_WeightMix(bpy.types.Operator):
    """Add Weight Mix Modifiers for Rein Mesh"""
    bl_label = "Mix Weights"
    bl_idname = "open.weightmix"
    
    def execute(self, context):
        
        scene = context.scene        
        cvalue = scene.custom_values

        arm_object = cvalue.reinobjectname
        armature_name = bpy.data.objects[arm_object] 
        
        character = cvalue.character_select
        
        for object in armature_name.children:
            if object.type == 'MESH':
    
                modifier = object.modifiers.new(name="Right_Leg_1", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "right_upleg"
                modifier.vertex_group_b = "sub_62"


                modifier = object.modifiers.new(name="Right_Leg_2", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "right_upleg"
                modifier.vertex_group_b = "sub_60"


                modifier = object.modifiers.new(name="Left_Leg_1", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "left_upleg"
                modifier.vertex_group_b = "sub_61"

                modifier = object.modifiers.new(name="Left_Leg_2", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "left_upleg"
                modifier.vertex_group_b = "sub_63"

                modifier = object.modifiers.new(name="Left_Arm_1", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "left_arm"
                modifier.vertex_group_b = "sub_71"

                modifier = object.modifiers.new(name="Left_Arm_2", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "left_arm"
                modifier.vertex_group_b = "sub_73"

                modifier = object.modifiers.new(name="Right_Arm_1", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "right_arm"
                modifier.vertex_group_b = "sub_70"

                modifier = object.modifiers.new(name="Right_Arm_2", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "right_arm"
                modifier.vertex_group_b = "sub_72"

                modifier = object.modifiers.new(name="Head1", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_c_upper_lip"

                modifier = object.modifiers.new(name="Head2", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_l_upper_lip"

                modifier = object.modifiers.new(name="Head3", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_r_upper_lip"

                modifier = object.modifiers.new(name="Head4", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_r_upper_lip"

                modifier = object.modifiers.new(name="Head5", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_r_outer_lip"

                modifier = object.modifiers.new(name="Head6", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_l_outer_lip"

                modifier = object.modifiers.new(name="Head7", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_l_brow1"

                modifier = object.modifiers.new(name="Head8", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_l_brow2"

                modifier = object.modifiers.new(name="Head9", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_l_brow3"

                modifier = object.modifiers.new(name="Head9", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_l_brow3"

                modifier = object.modifiers.new(name="Head10", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_l_eye"

                modifier = object.modifiers.new(name="Head10", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_l_inner_eyelid"

                modifier = object.modifiers.new(name="Head11", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_l_lower_eyelid"

                modifier = object.modifiers.new(name="Head12", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_l_outer_eyelid"

                modifier = object.modifiers.new(name="Head13", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_r_brow1"

                modifier = object.modifiers.new(name="Head14", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_r_brow2"

                modifier = object.modifiers.new(name="Head15", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_r_brow3"

                modifier = object.modifiers.new(name="Head16", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_r_eye"

                modifier = object.modifiers.new(name="Head17", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_r_inner_eyelid"

                modifier = object.modifiers.new(name="Head18", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_r_lower_eyelid"

                modifier = object.modifiers.new(name="Head18", type='VERTEX_WEIGHT_MIX')
                modifier.mix_set = 'ALL'
                modifier.mix_mode = 'ADD'
                modifier.vertex_group_a = "head"
                modifier.vertex_group_b = "fc_r_outer_eyelid"
                
                if character == '2B_1':
                    modifier = object.modifiers.new(name="Right_Elbow", type='VERTEX_WEIGHT_MIX')
                    modifier.mix_set = 'ALL'
                    modifier.mix_mode = 'ADD'
                    modifier.vertex_group_a = "right_arm"
                    modifier.vertex_group_b = "sub_40"
                    
                    modifier = object.modifiers.new(name="Left_Elbow", type='VERTEX_WEIGHT_MIX')
                    modifier.mix_set = 'ALL'
                    modifier.mix_mode = 'ADD'
                    modifier.vertex_group_a = "left_arm"
                    modifier.vertex_group_b = "sub_41"
                else:
                    continue
                    
                
                
        print (":: Weight-mix Modifiers Added")
        
        return {'FINISHED'} 
        
##-----------------------------------------------------
    
class OPEN_OT_BoneRename(bpy.types.Operator):
    """Rename Rein Armature Bones to NieR:Automata Bones"""
    bl_label = "Rename Bones (to NieR)"
    bl_idname = "open.bonerename"
    
    def execute(self, context):
        

        #object = bpy.context.active_object
        
        scene = context.scene        
        cvalue = scene.custom_values

        arm_object = cvalue.reinobjectname
        armature_name = bpy.data.objects[arm_object] 
        
        namelist_A2 = [("left_toe", "bone139"),
            ("right_foot", "bone134"),
            ("right_toe", "bone135"),
            ("left_foot", "bone138"),
            ("right_leg", "bone133"),
            ("left_leg", "bone137"),
            ("right_shoulder", "bone53"),
            ("left_shoulder", "bone80"),
            ("right_arm", "bone54"),
            ("left_arm", "bone81"),
            ("right_forearm", "bone55"),
            ("left_forearm", "bone82"),
            ("left_hand", "bone83"),
            ("right_hand", "bone56"),
            ("right_hand_thumb1", "bone57"),
            ("right_hand_thumb2", "bone58"),
            ("right_hand_thumb3", "bone59"),
            ("right_hand_index1", "bone60"),
            ("right_hand_index2", "bone61"),
            ("right_hand_index3", "bone62"),
            ("right_hand_index4", "bone63"),
            ("right_hand_middle1", "bone64"),
            ("right_hand_middle2", "bone65"),
            ("right_hand_middle3", "bone66"),
            ("right_hand_middle4", "bone67"),
            ("right_hand_ring1", "bone68"),
            ("right_hand_ring2", "bone69"),
            ("right_hand_ring3", "bone70"),
            ("right_hand_ring4", "bone71"),
            ("right_hand_pinky1", "bone72"),
            ("right_hand_pinky2", "bone73"),
            ("right_hand_pinky3", "bone74"),
            ("right_hand_pinky4", "bone75"),
            ("sub_10", "bone76"),
            ("sub_40", "bone78"),
            ("sub_20", "bone103"),
            ("sub_41", "bone105"),
            ("left_hand_thumb1", "bone100"),
            ("left_hand_thumb2", "bone101"),
            ("left_hand_thumb3", "bone102"),
            ("left_hand_index1", "bone96"),
            ("left_hand_index2", "bone97"),
            ("left_hand_index3", "bone98"),
            ("left_hand_index4", "bone99"),
            ("left_hand_middle1", "bone92"),
            ("left_hand_middle2", "bone93"),
            ("left_hand_middle3", "bone94"),
            ("left_hand_middle4", "bone95"),
            ("left_hand_ring1", "bone88"),
            ("left_hand_ring2", "bone89"),
            ("left_hand_ring3", "bone90"),
            ("left_hand_ring4", "bone91"),
            ("left_hand_pinky1", "bone84"),
            ("left_hand_pinky2", "bone85"),
            ("left_hand_pinky3", "bone86"),
            ("left_hand_pinky4", "bone87"),
            ("hip", "bone131"),
            ("spine1", "bone1"),
            ("spine2", "bone2"),
            ("spine3", "bone3"),
            ("neck", "bone4"),
            ("head", "bone5"),
            ("fc_c_jaw", "bone6"),
            ("sub_02", "bone52"),
            ("spring_f_breast001_01_02", "bone107"),
            ("left_upleg", "bone136"),
            ("right_upleg", "bone132"),
            ("fc_l_upper_eyelid", "bone8"),
            ("fc_r_upper_eyelid", "bone7")                    
            ]
            
        namelist_2B = [("left_toe", "bone97"),
            ("right_foot", "bone92"),
            ("right_toe", "bone93"),
            ("left_foot", "bone96"),
            ("right_leg", "bone91"),
            ("left_leg", "bone95"),
            ("right_shoulder", "bone34"),
            ("left_shoulder", "bone61"),
            ("right_arm", "bone35"),
            ("left_arm", "bone62"),
            ("right_forearm", "bone36"),
            ("left_forearm", "bone63"),
            ("left_hand", "bone64"),
            ("right_hand", "bone37"),
            ("right_hand_thumb1", "bone38"),
            ("right_hand_thumb2", "bone39"),
            ("right_hand_thumb3", "bone40"),
            ("right_hand_index1", "bone41"),
            ("right_hand_index2", "bone42"),
            ("right_hand_index3", "bone43"),
            ("right_hand_index4", "bone44"),
            ("right_hand_middle1", "bone45"),
            ("right_hand_middle2", "bone46"),
            ("right_hand_middle3", "bone47"),
            ("right_hand_middle4", "bone48"),
            ("right_hand_ring1", "bone49"),
            ("right_hand_ring2", "bone50"),
            ("right_hand_ring3", "bone51"),
            ("right_hand_ring4", "bone52"),
            ("right_hand_pinky1", "bone53"),
            ("right_hand_pinky2", "bone54"),
            ("right_hand_pinky3", "bone55"),
            ("right_hand_pinky4", "bone56"),
            ("sub_10", "bone57"),
            ("sub_20", "bone84"),
            ("left_hand_thumb1", "bone81"),
            ("left_hand_thumb2", "bone82"),
            ("left_hand_thumb3", "bone83"),
            ("left_hand_index1", "bone77"),
            ("left_hand_index2", "bone78"),
            ("left_hand_index3", "bone79"),
            ("left_hand_index4", "bone80"),
            ("left_hand_middle1", "bone73"),
            ("left_hand_middle2", "bone74"),
            ("left_hand_middle3", "bone75"),
            ("left_hand_middle4", "bone76"),
            ("left_hand_ring1", "bone69"),
            ("left_hand_ring2", "bone70"),
            ("left_hand_ring3", "bone71"),
            ("left_hand_ring4", "bone72"),
            ("left_hand_pinky1", "bone65"),
            ("left_hand_pinky2", "bone66"),
            ("left_hand_pinky3", "bone67"),
            ("left_hand_pinky4", "bone68"),
            ("hip", "bone89"),
            ("spine1", "bone3"),
            ("spine2", "bone4"),
            ("spine3", "bone5"),
            ("neck", "bone6"),
            ("head", "bone7"),
            ("fc_c_jaw", "bone8"),
            ("sub_02", "bone33"),
            ("spring_f_breast001_01_02", "bone88"),
            ("left_upleg", "bone94"),
            ("right_upleg", "bone90"),
            ("fc_l_upper_eyelid", "bone10"),
            ("fc_r_upper_eyelid", "bone9")                    
            ]
            
        character = cvalue.character_select
        
        #character_name_display is only used to display character names in the console
        character_name_display = (character.replace('_1', ''))
        
        if character == 'A2_1':
            namelist=namelist_A2
        elif character == '2B_1':
            namelist=namelist_2B
        print(':: Bone namelist assigned to', character_name_display)

        for name, newname in namelist:
            # get the pose bone with name
            pb = armature_name.pose.bones.get(name)
            # continue if no bone of that name
            if pb is None:
                continue
            # rename
            pb.name = newname
        
            
        print (":: Bones Renamed to", character_name_display)
            
        return {'FINISHED'} 

##-----------------------------------------------------  


class OPEN_OT_ConvertMesh(bpy.types.Operator):
    """Applies all Modifiers"""
    bl_label = "Apply Modifiers"
    bl_idname = "open.applymod"
    
    def execute(self, context):
        
        
        scene = context.scene        
        cvalue = scene.custom_values

        arm_object = cvalue.reinobjectname
        armature_name = bpy.data.objects[arm_object]
         
        
        for child in armature_name.children:
            if child.type == 'MESH':
                child.select = True
                bpy.context.view_layer.objects.active = child
                bpy.ops.object.convert(target='MESH')
            child.select = False
        
                
        bpy.context.view_layer.objects.active = armature_name
        bpy.ops.object.mode_set(mode='POSE')        
        bpy.ops.pose.armature_apply(selected=False)
        bpy.ops.object.mode_set(mode='OBJECT')
        
        for child in armature_name.children:
            if child.type == 'MESH':
                child.select = True
                bpy.context.view_layer.objects.active = child
                if (cvalue.add_armature_check == True):        
                    bpy.ops.object.modifier_add(type='ARMATURE')  
                    bpy.context.object.modifiers["Armature"].object = armature_name
                child.select = False
        
        if (cvalue.add_armature_check == True):
            print (":: Modifiers Applied + Reapplied Armature Modifier")
        else:
            print (":: Modifiers Applied")
        
        return {'FINISHED'} 
    
##----------------------------------------------------- 


                        
class OPEN_OT_FixMats(bpy.types.Operator):
    """Fixes Viewport Rein Materials"""
    bl_label = "Fix Rein Materials"
    bl_idname = "open.fixmats"
    
    def execute(self, context):
        
        object = bpy.context.active_object 
        
        scene = context.scene
        file_tool = bpy.path.abspath(scene.custom_values.rein_path)
        
        dir_list = []
        mso_list = []
        mso_string = "mso_.png"
        
        #redundant?
        for path in os.listdir(file_tool):
            if (os.path.isfile(os.path.join(file_tool, path))):
                dir_list.append(path)
        
        mso_list = [i for i in dir_list if mso_string in i]
                
        print("Retrieved MSO Maps:")    
                  
        
        for material in bpy.data.materials:
            #makes sure each material starts with mt_
            if not material.name.startswith("mt_"): continue
            #sets material type to hashed to fix bad backface culling
            material.blend_method = 'HASHED'
            
            #isolates the material name and removed the mt_ from it -- then stores it in a variable            
            clean_name = material.name
            clean_name = (clean_name.replace('mt_', ''))
            
            #removes the 0.001 from names in clean_name in order for the script to work on them
            period = "."
            if period in clean_name:                
                clean_name = clean_name[:-4]
                
            #appends a MSO texture string to MSO_value as long as they have a clean_name inside of it
            mso_value = [i for i in mso_list if clean_name in i]
            
            #turns the MSO_value list into a string
            image_value = ''.join(mso_value)
            print(image_value)
            
            existing_image = image_value
            
            image_value = file_tool + "\\" + image_value
            print(image_value)
            #image_value = bpy.data.images.load(filepath = image_value)
            
            
            #establishes material node and tree node values
            material.use_nodes = True
            nodes = material.node_tree.nodes
            links = material.node_tree.links
            
            #resets Principled BSDF values
            nodes["Principled BSDF"].inputs['Specular'].default_value = 0.1
            nodes["Principled BSDF"].inputs['Emission Strength'].default_value = 0.0
            
            ##checks for empty MSO filepath
            if not mso_value:
                continue
            else:
                #adds the MSO map
                inode = nodes.new('ShaderNodeTexImage')
                inode.location = (-1000,0)
                
                #if the image has already been imported in the scene, it uses that. Otherwise it imports the image.
                if existing_image in bpy.data.images:
                    inode.image = bpy.data.images[existing_image]
                else:                
                    inode.image = bpy.data.images.load(image_value)       
                
                RGB_split = nodes.new('ShaderNodeSeparateRGB')
                RGB_split.location = (-700,0)
                links.new(RGB_split.inputs[0], inode.outputs[0])
                
                links.new(nodes["Principled BSDF"].inputs['Metallic'], RGB_split.outputs[0])
                
                Invert_gloss = nodes.new('ShaderNodeInvert')
                Invert_gloss.location = (-500,0)
                
                links.new(Invert_gloss.inputs['Color'], RGB_split.outputs[1])
                links.new(nodes["Principled BSDF"].inputs['Roughness'], Invert_gloss.outputs[0])
                
    
            print (":: Materials Adjusted")
            
        return {'FINISHED'}
    
##----------------------------------------------------- 
          
class OPEN_OT_BONEPOSER(bpy.types.Operator):
    """Pose Bones"""
    bl_label = "Pose Bones (to NieR)"
    bl_idname = "open.posebones"
    
    def execute(self, context):
        
        scene = context.scene        
        cvalue = scene.custom_values

        rein_object = cvalue.reinobjectname
        rein_name = bpy.data.objects[rein_object]
        
        nier_object = cvalue.nierobjectname
        nier_name = bpy.data.objects[nier_object]                    
        
        armature = rein_name.data
        
        bpy.context.view_layer.objects.active = rein_name

        scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'

        bpy.ops.object.mode_set(mode='EDIT')

        all_bones = []

        #edit mode bone rotation
        
        for bone in armature.bones:
            all_bones.append(bone.name)
        for i in all_bones:
            armature.edit_bones[i].select_tail=False
            armature.edit_bones[i].select_head=False
            armature.edit_bones[i].select=False  

        left_arm_list = ['left_arm', 'left_shoulder', 'left_forearm']

        for i in left_arm_list:
            armature.edit_bones[i].select_tail=True
            bpy.ops.transform.rotate(value=radians(-90), orient_axis='Z', orient_type='LOCAL', constraint_axis=(False, False, True))
            armature.edit_bones[i].select_tail=False

        right_arm_list = ['right_arm', 'right_shoulder', 'right_forearm']

        for i in right_arm_list:
            armature.edit_bones[i].select_tail=True
            bpy.ops.transform.rotate(value=radians(90), orient_axis='Z', orient_type='LOCAL', constraint_axis=(False, False, True))
            armature.edit_bones[i].select_tail=False
            
        leg_list = ['left_upleg', 'right_upleg']

        for i in leg_list:
            armature.edit_bones[i].select_tail=True
            bpy.ops.transform.rotate(value=radians(180), orient_axis='Z', orient_type='LOCAL', constraint_axis=(False, False, True))
            armature.edit_bones[i].select_tail=False
            
        #pose mode bone constraints
            
        bpy.ops.object.mode_set(mode='POSE')
        
        character = cvalue.character_select
        
        #character_name_display is only used to display character names in the console
        character_name_display = (character.replace('_1', ''))
        
        if character == 'A2_1':
            C_list_shoulders = [ ("left_shoulder", "bone80"),
                         ("right_shoulder", "bone53")
                         ]
                        
            C_list_arms = [ ("left_arm", "bone81"),
                            ("left_forearm", "bone82"),
                            ("right_arm", "bone54"),
                            ("right_forearm", "bone55")
                            ]
                    
            C_list_legs = [ ("left_upleg", "bone136"),
                            ("right_upleg", "bone132")
                            ]
        elif character == '2B_1':
            C_list_shoulders = [ ("left_shoulder", "bone61"),
                         ("right_shoulder", "bone34")
                         ]
                        
            C_list_arms = [ ("left_arm", "bone62"),
                            ("left_forearm", "bone63"),
                            ("right_arm", "bone35"),
                            ("right_forearm", "bone36")
                            ]
                    
            C_list_legs = [ ("left_upleg", "bone94"),
                            ("right_upleg", "bone90")
                            ]
            
            
        print(":: Posing Bones for", character_name_display)
        
    
        
        for rein_bone, nier_bone in C_list_shoulders:
            cons = rein_name.pose.bones[rein_bone].constraints
            rein_constraint = cons.new('COPY_ROTATION')
            rein_constraint.target = nier_name
            rein_constraint.subtarget = nier_bone  
            
        for rein_bone, nier_bone in C_list_arms:
            cons = rein_name.pose.bones[rein_bone].constraints
            rein_constraint_r = cons.new('COPY_ROTATION')
            rein_constraint_r.target = nier_name
            rein_constraint_r.subtarget = nier_bone
            
            rein_constraint_l = cons.new('COPY_LOCATION')
            rein_constraint_l.target = nier_name
            rein_constraint_l.subtarget = nier_bone
            
        for rein_bone, nier_bone in C_list_legs:
            cons = rein_name.pose.bones[rein_bone].constraints
            rein_constraint = cons.new('COPY_ROTATION')
            rein_constraint.target = nier_name
            rein_constraint.subtarget = nier_bone
            rein_constraint.use_x = False
            rein_constraint.use_z = False
            rein_constraint.invert_y = True
            rein_constraint.mix_mode = 'BEFORE'
            
        
            
        #Permenantly Apply Constraints Toggle    
        if (cvalue.apply_constraints_check == True):
            arm_object = cvalue.reinobjectname
            armature_name = bpy.data.objects[arm_object] 
            
            for child in armature_name.children:
                if child.type == 'MESH':
                    child.select = True
                    bpy.context.view_layer.objects.active = child
                    bpy.ops.object.modifier_apply(modifier="Armature")
                    child.select = False
            
            bpy.context.view_layer.objects.active = rein_name        
            bpy.ops.pose.armature_apply(selected=False)
            bpy.ops.pose.select_all(action='SELECT')
            
            for bone in bpy.context.selected_pose_bones:
                constraint_list = [ c for c in bone.constraints]
                for c in constraint_list:
                    bone.constraints.remove(c)
                    
            for child in armature_name.children:
                if child.type == 'MESH':
                    child.select = True
                    bpy.context.view_layer.objects.active = child                
                    bpy.ops.object.modifier_add(type='ARMATURE')  
                    bpy.context.object.modifiers["Armature"].object = armature_name
                    child.select = False
                    
        if (cvalue.apply_constraints_check == True):
            print (":: Bones Posed + Constraints Permanantly Applied")
        else:
            print (":: Bones Posed")
                         
        
        return {'FINISHED'}     
    
    
##-----------------------------------------------------     
    
    
class MyProperties(bpy.types.PropertyGroup):
    
    rein_path : bpy.props.StringProperty(
          name = "Rein Path",
          default = "",
          description = "Choose the Rein Model Folder",
          subtype = 'DIR_PATH'
          )
          
    json_path : bpy.props.StringProperty(
          name = "JSON Path",
          default = "",
          description = "Choose your JSON file",
          subtype = 'DIR_PATH'
          )
          
    reinobjectname : bpy.props.StringProperty(
          name = "Armature Select",
          default = "",
          description = "Choose Rein Armature",
          )
          
    nierobjectname : bpy.props.StringProperty(
          name = "Armature Select",
          default = "",
          description = "Choose Rein Armature",
          )
          
    add_armature_check : bpy.props.BoolProperty(
          name = "Reapply Armature Modifier",
          description = "Reapplies the armature modifier after applying all modifiers",
          default = True
          )
    
    apply_constraints_check : bpy.props.BoolProperty(
          name = "Permenantly Apply Constraints",
          description = "Locks in the constraints",
          default = True
          )
          
    character_select : bpy.props.EnumProperty(
          name = "",
          description = "Select A2 or 2B for bonenames",
          items =  [('A2_1', "A2", ""),
                    ('2B_1', "2B", "")
                ]
          )
          
##----------------------------------------------------- 
          
class OPEN_OT_TEST(bpy.types.Operator):
    """TEST"""
    bl_label = "TEST"
    bl_idname = "open.test"
    
    def execute(self, context):
        
        scene = context.scene        
        cvalue = scene.custom_values

        arm_object = cvalue.reinobjectname
        armature_name = bpy.data.objects[arm_object]                    
        
        #actual armature
        print(armature_name)
        
        #armature name
        print(armature_name.name)

        
        return {'FINISHED'} 
    
##----------------------------------------------------- 


classes = [MyProperties, Devola_PT_Panel, DevolaOpen_PT_Panel, OPEN_OT_ScaleNIER, OPEN_OT_WeightMix, OPEN_OT_BoneRename, OPEN_OT_ConvertMesh, OPEN_OT_FixMats, OPEN_OT_BONEPOSER, OPEN_OT_TEST]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        bpy.types.Scene.custom_values = bpy.props.PointerProperty(type= MyProperties)
          


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        del bpy.types.Scene.custom_values
       
    
if __name__ == "__main__":
    register()
