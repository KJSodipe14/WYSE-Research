WYSE-Research
Transfer Function Characterization of Coaxial Cables
Frequency-Dependent Magnitude and Phase Modeling

This project analyzes the AC transfer function of multiple coaxial cables by fitting theoretical attenuation and phase-shift models to experimental data. The goal is to build accurate, frequency-dependent models that describe how real cables behave from low kilohertz to hundreds of megahertz.

The repository includes measurement data, model-fitting notebooks, and plots illustrating how the fitted functions compare to noisy real-world data.

Purpose of the Project

Real coaxial cables introduce frequency-dependent effects, including:

Magnitude attenuation (dB per 100 m)

Phase delay (radians per 100 m)

Skin-effect losses at high frequencies

Dielectric losses and dispersion

Non-ideal variations caused by manufacturing tolerances

The objective of this project is to derive empirical functions for:

Magnitude: Loss(f) in decibels per 100 m

Phase: Phase(f) in radians per 100 m

These functions can be used for transmission-line simulations, signal-integrity modeling, and high-frequency system analysis.

Project Contents
MagnitudeFigure.png           # Magnitude fit for AC cable
PhaseFigure.png               # Phase fit for AC cable
TestFigure.png                # Magnitude fit for CB50 cable

transfer-function-intro.ipynb
transfer_function_intro.ipynb
SquareWavePractice.ipynb
Research_Cable1.ipynb
Research_Cable2.ipynb
fittingfunctionpracticesecret.ipynb


Each notebook performs data loading, cleaning, curve fitting, and visualization.

Methodology
1. Data Acquisition

Data includes:

10 kHz magnitude measurements (low-scatter reference set)

1 MHz magnitude measurements (high-frequency scatter region)

High-frequency magnitude and phase data

Phase data extracted from square-wave timing offsets

These datasets contain significant natural scatter, so fitting is performed statistically.

2. Magnitude Model

The attenuation model uses a standard coax-loss structure:

Constant term → conductor geometry

Square-root term → skin effect

Linear term → dielectric loss

Model:

Loss
(
𝑓
)
=
𝑎
+
𝑏
𝑓
+
𝑐
𝑓
Loss(f)=a+b
f
	​

+cf

Coefficients are extracted using nonlinear regression.

3. Phase Model

Phase is modeled using frequency-dependent delay:

Phase
(
𝑓
)
=
−
2
𝜋
𝑓
 
𝜏
(
𝑓
)
Phase(f)=−2πfτ(f)

Where the delay 
𝜏
(
𝑓
)
τ(f) depends on:

Dielectric constant

Distributed L and C parameters

Frequency-dependent phase velocity

This produces a smooth, monotonic phase curve consistent with transmission-line theory.

Results Summary

Magnitude fits match measured attenuation from ~1 kHz to 100+ MHz.

Phase fits accurately capture expected frequency-dependent delay.

10 kHz and 1 MHz datasets provide stable low-/mid-frequency anchors.

High-frequency data exhibits large scatter but still follows a clear trend.

The CB50 cable exhibits significantly higher high-frequency attenuation than the AC cable.

Reproducing the Results

Install dependencies:

pip install numpy scipy matplotlib pandas


Open a notebook such as:

transfer-function-intro.ipynb


Then run all cells. Each notebook:

Loads measurement data

Selects frequency windows

Fits magnitude and phase functions

Generates the included plots

Applications

This model supports:

Signal integrity simulations

High-speed digital link modeling

RF system design

Cable quality assessment

Prediction of attenuation and phase shift across frequency
