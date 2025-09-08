import os
import sys
import traci
import traci.constants as tc

# Make sure SUMO_HOME is set (usually in ~/.bashrc or ~/.zshrc)
if 'SUMO_HOME' not in os.environ:
    sys.exit("Error: Please declare environment variable 'SUMO_HOME'")

tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
sys.path.append(tools)

# Config file path
SUMO_CONFIG = os.path.join("sumo_config", "~/sumo-rl/sumo_config/sumo_config.sumocfg")

def run():
    step = 0
    vehicle_counts = []

    while step < 500:  # Run for 500 timesteps
        traci.simulationStep()

        # Get number of vehicles in simulation
        num_vehicles = traci.simulation.getMinExpectedNumber()
        vehicle_counts.append(num_vehicles)

        print(f"Step {step}: {num_vehicles} vehicles in network")

        step += 1

    return vehicle_counts


if __name__ == "__main__":
    import sumolib

    sumo_binary = sumolib.checkBinary("sumo")  # headless
    traci.start([sumo_binary, "-c", SUMO_CONFIG])

    print("Running SUMO simulation headless...")
    vehicle_data = run()

    traci.close()
    print("Simulation finished.")
