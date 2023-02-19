import os
import shutil

# assign directory locations
src_dir = "E:\Minecraft_Servers\Fabric_1.19.2_0.14.13\Altis"
# Use raw string to ensure dir path with numbers is read correctly
dest_dir = r'E:\MultiMC\instances\1.19.3\.minecraft\saves\Altis' 

# if directory exists remove it
if (os.path.isdir(dest_dir)):
    print(dest_dir, "deleted")
    shutil.rmtree(dest_dir)

# copy minecraft world directory to single player world directory
shutil.copytree(src_dir, dest_dir)
print("World Copied Sucessfully")

