Here is a **clean, polished, final version** of your **Surveying: Land • Water • Aerial** project description, with your **ResearchGate Lab** and **GitHub repository** links properly integrated.  
You can paste this into **GitHub README**, **ResearchGate**, **Spatialnode**, **your website**, or as a project description in a portfolio.

***

# **Surveying: Land • Water • Aerial**

**Surveying: Land • Water • Aerial** is a unified, open repository for **land surveying**, **hydrographic/water science**, and **UAV/aerial mapping** workflows—bridging geomatics, remote sensing, and river science.  
Curated by **Pawan Thapa**.

***

## 🌍 Why This Repo?

Land, water, and aerial surveying workflows are often separated into different pipelines. This repository keeps them together in one consistent structure so you can:

*   Reuse **field + UAV + GIS** methods across projects
*   Compare **river corridor changes** with floodplain, bank, and migration metrics
*   Document **repeatable, transparent workflows** from *raw data → analysis → maps/reports*

***

## 🔑 Key Capabilities

### **Land**

*   GNSS/RTK workflows
*   Ground control point (GCP) management
*   DEM/DSM generation
*   Breaklines, terrain correction

### **Water**

*   River centerline + curvature metrics
*   Banklines & migration analysis
*   Flood extent mapping (SAR/optical fusion)
*   AWEI / NDWI indices
*   SHAP/XAI for geomorphic drivers

### **Aerial / UAV**

*   Mission planning
*   Radiometric calibration
*   RGB / multispectral / thermal / LiDAR notes
*   Image alignment, orthomosaics, DSMs
*   Water‑surface masking

***

## 📁 Repository Structure

    surveying-land-water-aerial/
    ├─ data/                # Sample/test data + links to large datasets
    │  ├─ land/
    │  ├─ water/
    │  └─ aerial/
    ├─ notebooks/           # Jupyter notebooks (EDA, methods, results)
    │  ├─ land/
    │  ├─ water/
    │  └─ aerial/
    ├─ src/                 # Reusable Python modules
    │  ├─ land/             # GNSS/RTK, DEMs, topo processing
    │  ├─ water/            # centerlines, migration, hydrology
    │  ├─ aerial/           # flight planning, ortho, QA/QC
    │  └─ common/           # I/O, utils, CRS, tiling
    ├─ scripts/             # CLI helpers
    ├─ docs/                # Project documentation, figures, reports
    ├─ README.md
    ├─ LICENSE (MIT)
    └─ .gitignore

***

## ⚙️ Quick Start

```bash
conda create -n survey python=3.11 -y
conda activate survey
pip install -r requirements.txt
```

### Example: Compute river curvature metrics

```bash
python -m src.water.example_curvature \
  --centerline data/water/sample_centerline.geojson \
  --out docs/curvature_demo.geojson
```

***

## 📚 Citation

```bibtex
@misc{surveying_land_water_aerial,
  title        = {Surveying: Land • Water • Aerial},
  author       = {Thapa, Pawan},
  year         = {2026},
  howpublished = {GitHub repository},
  url          = {https://github.com/thapawan/surveying-land-water-aerial}
}
```

***

## 🔗 Links

### **ResearchGate Lab**

<https://www.researchgate.net/lab/Geoinformatics-Earth-Observation-Artificial-Intelligence-Remote-Sensing-Pawan-Thapa>

### **GitHub Repository (Land/Water/UAV Projects)**

<https://github.com/thapawan/surveying-land-water-aerial>

***
