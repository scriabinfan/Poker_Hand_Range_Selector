import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")  # Use a non-GUI backend
import seaborn as sns
import itertools
import io
from flask import Flask, request, jsonify, send_file
import random
from flask_cors import CORS
import pandas as pd
import os

# creating a poker hand matrix
def create_poker_hand_matrix():
    ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    hands = [[None] * 13 for _ in range(13)]
    
    for i, r1 in enumerate(ranks):
        for j, r2 in enumerate(ranks):
            if i < j and not (r1 in "T98372" and r2 in "32"):  # Remove specific weak suited hands
                hands[i][j] = f"{r1}{r2}s"  # Suited hands
            elif i > j and not (r1 in "JT98765432" and r2 in "JT98765432"):  # Remove low unpaired offsuit hands
                hands[i][j] = f"{r2}{r1}o"  # Off-suited hands
            else:
                hands[i][j] = f"{r1}{r2}"  # Pocket pairs
    
    return hands

# creating a plot for hand ranges
def plot_hand_range(selected_hands, title="Basic Raise/Call/Fold Poker Hand Selection"):
    hands = create_poker_hand_matrix()  # Get the hand matrix
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Define colors for Raise (Green) and Fold (Red)
    raise_color = sns.color_palette("Greens", as_cmap=True)
    fold_color = sns.color_palette("Reds", as_cmap=True)
    
    for i in range(13):
        for j in range(13):
            hand = hands[12-i][j]
            if hand:
                color = raise_color(0.6) if hand in selected_hands else fold_color(0.6)
                ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color, edgecolor="black", lw=0.5))
                ax.text(j + 0.5, i + 0.5, hand, ha="center", va="center", fontsize=10, color="white")
    
    # Set labels and formatting
    ax.set_xticks(range(13))
    ax.set_yticks(range(0))
    ax.set_xticklabels(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])
    ax.set_yticklabels([])
    ax.set_xlim(0, 13)  # Fix x-axis to show all columns
    ax.set_ylim(0, 13)  # Fix y-axis to show all rows
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.grid(False)
    
    # Add a legend
    from matplotlib.patches import Patch
    legend_handles = [
        Patch(color=raise_color(0.6), label="Raise/Call"),
        Patch(color=fold_color(0.6), label="Fold")
    ]
    ax.legend(handles=legend_handles, loc="upper left", bbox_to_anchor=(1, 1), title="Action")

    #generating a png
    img_io = io.BytesIO()
    plt.savefig(img_io, format='png', bbox_inches='tight')
    plt.close(fig)
    img_io.seek(0)
    return img_io

# hand ranking probabilities
output_dir = os.getcwd()
csv_mc_name = os.path.join(output_dir, "hand_probabilities.csv")
df_mc = pd.read_csv(csv_mc_name)
monte_carlo_hands = dict(zip(df_mc["Hand"], df_mc["Probability"]))

def generate_bb_based_range(bb, variance_level=0.1):
    """Generates a poker hand range based on BB size and variance level."""
    
    # Base selection probability
    if bb >= 50:  # Deep stack: Wider range
        selection_threshold = df_mc["Probability"].quantile(0.4)
        # determines how strict the hand selection is
        # it is a cutoff probability
        # lower -> wider selection
        # higher -> tigther range

    elif 20 <= bb < 50:  # Mid stack: Moderate range
        selection_threshold = df_mc["Probability"].quantile(0.5)
    elif 10 <= bb < 20:  # Short stack: Tighter range
        selection_threshold = df_mc["Probability"].quantile(0.6)
    else:  # <10 BBs (Hyper-aggressive push/fold)
        selection_threshold = df_mc["Probability"].quantile(0.7)

#adjust threshold based on hand strength and variance
    selected_hands = {}
    
# Logarithmic scaling so it prevents high variance from selecting all hands
 # Ensure variance impacts different stack sizes differently
    adjusted_threshold = selection_threshold - (variance_level * 0.05)
    adjusted_threshold = max(0.3, min(adjusted_threshold, 0.85))  # Ensure within reasonable bounds
    
    # Hand Selection Based on Monte Carlo Probabilities and adjusted_threshhold
    selected_hands = {hand for hand, prob in monte_carlo_hands.items() if prob >= adjusted_threshold}
    return selected_hands
# getting the input for ranges
# to work with the HTML page
app = Flask(__name__)
CORS(app)
@app.route('/get_range', methods=['GET'])
def get_range():
    try:
        bb = int(request.args.get("bb", 20))
        variance = float(request.args.get("variance", 0.1))
        print(f"Received BB: {bb}, Variance: {variance}") #print in console
        hand_range = generate_bb_based_range(bb, variance_level=variance)
        img_io = plot_hand_range(hand_range)
        return send_file(img_io, mimetype='image/png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
