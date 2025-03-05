# Poker_Hand_Range_Selector <br>
A poker tournament hand range selector based on the number of Big Blinds (BBs). <br>
<p><strong>Note:</strong> This is a very basic project, developed just to better understand Monte Carlo simulations. I was also curious to see how eval7 works. I've been playing a lot of poker recently, and I wanted to do something related.</p>

<p>So many variables are not considered in this project, such as:</p>
<ul>
    <li><strong>Table positioning:</strong> The importance of early, middle, and late position when making decisions.</li>
    <li><strong>Opponent tendencies:</strong> How tight or loose opponents play, their aggression levels, and exploitability.</li>
    <li><strong>ICM considerations:</strong> Tournament-specific strategies like Independent Chip Model (ICM), which affect decision-making in later stages.</li>
    <li><strong>Bet sizing strategies:</strong> The impact of different bet sizes on the effectiveness of a play.</li>
    <li><strong>Equity realization:</strong> The ability to realize the expected value of a hand post-flop rather than just pre-flop probabilities.</li>
    <li><strong>Multi-way pots:</strong> Hands that perform differently in multi-way situations compared to heads-up play.</li>
    <li><strong>Exploitative vs. GTO play:</strong> How a Game Theory Optimal (GTO) approach differs from an exploitative approach against specific opponents.</li>
</ul>

<p>This project is a simplified model and does not account for these nuances. However, it serves as a foundation for deeper exploration into poker hand range selection and probabilistic decision-making.</p>

**Overview** <br>
In poker tournaments, effective decision-making is crucial, especially when considering hand ranges relative to your stack size measured in Big Blinds (BBs). This tool assists players in selecting appropriate hand ranges based on their current BB count, enhancing strategic play.

**Features** <br>
_Hand Range Selection_: Provides recommended hand ranges tailored to various BB levels. <br>
_Monte Carlo Simulations_: Utilizes Monte Carlo methods to estimate hand probabilities and outcomes. The simulation runs 250,000 iterations in heads-up scenarios to provide probabilistic insights into hand strengths. <br>
_Hand Probabilities_: Includes precomputed hand probabilities for quick reference.

**Files** <br>
montecarlo_hands.py: Script implementing Monte Carlo simulations to evaluate hand strengths and probabilities.<br>
poker_hands.py: Contains functions and classes related to poker hand evaluations.<br>
poker_range.html: HTML file presenting visual representations of recommended hand ranges based on BB count.<br>
hand_probabilities.csv: CSV file with precomputed probabilities for different hands, serving as a reference for decision-making.<br>

**Usage** <br>
Clone the Repository: Clone this repository to your local machine using:

<code> git clone https://github.com/andreboiko777/Poker_Hand_Range_Selector.git </code>


**Run Simulations**: <br>
_Execute montecarlo_hands.py_ to perform Monte Carlo simulations and assess hand strengths. <br>
_View Hand Ranges_: Open poker_range.html in a web browser to explore recommended hand ranges corresponding to different BB levels.
