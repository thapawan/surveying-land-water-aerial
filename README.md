# Surveying: Land • Water • Aerial

A unified, open repository for **land, hydrographic (water), and UAV/aerial surveying** workflows—bridging **geomatics, remote sensing, and river science**. Curated by **Pawan Thapa**.


## Total Station Survey Photo

<p align="center">
  <img src="https://github.com/thapawan/surveying-land-water-aerial/blob/main/Photos/TotalStation.jpg"
</p>


## Why this repo?
Researchers and practitioners often split **land**, **water**, and **aerial** work into separate silos. This repo keeps them together with a consistent structure, so you can:

- Reuse field + UAV + GIS methods across projects
- Compare **river corridor** change with **floodplain** and **bank** metrics
- Document **repeatable** workflows (from raw data → analysis → map/report)

## Key Capabilities

### Land: GNSS/RTK processing, ground control, DEM/DSM generation, breaklines
### Water: River centerline & curvature, banklines, flood extent (SAR/optical), AWEI/NDWI, migration metrics, SHAP/XAI for drivers
### Aerial/UAV: Mission planning, radiometric calibration, sensor notes (RGB, multispectral, thermal, LiDAR), image alignment, orthomosaics, water-surface masking

---

## Repository Structure

```text
surveying-land-water-aerial/
├─ data/                # Small sample/test data & README links to large data locations
│  ├─ land/
│  ├─ water/
│  └─ aerial/
├─ notebooks/          # Jupyter notebooks (EDA, methods, results)
│  ├─ land/
│  ├─ water/
│  └─ aerial/
├─ src/                # Reusable Python modules
│  ├─ land/            # topography, GNSS/RTK, control networks, DEMs
│  ├─ water/           # river centerlines, migration, bathy, discharge proxies
│  ├─ aerial/          # flight planning, radiometric calib, ortho/DSM, QA/QC
│  └─ common/          # io, utils, CRS, tiling, validation
├─ scripts/            # CLI helpers (data prep, tiles, export)
├─ docs/               # Project docs, figures, reports
├─ README.md
├─ LICENSE (MIT)
└─ .gitignore

'''

conda create -n survey python=3.11 -y
conda activate survey
pip install -r requirements.txt

# Example: compute river curvature metrics from a centerline
python -m src.water.example_curvature --centerline data/water/sample_centerline.geojson \
    --out docs/curvature_demo.geojson

@misc{surveying_land_water_aerial,
  title        = {Surveying: Land • Water • Aerial},
  author       = {Thapa, Pawan},
  year         = {2026},
  howpublished = {GitHub repository},
  url          = {https://github.com/USERNAME/surveying-land-water-aerial}
}
``
