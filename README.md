# WYSE-Research
# Transfer Function Characterization of Coaxial Cables

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

Magnitude:
Loss(f) [decibels per 100 m]

Phase:
Phase(f) [radians per 100 m]

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

High-frequency magnitude and phase data from additional measurements

Phase data extracted from square-wave timing offsets

These datasets contain significant natural scatter, so fitting is performed statistically.

2. Magnitude Model

The attenuation model uses a standard coax-loss structure:

Constant term → conductor geometry

Square-root term → skin effect

Linear term → dielectric loss

A generic model form is:

Loss(f) = a + b * sqrt(f) + c * f

Coefficients are obtained via nonlinear regression.

3. Phase Model

Phase is modeled using frequency-dependent delay:

Phase(f) = -2 * pi * f * τ(f)

Where the delay τ(f) is derived from:

Cable dielectric constant

Distributed L and C parameters

Decreasing phase velocity at higher frequencies

This produces a smooth, monotonic phase curve consistent with transmission-line theory.

Results Summary

Magnitude fits match measured attenuation from about 1 kHz to 100+ MHz.

Phase fits accurately capture the expected delay behavior.

10 kHz and 1 MHz datasets provide stable references for low and mid frequencies.

High-frequency data exhibits large scatter but still forms a reliable trend.

The CB50 cable shows substantially higher high-frequency attenuation than the AC cable.

Reproducing the Results

Install dependencies:

pip install numpy scipy matplotlib pandas


Open any notebook such as:

transfer-function-intro.ipynb


Then run all cells. Each notebook:

Loads measurement data

Selects data windows (10 kHz → 1 MHz → high-frequency region)

Fits the magnitude and phase functions

Produces the plots included in this repository

Applications

The models developed here can be applied to:

Signal integrity simulations

High-speed digital link modeling

RF system design

Cable quality assessment

Prediction of attenuation and phase shift over frequency
