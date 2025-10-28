import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

def plot_data_from_file(filename="./logs/zweipunktregelung.log"):
    x_data = []
    y_data = []
    power_data = []
    start_temp = "N/A"

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

            if not lines:
                print(f"Error: The file '{filename}' is empty.")
                return

            start_temp = lines[0].strip()
            data_lines = lines[1:]

            for line in data_lines:
                parts = line.strip().split()
                if len(parts) >= 3:
                    try:
                        x_data.append(float(parts[0]))
                        power_data.append(float(parts[1]))
                        y_data.append(float(parts[2]))
                    except ValueError:
                        print(
                            f"Warning: Skipping line due to non-numeric data: {line.strip()}"
                        )
                        continue
                else:
                    print(
                        f"Warning: Skipping line due to insufficient columns (expected 3): {line.strip()}"
                    )
                    continue

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please ensure it exists.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    if not x_data:
        print("No valid data points found to plot.")
        return

    x_np = np.array(x_data)
    y_np = np.array(y_data)

    x_smooth = np.linspace(x_np.min(), x_np.max(), 500 if len(x_np) > 1 else 2)

    try:
        spl = make_interp_spline(x_np, y_np, k=3)
    except ValueError:
        print("Not enough data points for cubic spline. Using linear plot.")
        x_smooth = x_np
        y_smooth = y_np
    else:
        y_smooth = spl(x_smooth)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True, gridspec_kw={'height_ratios': [3, 1]})

    ax1.plot(
        x_smooth,
        y_smooth,
        marker="",
        linestyle="-",
        linewidth=2,
        color="forestgreen",
        label="Temperature Difference",
    )

    ax1.axhline(3.0, color='red', linestyle='--', linewidth=1.5, label='$T_z$')
    ax1.axhline(3.2, color='darkorange', linestyle=':', linewidth=1, label='Hysteresis Bounds')
    ax1.axhline(2.8, color='darkorange', linestyle=':', linewidth=1)
    
    ax1.set_xlim(left=0)

    ax1.set_ylabel("Temperature Difference")

    ax1.grid(True, linestyle="--", alpha=0.6)

    ax1.legend()

    ax2.step(
        x_data,
        power_data,
        where='post',
        color='navy',
        label="Power Level"
    )

    ax2.set_xlabel("Time (min)")
    ax2.set_ylabel("Power Level")
    ax2.set_yticks([0, 50])
    ax2.set_ylim(-5, 55)

    ax2.grid(True, linestyle="--", alpha=0.6)

    plt.tight_layout()

    plt.savefig("./assets/zweipunktregelung-messung.png")


if __name__ == "__main__":
    plot_data_from_file()

