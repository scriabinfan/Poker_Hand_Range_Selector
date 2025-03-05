import random
import csv
import multiprocessing
import os
import eval7

def monte_carlo_equity(hand_label, iterations=250_000): #250k simulated matches
    """Simulate hand equity over many random matchups using eval7."""
    ranks = "AKQJT98765432"
    suits = ["h", "d", "c", "s"]
    
    r1, r2 = hand_label[:2]  # Extract rank1 and rank2
    suited = "s" in hand_label  # Check if suited
    offsuit = "o" in hand_label  # Check if offsuit
    
    if suited:
        hand_cards = [eval7.Card(r1 + suits[0]), eval7.Card(r2 + suits[0])]  # Both same suit
    elif offsuit:
        hand_cards = [eval7.Card(r1 + suits[0]), eval7.Card(r2 + suits[1])]  # Different suits
    else:  # Pocket pairs (e.g., "QQ", "TT")
        hand_cards = [eval7.Card(r1 + suits[0]), eval7.Card(r1 + suits[1])]  # Different suits

    wins = 0
    
    for _ in range(iterations):
        deck = eval7.Deck()
        for card in hand_cards:
            deck.cards.remove(card)
        
        deck_list = list(deck)
        
        opponent = random.sample(deck_list, 2)  # Draw random opponent hand
        board = random.sample(deck_list, 5)  # Draw a random board
        
        our_hand = eval7.evaluate(hand_cards + board)
        opp_hand = eval7.evaluate(opponent + board)
        
        if our_hand > opp_hand:
            wins += 1

    return hand_label, wins / iterations  # Return hand & probability tuple

# Generate all 169 possible starting hands
ranks = "AKQJT98765432"
hands = []

for i, r1 in enumerate(ranks):
    for j, r2 in enumerate(ranks):
        if i < j:
            hands.append(f"{r1}{r2}s")  # Suited hands
        elif i > j:
            hands.append(f"{r2}{r1}o")  # Off-suit hands
        else:
            hands.append(f"{r1}{r2}")  # Pocket pairs

# ✅ **Parallel Processing**
if __name__ == "__main__":
    num_workers = multiprocessing.cpu_count()  # Use all available CPU cores
    with multiprocessing.Pool(num_workers) as pool:
        results = pool.map(monte_carlo_equity, hands)

    # Convert list of tuples to dictionary
    HAND_PROBABILITIES = dict(results)

    # Save to CSV
    # Save to the current directory
    output_dir = os.getcwd()  # Set the current working directory
    csv_filename = os.path.join(output_dir, "hand_probabilities.csv")

    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Hand", "Probability"])  # Write header
        for hand, probability in HAND_PROBABILITIES.items():
            writer.writerow([hand, probability])  # Write data row

    print(f"Hand probabilities saved to {csv_filename}")
