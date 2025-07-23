import numpy as np
import torch
import open3d as o3d
from plyfile import PlyData, PlyElement
from sklearn.cluster import DBSCAN  # Using actual clustering algorithm
import matplotlib.pyplot as plt

class PointCloudSegmenter:
    def __init__(self, num_classes=6):
        self.num_classes = num_classes
        self.class_names = ["DontCare", "Car", "Cyclist", "Truck", "Pedestrian", "Misc"]
        self.color_map = plt.get_cmap('tab20')

    def read_ply(self, file_path):
        """Read PLY file and return points"""
        try:
            plydata = PlyData.read(file_path)
            vertex = plydata['vertex']
            points = np.vstack([vertex['x'], vertex['y'], vertex['z']]).T
            return points.astype(np.float32)
        except Exception as e:
            print(f"Error reading PLY file: {e}")
            return None

    def cluster_points(self, points):
        """Perform actual clustering/segmentation"""
        # Normalize points
        points_norm = (points - points.mean(0)) / (points.std(0) + 1e-6)
        
        # Use DBSCAN for clustering (replace with your actual model)
        clustering = DBSCAN(eps=0.5, min_samples=10).fit(points_norm)
        labels = clustering.labels_
        
        # Convert to class labels (simple mapping for demo)
        unique_labels = np.unique(labels)
        class_labels = np.zeros_like(labels)
        for i, lbl in enumerate(unique_labels):
            class_labels[labels == lbl] = i % self.num_classes
        
        return class_labels

    def visualize(self, points, labels):
        """Visualize segmented point cloud"""
        # Assign colors based on labels
        colors = self.color_map(labels / (self.num_classes - 1))[:, :3]
        
        # Create Open3D point cloud
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points)
        pcd.colors = o3d.utility.Vector3dVector(colors)
        
        # Add coordinate frame
        coord_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0)
        
        # Custom visualization
        vis = o3d.visualization.Visualizer()
        vis.create_window(window_name='Point Cloud Segmentation', width=1024, height=768)
        vis.add_geometry(pcd)
        vis.add_geometry(coord_frame)
        
        # Set view parameters
        ctr = vis.get_view_control()
        ctr.set_front([0, 0, -1])
        ctr.set_up([0, -1, 0])
        
        vis.run()
        vis.destroy_window()

    def save_segmented_ply(self, points, labels, output_path):
        """Save segmented point cloud to PLY file"""
        colors = (self.color_map(labels / (self.num_classes - 1))[:, :3] * 255).astype(np.uint8)
        
        vertex = np.array(
            [(points[i,0], points[i,1], points[i,2], colors[i,0], colors[i,1], colors[i,2]) 
            for i in range(points.shape[0])],
            dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4'),
                   ('red', 'u1'), ('green', 'u1'), ('blue', 'u1')]
        )
        
        ply_el = PlyElement.describe(vertex, 'vertex')
        PlyData([ply_el], text=False).write(output_path)
        print(f"Saved segmented point cloud to {output_path}")

    def analyze_results(self, labels):
        """Print segmentation statistics"""
        unique, counts = np.unique(labels, return_counts=True)
        print("\nSegmentation Results:")
        print("--------------------")
        for cls, cnt in zip(unique, counts):
            print(f"{self.class_names[cls]:<15}: {cnt:>6} points ({cnt/len(labels):.1%})")

def main():
    segmenter = PointCloudSegmenter()
    
    # Load point cloud
    input_path = "/home/intern/Desktop/zed_out.ply"  # Change to your file path
    points = segmenter.read_ply(input_path)
    if points is None:
        return
    
    print(f"Loaded {points.shape[0]} points")
    
    # Perform segmentation
    labels = segmenter.cluster_points(points)
    
    # Visualize results
    segmenter.visualize(points, labels)
    
    # Save results
    output_path = input_path.replace(".ply", "_segmented.ply")
    segmenter.save_segmented_ply(points, labels, output_path)
    
    # Show statistics
    segmenter.analyze_results(labels)

if __name__ == "__main__":
    main() 
