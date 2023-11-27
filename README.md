# FurtherPrimitivesCollection

This addon adds a submenu to the Add -> Add Mesh menu in Blender, where the user can add additional mesh and curve types to the scene. Developed on Blender version 3.6.5. The latest version can be downloaded under https://github.com/LStefanCoder/FurtherPrimitivesCollection.

## Use

The furtherprimitivescollecition.py file should be installed separately, not as a zip file. Open the Add Menu in object mode, and go to "Add mesh", where there is an additional menu item at the bottom: "Further primitives". This item contains nine options.

## Options

- **Semisphere on ground (32)**: adds a semisphere with 32-16 vertices
- **Semisphere on ground (64)**: adds a semisphere with 64-32 vertices
- **Semisphere on ground (128)**: adds a semisphere with 128-64 vertices

- **Cube with hooked vertices**: adds a cube with all vertices hooked to new object (an empty)
- **Cube on the ground with hooked vertices**: adds a cube with all vertices hooked to new object (an empty), with the origin of the cube being at the base
- **Plane with hooked vertices**: adds a plane with all vertices hooked to new object (an empty)

- **Cable (1 mm)**: adds a Bézier curve with a resolution of 24, a bevel depth of 1 mm and a bevel resolution of 8
- **Cable (2 mm)**: adds a Bézier curve with a resolution of 24, a bevel depth of 2 mm and a bevel resolution of 8
- **Cable (5 mm)**: adds a Bézier curve with a resolution of 24, a bevel depth of 5 mm and a bevel resolution of 8

## Notes

The addon only works in Object mode.

## Versions

### 1.0

Developed on Blender 3.6.5.

## License

Released under the GPL v. 3.0 license (see https://www.gnu.org/licenses/gpl-3.0.txt).
