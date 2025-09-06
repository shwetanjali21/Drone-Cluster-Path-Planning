# Drone Cluster Path Planning 🚀

This repository contains my solution to the *Aerokart Internship Assignment*.  
It simulates two clusters of drones moving from a start point to a target while avoiding an obstacle, and visualizes their paths.

## ✨ Features
1. Two independent drone clusters (*5 drones each*)  
- Random path generation from *Start → Target*  
- Visualization of:
  - ✅ Start point (green diamond)  
  - ✅ Target (black star)  
  - ✅ Obstacle (red X)  
  - ✅ Drone paths (Cluster A = circles, Cluster B = squares)

2. *A Path Planning (drone2.py)**  
   - Single drone uses the *A\** algorithm on a grid.  
   - Finds the shortest path while avoiding obstacles.  

3.  Multi-Drone A Clusters (drone3.py)**  
   - Two clusters (5 drones each) navigate using *A\.  
   - Each drone has a slightly different goal offset to create distinct paths.  
   - Obstacles are handled intelligently, ensuring valid routes.  

## ⚙ How to Run
Install dependency:
```bash
pip install matplotlib

