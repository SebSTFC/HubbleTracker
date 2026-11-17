# EEP - Tracking the Hubble Space Telescope

## Overview

This project is part of the Engineering Education Programme (EEP) and explores how publicly available satellite tracking data can be used to monitor the position and motion of the Hubble Space Telescope (HST).

Using orbital data sources such as TLEs (Two-Line Element Sets), the project calculates Hubble's position relative to a user-defined observation site and determines when it is visible above a specified elevation angle.

## Initial Objectives

- Retrieve real-time or near real-time Hubble orbital data.
- Calculate Hubble's position relative to a chosen site.
- Determine when Hubble is above the local horizon and exceeds a 10° elevation threshold.
- Visualise Hubble's position and ground track.

## Data Sources

Potential sources of Hubble position data include:

- **N2YO API** - Satellite tracking API requiring an API key.
- **CelesTrak** - Public satellite orbital elements (TLE data).
- **Space-Track** - Official satellite tracking database (free account required).

## Technologies

This project uses free and open-source tools and technologies, including:

- Python
- Skyfield
- SGP4
- TLE (Two-Line Element) orbital data

## Future Enhancements

Possible extension features include:

- Historical pass analysis
- Predicting future visibility windows for any observation site
- Investigating how orbital parameters affect Hubble's trajectory
- Comparing orbital mechanics models with machine learning approaches for position prediction
- Modelling and visualising Hubble's orbit around the Earth

## References

- Hubble Space Telescope
- TLE Format (Two-Line Element Sets)
- CelesTrak Satellite Data
- N2YO Satellite Tracking API
- Space-Track