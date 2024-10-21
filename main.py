import sympy as sp
import numpy as np
import matplotlib.pyplot as plt #graph
import pandas as pd  #tables in terminal

# define symbols/variables
t = sp.symbols('t')
k = sp.symbols('k', positive=True)  # assume k > 0
L, P0 = sp.symbols('L P0')
P = sp.Function('P')(t)

# format/display questions with results
def show_question_answer(question_number, question, answer):
    print(f"Question {question_number}: {question}")
    print(f"Answer: {answer}\n")

#display population values in a table
def show_population_table(model, time_vals, pop_vals):
    df = pd.DataFrame({'Time (t)': time_vals, f'{model} Population (P)': pop_vals})
    print(f"\n{model} Population Data:\n")
    print(df.head(10))  # Show the first 10 values as an example
    print("\nExplanation: This table shows the population (P) at different time intervals (t).")

# Model 1: UNCONSTRAINED GROWTH
def model_1_unconstrained_growth(halved=False, question_start=1):
    eq = sp.Eq(P.diff(t), k * P)  # DE for unconstrained growth
    solution = sp.dsolve(eq, P)  # solve the DE

    # substitute initial condition P(0)=P0 or P0/2 if halved
    if halved:
        initial_value = P0 / 2
    else:
        initial_value = P0
    initial_condition = solution.subs(t, 0)
    solution_with_IC = sp.Eq(initial_value, initial_condition.rhs)

    # solve for the constant in the solution
    constant = sp.solve(solution_with_IC, sp.Symbol('C1'))[0]

    # substitute the constant back into the solution
    final_solution = solution.subs(sp.Symbol('C1'), constant)

    # show equation/solution
    model = "Halved Unconstrained Growth" if halved else "Unconstrained Growth"
    show_question_answer(question_start, f"{model} Differential Equation", r"dP/dt = kP")
    show_question_answer(question_start + 1, "Solved differential equation", sp.pretty(final_solution))

    # long-term behavior
    long_term_behavior = sp.limit(final_solution.rhs, t, sp.oo)
    show_question_answer(question_start + 2, "Long-term behavior of population",
                         f"As t approaches infinity, the population grows indefinitely: {long_term_behavior}")

    # graph representation: Convert symbolic expression to numerical function using lambdify
    # we do conversions to be able to print the graph
    P_func = sp.lambdify((t, k, P0), final_solution.rhs, 'numpy')

    # time range for plotting
    time_vals = np.linspace(0, 10, 400)

    # Evaluate function numerically
    if halved:
        pop_vals = P_func(time_vals, 0.5, 100 / 2)  # k=0.5, halved P0=100/2
    else:
        pop_vals = P_func(time_vals, 0.5, 100)  # k=0.5, original P0=100

    # display the population values in table
    show_population_table(model, time_vals, pop_vals)

    # plot the numerical values
    plt.plot(time_vals, pop_vals, label=model)

# Logistic Growth Model (Model 2)
def logistic_growth(t, k, P0, L):
    return L / (1 + ((L - P0) / P0) * np.exp(-k * t))

def model_2_constrained_growth(halved=False, question_start=7):
    # Example values for k, P0, and L
    k = 0.2  # growth rate
    L = 1000  # carrying capacity
    if halved:
        P0 = 50  # halved initial population
        label = 'Halved Constrained Growth'
    else:
        P0 = 100  # original initial population
        label = 'Constrained Growth'

    # time range extended to 50 units to see leveling off
    time_vals = np.linspace(0, 50, 400)

    # calculate population values using logistic growth equation
    pop_vals_logistic = logistic_growth(time_vals, k, P0, L)

    # display the population values in table
    show_population_table(label, time_vals, pop_vals_logistic)

    # plotting the logistic growth
    plt.plot(time_vals, pop_vals_logistic, label=label)

    # show questions and answers for the logistic model
    show_question_answer(question_start, f"{label} Differential Equation", r"dP/dt = kP(1 - P/L)")
    show_question_answer(question_start + 1, "Carrying capacity and behavior",
                         f"The population will stabilize at {L} over time.")

# Final Report to Thanos
def report_to_thanos():
    print("\n=== Report to Thanos ===")
    print(
        "We modeled the population growth with two models: "
        "unconstrained growth (dP/dt = kP) and constrained (logistic) growth (dP/dt = kP(1 - P/L)).\n"
        "1. Unconstrained growth assumes infinite resources, leading to exponential growth. "
        "Even if the population is halved, it will grow indefinitely in the long run.\n"
        "2. Logistic growth assumes limited resources with a carrying capacity (L). If halved, "
        "the population will still recover but will stabilize at L over time.\n"
        "Conclusion: Halving the population has a temporary effect. Both models suggest that the population will eventually "
        "recover, though the logistic model introduces resource limits."
    )

# Main function
def main():
    print("=== Thanos Population Dynamics ===\n")
    print("Project: Investigating Thanos' claim through population dynamics modeling.\n")

    # Unconstrained growth with original and halved population
    model_1_unconstrained_growth(question_start=1)
    model_1_unconstrained_growth(halved=True, question_start=4)

    # Constrained growth with original and halved population
    model_2_constrained_growth(question_start=7)
    model_2_constrained_growth(halved=True, question_start=9)

    # Show the graph
    plt.title("Population Growth Models: Original vs Halved")
    plt.xlabel("Time (t)")
    plt.ylabel("Population (P)")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Final report to Thanos
    report_to_thanos()

if __name__ == "__main__":
    main()
