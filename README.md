# Traffic Simulation Model

## Project Overview
Traffic congestion is a major challenge in urban planning, leading to economic losses, environmental impact, and decreased quality of life. This project aims to develop a Python-based traffic simulation model that realistically captures vehicular movement, lane-changing behaviors, and traffic signal interactions. The simulation will be used to analyze traffic dynamics and test optimization strategies.

## Implementation Goals
- **Develop a modular traffic simulation system** using Python.
- **Incorporate key traffic behaviors**, such as lane changes, speed variations, and signal responses.
- **Utilize an agent-based modeling approach** to simulate individual vehicle interactions.
- **Provide visualization** of traffic flow using Pygame.
- **Validate simulation results** against real-world traffic data.

## Planned Features
- Vehicle movement simulation with adjustable parameters.
- Traffic signal management and intersection controls.
- Lane-changing behavior based on predefined decision models.
- Visualization of simulation using Pygame.
- Data collection for performance metrics (e.g., congestion, vehicle throughput).

## Tools & Libraries
- **Programming Language**: Python
- **Libraries**:
  - `pygame` (Graphical visualization of the simulation)
  - `numpy` (Numerical computations for vehicle behaviors and optimizations)
  - `random` (Generating vehicle speeds and lane assignment)
  - `matplotlib` (Future data visualization and performance metrics)
- **Version Control**: Git & GitHub (for code management and collaboration)

## Installation & Usage Instructions
### Prerequisites
Ensure you have Python installed on your system (version 3.8 or later). Install the required dependencies:
```bash
pip install pygame numpy
```
## Code Overview
### `main.py`
- Entry point for running the simulation.
- Imports `TrafficSimulator` from `trafficSim.py` and starts the simulation.

### `traffic_simulator.py`
- Defines the `TrafficSimulator` class to manage the simulation loop.
- Uses the `Road` class to manage vehicle movement.
- Vehicles spawn at random intervals and move downward.

### `Vehicle Class`
- Each vehicle has:
  - Randomized speed (within a defined range)
  - Lane-based movement logic
  - Visual representation via `pygame`.

### `Road Class`
- Handles road structure and manages vehicle movements.
- Vehicles are randomly added to lanes and removed once they exit the screen.

## Future Extensions
- Integration of real-time traffic data.
- Advanced AI-based traffic signal control.
- Multi-agent system with autonomous vehicle interactions.
- Lane-changing mechanics and congestion-based rerouting.
