import pyomo.environ as pyo

def build_optimization_model(water, demand):
    """Simple optimization model: allocate water to minimize unmet demand."""
    model = pyo.ConcreteModel()

    # Index = time steps
    T = list(range(len(water)))
    model.T = pyo.Set(initialize=T)

    # Decision variables
    model.alloc_up = pyo.Var(model.T, domain=pyo.NonNegativeReals)
    model.alloc_down = pyo.Var(model.T, domain=pyo.NonNegativeReals)

    # Constraint: allocation <= available water
    def water_balance_rule(m, t):
        return m.alloc_up[t] + m.alloc_down[t] <= water[t]
    model.water_balance = pyo.Constraint(model.T, rule=water_balance_rule)

    # Objective: minimize unmet demand
    def objective_rule(m):
        unmet = sum(max(0, demand[t] - (m.alloc_up[t] + m.alloc_down[t])) for t in m.T)
        return unmet
    model.obj = pyo.Objective(rule=objective_rule, sense=pyo.minimize)

    return model
