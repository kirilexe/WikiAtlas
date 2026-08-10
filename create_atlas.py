import os
import webbrowser

import pandas as pd
from pyvis.network import Network


def create_atlas(filename):
    net = Network(
        height="100vh",
        width="100%",
        bgcolor="#222222",
        font_color="white", # type: ignore -- ignore type check here
        directed=False,
        cdn_resources="remote",
    )

    csv_file = filename

    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)

        df["Source"] = df["Source"].astype(str).str.strip().str.capitalize()
        df["Target"] = df["Target"].astype(str).str.strip().str.capitalize()

        all_nodes_series = pd.concat([df["Source"], df["Target"]])
        degree_counts = all_nodes_series.value_counts().to_dict()

        categories = df["Source"].unique()
        palette = [
            "#7eb0d5",
            "#b2e061",
            "#bd7ebe",
            "#ffb55a",
            "#ffee65",
            "#beb9db",
            "#fdcce5",
            "#8bd3c7",
        ]

        cat_to_color = {
            cat: palette[i % len(palette)] for i, cat in enumerate(categories)
        }

        added_nodes = set()
        for _, row in df.iterrows():
            s, t = row["Source"], row["Target"]
            group_color = cat_to_color.get(s, "#ffffff")

            if s not in added_nodes:
                net.add_node(
                    s,
                    label=s,
                    color=group_color,
                    size=10 + (degree_counts.get(s, 1) * 2),
                )
                added_nodes.add(s)

            if t not in added_nodes:
                net.add_node(
                    t,
                    label=t,
                    color=group_color,
                    size=10 + (degree_counts.get(t, 1) * 2),
                )
                added_nodes.add(t)

            net.add_edge(s, t, color="#555555")

        net.force_atlas_2based()

        output_filename = "wikipedia_map.html"
        path = os.path.abspath(output_filename)
        net.write_html(path)

        print(f"Success! Map generated. {len(categories)} distinct categories found.")
        webbrowser.open("file://" + path)
    else:
        print(f"Error: {csv_file} not found.")
