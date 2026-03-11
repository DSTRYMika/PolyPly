import trimesh
import numpy as np
from collections import deque


class Object_Cleaner_And_Error_Checker():
    def __init__(self,object_folder: str, std_threshold : int) :
        self.object_folder = object_folder
        self.mesh = mesh = trimesh.load("model.obj", force='mesh')
        # force='mesh' fusionne tout en un seul Trimesh triangulé
        self.std_threshold = std_threshold

    def cleanup_mesh (self) :
        self.mesh.remove_unreferenced_vertices()

        #check if mesh is watertight
        if self.mesh.is_watertight :
            print("Mesh is watertight")
        else :
            raise "Mesh is not watertight"

        # check if mesh is valid

        if self.mesh.is_valid :
            print("Mesh is valid")
        else :
            raise "Mesh is not valid"

        # Full report
        print(trimesh.repair.broken_faces(self.mesh))


    def get_optimal_radius(self):
        # Longueur de toutes les arêtes
        edges = self.mesh.edges_unique
        v0 = self.mesh.vertices[edges[:, 0]]
        v1 = self.mesh.vertices[edges[:, 1]]
        edge_lengths = np.linalg.norm(v1 - v0, axis=1)

        avg_edge_length = np.mean(edge_lengths)

        # Règle standard : radius = 2x à 5x la longueur moyenne des arêtes
        radius = avg_edge_length * 2.0
        return radius


    def render_gaussian_curve(self):
        radius = self.get_optimal_radius()
        self.curve = trimesh.curvature.discrete_gaussian_curvature_measure(
            self.mesh, self.mesh.vertices, radius=radius
        )


