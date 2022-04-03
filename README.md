## Introduction
The goal of this project is to provide a framework for acquiring and pre-processing magnetic field data collected by the MESSENGER mission to Mercury in 2011-2015, and make this data suitable for analytical analysis and machine learning projects.

The original datasets and the accompanying metadata files are hosted by [NASA PDS PPI](https://pds-ppi.igpp.ucla.edu/search/view/?f=yes&id=pds://PPI/MESS-E_V_H_SW-MAG-4-SUMM-CALIBRATED-V1.0/DATA/MSO).

The following pre-processing steps are performed by the present project:
* Elimination of calibration signals. As a part of maintenance procedures, the MESSENGER magnetometer needed to be occasionally calibrated. However, the measurements of the magnetometer collected while a calibration signal was applied to it are still present in the original datasets. These signals are located and removed by us so that subsequent analysis is not biased by them.
* Enrichment with Mercury information. For a number of scientific purposes it may be useful to possess information not only on the magnetic field and the position of the spacecraft in the space around Mercury, but also information on the position of the planet around the Sun. We acquire this information from the [NAZA Horizons](https://ssd.jpl.nasa.gov/horizons/) application and merge it with the main dataset.
* Restructurization. The original data files are split according to UTC-based day boundaries. However, for many scientific purposes it is preferable to possess data split according to orbit boundaries. We use MESSENGER orbit apoapsis points as markers to separate individual orbits. We also enumerate the orbits in the same manner as [Philpott et al., 2020](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019JA027544); this enumeration has some differences from the enumeration of orbits as calculated according to the orbital correction maneuver table.
* Enrichment with auxiliary information. To simplify subsequent analysis, we also include the estimated planetary dipole magnetic field contribution for each point, planetocentric distance of the spacecraft and several other items explained in detail further.


## Setting up
To initialize the workspace, simply run `bash setup.sh` in the project directory. This will initialize the Python virtual environment, download and unpack the magnetic field files, Mercury orbital information and magnetometer checkout information. 

## Usage
The main workload is performed by the `master.py` Python script. First, activate the Python virtual environment in the project's directory:
```bash
$ source venv/bin/activate
```
This will ensure that the dependencies installed during setup are available to it.
Now, simply run the main script as follows:
```bash
$ python3 master.py [RESOLUTION] [YEAR] [DOY_START] [DOY_END]
```

Here:
* `RESOLUTION` is the temporal resolution of the magnetometer data that you are interested in (valid options are 1, 5, 10, 60 seconds; default is 60)
* `YEAR` is the year to process (when not provided, process all years by default)
* `DOY_START` is the first day of the year to process (Jan.1st  by default)
* `DOY_END` is the last day of the year to process (Dec.31st by default)
