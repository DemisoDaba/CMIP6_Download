import os
from pyesgf.search import SearchConnection
import xarray as xr

# Step 1: Define parameters for downloading CMIP6 Data
esgf_url = "https://esgf-node.llnl.gov/esg-search"
conn = SearchConnection(esgf_url, distributed=True)

# Define the CMIP6 project and model
project = "CMIP6"
model = "MRI-ESM2-0"  # You can choose another model (e.g., "MPI-ESM1-2-HR")
experiment = "ssp245"  # You can specify other experiments like "historical", "ssp585", etc.
variable = "tas"  # Example variable (temperature). You can change this to other variables like "pr" for rainfall
frequency = "mon"  # Monthly data frequency, can be "day", "yr", etc.
start_time = "2001"  # Start year for the data range
end_time = "2005"  # End year for the data range

# Facets for filtering the data (you can keep "latest" and "replica")
facets = ["latest", "replica"]

# Step 2: Perform the search query for the specified parameters
search = conn.search(
    project=project,
    model=model,
    experiment=experiment,
    variable=variable,
    frequency=frequency,  # Monthly data
    time=f"{start_time}/{end_time}",  # Define the time period for 5 years
    format="application/solr+xml",  # Specify data format
    facets=facets  # Add facets for filtering the data
)

# Step 3: Get the current working directory and create 'CMIP6' folder if it doesn't exist
current_directory = os.getcwd()
cmip6_dir = os.path.join(current_directory, "CMIP6")
if not os.path.exists(cmip6_dir):
    os.makedirs(cmip6_dir)

# Set the file path for saving the downloaded file
file_path = os.path.join(cmip6_dir, "cmip6file.nc")

# Step 4: Download the dataset if found
if search:
    dataset = search[0]  # Get the first dataset from the search results
    print(f"Downloading {dataset.title}")
    dataset.download(target_dir=cmip6_dir)  # Download to the CMIP6 folder

# Step 5: Subset the Data for Ethiopia (Latitude: 3°N to 15°N, Longitude: 33°E to 48°E)
ds = xr.open_dataset(file_path)  # Open the downloaded dataset
lat_min, lat_max = 3, 15  # Latitude range for Ethiopia
lon_min, lon_max = 33, 48  # Longitude range for Ethiopia

# Subset the data for Ethiopia
subset = ds.sel(lat=slice(lat_min, lat_max), lon=slice(lon_min, lon_max))

# Step 6: Save the subsetted data for Ethiopia
subset_file = os.path.join(cmip6_dir, "ethiopia_temperature_data.nc")  # Save with a relevant name
subset.to_netcdf(subset_file)

print(f"Data for Ethiopia has been saved to {subset_file}")
