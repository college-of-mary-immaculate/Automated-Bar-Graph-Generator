import os
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import numpy as np  # type: ignore
import time

def generate_bar_graphs(excel_file):
    try:
        df = pd.read_excel(excel_file)
        if df.empty:
            print(f"No data found in {excel_file}.")
            return

        base_output_dir = "Automated Bar Graphs"
        if not os.path.exists(base_output_dir):
            os.makedirs(base_output_dir)

        file_name_without_ext = os.path.splitext(os.path.basename(excel_file))[0]
        output_dir = os.path.join(base_output_dir, file_name_without_ext)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        if len(df.columns) < 2:
            print(f"Insufficient columns in {excel_file}.")
            return

        for index, row in df.iterrows():
            try:
                plt.figure(figsize=(10, 6))
                row_data = row[1:]

                if row_data.empty:
                    print(f"No data to plot for row '{row.iloc[0]}'.")
                    continue

                # Sort the data in increasing order
                row_data = row_data.sort_values()

                colors = plt.get_cmap('tab20', len(row_data))
                row_data.plot(kind='bar', title=row.iloc[0], color=[colors(i) for i in np.arange(len(row_data))])
                plt.xlabel('Column')
                plt.ylabel('Value')
                plt.xticks(rotation=45, ha='right')

                safe_title = row.iloc[0].replace(' ', '_').replace('/', '_')
                image_path = os.path.join(output_dir, f'{safe_title}_bar_graph.jpg')
                plt.savefig(image_path)
                plt.close()
                print(f"Bar graph for row '{row.iloc[0]}' saved as {image_path}")

            except Exception as e:
                print(f"Error generating graph for row '{row.iloc[0]}': {e}")

    except Exception as e:
        print(f"Error reading {excel_file}: {e}")

if __name__ == "__main__":
    watched_files = set()
    print("Monitoring for new Excel files...")
    while True:
        current_files = {file for file in os.listdir() if file.endswith('.xlsx')}
        new_files = current_files - watched_files

        for new_file in new_files:
            print(f"Processing {new_file}...")
            generate_bar_graphs(new_file)

        watched_files.update(new_files)
        time.sleep(0)
