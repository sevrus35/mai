import matplotlib.pyplot as plt
import numpy as np


def simulate_motion(x0, y0, vx, vy, g, t):
    time = np.linspace(0, t, 1000)
    x = x0 + vx * time
    y = y0 + vy * time - 0.5 * g * time ** 2
    y = np.clip(y, 0, np.inf)
    return x, y

def save_to_file(x, y, filename):
    with open(filename, 'w') as file:
        for i in range(len(x)):
            file.write(f"{x[i]}, {y[i]}\n")

def draw_arc(x, y):
    plt.plot(x, y)
    plt.xlabel('Horizontal Distance (m)')
    plt.ylabel('Vertical Distance (m)')
    plt.title('Projectile Motion')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":

  while True:
    try:
      x0 = float(input("Enter initial horizontal position (m): "))
      y0 = float(input("Enter initial vertical position (m): "))
      vx = float(input("Enter initial horizontal velocity (m/s): "))
      vy = float(input("Enter initial vertical velocity (m/s): "))
      g = 9.8 
      t = float(input("Enter simulation time (seconds): "))
      break  
    except ValueError:
      print("Invalid input. Please enter numbers only.")
