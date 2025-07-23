import pyzed.sl as sl

# Initialize camera
init = sl.InitParameters()
init.camera_resolution = sl.RESOLUTION.HD720
init.depth_mode = sl.DEPTH_MODE.ULTRA
zed = sl.Camera()
status = zed.open(init)
if status != sl.ERROR_CODE.SUCCESS:
    print(repr(status))
    exit()

# Grab frame
runtime = sl.RuntimeParameters()
zed.grab(runtime)

# Retrieve point cloud
point_cloud = sl.Mat()
zed.retrieve_measure(point_cloud, sl.MEASURE.XYZRGBA)

# Save point cloud
point_cloud_filename = "pointcloud.ply"
point_cloud.write(point_cloud_filename)

print(f"Point cloud saved to {point_cloud_filename}")
zed.close()

