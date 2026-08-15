# 🌱 District-Level Carbon Stock Estimation

### Grid-Based Machine Learning Framework for Agricultural Landscapes in Ludhiana District, Punjab, India

---
> ## ⚠️ Project Status & Important Note
>
> This project was developed as part of the **Big Data Analytics** course during the **2nd semester of the M.Sc. Agriculture Analytics programme at the Indian Institute of Remote Sensing (IIRS), Dehradun**, under the guidance of **Dr. Kapil Oberoi Sir**.
>
> The project demonstrates a complete geospatial and machine-learning workflow for **district-level carbon stock estimation**, integrating remote sensing, environmental variables, spatial grids, machine learning, GIS, database technologies, and web-based visualization.
>
> **Important:** This repository represents an **academic project and an ongoing research-learning workflow**. The current carbon-stock estimates should **not be interpreted as final or fully validated scientific estimates**.
>
> During post-project review and methodological evaluation, several issues and limitations were identified that require further investigation:
>
> ### 1. Precipitation Variable
>
> The NPP model assigns a relatively high feature importance to the **`Rabi_Preci`** variable. This raises an important methodological question regarding the exact definition, temporal aggregation, units, and spatial representation of the precipitation data used in the model.
>
> In particular, it is necessary to verify whether the variable represents **Rabi-season precipitation, annual precipitation, or another aggregation**, and whether the selected representation is consistent with the intended modelling methodology.
>
> ### 2. High Feature Importance of `Rabi_Preci`
>
> The Random Forest NPP model gives substantial importance to `Rabi_Preci`. While precipitation is an ecologically relevant driver of vegetation productivity, its disproportionately high importance requires additional investigation to determine whether it represents a genuine environmental relationship or is partly associated with data-processing, feature-construction, or spatial-data issues.
>
> Therefore, the feature-importance results are treated as an **indicator for further investigation rather than definitive evidence of causality**.
>
> ### 3. 250 m × 250 m Spatial Grid
>
> The analysis uses **250 m × 250 m grid cells**. The suitability of this spatial resolution needs to be evaluated carefully for each predictor variable, particularly climate variables such as precipitation.
>
> Predictor datasets must be spatially and temporally compatible with the grid-based modelling framework. Further validation of resampling, aggregation, spatial alignment, and spatial variability is required.
>
> ### 4. NPP Prediction Uncertainty
>
> The NPP model achieved moderate predictive performance. Therefore, the resulting above-ground carbon estimates contain considerable uncertainty and should not be considered definitive without additional validation and model improvement.
>
> ### 5. Carbon-Stock Scaling
>
> The conversion of grid-level carbon densities into district-level carbon stock requires careful validation of the study-area boundary, grid coverage, agricultural/non-agricultural masking, and area-scaling procedure.
>
> The current inventory contains **66,790 grid cells**, and the relationship between the grid-based area and the official district area requires further verification before the final district-scale carbon stock is treated as authoritative.
>
> ### 6. Ongoing Research
>
> These limitations are an important part of the project's learning process. The purpose of documenting them here is to maintain **scientific transparency and reproducibility** rather than present the current outputs as final results.
>
> I am continuing to work on the broader concepts of **carbon stock estimation, soil organic carbon, carbon sequestration, remote sensing, geospatial machine learning, and carbon MRV (Measurement, Reporting and Verification)**.
>
> Future work will focus on:
>
> - validating and reconstructing the precipitation variables;
> - evaluating seasonal versus annual climate representations;
> - investigating the high importance of `Rabi_Preci`;
> - improving spatial and temporal consistency of predictor datasets;
> - validating the 250 m grid-based modelling approach;
> - improving NPP prediction performance;
> - validating carbon-stock scaling against the actual study-area boundary;
> - performing additional model validation and uncertainty analysis; and
> - developing a more scientifically robust carbon-stock estimation framework.
>
> **Therefore, this repository should be viewed as an academic prototype and an ongoing research workflow rather than a final authoritative carbon inventory for Ludhiana district.**
>
## 🚀 Live Dashboard

### Carbon Stock Intelligence — Ludhiana

**Live application:**
https://district-level-carbon-stock-estimation.streamlit.app/

The interactive Streamlit dashboard provides:

* District-level carbon stock visualization
* Above-ground carbon (AGC)
* Below-ground carbon (BGC)
* Total carbon stock
* CO₂-equivalent estimates
* Monthly NDVI temporal analysis
* Grid-level carbon analysis
* Grid-level NDVI profiles
* Integrated Carbon–NDVI dataset
* Interactive spatial carbon map
* Carbon dataset statistics and coverage information

---

## 📌 Project Highlights

* ✔ District-wide agricultural carbon stock estimation
* ✔ 250 m × 250 m spatial grid framework
* ✔ Integration of remote sensing, soil and productivity datasets
* ✔ Random Forest and XGBoost machine learning models
* ✔ Above-ground and below-ground carbon estimation
* ✔ Grid-level spatial prediction
* ✔ Monthly NDVI analysis for June 2024–May 2025
* ✔ Interactive Streamlit dashboard
* ✔ GitHub-based project architecture
* ✔ Publicly deployed web application

---
## 📖 Project Overview

This project estimates carbon stock across agricultural landscapes of **Ludhiana District, Punjab, India**, using a grid-based geospatial framework and machine learning.

The workflow integrates:

* Remote sensing data
* Soil properties
* Digital elevation and terrain variables
* Vegetation indices
* Net Primary Productivity (NPP)
* Land-use/land-cover information
* Machine learning models

The resulting spatial predictions are used to estimate above-ground carbon, below-ground carbon, total carbon stock and CO₂-equivalent storage.

The final outputs are presented through an interactive **Carbon Stock Intelligence** dashboard developed using Streamlit.

---

## 🎯 Objectives

1. Generate a uniform spatial grid across Ludhiana district.
2. Identify agricultural areas using LULC information.
3. Extract environmental and geospatial variables for each grid cell.
4. Estimate above-ground carbon using productivity information.
5. Estimate below-ground carbon using soil properties.
6. Develop machine learning models for carbon prediction.
7. Apply trained models to the district-wide spatial grid.
8. Generate spatial carbon stock outputs.
9. Integrate carbon predictions with remote sensing information.
10. Develop an interactive web-based carbon intelligence platform.

---

## 📍 Study Area

| Parameter                       | Value                            |
| ------------------------------- | -------------------------------- |
| Study Area                      | Ludhiana District, Punjab, India |
| Grid Resolution                 | 250 m × 250 m                    |
| Area per Grid                   | 6.25 ha                          |
| Initial Spatial Grid Framework  | 66,790 cells                     |
| Final Carbon Prediction Dataset | 64,545 grids                     |
| NDVI Dataset Records            | 20,000                           |
| Unique NDVI Grids               | 19,801                           |
| NDVI Period                     | June 2024 – May 2025             |

The initial spatial framework contains 66,790 grid cells. The final carbon prediction dataset used by the dashboard contains 64,545 spatial prediction grids.

---

## 🛰️ Data Integration

The project combines multiple geospatial and environmental datasets.

### Remote Sensing Variables

* NDVI — Normalized Difference Vegetation Index
* NDWI — Normalized Difference Water Index
* Land Surface Temperature (LST)
* Satellite-derived vegetation information

### Terrain Variables

* DEM
* Slope

### Soil Variables

* Soil Organic Carbon (SOC)
* Bulk Density
* Clay Content
* Sand Content

### Productivity Variable

* Net Primary Productivity (NPP)

### Land Use / Land Cover

LULC information is used to identify agricultural areas and support spatial masking.

---

## 🔬 System Workflow

```text
                 Study Area
                     │
                     ▼
            Spatial Grid Creation
                     │
                     ▼
              LULC / Ag Mask
                     │
                     ▼
       ┌─────────────┼─────────────┐
       │             │             │
       ▼             ▼             ▼
 Remote Sensing    Soil Data     NPP Data
       │             │             │
       └─────────────┼─────────────┘
                     ▼
              Feature Extraction
                     │
                     ▼
             Training Dataset
                     │
                     ▼
        Random Forest + XGBoost
                     │
                     ▼
           Carbon Prediction
                     │
                     ▼
       AGC + BGC + Total Carbon
                     │
                     ▼
          Spatial Carbon Mapping
                     │
                     ▼
        Carbon–NDVI Integration
                     │
                     ▼
          Streamlit Dashboard
```

---

# 🧮 Methodology

## 1. Study Area Preparation

The administrative boundary of Ludhiana District was prepared and used as the Area of Interest (AOI).

## 2. Spatial Grid Generation

A uniform **250 m × 250 m** grid framework was generated across the study area.

Each grid represents approximately:

**6.25 hectares**

## 3. Agricultural Masking

Land Use/Land Cover information was used to identify agricultural grid cells.

The agricultural mask was used to focus the carbon estimation workflow on relevant agricultural landscapes.

## 4. Feature Extraction

Environmental and geospatial variables were extracted for the spatial grid using raster and spatial analysis techniques.

### Major predictor variables

* DEM
* Slope
* Sand percentage
* Clay percentage
* Bulk density
* Soil Organic Carbon
* NPP
* NDVI
* Other remote sensing variables

## 5. Carbon Estimation

### Above-Ground Carbon

Above-ground carbon is estimated from productivity-based information.

The implemented workflow uses NPP-derived carbon estimation.

### Below-Ground Carbon

Below-ground carbon is estimated using soil-related variables, including Soil Organic Carbon, bulk density and soil depth.

A representative SOC stock relationship is:

```text
SOC Stock = SOC × Bulk Density × Soil Depth / 10
```

where soil depth is expressed in centimetres.

## 6. Machine Learning

Machine learning models were developed to estimate carbon-related variables from environmental and spatial predictors.

### Algorithms

* Random Forest
* XGBoost

Separate modeling workflows were used for above-ground and below-ground carbon estimation.

## 7. District-Wide Prediction

The trained models were applied to the final spatial prediction grid.

The resulting dataset contains **64,545 final carbon prediction grids** used by the dashboard.

## 8. Carbon Stock Outputs

The final dataset contains variables including:

* `Predicted_SOC`
* `BGC_tC_ha`
* `Predicted_NPP`
* `AGC_tC_ha`
* `Total_C_tC_ha`
* `Total_CO2e_tC_ha`

## 9. NDVI Temporal Analysis

Monthly NDVI data are available for:

```text
Jun 2024
Jul 2024
Aug 2024
Sep 2024
Oct 2024
Nov 2024
Dec 2024
Jan 2025
Feb 2025
Mar 2025
Apr 2025
May 2025
```

The NDVI dataset contains 20,000 records corresponding to 19,801 unique grid IDs.

Where duplicate NDVI records occur for the same grid, monthly NDVI values are averaged to create a single grid-level NDVI profile.

---

# 🌿 Carbon–NDVI Integration

The carbon prediction dataset is treated as the **master spatial dataset**.

A left join is used to associate NDVI information with carbon grids.

Therefore:

```text
Carbon prediction grids       = 64,545
Unique NDVI grids              = 19,801
Carbon grids without NDVI     = 44,744
```

The 44,744 grids without NDVI do **not** indicate a dashboard error. They represent carbon prediction grids for which a corresponding NDVI Grid_ID is not available in the current NDVI dataset.

This allows the dashboard to retain all carbon prediction grids while displaying NDVI only where corresponding observations are available.

---

# 💻 Interactive Dashboard

The final application is developed using **Streamlit**.

### Dashboard components

#### 1. Carbon Stock Overview

Displays:

* Mean Above-Ground Carbon
* Mean Below-Ground Carbon
* Mean Total Carbon
* Mean CO₂ Equivalent

#### 2. Carbon Component Comparison

Interactive comparison of:

* AGC
* BGC
* Total Carbon

#### 3. NDVI Temporal Analysis

Displays the district-level monthly NDVI profile from June 2024 to May 2025.

#### 4. Grid-Level Analysis

Users can select a Grid ID and inspect:

* Above-ground carbon
* Below-ground carbon
* Total carbon
* CO₂ equivalent
* Monthly NDVI profile, where available

#### 5. Integrated Carbon–NDVI Dataset

The dashboard combines carbon predictions with available NDVI profiles while retaining all carbon prediction grids.

#### 6. Spatial Carbon Map

The dashboard provides an interactive spatial visualization of:

* Total Carbon
* Above-Ground Carbon
* Below-Ground Carbon
* CO₂ Equivalent
* Predicted SOC
* Predicted NPP

---

# 🖥️ Web Application Architecture

```text
GitHub Repository
       │
       ▼
Streamlit Application
       │
       ├── app.py
       ├── requirements.txt
       │
       ▼
Carbon Prediction CSV
       │
       ▼
NDVI CSV
       │
       ▼
Interactive Dashboard
       │
       ▼
Streamlit Community Cloud
```

### Technology Stack

| Technology          | Purpose                                     |
| ------------------- | ------------------------------------------- |
| Python              | Data processing and application development |
| Pandas              | Tabular data processing                     |
| NumPy               | Numerical operations                        |
| Shapely             | Spatial geometry processing                 |
| PyDeck              | Interactive spatial visualization           |
| Folium              | Web mapping support                         |
| Streamlit           | Interactive dashboard                       |
| QGIS                | GIS and spatial analysis                    |
| Google Earth Engine | Remote sensing processing                   |
| Scikit-learn        | Machine learning                            |
| XGBoost             | Gradient boosting                           |
| PostgreSQL/PostGIS  | Spatial database                            |
| MongoDB Atlas       | Data storage                                |
| Git/GitHub          | Version control and repository management   |

---

# 📂 Repository Structure

```text
District-Level-Carbon-Stock-Estimation/
│
├── README.md
├── LICENSE
│
├── 01_Presentation/
│
├── 02_Report/
│
├── 03_Code/
│
├── 04_Data/
│   ├── README.md
│   ├── 04_Remote_Sensing_Inputs/
│   └── 07_Processed_Grid_Dataset/
│
├── 05_Model_Results/
│
├── 06_Trained_Models/
│
└── 07_Website/
    │
    ├── Frontend/
    │
    └── Streamlit_App/
        ├── app.py
        └── requirements.txt
```

---

# 📊 Final Carbon Prediction Dataset

The dashboard uses:

```text
04_Data/
└── 07_Processed_Grid_Dataset/
    └── 04_Final_Output/
        └── carbon_all_66790_final.csv
```

Important fields include:

```text
Grid_ID
WKT
Ag/NonAg_m
agri_class
DEM_mean
Slope_mean
sand_pct
clay_pct
bd_gcm3
Predicted_SOC
BGC_tC_ha
Predicted_NPP
AGC_tC_ha
source
Total_C_tC_ha
Total_CO2e_tC_ha
```

---

# 📈 Model Evaluation

Model performance is evaluated using standard regression metrics including:

| Metric | Description                  |
| ------ | ---------------------------- |
| R²     | Coefficient of Determination |
| RMSE   | Root Mean Square Error       |
| MAE    | Mean Absolute Error          |

Detailed model evaluation files are available within the project code and model-results directories.

---

# 📦 Large Files

Some spatial datasets, prediction outputs, archives and model files may exceed GitHub's standard file-size limits.

Large datasets are therefore maintained externally where required.

Download instructions are provided in:

```text
04_Data/README.md
```

Users should follow the download instructions before attempting to reproduce the complete workflow.

---

# ▶️ Running the Streamlit Dashboard Locally

Clone the repository:

```bash
git clone https://github.com/HimanshuBhanja/District-Level-Carbon-Stock-Estimation.git
```

Navigate to the application:

```bash
cd District-Level-Carbon-Stock-Estimation/07_Website/Streamlit_App
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

# ☁️ Deployment

The Streamlit dashboard is deployed using **Streamlit Community Cloud**.

### Live URL

https://district-level-carbon-stock-estimation.streamlit.app/

The application is connected to the project's GitHub repository and uses:

```text
Branch: main

Application:
07_Website/Streamlit_App/app.py
```

---

# 🌍 Applications

The developed framework can support:

* Agricultural carbon monitoring
* Carbon accounting
* Climate mitigation planning
* Soil carbon assessment
* Spatial decision support
* Sustainable agricultural management
* Carbon stock visualization
* Remote sensing-based environmental monitoring

---

# 👨‍💻 Author

**Himanshu Bhanja**

M.Sc. Agriculture Analytics

Indian Institute of Remote Sensing (IIRS–ISRO)

### Areas of Expertise

* Remote Sensing
* GIS and Spatial Analysis
* Geospatial Data Science
* Machine Learning
* Python
* Google Earth Engine
* QGIS
* PostgreSQL/PostGIS
* Agricultural Analytics

---

# 📄 Project Report

The detailed technical report is available in:

```text
02_Report/
```

---

# 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

# 📌 Conclusion

This project demonstrates an integrated geospatial machine learning framework for estimating agricultural carbon stock at district scale.

By combining remote sensing, soil properties, productivity indicators, spatial modeling and machine learning, the workflow generates spatially explicit carbon estimates and presents them through an interactive web-based dashboard.

The resulting **Carbon Stock Intelligence** platform provides a practical interface for exploring carbon stock, vegetation dynamics and spatial prediction outputs for Ludhiana District.
