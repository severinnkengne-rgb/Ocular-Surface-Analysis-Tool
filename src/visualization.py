import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_atrophy_distribution(csv_path, output_image='results/atrophy_distribution.png'):
    """
    Generates a professional histogram of Meibomian Gland Atrophy grades.
    """
    # Load data
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: {csv_path} not found.")
        return

    # Set aesthetic style
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(12, 7))
    
    # Create histogram
    n, bins, patches = plt.hist(df['Atrophy_Percentage'], bins=[0, 25, 50, 75, 100], 
                                color='#3498db', edgecolor='white', rwidth=0.85)

    # Add titles and labels (English for international standards)
    plt.title('Statistical Distribution of Meibomian Gland Atrophy (MGD1-k)', fontsize=16, pad=20)
    plt.xlabel('Atrophy Grade (%)', fontsize=12)
    plt.ylabel('Number of Images', fontsize=12)
    
    # Add grade labels on X-axis
    plt.xticks([12.5, 37.5, 62.5, 87.5], 
               ['Grade 0\n(0-25%)', 'Grade 1\n(26-50%)', 'Grade 2\n(51-75%)', 'Grade 3\n(76-100%)'])

    # Add data labels on top of bars
    for i in range(len(n)):
        if n[i] > 0:
            plt.text(bins[i] + 12.5, n[i] + 10, int(n[i]), ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    plt.savefig(output_image)
    print(f"📊 Visualization saved to {output_image}")

if __name__ == "__main__":
    # Path relative to the root of the project
    plot_atrophy_distribution('results/resultats_atrophie.csv')
