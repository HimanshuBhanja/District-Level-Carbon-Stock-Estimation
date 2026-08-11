# District-Level Carbon Stock Estimation

### Grid-Based Machine Learning Framework for Agricultural Landscapes in Ludhiana District, Punjab, India

---

## Repository Highlights

✔ District-wide Carbon Stock Estimation

✔ 66,790 Spatial Grid Cells Analyzed

✔ Integration of Remote Sensing, Soil, and Productivity Data

✔ Random Forest and XGBoost Machine Learning Models

✔ Interactive Carbon Intelligence Web Application

✔ PostgreSQL/PostGIS and MongoDB-Based Data Architecture

---

## Project Overview

This project estimates the total carbon stock of Ludhiana District, Punjab, India, using a grid-based spatial framework and machine learning techniques.

The study integrates remote sensing products, soil properties, and vegetation productivity datasets to estimate both above-ground carbon (AGC) and below-ground carbon (BGC) across agricultural landscapes.

Machine learning models were trained using sampled grid cells and subsequently applied to predict carbon stock across all 66,790 grid cells covering the district.

The final outputs are visualized through an interactive web application designed for carbon monitoring, reporting, and decision support.

---

## Project Objectives

1. Generate a district-wide 250 m × 250 m grid framework.
2. Identify agricultural areas using LULC-based masking.
3. Extract environmental and geospatial variables for each grid cell.
4. Estimate above-ground carbon using productivity indicators.
5. Estimate below-ground carbon using soil properties.
6. Train machine learning models using representative sample grids.
7. Predict carbon stock for all district grid cells.
8. Generate district-wide carbon stock maps and summaries.
9. Deploy an interactive carbon intelligence platform.

---

## Study Area

| Parameter                     | Value                            |
| ----------------------------- | -------------------------------- |
| Study Area                    | Ludhiana District, Punjab, India |
| Grid Resolution               | 250 m × 250 m                    |
| Area per Grid                 | 6.25 ha                          |
| Total Grid Cells              | 66,790                           |
| Agricultural Grid Cells       | ~50,402                          |
| Above-Ground Training Samples | 12,602                           |
| Below-Ground Training Samples | 20,000                           |

---

## System Workflow

```text
Remote Sensing Data
        +
Soil Data
        +
NPP Data
        ↓
Feature Extraction
        ↓
Training Dataset Creation
        ↓
Random Forest & XGBoost Models
        ↓
District-Wide Prediction
        ↓
Carbon Stock Mapping
        ↓
Interactive Web Application
```

---

## Methodology

### Step 1: Study Area Preparation

The administrative boundary of Ludhiana District was prepared and used as the Area of Interest (AOI).

### Step 2: Grid Generation

A uniform 250 m × 250 m grid framework was generated across the district.

### Step 3: Agricultural Masking

Land Use Land Cover (LULC) data was used to identify agricultural areas.

Only agricultural grid cells were retained for carbon estimation.

### Step 4: Feature Extraction

Environmental variables were extracted using zonal statistics.

#### Remote Sensing Variables

* NDVI (Normalized Difference Vegetation Index)
* NDWI (Normalized Difference Water Index)
* Land Surface Temperature (LST)
* Precipitation
* DEM
* Slope

#### Soil Variables

* Soil Organic Carbon (SOC)
* Bulk Density
* Clay Content
* Sand Content

#### Productivity Variable

* Net Primary Productivity (NPP)

### Step 5: Carbon Stock Calculation

#### Above-Ground Carbon

AGC = NPP × 0.47

where:

* NPP = Net Primary Productivity
* 0.47 = Carbon fraction of biomass

#### Soil Organic Carbon Stock

SOC Stock = SOC × Bulk Density × Depth ÷ 10

where:

* Depth = 30 cm

### Step 6: Machine Learning Model Development

Separate models were developed for:

* Above-Ground Carbon
* Below-Ground Carbon

Algorithms used:

* Random Forest
* XGBoost

### Step 7: District-Wide Prediction

Trained models were applied to all 66,790 grid cells.

Predictions were combined to generate district-level carbon stock estimates.

### Step 8: Web Platform Deployment

Prediction outputs were integrated into a web application powered by:

* Flask
* PostgreSQL/PostGIS
* MongoDB Atlas

---

## Data Sources

| Dataset                  | Source                     |
| ------------------------ | -------------------------- |
| NDVI                     | Sentinel-2                 |
| NDWI                     | Sentinel-2                 |
| Land Surface Temperature | Satellite-derived products |
| DEM                      | SRTM / Copernicus DEM      |
| Slope                    | Derived from DEM           |
| Precipitation            | Climate Raster Products    |
| NPP                      | MODIS NPP                  |
| Soil Organic Carbon      | ISRIC SoilGrids            |
| Bulk Density             | ISRIC SoilGrids            |
| Clay Content             | ISRIC SoilGrids            |
| Sand Content             | ISRIC SoilGrids            |

---

## Machine Learning Models

### Random Forest

An ensemble learning algorithm capable of modeling complex nonlinear relationships between environmental variables and carbon stock.

### XGBoost

A gradient boosting framework that improves predictive performance through iterative learning.

Four models were developed:

* Above-Ground Carbon Random Forest
* Above-Ground Carbon XGBoost
* Below-Ground Carbon Random Forest
* Below-Ground Carbon XGBoost

---

## Model Evaluation

The following metrics were used:

| Metric | Description                  |
| ------ | ---------------------------- |
| R²     | Coefficient of Determination |
| RMSE   | Root Mean Square Error       |
| MAE    | Mean Absolute Error          |

Detailed evaluation reports are available in:

```text
03_Code/evaluation_report.txt
03_Code/carbon_final_report.txt
```

---

## Repository Structure

```text
District-Level-Carbon-Stock-Estimation
│
├── README.md
├── PROJECT_FLOW.md
├── FOLDER_STRUCTURE.md
│
├── 01_Presentation/
├── 02_Report/
├── 03_Code/
├── 04_Data/
├── 05_Model_Results/
├── 06_Trained_Models/
└── 07_Website/
```

---

## Large File Downloads

Certain raster datasets and trained machine learning models exceed GitHub's file size limitations.

Download instructions are provided inside their respective folders.

Examples:

```text
04_Data/03_LULC_Data/
04_Data/04_Remote_Sensing_Inputs/
06_Trained_Models/
```

Each folder contains download instructions and dataset descriptions.

---

## Key Results

| Metric                  | Value             |
| ----------------------- | ----------------- |
| Total Grid Cells        | 66,790            |
| Agricultural Grid Cells | ~50,402           |
| Estimated District Area | ~4,168 km²        |
| Above-Ground Carbon     | ~1.66 Million tC  |
| Below-Ground Carbon     | ~52.56 Million tC |
| Total Carbon Stock      | ~54.23 Million tC |

---

## Software and Technologies

| Tool                | Purpose                        |
| ------------------- | ------------------------------ |
| Google Earth Engine | Remote Sensing Data Processing |
| QGIS                | Spatial Analysis               |
| Python              | Data Processing and Modeling   |
| Scikit-Learn        | Random Forest Modeling         |
| XGBoost             | Gradient Boosting Models       |
| PostgreSQL/PostGIS  | Spatial Database               |
| MongoDB Atlas       | Carbon Data Storage            |
| Flask               | Backend API                    |
| Leaflet.js          | Interactive Mapping            |
| Render              | Cloud Deployment               |

---

## Project Report

The detailed technical report is available in:

```text
02_Report/Carbon_Stock_Report.docx
```

---

## How to Run

1. Open `03_Code/carbon_stock_pipeline_FIXED.ipynb`.
2. Ensure all required datasets are available in the corresponding data folders.
3. Run notebook cells sequentially.
4. Generated models will be saved in `06_Trained_Models/`.
5. Visualizations will be saved in `05_Model_Results/`.
6. Final predictions will be generated in:

```text
04_Data/07_Processed_Grid_Dataset/04_Final_Output/
```

---

## Author

**Himanshu Bhanja**

M.Sc. Agriculture Analytics

Indian Institute of Remote Sensing (IIRS–ISRO)

### Skills

* Remote Sensing
* GIS and Spatial Analysis
* Machine Learning
* Python
* PostgreSQL/PostGIS
* Geospatial Data Science

---

## Conclusion

This project demonstrates the integration of remote sensing, geospatial analytics, soil science, and machine learning to estimate district-level carbon stock using a scalable grid-based framework.

The developed workflow enables carbon monitoring at landscape scale and provides a foundation for climate mitigation planning, carbon accounting, and sustainable agricultural management.
