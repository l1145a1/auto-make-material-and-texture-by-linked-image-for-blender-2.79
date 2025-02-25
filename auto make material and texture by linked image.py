import bpy

# Pastikan objek dalam Object Mode
if bpy.context.object.mode == 'OBJECT':
    # Ambil objek yang dipilih
    selected_objects = bpy.context.selected_objects

    # Iterasi melalui setiap objek yang dipilih
    for obj in selected_objects:
        # Pastikan objek tersebut adalah mesh
        if obj.type == 'MESH':
            # Cek UV Map aktif
            if obj.data.uv_textures.active:
                uv_layer = obj.data.uv_textures.active.data

                # Membuat dictionary untuk menyimpan material dan gambar terkait
                material_dict = {}

                # Iterasi melalui faces untuk mendeteksi gambar yang digunakan
                for face in obj.data.polygons:
                    image = uv_layer[face.index].image  # Gambar yang terlink dengan face ini
                    if image:
                        if image.name not in material_dict:
                            # Jika material belum ada, buat material dan tekstur
                            new_material = bpy.data.materials.new(name="Material_" + image.name)
                            obj.data.materials.append(new_material)

                            # Buat tekstur baru dan link ke material
                            new_texture = bpy.data.textures.new(name="Texture_" + image.name, type='IMAGE')
                            new_texture.image = image

                            # Tambahkan tekstur ke material
                            texture_slot = new_material.texture_slots.add()
                            texture_slot.texture = new_texture
                            texture_slot.texture_coords = 'UV'

                            # Simpan material dalam dictionary berdasarkan gambar
                            material_dict[image.name] = new_material

                        # Assign material berdasarkan gambar yang terlink
                        material_index = obj.data.materials.find(material_dict[image.name].name)
                        if material_index != -1:
                            obj.data.polygons[face.index].material_index = material_index

                print("Materials and textures assigned for {0} based on linked images.".format(obj.name))
            else:
                print("No active UV Map found for {0}. Cannot link images.".format(obj.name))
        else:
            print("{0} is not a mesh object.".format(obj.name))
else:
    print("Switch to Object Mode to run this script.")
