# Blender Auto Material Assignment Script

## Overview
This Blender Python script automates the process of assigning materials and textures to selected mesh objects based on their linked images. It ensures that each unique image used in the object's UV map is assigned to a corresponding material.

## Features
- Automatically detects selected mesh objects.
- Checks for an active UV map.
- Creates new materials based on linked images.
- Generates textures and assigns them to the corresponding materials.
- Applies the materials to faces based on the linked image.

## Prerequisites
- Blender (compatible with Blender 2.8 and above)
- Basic knowledge of Blender scripting (optional)

## Installation
1. Open Blender.
2. Switch to the **Scripting** tab.
3. Create a new script and paste the provided code.
4. Ensure your objects are selected in **Object Mode**.
5. Run the script.

## Usage
1. Select the mesh objects in **Object Mode**.
2. Run the script from the **Scripting** editor.
3. The script will create materials and assign textures based on linked images.
4. Check the **Material Properties** tab to see the assigned materials.

## Notes
- Ensure that the objects have an active UV map with linked images.
- The script does not work in **Edit Mode**.
- Only mesh objects are processed.

## Author
L1145A1
