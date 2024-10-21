# Thanos-Population-Dynamics-Project
## Required Packages:
```bash
pip install sympy
pip install numpy
pip install matplotlib
pip install pandas
```
---
## Project descriptions:
In the end of the *“Avengers: Infinity War,”* the villain Thanos snaps his fingers and turns half of all living creatures to dust with the hope of restoring balance to the natural world. How does this affect the long term behavior of various species? Investigate the validity of his claim by modeling various population dynamics such as unconstrained and constrained growth. 

In the 2018 Marvel Studios blockbuster, *“Avengers: Infinity War,”* the villain Thanos snaps his fingers and turns half of all living creatures in the universe to dust. He was concerned that overpopulation on a planet would eventually lead to the suffering and extinction of the entire population. This is evident in the following quote from Thanos: > 

	“Little one, it’s a simple calculus. This universe is finite, its resources finite. If life is left unchecked, life will cease to exist. It needs correction.” In this activity, we will investigate the validity of Thanos’ claims using mathematical models for population dynamics. 
### (a) There is a bit to unpack in Thanos’ quote. What are some of the assumptions that Thanos is making?
Thanos is making several key assumptions in his quote regarding population dynamics:

1. **Finite Resources**: Thanos assumes that resources (such as food, water, and space) are limited and that overpopulation will eventually deplete these resources, leading to societal collapse.

2. **Exponential Growth**: He assumes that population growth follows an exponential trajectory, where the population increases rapidly without any natural limits, which he believes will result in the exhaustion of available resources.

3. **Reducing Population as a Solution**: Thanos assumes that halving the population is a viable long-term solution to resource scarcity, without considering other factors like technology, sustainable resource management, or environmental conservation.

4. **Static Carrying Capacity**: He assumes that the carrying capacity of a given environment (or the universe) is fixed and cannot be changed or expanded through advancements in technology or social changes.

These assumptions overlook the potential for sustainable solutions to balance population and resources, making his approach overly simplistic.

---
### (b) Model 1 
**First, we will consider the following initial value problem**:

$$
\frac{dP}{dt} = kP, \quad P(0) = P_0
$$

where $P$ is the population at time $t$, and $k$ and $P_0$ are constant parameters.

#### (i) Interpret the meaning of this differential equation.
This differential equation describes exponential growth of a population $P$ over time. The term $kP$ indicates that the rate of change of the population (how fast the population is growing) is proportional to the current population size $P$. The constant $k$ represents the growth rate: if $k > 0$, the population increases over time, while if $k < 0$, the population decreases.

#### (ii) Solve the initial value problem and determine what would happen to a population in the long run. Explain why your answer makes sense in terms of the differential equation.
To solve the differential equation, we first separate variables:

$$
\frac{dP}{P} = k \, dt
$$

Next, we integrate both sides:

$$
\int \frac{1}{P} \, dP = \int k \, dt
$$

This yields:

$$
\ln P = kt + C
$$

Exponentiating both sides gives:

$$
P(t) = e^{kt + C} = e^C e^{kt}
$$

Letting $e^C = P_0$ (since $P(0) = P_0$), the solution becomes:

$$
P(t) = P_0 e^{kt}
$$

In the long run, if $k > 0$, the population grows exponentially without bound as $t \to \infty$. If $k < 0 $, the population decays toward zero. This makes sense in terms of the differential equation because when  
$k > 0$, the rate of growth increases with population size, leading to unchecked growth.

#### (iii) This model is called *unconstrained growth*, since the population grows without bound. Under what assumptions would it be appropriate to use this type of model? Does this model fit the situation Thanos is describing?
This **unconstrained growth** model assumes there are no limitations on resources, space, or other factors that would slow down population growth. It assumes ideal conditions where the population can grow indefinitely, and is appropriate when considering situations like early population growth with abundant resources.

However, this model does not fit Thanos' situation. Thanos is concerned with limiting population growth to prevent overpopulation and resource depletion, so a model with a carrying capacity (like the logistic growth model) would better represent the situation. The unconstrained growth model assumes infinite growth, which contradicts Thanos' philosophy of halving the population to preserve balance.

#### (iv) Thanos’ plan is to eliminate half of all living creatures in the universe. What would happen if the population size was suddenly cut in half? How could that be represented with this model? What parameters would change?
If the population is suddenly cut in half, this would be represented as a sudden decrease in the initial population $P_0$. The new initial population after Thanos’ intervention would be $\frac{P_0}{2}$, but the growth rate $k$ would remain the same. The solution to the differential equation would then be:

$$
P(t) = \frac{P_0}{2} e^{kt}
$$

This shows that the population would still grow exponentially after the reduction, just from a smaller starting point. However, the long-term growth would follow the same pattern as before unless other constraints were introduced.

---
### (c) Model 2
Next, consider the following initial value problem:

$$
\frac{dP}{dt} = kP \left( 1 - \frac{P}{L} \right), \quad P(0) = P_0
$$

Where:
- $P$ is the population at time $t$,
- $k$ is the intrinsic growth rate,
- $L$ is the carrying capacity (the maximum sustainable population size),
- $P_0$ is the initial population size.

### (i) How does each parameter affect the growth of the population?

- **$k$ (growth rate)**: This parameter controls how fast the population grows. If $k > 0$, the population increases; if $k < 0$, the population decreases (though the problem specifies $k$ is positive).
  
- **$L$ (carrying capacity)**: This represents the maximum population the environment can support. As the population $P$ approaches $L$, the growth rate slows down, eventually reaching zero when $P = L$.
  
- **$P_0$ (initial population)**: This is the population size at time $t = 0$. It determines the starting point of the population growth. If $P_0$ is smaller than $L$, the population will grow towards $L$; if $P_0 > L$, the population will decrease towards $L$.

### (ii) For what value(s) of $P$, if any, would the population stay constant? This value will be called an equilibrium solution.

The population stays constant when $\frac{dP}{dt} = 0$. From the equation:

$$
\frac{dP}{dt} = kP \left( 1 - \frac{P}{L} \right)
$$

Set $\frac{dP}{dt} = 0$:

$$
kP \left( 1 - \frac{P}{L} \right) = 0
$$

This gives two equilibrium solutions:

- $P = 0$: The population stays constant at zero, representing extinction.
- $P = L$: The population remains constant at the carrying capacity.

### (iii) Determine the stability of each equilibrium value.

To determine the stability of each equilibrium point, we look at how the population changes when $P$ is slightly above or below each equilibrium value.

- **At $P = 0$**: When $P$ is slightly greater than 0, the term $(1 - P/L)$ is positive, so $\frac{dP}{dt} > 0$. This means that the population will increase away from 0, indicating that $P = 0$ is an **unstable** equilibrium.
  
- **At $P = L$**: When $P$ is slightly less than $L$, the term $(1 - P/L)$ is positive, so $\frac{dP}{dt} > 0$, and the population grows toward $L$. When $P$ is slightly greater than $L$, the term $(1 - P/L)$ becomes negative, so $\frac{dP}{dt} < 0$, and the population decreases toward $L$. Therefore, $P = L$ is a **stable** equilibrium.

### (iv) Solve the initial value problem and determine what would happen to a population in the long run. Explain why your answer makes sense in terms of the differential equation.

### To solve the initial value problem:
  $\frac{dP}{dt} = kP \left( 1 - \frac{P}{L} \right)$

1. **Separate variables**:  
   $\frac{1}{P(L - P)} \, dP = k \, dt$

2. **Use partial fractions** to decompose the left-hand side:  
   $\frac{1}{P(L - P)} = \frac{A}{P} + \frac{B}{L - P}$

   Solving for $A$ and $B$ gives $A = \frac{1}{L}$ and $B = \frac{1}{L}$, so:

   $\frac{1}{P(L - P)} = \frac{1}{L} \left( \frac{1}{P} + \frac{1}{L - P} \right)$

3. **Integrate both sides**:  
   $\int \left( \frac{1}{P} + \frac{1}{L - P} \right) dP = \int k \, dt$

   The left-hand side integrates to:

   $\ln P - \ln (L - P) = kt + C$

4. **Simplify**:  
   $\ln \frac{P}{L - P} = kt + C$

5. **Exponentiating both sides** gives:  
   $\frac{P}{L - P} = e^{kt + C} = e^C e^{kt}$

   Let $e^C = \frac{P_0}{L - P_0}$ (from the initial condition $P(0) = P_0$):

   $\frac{P}{L - P} = \frac{P_0}{L - P_0} e^{kt}$

6. **Solve for $P(t)$**:  
   $P(t) = \frac{L}{1 + \left( \frac{L - P_0}{P_0} \right) e^{-kt}}$

In the long run, as $t \to \infty$, the exponential term $e^{-kt}$ approaches 0, so:

$P(t) \to L$


This means the population will approach the carrying capacity $L$. This result makes sense because, according to the differential equation, as $P$ gets closer to $L$, the growth rate slows down, eventually reaching zero when $P = L$.

### (v) Thanos’ plan is to eliminate half of all living creatures in the universe. How would halving the initial population impact the overall dynamics of the system?

If Thanos cuts the population in half, the new initial population would be $P_0/2$. The carrying capacity $L$ and the growth rate $k$ remain unchanged. The solution to the differential equation would then be:

$$
P(t) = \frac{L}{1 + \left( \frac{L - \frac{P_0}{2}}{\frac{P_0}{2}} \right) e^{-kt}}
$$

This would shift the dynamics in such a way that the population starts at a smaller size but would still grow toward the same carrying capacity $L$. It would take longer to reach the carrying capacity compared to when the population started at $P_0$.

### (vi) Model 2 is called constrained growth, since the population grows or decays until it reaches a carrying capacity. Under what assumptions would it be appropriate to use this model? Does this model seem more reasonable than the first model for describing Thanos’ version of reality?

This **constrained growth** model assumes that population growth is limited by resources, space, or other factors, leading to a maximum sustainable population (the carrying capacity $L$). This model is appropriate in realistic settings where resources are finite, and overpopulation could strain the environment.

In Thanos' scenario, where he is concerned with the balance between population and resources, **Model 2** is much more reasonable than **Model 1**. While Model 1 assumes infinite growth, Model 2 realistically accounts for the fact that populations cannot grow without bound and must stabilize at some carrying capacity. This better aligns with Thanos' objective of preventing overpopulation.

---
### (d) The Assignment—A Report for Thanos
Thanos claims to be a logical person. In the sequel, “Avengers: End Game,” time
travel is used to undo Thanos’ work. Suppose you go back in time and work your
way through to become a part of Thanos’ inner circle. Prepare a report to Thanos
to encourage him to rethink his plan. Your report should discuss the assumption and
results from both of the mathematical models discussed.

#### Introduction

This report presents an analysis of two mathematical models of population growth and decay. The objective is to compare and assess the implications of each model, discuss their assumptions, and examine the results of each model. Both **Model 1** (unconstrained growth) and **Model 2** (constrained growth) were analyzed using differential equations to model population changes over time.

#### Model 1: Unconstrained Growth

The first model assumes that the population grows exponentially without any limitations. The differential equation governing this model is:

$$
\frac{dP}{dt} = kP, \quad P(0) = P_0
$$

Where:
- $P(t)$ is the population at time $t$,
- $k$ is the intrinsic growth rate (a constant),
- $P_0$ is the initial population size.

##### Assumptions:
1. **Unlimited Resources**: This model assumes that the population can grow indefinitely without any constraints. Resources such as food, space, and other essentials are assumed to be infinitely available.
2. **Constant Growth Rate**: The population grows at a rate proportional to its current size, meaning that the larger the population, the faster it grows.

##### Results:
The solution to the equation is:

$$
P(t) = P_0 e^{kt}
$$

As $t \to \infty$, if $k > 0$, the population grows exponentially without bound. If $k < 0$, the population decays to zero over time.

##### Implications:
The major flaw of this model is the unrealistic assumption of unlimited resources. In the real world, there are constraints on resources, space, and environmental capacity, which means populations cannot grow indefinitely. While this model may be applicable in very short-term scenarios where resources are temporarily abundant, it fails to account for long-term sustainability.

#### Model 2: Constrained Growth

The second model accounts for environmental constraints and assumes that population growth is limited by available resources. The governing differential equation for this model is:

$$
\frac{dP}{dt} = kP \left( 1 - \frac{P}{L} \right), \quad P(0) = P_0
$$

Where:
- $P(t)$ is the population at time $t$,
- $k$ is the intrinsic growth rate,
- $L$ is the carrying capacity (the maximum population size that the environment can support),
- $P_0$ is the initial population size.

##### Assumptions:
1. **Limited Resources**: This model assumes that resources are finite, and as the population approaches the carrying capacity $L$, the growth rate slows down.
2. **Carrying Capacity**: The carrying capacity $L$ represents the maximum sustainable population size. Beyond this point, the environment cannot support additional population growth.
3. **Logistic Growth**: The model assumes that population growth is initially exponential, but it slows as the population approaches $L$ and eventually stabilizes.

##### Results:
The solution to the equation is:

$$
P(t) = \frac{L}{1 + \left( \frac{L - P_0}{P_0} \right) e^{-kt}}
$$

As $t \to \infty$, the population approaches the carrying capacity $L$, meaning that the population stabilizes rather than growing indefinitely.

##### Implications:
This model is much more realistic in describing long-term population dynamics. It accounts for resource limitations and shows that population growth slows and eventually stabilizes at the carrying capacity. This model reflects real-world scenarios more accurately, particularly in ecosystems where resources are limited. It also implies that, even if a population is initially reduced, it will eventually grow back toward the carrying capacity unless there are permanent reductions in resources or other limiting factors.

#### Comparison of the Models

1. **Assumptions**:
   - **Model 1** assumes unlimited growth without resource limitations, which is highly unrealistic in the real world.
   - **Model 2** incorporates the concept of a carrying capacity, making it more applicable to real-world population dynamics where resources are finite.

2. **Long-Term Behavior**:
   - **Model 1** predicts exponential growth without bound, which cannot happen indefinitely in any real-world scenario.
   - **Model 2** predicts that population growth will slow and stabilize once the carrying capacity is reached, which is a more plausible outcome in ecosystems or human populations.

3. **Applicability**:
   - **Model 1** might be useful for very short-term projections where growth is unconstrained, such as in early-stage bacterial growth or initial colonization of a new habitat.
   - **Model 2** is better suited for long-term population predictions, as it accounts for limited resources and environmental constraints.

#### Conclusion

In conclusion, **Model 2**, the constrained growth model, is far more reasonable for modeling real-world population dynamics because it accounts for finite resources and the natural limitations imposed by the environment. While **Model 1** may describe short-term growth patterns, it fails to capture the eventual stabilization that occurs in real ecosystems.

The constrained growth model shows that, even if populations are reduced, they will eventually grow back to the carrying capacity unless there are long-term restrictions on resources. This highlights the importance of addressing the root causes of overpopulation and resource depletion rather than temporary reductions in population size.
