import json
import matplotlib.pyplot as plt
import numpy as np

# List of dataset filenames
filenames = [
    'chain_of_thought.json',
    'ReACT.json',
    'role_prompting.json',
    'self_consistency.json'
]

# Define colors for each file and evaluation type
file_colors = {
    'chain_of_thought.json': {'True': 'blue', 'False': 'lightblue'},
    'ReACT.json': {'True': 'green', 'False': 'lightgreen'},
    'role_prompting.json': {'True': 'orange', 'False': 'lightcoral'},
    'self_consistency.json': {'True': 'red', 'False': 'pink'}
}

# Initialize a dictionary to store counts for each file
file_counts = {filename: {'True': 0, 'False': 0} for filename in filenames}

# Read and aggregate data from each file
for filename in filenames:
    with open(filename, 'r') as file:
        data = json.load(file)
        for entry in data:
            if "Binary Evaluation" in entry:
                if entry["Binary Evaluation"]:
                    file_counts[filename]['True'] += 1
                else:
                    file_counts[filename]['False'] += 1
            else:
                print(f"Warning: 'Binary Evaluation' key missing in file {filename}")

# Prepare data for plotting
file_labels = list(file_counts.keys())
true_counts = [file_counts[file]['True'] for file in file_labels]
false_counts = [file_counts[file]['False'] for file in file_labels]

# Create bar chart
x = np.arange(len(file_labels))  # The label locations
width = 0.35  # The width of the bars

fig, ax = plt.subplots(figsize=(16, 11))

# Create bars for each file with custom colors for True and False
for i, file in enumerate(file_labels):
    color_true = file_colors.get(file, {'True': 'gray', 'False': 'lightgray'})['True']
    color_false = file_colors.get(file, {'True': 'gray', 'False': 'lightgray'})['False']
    ax.bar(x[i] - width/2, true_counts[i], width, label=f'{file} True', color=color_true)
    ax.bar(x[i] + width/2, false_counts[i], width, label=f'{file} False', color=color_false)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('s')
ax.set_ylabel('Number of Instances')
ax.set_title('Number of True and False Evaluations Across Datasets')
ax.set_xticks(x)
ax.set_xticklabels(file_labels, rotation=45, ha='right')

# Handle the legend to avoid duplication
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys())
plt.savefig('accuracy_bar_plot.png', format='png', dpi=500)

plt.tight_layout()
plt.show()
