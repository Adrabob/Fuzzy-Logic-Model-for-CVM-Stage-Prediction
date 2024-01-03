import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt  

# Define the universe of discourse for concavity and shape
concavity = ctrl.Antecedent(np.arange(0, 11, 1), 'concavity')
shape = ctrl.Antecedent(np.arange(0, 11, 1), 'shape')
cvm_stage = ctrl.Consequent(np.arange(0, 8, 1), 'cvm_stage')

# Adjust membership functions 
concavity['Flat'] = fuzz.trimf(concavity.universe, [0, 0, 5])  
concavity['Concave'] = fuzz.trimf(concavity.universe, [2, 5, 10])

shape['Trapezoidal'] = fuzz.trimf(shape.universe, [0, 0, 4])
shape['Horizontal'] = fuzz.trimf(shape.universe, [2, 4, 6])
shape['Square'] = fuzz.trimf(shape.universe, [4, 6, 8])
shape['Vertical'] = fuzz.trimf(shape.universe, [6, 8, 10])

cvm_stage['1'] = fuzz.trimf(cvm_stage.universe, [0, 1, 2])
cvm_stage['2'] = fuzz.trimf(cvm_stage.universe, [1, 2, 3])
cvm_stage['3'] = fuzz.trimf(cvm_stage.universe, [2, 3, 4])
cvm_stage['4'] = fuzz.trimf(cvm_stage.universe, [3, 4, 5])
cvm_stage['5'] = fuzz.trimf(cvm_stage.universe, [4, 5, 6])
cvm_stage['6'] = fuzz.trimf(cvm_stage.universe, [5, 6, 7])

# Define rules
rule1 = ctrl.Rule(concavity['Flat'] & shape['Trapezoidal'], cvm_stage['1'])
rule2 = ctrl.Rule(concavity['Flat'] & shape['Horizontal'], cvm_stage['2'])
rule3 = ctrl.Rule(concavity['Concave'] & shape['Trapezoidal'], cvm_stage['3'])
rule4 = ctrl.Rule(concavity['Concave'] & shape['Horizontal'], cvm_stage['4'])
rule5 = ctrl.Rule(concavity['Concave'] & shape['Square'], cvm_stage['5'])
rule6 = ctrl.Rule(concavity['Concave'] & shape['Vertical'], cvm_stage['6'])

cvm_control = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
cvm_simulation = ctrl.ControlSystemSimulation(cvm_control)

# Input values for simulation
cvm_simulation.input['concavity'] = 3
cvm_simulation.input['shape'] = 3

cvm_simulation.compute()
print(cvm_simulation.output['cvm_stage'])

# Visualization of the output and input
cvm_stage.view(sim=cvm_simulation)
concavity.view(sim=cvm_simulation)
shape.view(sim=cvm_simulation)

plt.show()