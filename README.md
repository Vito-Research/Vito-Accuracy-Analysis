# Vito Accuracy Analysis 

## This document outlines Vito’s unit testing process to ensure all systems are functioning appropriately.

> Please note that most of this is already implemented, it simply needs to be combined into one working workflow and repository

The following items should be tested end to end…

- NightSignal Swift and Kotlin state machines
   - Output is equal to NightSignal’s python algorithm output
- Vito Swift and Kotlin State Machines
   - Accuracy is above 79% (NightSignal’s baseline) in predicting Covid-19 infection within NightSignal’s raw data
   - Note: Vito’s state machine is different than NightSignal due to adjustments in data ingestion
- Vito machine learning models
   - Accuracy is above 79% in predicting Covid-19 infection
- Based on the accuracies computed above, how would these accuracies impact the pandemic in 2020 assuming recipients of alerts either a) practiced social distancing and mask usage or b) self isolated
- These tests would occur if changes are made to VitoKit (iOS or Android [TBD])

Resources for development…

h[ttps://github.com/Vito-Research/Vito_Swift_API](https://github.com/Vito-Research/Vito_Swift_API)

[GitHub - Vito-Research/Vito-State_Kotlin](https://github.com/Vito-Research/Vito-State_Kotlin)

[GitHub - Vito-Research/covasim: COVID-19 Agent-based Simulator (Covasim): a model for exploring coronavirus dynamics and interventions](https://github.com/Vito-Research/covasim)

[Vito-Visualization/pages at main · Vito-Research/Vito-Visualization](https://github.com/Vito-Research/Vito-Visualization/tree/main/pages)

[GitHub - Vito-Research/Bulk_Data_Processing](https://github.com/Vito-Research/Bulk_Data_Processing)

