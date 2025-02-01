# CMIP6 Data Download and Subsetting for Ethiopia

This project provides a Python script that allows users to download CMIP6 data, subset the data for Ethiopia, and save it as a NetCDF file. The data is retrieved from the Earth System Grid Federation (ESGF) based on specific parameters such as model, experiment, variable, and time range. The subsetted data focuses on the geographical region of Ethiopia, including latitude from 3°N to 15°N and longitude from 33°E to 48°E.

## Script Overview

The script performs the following steps:

1. **Download CMIP6 Data**: The script queries the ESGF (Earth System Grid Federation) and downloads CMIP6 data based on the specified parameters such as project, model, experiment, variable, and time range.
   
2. **Subset the Data for Ethiopia**: Once the data is downloaded, it is subsetted to focus on the geographical area of Ethiopia, specifically with the latitude range of 3°N to 15°N and longitude range of 33°E to 48°E.
   
3. **Save the Subsetted Data**: The subsetted data is then saved as a new NetCDF file for further analysis or use.

## Usage

1. **Clone the repository or download the script** to your local machine.
   
2. **Run the script** after installing the necessary libraries. The script will automatically query the ESGF, download the dataset, and subset the data for Ethiopia.
   
3. The subsetted data will be saved in a folder named `CMIP6` in the current working directory. The resulting NetCDF file will be named `ethiopia_temperature_data.nc`.

## Customization

You can modify the following parameters in the script to customize the data download and subsetting process:

- `project`: The CMIP6 project (e.g., "CMIP6").
- `model`: The model used for the simulation (e.g., "MRI-ESM2-0").
- `experiment`: The experiment to query (e.g., "ssp245", "historical", "ssp585").
- `variable`: The variable of interest (e.g., "tas" for temperature, "pr" for precipitation).
- `frequency`: The frequency of the data (e.g., "mon" for monthly, "day" for daily, "yr" for yearly).
- `start_time` and `end_time`: The range of years for which data is downloaded (e.g., 2001-2005).
- `lat_min`, `lat_max`, `lon_min`, `lon_max`: The latitude and longitude range for subsetting the data. By default, it is set to the region covering Ethiopia (3°N to 15°N and 33°E to 48°E).

## Example Output

Once the script has finished running, you will have:

- A NetCDF file named `ethiopia_temperature_data.nc` containing the subsetted data for Ethiopia.
  
## Notes

- Ensure your machine has enough storage space as CMIP6 datasets can be quite large.
- The script assumes a basic understanding of how to interact with Python and install Python packages.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 

## GitHub Repository
You can find the code on my GitHub: [Demiso Daba](https://github.com/DemisoDaba)

