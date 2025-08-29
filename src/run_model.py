import argparse
from utils import load_swat_data, load_aquacrop_data
from optimization import build_optimization_model
import pyomo.environ as pyo

def main(input_folder, output_folder):
    # Load input data
    swat = load_swat_data(f"{input_folder}/SWAT_output.csv")
    ac = load_aquacrop_data(f"{input_folder}/AquaCrop_output.csv")

    water = swat["upstream_water"] + swat["downstream_water"]
    demand = ac["et_demand"]

    # Build model
    model = build_optimization_model(water.tolist(), demand.tolist())

    # Solve
    solver = pyo.SolverFactory("glpk")
    results = solver.solve(model)

    print("Optimization complete.")
    for t in model.T:
        print(f"Time {t+1}: Upstream={model.alloc_up[t].value:.1f}, Downstream={model.alloc_down[t].value:.1f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="data", help="Folder with input CSV files")
    parser.add_argument("--output", type=str, default="results", help="Folder to save outputs")
    args = parser.parse_args()

    main(args.input, args.output)
