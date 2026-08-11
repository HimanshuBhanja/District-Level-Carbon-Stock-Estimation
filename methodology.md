# Project Methodology

## 1. Folder Structure and Contents

The project is organized into separate folders so that data, processing,
models, results, documentation, and the web application can be managed
independently.

  -----------------------------------------------------------------------
  Folder                  Main Contents           Purpose
  ----------------------- ----------------------- -----------------------
  `01_Presentation/`      Project presentation    Communicates the
                          files                   objectives,
                                                  methodology, results,
                                                  and key findings.

  `02_Report/`            Technical report and    Provides the detailed
                          documentation           scientific and
                                                  technical description
                                                  of the project.

  `03_Code/`              Python/GIS/ML           Performs preprocessing,
                          processing scripts      feature preparation,
                                                  modelling, prediction,
                                                  and analysis.

  `04_Data/`              Remote sensing inputs,  Stores the input and
                          spatial data, grids,    intermediate datasets
                          and processed datasets  required for carbon
                                                  estimation.

  `05_Model_Results/`     Model evaluation and    Stores performance
                          prediction outputs      metrics, validation
                                                  results, and
                                                  model-generated
                                                  results.

  `06_Trained_Models/`    Saved machine-learning  Contains trained models
                          models                  that can be reused for
                                                  prediction without
                                                  retraining.

  `07_Website/`           Web application files   Provides the
                                                  user-facing Carbon
                                                  Stock Intelligence
                                                  dashboard.
  -----------------------------------------------------------------------

## 2. Purpose and Usage of Key Files

### `04_Data/`

This is the main data repository of the workflow.

-   `04_Remote_Sensing_Inputs/` contains remote-sensing-derived inputs,
    including `ndvi_monthly_ludhiana_jun24_may25.csv`. The NDVI file
    contains monthly values from June 2024 to May 2025 and supports
    temporal vegetation analysis.
-   `07_Processed_Grid_Dataset/04_Final_Output/carbon_all_66790_final.csv`
    contains the final grid-level carbon prediction dataset used by the
    dashboard.
-   `README.md` documents the data directory and identifies large
    datasets that are stored externally when required.

The final carbon dataset includes fields such as `Grid_ID`, `WKT`,
`DEM_mean`, `Slope_mean`, `sand_pct`, `clay_pct`, `bd_gcm3`,
`Predicted_SOC`, `BGC_tC_ha`, `Predicted_NPP`, `AGC_tC_ha`,
`Total_C_tC_ha`, and `Total_CO2e_tC_ha`.

### `03_Code/`

The code folder contains the scripts used to process spatial and
environmental data, prepare machine-learning inputs, train models, and
generate predictions. These scripts connect the raw inputs to the
processed datasets and model outputs.

### `05_Model_Results/` and `06_Trained_Models/`

Model results provide evidence of model performance and prediction
quality. Trained model files preserve the fitted machine-learning models
so that they can be reused for district-wide prediction and application
development.

### `07_Website/`

The website folder contains both the earlier frontend implementation and
the final Streamlit application.

-   `Frontend/` contains the original web frontend files.
-   `Streamlit_App/app.py` is the main dashboard application. It loads
    carbon and NDVI datasets, calculates carbon statistics, performs
    Carbon--NDVI integration, provides grid-level analysis, and displays
    the spatial carbon map.
-   `Streamlit_App/requirements.txt` lists the Python packages required
    to run the dashboard.

The deployed dashboard is available at:

https://district-level-carbon-stock-estimation.streamlit.app/

## 3. Project Completion Workflow

The complete project follows these stages:

1.  **Study-area and grid preparation** -- establish the Ludhiana study
    area and spatial grid.
2.  **Data collection** -- assemble remote sensing, soil, terrain,
    land-use, and productivity datasets.
3.  **Preprocessing** -- clean, align, mask, and extract variables for
    the spatial grid.
4.  **Feature preparation** -- create the predictor variables required
    for carbon modelling.
5.  **Machine learning** -- train and evaluate carbon prediction models.
6.  **Spatial prediction** -- apply the trained models to generate
    grid-level carbon estimates.
7.  **Carbon calculation** -- derive AGC, BGC, total carbon, and
    CO₂-equivalent outputs.
8.  **NDVI integration** -- associate the available monthly NDVI
    profiles with carbon grids using `Grid_ID`.
9.  **Visualization** -- generate spatial maps, temporal NDVI charts,
    and carbon summaries.
10. **Web deployment** -- present the final results through the
    Streamlit Carbon Stock Intelligence dashboard.

The final carbon dataset contains 64,545 prediction grids, while the
NDVI dataset contains 19,801 unique NDVI grids. The dashboard retains
all carbon grids and displays NDVI where a matching grid record exists.

## 4. Main Project Flow Chart

``` text
                STUDY AREA: LUDHIANA
                         |
                         v
                SPATIAL GRID CREATION
                         |
                         v
                  DATA COLLECTION
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
     REMOTE SENSING    SOIL DATA    TERRAIN/NPP
          |              |              |
          +--------------+--------------+
                         |
                         v
                  DATA PREPROCESSING
                         |
                         v
                  FEATURE EXTRACTION
                         |
                         v
                MACHINE LEARNING
              (Training + Evaluation)
                         |
                         v
                DISTRICT-WIDE
              CARBON PREDICTION
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
         AGC            BGC        TOTAL CARBON
          |              |              |
          +--------------+--------------+
                         |
                         v
                CO2-EQUIVALENT
                         |
                         v
                 NDVI INTEGRATION
              (June 2024-May 2025)
                         |
                         v
               SPATIAL + TEMPORAL
                 VISUALIZATION
                         |
                         v
             STREAMLIT DASHBOARD
                         |
                         v
              PUBLIC WEB DEPLOYMENT
```

This structure connects the project's data, analytical, modelling, and
visualization components into one reproducible workflow from raw inputs
to the final public carbon intelligence application.
