import sys
import pandas as pd
import matplotlib.pyplot as plt

def plot_data(input_file, field_to_plot):
    df = pd.read_csv(input_file, sep='\t', parse_dates=['_time'])

    plt.figure(figsize=(12, 6))

    ue1_data = df[df['srsue_data_id'] == 'ue1_uhd']
    plt.scatter(ue1_data['_time'],
                ue1_data[field_to_plot],
                color='green',
                label='ue1_uhd',
                s=3)

    ue2_data = df[df['srsue_data_id'] == 'ue2_uhd']
    plt.scatter(ue2_data['_time'],
                ue2_data[field_to_plot],
                color='red',
                label='ue2_uhd',
                s=3)

    plt.title(f'{field_to_plot.upper()} against Time')
    plt.xlabel('Time')
    plt.ylabel(f'{field_to_plot.upper()} Value')
    plt.grid(True)
    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    
    plt.savefig(f'{field_to_plot}_vs_time.png', dpi=300, bbox_inches='tight')
    
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 plotter.py <input_file> <field_to_plot>")
        sys.exit(1)

    input_file = sys.argv[1]
    field_to_plot = sys.argv[2]

    plot_data(input_file, field_to_plot)
