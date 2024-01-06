<br/>
<p align="center">
  <a href="https://github.com/ChengaFEI/dqn-driven-route-planner">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Intelligent Route Planner</h3>

  <p align="center">
    Deep-Q-Networks Implementation Project
    <br/>
    <br/>
    <a href="https://github.com/ChengaFEI/dqn-driven-route-planner/issues">Report Bug</a>
    .
    <a href="https://github.com/ChengaFEI/dqn-driven-route-planner/issues">Request Feature</a>
  </p>
</p>

<!-- ![Downloads](https://img.shields.io/github/downloads/ChengaFEI/ReadME-Generator/total) -->

![Contributors](https://img.shields.io/github/contributors/ChengaFEI/dqn-driven-route-planner?color=dark-green) ![Forks](https://img.shields.io/github/forks/ChengaFEI/dqn-driven-route-planner?style=social) ![Stargazers](https://img.shields.io/github/stars/ChengaFEI/dqn-driven-route-planner?style=social) ![Issues](https://img.shields.io/github/issues/ChengaFEI/dqn-driven-route-planner) ![License](https://img.shields.io/github/license/ChengaFEI/dqn-driven-route-planner)

## Table Of Contents

- [Table Of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Deep Q-Networks](#deep-q-networks)
- [Project Structure](#project-structure)
- [Built With](#built-with)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
  - [Creating A Pull Request](#creating-a-pull-request)
- [License](#license)
- [Authors](#authors)
- [Acknowledgements](#acknowledgements)

## About The Project

This project applies the `Deep-Q-Networks` model to train an agent to find the most energy efficient route between two points in a city. The agent is trained to learn the optimal route by interacting with the environment, which is a city map with roads. The model also extracts environment parameters (such as wind, slope, topography) from Google Maps API. The agent is rewarded for finding the most energy efficient route and penalized for taking longer routes.

### Deep Q-Networks

**Q-Learning**: It is a specific method in RL. It involves learning a function called the `Q-function`, denoted as `Q(s,a)`. This function estimates the total reward an agent can expect to receive by taking action a in state s, and then following a certain policy (a strategy for choosing actions) thereafter. The main challenge in Q-learning is to accurately estimate the Q-values for each state-action pair.

**Deep Q-Networks**: Traditional Q-learning struggles with environments that have a large number of states and actions, as it becomes impractical to store and update the Q-values for every possible state-action pair. DQN solves this problem by using a neural network to approximate the Q-function. The network takes the state as input and outputs the estimated Q-values for each action.

**Experience Replay**: DQN uses a technique called experience replay to improve the training process. Instead of training the network in the order experiences are observed, experiences (state, action, reward, next state) are stored in a replay buffer. The network is then trained on random batches from this buffer, which helps to break the correlation between consecutive training samples and leads to more stable learning.

**Q-Target Network Pair**: In DQN, two networks are used: one for the current iteration of the Q-function and another for the Q-targets, which are used to compute the error for updating the first network. The Q-target network's weights are fixed for a number of steps and then updated with the weights of the current Q-function network. This reduces the variance of the target, aiding in stable learning.

## Project Structure

```sh
.
│── .gitignore
├── LICENSE
├── README.md
├── images  # images for README.md
│   └── logo.png
├── poetry.lock
├── pyproject.toml  # project dependencies
└── src  # source code
    ├── components  # components of DQN
    │   ├── Battery.py  # vehicle battery modules
    │   ├── Context.py  # environment context modules
    │   └── Energy.py  # energy consumption modules
    ├── main.py  # main function
    └── networks  # DQN networks
        └── DQN.py  # network modules
```

## Built With

- [`python`](https://www.python.org/)
- [`tensorflow`](https://www.tensorflow.org/)
- [`numpy`](https://numpy.org/)
- [`pandas`](https://pandas.pydata.org/)
- [`haversine`](https://pypi.org/project/haversine/)
- [`requests`](https://docs.python-requests.org/en/master/)
- [`urllib`](https://docs.python.org/3/library/urllib.html)

### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/ChengaFEI/dqn-driven-route-planner.git
   ```

2. Install [Poetry](https://python-poetry.org/docs/) dependency management tool

   ```sh
   pip install poetry
   ```

3. Create a [virtual environment](https://python-poetry.org/docs/)

   ```sh
   poetry install
   ```

4. Set up [Google Maps API](https://developers.google.com/maps/documentation/directions/overview) key

   ```sh
   export GOOGLE_MAPS_API_KEY=<your-api-key>
   ```

## Usage

Run the main function

```sh
python src/main.py
```

## Roadmap

See the [open issues](https://github.com/ChengaFEI/dqn-driven-route-planner/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

- If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/ChengaFEI/dqn-driven-route-planner/issues/new) to discuss it, or directly create a pull request after you edit the _README.md_ file with necessary changes.
- Please make sure you check your spelling and grammar.
- Create individual PR for each suggestion.
- Please also read through the [Code Of Conduct](https://github.com/ChengaFEI/dqn-driven-route-planner/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/ChengaFEI/dqn-driven-route-planner/blob/main/LICENSE) for more information.

## Authors

- **Cheng Fei** - _MEng CS student_ - [Cheng Fei](https://github.com/ChengaFEI) - _Built the project_

## Acknowledgements
