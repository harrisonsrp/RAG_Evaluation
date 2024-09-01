import json
import matplotlib.pyplot as plt


def read_accuracies(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    if isinstance(data, list) and len(data) >= 10:
        return [record["Accuracy"] for record in data[:10]]  # Take only the first 10 records
    else:
        raise ValueError("JSON file does not contain enough records or the expected data structure")


file_paths = ['evaluation_chain_of_thought_prompting.json', 'evaluation_ReACT_prompting.json', 'evaluation_role_prompting.json', 'evaluation_self_consistency_prompting.json']



plt.figure(figsize=(12, 8))
# Add a horizontal line for the boundary value (85)
# plt.axhline(y=85, color='r', linestyle='--', label='Boundary (85)')


for i, file_path in enumerate(file_paths):
    accuracies = read_accuracies(file_path)
    x_values = range(1, len(accuracies) + 1)
    plt.plot(x_values, accuracies, marker='o', linestyle='-', label=file_path)


plt.xlabel('Record Index')
plt.ylabel('Accuracy')
plt.title('Accuracy Values from Multiple Prompt Engineering Techniques')
plt.ylim(min(min(accuracies) for accuracies in map(read_accuracies, file_paths)) - 20,
         max(max(accuracies) for accuracies in map(read_accuracies, file_paths)) + 10)

plt.legend(loc='lower right')
plt.savefig('accuracy_plot2.png', format='png', dpi=300)  # Save as PNG with 300 DPI


plt.grid(True)
plt.show()