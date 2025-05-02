import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
file_path = 'output_cleaned.xlsx'
data = pd.read_excel(file_path)

# Plot the Campbell diagram
plt.figure(figsize=(11, 6))

# Create a new DataFrame from column 5 to the end
new_data = data.iloc[:, 4:]

# Plot scatter with the 1st row as x-axis and the rest as y-axis
x_values = new_data.columns

for i in range(0, new_data.shape[0]):
    y_values = new_data.iloc[[i]]
    plt.plot(x_values, y_values.values.flatten(), label=f'Mode {i+1}', marker='o', linestyle='-')

# Add labels, legend, and title
plt.xlabel('Speed (RPM)')
plt.ylabel('Frequency (Hz)')
plt.title('Campbell Diagram')
plt.legend()
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()