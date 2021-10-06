from pyomo.core.base.objective import Objective
from pyomo.core.base.var import Var
from pyomo.environ import ConcreteModel
from pyomo.environ import NonNegativeReals
from pyomo.environ import minimize
from pyomo.environ import Constraint
from pyomo.opt.base.solvers import SolverFactory

model = ConcreteModel()

# variable decision
model.x1 = Var(domain = NonNegativeReals)
model.x2 = Var(domain = NonNegativeReals)
model.x3 = Var(domain = NonNegativeReals)
model.x4 = Var(domain = NonNegativeReals)

# function objective
model.profit = Objective(
    expr = 2*model.x1 + 4*model.x2 + 1.5*model.x3 + model.x4,
    sense = minimize
)

# constraints
model.c1 = Constraint(expr = 2*model.x1 + 2*model.x2 + 10*model.x3 + 20*model.x4 >= 11)
model.c2 = Constraint(expr = 5*model.x1 + 20*model.x2 + 10*model.x3 + 30*model.x4 >= 70)
model.c3 = Constraint(expr = 80*model.x1 + 70*model.x2 + 10*model.x3 + 80*model.x4 >= 250)

#solve
solver = SolverFactory('cbc').solve(model).write()

print("\nValor FO: {}".format(model.profit()))
print("X1: {}".format(model.x1()))
print("X2: {}".format(model.x2()))
print("X3: {}".format(model.x3()))
print("X4: {}\n".format(model.x4()))