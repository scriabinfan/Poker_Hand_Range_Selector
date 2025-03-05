**# Poker_Hand_Range_Selector**
A poker tournament hand range selector based on the number of Big Blinds (BBs) a player has.

**Overview**
In poker tournaments, effective decision-making is crucial, especially when considering hand ranges relative to your stack size measured in Big Blinds (BBs). This tool assists players in selecting appropriate hand ranges based on their current BB count, enhancing strategic play.

**Features**
Hand Range Selection: Provides recommended hand ranges tailored to various BB levels.
Monte Carlo Simulations: Utilizes Monte Carlo methods to estimate hand probabilities and outcomes.
Hand Probabilities: Includes precomputed hand probabilities for quick reference.

**Files**
montecarlo_hands.py: Script implementing Monte Carlo simulations to evaluate hand strengths and probabilities.
poker_hands.py: Contains functions and classes related to poker hand evaluations.
poker_range.html: HTML file presenting visual representations of recommended hand ranges based on BB count.
hand_probabilities.csv: CSV file with precomputed probabilities for different hands, serving as a reference for decision-making.

**Usage**
Clone the Repository: Clone this repository to your local machine using

git clone https://github.com/andreboiko777/Poker_Hand_Range_Selector.git


**Run Simulations**: Execute montecarlo_hands.py to perform Monte Carlo simulations and assess hand strengths.
View Hand Ranges: Open poker_range.html in a web browser to explore recommended hand ranges corresponding to different BB levels.
