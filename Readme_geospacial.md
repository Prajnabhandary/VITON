

# Attribute Value Extraction
<a name="readme-top"></a>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href>Introduction</a></li>
       <li><a href>Solution Architecture</a>
    </li>
    <li><a href>Tools</a></li>
    <li><a href>Results</a></li>
    <li><a href >End to End pipeline</a></li>
    <!-- <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>

# Introduction
TA Agro Observer is a Dash-based web application for monitoring greenhouse gas (GHG) emissions. The application provides a user-friendly interface for visualizing methane emissions globally and at the county level in the United States. It also includes tools for estimating nitrogen and methane emissions from agricultural fields.

The increasing concern over greenhouse gas emissions and their impact on climate change has necessitated effective monitoring and management solutions. TA Agro Observer harnesses advanced data visualization and analysis capabilities to provide stakeholders with critical insights into methane and nitrogen emissions, helping to inform better agricultural practices and policy decisions.


# Solution Architecture

### Solution Diagram
An overview of the proposed framework:

![Blank diagram](https://github.com/user-attachments/assets/98a9bd05-89d4-4a56-9f39-d3c42cd2e961)





### Features

- **Methane Emission Visualization**: View global methane emissions on an interactive map and explore methane emission data at the county level in the United States.
- **County Data Dashboard**: Select a state and county to view detailed methane emission data over a specified date range.
- **Field Level Emission Calculation**: Calculate nitrogen emissions for specific agricultural fields based on their location and the season.
- **Methane Emission Analysis from Sentinel-2 Data**: Perform detailed methane emission analysis using Sentinel-2 satellite data.

# Tools

- **Dash and Plotly**: Used for creating interactive web-based dashboards and visualizations.
- **Google Earth Engine (GEE)**: Leveraged for remote sensing data retrieval and processing.
- **GeoPandas and Shapely**: Utilized for geospatial data manipulation and analysis.
- **PlotlyMap (geemap)**: Employed for advanced geospatial visualizations.
- **Pandas**: Used for data manipulation and analysis.


# Results

### Home Page
- Welcoming interface with an intuitive user input system.
- Personalized user experience with a name input and submission functionality.
- Navigation to a detailed analysis page for in-depth insights.
![image (8)](https://github.com/user-attachments/assets/7e0d28fd-918f-4249-82f1-80dff2f8b74c)
### Methane Emission
- Interactive world map displaying methane emissions by country.
- Yearly selection to observe changes over time.
- Detailed information on country-wise methane emissions.
![image (10)](https://github.com/user-attachments/assets/167fa287-b267-42cb-9575-b89aec93500f)
### Field level Emission calculation
- Selection of specific agricultural fields.
- Calculation of nitrogen emissions at different growth stages: pre-planting, early growth, mid-season, and late season.
![image (9)](https://github.com/user-attachments/assets/661b85ad-a2d6-4682-a743-faecdded44aa)
### Methane Emission From Sentinal-2
- Date range selection for satellite data analysis.
- Generation of methane emission data using Sentinel-2 imagery.
- Normalized and visualized emission data on an interactive map.
![image (11)](https://github.com/user-attachments/assets/6502e74c-97c4-427a-b0d4-20c2b11ca20e)





## End to End pipeline:
We have successfully implemented the above approaches and have created an end to end pipeline. To make process very simple. Follow below instructions to run them.


### Prerequisites

- Python 3.8+

### Dependencies

Install the required Python packages using `pip`:

        $ pip install -r requirements.txt

 After installing all the required libraries, now let's run the code

        $ python app.py


Note:- This was our *version 1 release*. We, are continuosly working to improve the accuracy of the model.



