# **Optimized Particle Collision Simulation**  

## **Overview**  
This project implements an optimized **particle collision simulation** using **grid-based spatial partitioning** to improve performance. Instead of checking all particle pairs (**O(n²)** complexity), the simulation reduces unnecessary calculations by limiting collision checks to **local neighboring cells**, achieving an **O(n) complexity**.  

The project supports real-time visualization using **Matplotlib animation** and ensures accurate collision handling using **elastic collision physics**.  

## **Features**  
✅ **Optimized Grid-Based Collision Detection** – Faster than brute-force methods  
✅ **Real-Time Visualization** – Uses Matplotlib for dynamic animations  
✅ **Efficient Memory Management** – Stores particles in a spatial grid  
✅ **Scalable Performance** – Handles thousands of particles smoothly  

## **Implementation Details**  
- **Spatial Partitioning:** The simulation space is divided into grid cells to limit collision checks.  
- **Collision Detection:** Uses **Euclidean distance** to determine collisions.  
- **Collision Resolution:** Applies **elastic collision physics** to update velocities.  
- **Animation:** Uses **Matplotlib’s FuncAnimation** to visualize particle movement.  
-**Visulaization:** Uses **PyGame** to visualiza the particle collision.


## **Setup & Usage**  
### **1. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **2. Run the Simulation**  
```bash
python CollisionCode.py
```

### **3. View the Animation**  
The simulation will generate an **animated visualization** of the particles in motion.

## **Performance Optimization**  
🔹 **Brute-Force Approach (O(n²)):** Inefficient for large particle counts.  
🔹 **Grid-Based Optimization (O(n)):** Particles only check for collisions within **neighboring cells**, improving speed.  

## **Contributed By**  
💡 **Tigist Wondimneh Birhan** – GSR/5506/17