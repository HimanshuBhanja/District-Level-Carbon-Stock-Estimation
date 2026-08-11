import streamlit as st
import pandas as pd
from pathlib import Path

# ============================================================
# STREAMLIT PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Carbon Stock Intelligence",
    page_icon="🌱",
    layout="wide"
)

# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CARBON_DATA = (
    PROJECT_ROOT
    / "04_Data"
    / "07_Processed_Grid_Dataset"
    / "04_Final_Output"
    / "carbon_all_66790_final.csv"
)

NDVI_FILE = (
    PROJECT_ROOT
    / "04_Data"
    / "04_Remote_Sensing_Inputs"
    / "ndvi_monthly_ludhiana_jun24_may25.csv"
)

# ============================================================
# NDVI MONTH DEFINITIONS
# ============================================================

NDVI_COLUMNS = [
    "NDVI_Jun24",
    "NDVI_Jul24",
    "NDVI_Aug24",
    "NDVI_Sep24",
    "NDVI_Oct24",
    "NDVI_Nov24",
    "NDVI_Dec24",
    "NDVI_Jan25",
    "NDVI_Feb25",
    "NDVI_Mar25",
    "NDVI_Apr25",
    "NDVI_May25"
]

MONTH_LABELS = [
    "Jun 2024",
    "Jul 2024",
    "Aug 2024",
    "Sep 2024",
    "Oct 2024",
    "Nov 2024",
    "Dec 2024",
    "Jan 2025",
    "Feb 2025",
    "Mar 2025",
    "Apr 2025",
    "May 2025"
]

# ============================================================
# LOAD CARBON DATA
# ============================================================

@st.cache_data
def load_carbon_data():

    df = pd.read_csv(CARBON_DATA)

    # Standardize Grid_ID
    df["Grid_ID"] = (
        pd.to_numeric(
            df["Grid_ID"],
            errors="coerce"
        )
        .astype("Int64")
    )

    return df


# ============================================================
# LOAD AND CLEAN NDVI DATA
# ============================================================

@st.cache_data
def load_ndvi_data():

    ndvi = pd.read_csv(NDVI_FILE)

    # --------------------------------------------------------
    # Standardize Grid_ID
    # --------------------------------------------------------

    ndvi["Grid_ID"] = (
        pd.to_numeric(
            ndvi["Grid_ID"],
            errors="coerce"
        )
        .astype("Int64")
    )

    # --------------------------------------------------------
    # Convert NDVI columns to numeric
    # --------------------------------------------------------

    for column in NDVI_COLUMNS:

        if column in ndvi.columns:

            ndvi[column] = pd.to_numeric(
                ndvi[column],
                errors="coerce"
            )

    # --------------------------------------------------------
    # Remove records without Grid_ID
    # --------------------------------------------------------

    ndvi = ndvi.dropna(
        subset=["Grid_ID"]
    )

    # --------------------------------------------------------
    # Remove duplicate Grid_ID issue
    #
    # If one Grid_ID occurs multiple times,
    # calculate the mean NDVI for every month.
    # --------------------------------------------------------

    ndvi_clean = (
        ndvi
        .groupby(
            "Grid_ID",
            as_index=False
        )[NDVI_COLUMNS]
        .mean()
    )

    return ndvi_clean


# ============================================================
# LOAD DATA
# ============================================================

try:

    df = load_carbon_data()

except Exception as e:

    st.error(
        f"Unable to load carbon dataset: {e}"
    )

    st.stop()


try:

    ndvi_df = load_ndvi_data()

except Exception as e:

    st.error(
        f"Unable to load NDVI dataset: {e}"
    )

    st.stop()


# ============================================================
# HEADER
# ============================================================

st.title("🌱 Carbon Stock Intelligence")

st.subheader(
    "District-Level Carbon Stock Estimation — Ludhiana"
)

st.write(
    "Interactive dashboard for exploring above-ground carbon, "
    "below-ground carbon, NDVI and spatial carbon predictions."
)


# ============================================================
# DATA STATUS
# ============================================================

st.success(
    "Carbon prediction dataset loaded successfully."
)

col1, col2 = st.columns(2)

with col1:

    st.write(
        f"**Carbon prediction grids:** {len(df):,}"
    )

with col2:

    st.write(
        f"**Unique NDVI grids:** {len(ndvi_df):,}"
    )


# ============================================================
# CARBON STOCK OVERVIEW
# ============================================================

st.subheader("Carbon Stock Overview")

avg_agc = df["AGC_tC_ha"].mean()

avg_bgc = df["BGC_tC_ha"].mean()

avg_total = df["Total_C_tC_ha"].mean()

avg_co2e = df["Total_CO2e_tC_ha"].mean()


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Above-Ground Carbon",
        f"{avg_agc:,.2f} t C/ha"
    )


with col2:

    st.metric(
        "Below-Ground Carbon",
        f"{avg_bgc:,.2f} t C/ha"
    )


with col3:

    st.metric(
        "Total Carbon",
        f"{avg_total:,.2f} t C/ha"
    )


with col4:

    st.metric(
        "CO₂ Equivalent",
        f"{avg_co2e:,.2f} t CO₂e/ha"
    )


# ============================================================
# CARBON COMPONENT COMPARISON
# ============================================================

st.subheader("Carbon Component Comparison")

carbon_chart = pd.DataFrame({

    "Carbon Component": [
        "Above-Ground Carbon",
        "Below-Ground Carbon",
        "Total Carbon"
    ],

    "Mean Carbon (t C/ha)": [
        avg_agc,
        avg_bgc,
        avg_total
    ]

})


st.bar_chart(
    carbon_chart,
    x="Carbon Component",
    y="Mean Carbon (t C/ha)"
)


# ============================================================
# NDVI TEMPORAL ANALYSIS
# ============================================================

st.subheader("NDVI Temporal Analysis")


# ------------------------------------------------------------
# Calculate monthly mean NDVI across available NDVI grids
# ------------------------------------------------------------

monthly_ndvi = ndvi_df[NDVI_COLUMNS].mean()


ndvi_chart = pd.DataFrame({

    "Month": MONTH_LABELS,

    "Mean NDVI": monthly_ndvi.values

})


ndvi_chart = ndvi_chart.set_index("Month")


# ------------------------------------------------------------
# NDVI LINE CHART
# ------------------------------------------------------------

st.line_chart(
    ndvi_chart,
    y="Mean NDVI"
)


# ============================================================
# NDVI SUMMARY
# ============================================================

col1, col2, col3 = st.columns(3)


with col1:

    overall_mean_ndvi = (
        ndvi_chart["Mean NDVI"].mean()
    )

    st.metric(
        "Mean NDVI",
        f"{overall_mean_ndvi:.3f}"
    )


with col2:

    max_month = (
        ndvi_chart["Mean NDVI"]
        .idxmax()
    )

    max_value = (
        ndvi_chart["Mean NDVI"]
        .max()
    )

    st.metric(
        "Peak NDVI",
        f"{max_value:.3f}",
        max_month
    )


with col3:

    min_month = (
        ndvi_chart["Mean NDVI"]
        .idxmin()
    )

    min_value = (
        ndvi_chart["Mean NDVI"]
        .min()
    )

    st.metric(
        "Lowest NDVI",
        f"{min_value:.3f}",
        min_month
    )


# ============================================================
# MONTHLY NDVI TABLE
# ============================================================

with st.expander("View Monthly NDVI Values"):

    display_ndvi = ndvi_chart.copy()

    display_ndvi["Mean NDVI"] = (
        display_ndvi["Mean NDVI"]
        .round(4)
    )

    st.dataframe(
        display_ndvi,
        use_container_width=True
    )


# ============================================================
# GRID-LEVEL ANALYSIS
# ============================================================

st.subheader("Grid-Level Carbon and NDVI Analysis")


# ------------------------------------------------------------
# Carbon Grid Selector
# ------------------------------------------------------------

grid_ids = (
    df["Grid_ID"]
    .dropna()
    .astype(int)
    .sort_values()
    .unique()
)


selected_grid = st.selectbox(
    "Select Grid ID",
    grid_ids,
    index=0
)


# ============================================================
# SELECTED CARBON GRID
# ============================================================

selected_carbon = df[
    df["Grid_ID"] == selected_grid
]


if selected_carbon.empty:

    st.error(
        "Selected Grid ID was not found in the carbon dataset."
    )

    st.stop()


carbon_record = selected_carbon.iloc[0]


# ============================================================
# SELECTED GRID CARBON KPIs
# ============================================================

st.markdown(
    f"## Selected Grid: {selected_grid}"
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Above-Ground Carbon",
        f"{carbon_record['AGC_tC_ha']:,.2f} t C/ha"
    )


with col2:

    st.metric(
        "Below-Ground Carbon",
        f"{carbon_record['BGC_tC_ha']:,.2f} t C/ha"
    )


with col3:

    st.metric(
        "Total Carbon",
        f"{carbon_record['Total_C_tC_ha']:,.2f} t C/ha"
    )


with col4:

    st.metric(
        "CO₂ Equivalent",
        f"{carbon_record['Total_CO2e_tC_ha']:,.2f} t CO₂e/ha"
    )


# ============================================================
# SELECTED GRID NDVI PROFILE
# ============================================================

st.subheader(
    f"Monthly NDVI Profile — Grid {selected_grid}"
)


selected_ndvi = ndvi_df[
    ndvi_df["Grid_ID"] == selected_grid
]


if selected_ndvi.empty:

    st.warning(
        f"NDVI data is not available for Grid {selected_grid}. "
        "Carbon prediction is available, but this particular "
        "grid does not have a matching NDVI record."
    )

else:

    # --------------------------------------------------------
    # Extract cleaned NDVI profile
    # --------------------------------------------------------

    ndvi_record = selected_ndvi.iloc[0]

    selected_ndvi_values = []

    for column in NDVI_COLUMNS:

        value = ndvi_record[column]

        if pd.isna(value):

            selected_ndvi_values.append(None)

        else:

            selected_ndvi_values.append(
                float(value)
            )


    # --------------------------------------------------------
    # Create profile dataframe
    # --------------------------------------------------------

    selected_ndvi_chart = pd.DataFrame({

        "Month": MONTH_LABELS,

        "NDVI": selected_ndvi_values

    })


    selected_ndvi_chart = (
        selected_ndvi_chart
        .set_index("Month")
    )


    # --------------------------------------------------------
    # NDVI PROFILE CHART
    # --------------------------------------------------------

    st.line_chart(
        selected_ndvi_chart,
        y="NDVI"
    )


    # --------------------------------------------------------
    # Grid NDVI statistics
    # --------------------------------------------------------

    valid_ndvi = (
        selected_ndvi_chart["NDVI"]
        .dropna()
    )


    if not valid_ndvi.empty:

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Grid Mean NDVI",
                f"{valid_ndvi.mean():.3f}"
            )


        with col2:

            peak_month = valid_ndvi.idxmax()

            peak_value = valid_ndvi.max()

            st.metric(
                "Grid Peak NDVI",
                f"{peak_value:.3f}",
                peak_month
            )


        with col3:

            lowest_month = valid_ndvi.idxmin()

            lowest_value = valid_ndvi.min()

            st.metric(
                "Grid Lowest NDVI",
                f"{lowest_value:.3f}",
                lowest_month
            )


    # --------------------------------------------------------
    # Monthly values
    # --------------------------------------------------------

    with st.expander(
        f"View NDVI Values — Grid {selected_grid}"
    ):

        st.dataframe(
            selected_ndvi_chart.round(4),
            use_container_width=True
        )


# ============================================================
# SELECTED GRID CARBON ATTRIBUTES
# ============================================================

with st.expander(
    f"View Carbon Attributes — Grid {selected_grid}"
):

    st.dataframe(
        selected_carbon,
        use_container_width=True
    )


# ============================================================
# INTEGRATED CARBON-NDVI DATASET
# ============================================================

st.subheader("Integrated Carbon–NDVI Dataset")


# ------------------------------------------------------------
# Carbon remains the MASTER dataset.
#
# LEFT JOIN means:
#
# 64,545 carbon grids are retained.
# NDVI values are added where available.
# ------------------------------------------------------------

integrated_df = df.copy()


integrated_df = integrated_df.merge(
    ndvi_df,
    on="Grid_ID",
    how="left"
)


st.write(
    f"**Integrated records:** {len(integrated_df):,}"
)


# ------------------------------------------------------------
# Calculate actual NDVI coverage
#
# We use Grid_ID membership rather than one particular
# monthly column so that the statistic means:
# "How many carbon grids have an NDVI profile?"
# ------------------------------------------------------------

ndvi_grid_set = set(
    ndvi_df["Grid_ID"]
    .dropna()
    .astype(int)
)


carbon_grid_set = set(
    df["Grid_ID"]
    .dropna()
    .astype(int)
)


ndvi_available_count = len(
    carbon_grid_set.intersection(
        ndvi_grid_set
    )
)


ndvi_missing_count = (
    len(carbon_grid_set)
    - ndvi_available_count
)


# ============================================================
# DATA COVERAGE INFORMATION
# ============================================================

col1, col2 = st.columns(2)


with col1:

    st.info(
        f"NDVI profile available for "
        f"{ndvi_available_count:,} carbon grids"
    )


with col2:

    st.warning(
        f"Carbon grids without NDVI: "
        f"{ndvi_missing_count:,}"
    )


st.caption(
    "These are dataset-level coverage statistics. "
    "They do not describe the currently selected grid."
)


# ------------------------------------------------------------
# Display integrated dataset
# ------------------------------------------------------------

st.dataframe(
    integrated_df.head(10),
    use_container_width=True
)


# ============================================================
# SPATIAL CARBON STOCK DISTRIBUTION
# ============================================================

st.subheader(
    "🗺️ Spatial Carbon Stock Distribution"
)

st.write(
    "Interactive spatial visualization of predicted carbon "
    "stock across the Ludhiana district."
)


# ============================================================
# CARBON VARIABLE SELECTION
# ============================================================

carbon_variable_options = {

    "Total Carbon (t C/ha)": "Total_C_tC_ha",

    "Above-Ground Carbon (t C/ha)": "AGC_tC_ha",

    "Below-Ground Carbon (t C/ha)": "BGC_tC_ha",

    "CO₂ Equivalent (t CO₂e/ha)": "Total_CO2e_tC_ha",

    "Predicted SOC": "Predicted_SOC",

    "Predicted NPP": "Predicted_NPP"

}


selected_variable_label = st.selectbox(
    "Select Carbon Variable",
    list(carbon_variable_options.keys())
)


selected_variable = carbon_variable_options[
    selected_variable_label
]


# ============================================================
# SPATIAL MAP
# ============================================================

try:

    import pydeck as pdk
    from shapely import wkt
    from shapely.ops import unary_union


    # --------------------------------------------------------
    # Map sample
    # --------------------------------------------------------

    MAP_SAMPLE_SIZE = min(
        5000,
        len(df)
    )


    if len(df) > MAP_SAMPLE_SIZE:

        map_df = df.sample(
            MAP_SAMPLE_SIZE,
            random_state=42
        ).copy()

        st.info(
            f"Displaying {MAP_SAMPLE_SIZE:,} sampled grids "
            f"on the map for browser performance. "
            f"All {len(df):,} grids remain available for analysis."
        )

    else:

        map_df = df.copy()


    # --------------------------------------------------------
    # Convert WKT polygons
    # --------------------------------------------------------

    polygons = []

    values = []


    for _, row in map_df.iterrows():

        try:

            geometry = wkt.loads(
                row["WKT"]
            )

            geometry_type = geometry.geom_type


            # ------------------------------------------------
            # Polygon
            # ------------------------------------------------

            if geometry_type == "Polygon":

                polygons.append(
                    [
                        list(ring.coords)
                        for ring in geometry.interiors
                    ]
                    +
                    [
                        list(geometry.exterior.coords)
                    ]
                )

                values.append(
                    float(
                        row[selected_variable]
                    )
                )


            # ------------------------------------------------
            # MultiPolygon
            # ------------------------------------------------

            elif geometry_type == "MultiPolygon":

                for polygon in geometry.geoms:

                    polygons.append(
                        [
                            list(ring.coords)
                            for ring in polygon.interiors
                        ]
                        +
                        [
                            list(
                                polygon.exterior.coords
                            )
                        ]
                    )

                    values.append(
                        float(
                            row[selected_variable]
                        )
                    )


        except Exception:

            continue


    # ========================================================
    # RENDER MAP
    # ========================================================

    if polygons:

        map_plot_df = pd.DataFrame({

            "polygon": polygons,

            "value": values

        })


        # ----------------------------------------------------
        # Find approximate map centre
        # ----------------------------------------------------

        map_geometries = []


        for _, row in map_df.head(500).iterrows():

            try:

                geometry = wkt.loads(
                    row["WKT"]
                )

                map_geometries.append(
                    geometry
                )

            except Exception:

                pass


        if map_geometries:

            combined_geometry = unary_union(
                map_geometries
            )

            center = combined_geometry.centroid

            map_lat = center.y

            map_lon = center.x

        else:

            map_lat = 30.90

            map_lon = 75.85


        # ----------------------------------------------------
        # Polygon layer
        # ----------------------------------------------------

        polygon_layer = pdk.Layer(

            "PolygonLayer",

            map_plot_df,

            get_polygon="polygon",

            get_fill_color=[
                30,
                120,
                180,
                140
            ],

            get_line_color=[
                255,
                255,
                255,
                80
            ],

            line_width_min_pixels=0.5,

            pickable=True,

            auto_highlight=True

        )


        # ----------------------------------------------------
        # Tooltip
        # ----------------------------------------------------

        tooltip = {

            "html": (
                "<b>Value:</b> {value}"
                "<br/>"
                f"<b>Variable:</b> "
                f"{selected_variable_label}"
            ),

            "style": {
                "backgroundColor": "black",
                "color": "white"
            }

        }


        # ----------------------------------------------------
        # View
        # ----------------------------------------------------

        view_state = pdk.ViewState(

            latitude=map_lat,

            longitude=map_lon,

            zoom=9,

            pitch=0

        )


        # ----------------------------------------------------
        # Render
        # ----------------------------------------------------

        deck = pdk.Deck(

            layers=[
                polygon_layer
            ],

            initial_view_state=view_state,

            tooltip=tooltip

        )


        st.pydeck_chart(
            deck,
            use_container_width=True
        )


    else:

        st.warning(
            "No valid polygon geometries were available "
            "for the spatial map."
        )


except ImportError:

    st.warning(
        "Spatial map requires Shapely and PyDeck. "
        "The rest of the dashboard is still available."
    )


except Exception as e:

    st.warning(
        f"Spatial map could not be generated: {e}"
    )


# ============================================================
# DATASET SUMMARY
# ============================================================

st.subheader("Dataset Summary")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Carbon Grids",
        f"{len(df):,}"
    )


with col2:

    st.metric(
        "Unique NDVI Grids",
        f"{len(ndvi_df):,}"
    )


with col3:

    st.metric(
        "NDVI Monthly Variables",
        len(NDVI_COLUMNS)
    )


with col4:

    coverage = (
        ndvi_available_count
        / len(carbon_grid_set)
        * 100
    )

    st.metric(
        "NDVI Coverage",
        f"{coverage:.1f}%"
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Carbon Stock Intelligence | "
    "District-Level Carbon Stock Estimation — Ludhiana"
)