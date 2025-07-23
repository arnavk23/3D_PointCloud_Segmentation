import open3d as o3d
import numpy as np

def load_and_segment_pcd(file_path):
    # Load PLY point cloud
    pcd = o3d.io.read_point_cloud(file_path)
    points = np.asarray(pcd.points)

    # Simulate semantic labels (e.g., 0–3 labels)
    num_labels = 4
    labels = np.random.randint(0, num_labels, size=(points.shape[0],))

    # Assign colors based on labels
    color_map = np.array([
        [1, 0, 0],    # red
        [0, 1, 0],    # green
        [0, 0, 1],    # blue
        [1, 1, 0],    # yellow
    ])
    colors = color_map[labels]
    pcd.colors = o3d.utility.Vector3dVector(colors)

    return pcd

if __name__ == "__main__":
    pcd = load_and_segment_pcd("zed_output.ply")
    o3d.visualization.draw_geometries([pcd], window_name="Dummy Segmentation")

