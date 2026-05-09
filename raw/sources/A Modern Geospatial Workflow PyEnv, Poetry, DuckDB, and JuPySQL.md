---
title: "A Modern Geospatial Workflow: PyEnv, Poetry, DuckDB, and JuPySQL"
source: https://medium.com/@jake.gearon_34983/a-modern-geospatial-workflow-pyenv-poetry-duckdb-and-jupysql-7e7d355655f5
author:
  - "[[Jake Gearon]]"
published: 2023-11-13
created: 2026-04-08
description: "A Modern Geospatial Workflow: PyEnv, Poetry, DuckDB, and JuPySQL I just recently took (and passed!) my PhD qualifying exam. While I was studying, I promised myself a little treat as reward afterwards …"
tags:
  - clippings
  - duckdb
  - mapping
topic:
type: note
---
[Sitemap](https://medium.com/sitemap/sitemap.xml)

I just recently took (and passed!) my PhD qualifying exam. While I was studying, I promised myself a little treat as reward afterwards — updating my personal GIS workflow. I was probably like you, happily using `conda` as my package manager, `jupyter` and PyCharm as my IDEs. It was a manageable existence, but one that often had me ripping apart `conda` environments and rebuilding time after time. This is particularly relevant for geospatial coding, as GDAL can rise from the depths and take your code hostage pretty much whenever you need it to least (`dll` errors, anyone?). This was most notable on a recent project I was helping out on. We were using a boutique neural network that identifies certain geomorphic processes from digital elevation model (DEM) data. I was struggling to use my normal `conda` workflow on the High Performance Computer here at Indiana University (If you are an experienced HPC coder, you may chortle at my naïvete…). I knew that I needed something more lightweight and flexible than a bloated geospatial `conda` installation. I was searching for options, and I settled on two software stacks to run the basis of my Python operations: PyEnv and Poetry.

*A note to the time-poor:* *I’ve written previously about* [*Python-as-GIS*](https://www.esipfed.org/merge/community-fellow-blog/python-for-gis)*, but this write-up will be much more technical and involved. I’m going to start from the beginning of my overhaul. If you want just the geospatial parts, skip to the SWORD section. However, if you are like most scientists or data scientists and use* `*conda*` *as your package manager, maybe stick around and learn something new that will save you headaches in the future. If you use the Anaconda Navigator to open Python, then definitely stick around, as its time to grow past that, folks (I say this lovingly). Additionally, I switched to Cursor IDE instead of PyCharm. Cursor itself is really just a downstream fork of VSCode that enables ~AI~. I highly recommend switching to VSCode or Cursor as its lightweight nature complements this workflow quite well. However, its a not a requirement and I won’t be covering the aspects of that switch specifically.*

## PyEnv: The Foundation

PyEnv simplifies Python version management, particularly on UNIX-based systems like macOS, where a system Python version already exists. This pre-installed Python, tucked away in `/usr/local/bin/python`, is best left untouched. It could be integral to other applications, or perhaps it's just a relic of your first Python foray. Either way, PyEnv is the safer route—it allows you to manage multiple Python versions without disrupting the system Python.

On Windows, while the concept remains the same, PyEnv uses a plugin called `pyenv-win` to replicate its functionality. No matter your OS, PyEnv ensures that you can work with any Python version, project-specific, without global repercussions.

PyEnv is, in essence, a Python version control system. It enables you to install multiple versions of Python locally, select a global default, and specify per-project versions. With PyEnv, your system’s sanctity remains intact, and your projects can live in their tailored environments. I picked 3.9.6, feel free to do the same or pick the version of your choice (as long as its recent enough)

### Installing PyEnv

PyEnv is a tool that allows you to easily install, manage, and switch between multiple versions of Python.

**Official Installer**  
The official installer is the simplest and most straightforward method to install PyEnv. It handles the cloning of the PyEnv repository and the modification of your shell startup files for you. To proceed with this method, use the following command in your terminal:

```c
curl https://pyenv.run | zsh
```

**Homebrew (macOS)**  
If you are on macOS and prefer using the Homebrew package manager (as I do), you can install PyEnv with Homebrew. Open your terminal and run:

```c
brew install pyenv
```

**Manual Git Clone**  
For those who want more control over the installation process, you can manually clone the PyEnv repository to a `.pyenv` directory in your home directory:

```c
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

**Validating the Install**

```c
pyenv - version
```

This command should return the version of PyEnv if the installation was successful.

**Install Python Versions**

Now you can install different versions of Python. For example, to install Python 3.9.6, you would run:

```c
pyenv install 3.9.6
```

**Switching Between Python Versions**

To set a local Python version for a particular project:

```c
pyenv local 3.9.6
```

And to set a global Python version for your entire system:

```c
pyenv global 3.9.6
```

**More Information**

For more detailed instructions, troubleshooting, and advanced usage, please refer to the [PyEnv installation guide](https://github.com/pyenv/pyenv#installation).

## Poetry: The Virtual Environment and Dependency Manager

Poetry represents a significant advancement in managing Python projects. It’s not just about installing packages but about creating a whole ecosystem for your project that’s isolated, reproducible, and intuitive (and more [FAIR](https://www.go-fair.org/fair-principles/)!).

**Understanding the Role of Poetry**

Whereas PyEnv is like the foundation, setting up the correct version of Python for your system, Poetry is like constructing a dedicated workspace on that foundation. Each project gets its own clean, self-contained environment, free from the dependencies and settings of other projects. Moving from `conda` to Poetry can seem daunting at first — it’s like leaving a familiar environment to embrace a new methodology. But tools like Poetry extend our *scientific* capabilities, providing structured and controlled spaces that emulate the rigor of an experiment.

**How Poetry Enhances Python Environments**

Poetry utilizes the Python version that PyEnv sets up, but it goes further by ensconcing it within a virtual environment. This creates a distinct separation between project environments, ensuring that the setup for one project does not interfere with another. Poetry employs a `pyproject.toml` file at the heart of each project. This file serves as the blueprint for your project’s configuration and dependencies, replacing the traditional `requirements.txt` file. It’s designed to be straightforward and user-friendly, embodying a less-is-more philosophy in project management.

### Setting Up a Python Project with Poetry

Poetry is not just a package manager; it’s a complete tool that manages project dependencies, virtual environments, and even package publishing. Below, we’ll walk through the process of setting up a new Python project with Poetry.

**Installing Poetry**

I recommend installing Poetry into the global PyEnv environment you just created (i.e., your new system Python). You can install Poetry in various ways, but the recommended method is with `curl`:

```c
curl -sSL https://install.python-poetry.org | python3 -
```

**Configuring Poetry**

Once installed, you can configure Poetry to your preferences. For example, if you’re using VSCode, it’s helpful to set Poetry to create the virtual environment within the project directory. To do this, run:

```c
poetry config virtualenvs.in-project true
```

**Starting a New Project**

Creating a new project with Poetry is simple. Navigate to your home directory and run the following command:

```c
poetry new sword
```

Poetry creates a directory named `sword` with the following structure:

```c
sword
├── pyproject.toml
├── README.md
├── tests
│   └── __init__.py
└── sword
    └── __init__.py
```

The `pyproject.toml` file is where your project's dependencies and metadata are declared, it looks like this:

```c
[tool.poetry]
name = "sword"
version = "0.1.0"
description = ""
authors = ["Jake Gearon <jake.gearon@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.9"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

**Adding Dependencies**

To add a new package to your project, use the `add` command. For example:

```c
poetry add duckdb geopandas numpy matplotlib seaborn
```

**Installing Dependencies**

After adding dependencies, or if you’ve cloned an existing project, install the dependencies with:

```c
poetry install
```

This command reads the `pyproject.toml` file and installs all the necessary packages. You can also install first and then add dependencies as needed.

**Running the Project**

To run your Python application within the virtual environment managed by Poetry, you can use the `run` command:

```c
poetry run python sword/__init__.py # just as an example, this wont do anything
```

**Command-Line Interface (CLI)**

Poetry’s command-line interface (CLI) is the gateway to its functionality. Here are some common commands you will need:

- **Creating a new project:** `poetry new my-project`
- **Adding a dependency:** `poetry add package-name`
- **Installing dependencies:** `poetry install`
- **Updating dependencies:** `poetry update`
- **Entering the Poetry shell:** `poetry shell`
- **Run a file:** `poetry run python my-file.py`

For those interested in integrating Poetry into their workflow, extensive documentation is available. It covers everything from getting started to mastering advanced features of Poetry.

\- Official documentation: [Poetry Docs](https://python-poetry.org/docs/)  
\- GitHub repository: [Poetry GitHub](https://github.com/python-poetry/poetry)

## DuckDB

[DuckDB](https://duckdb.org/) has seen a rise in popularity in data engineering corners of the internet.. I paid little attention to the Duck until I saw a [blog post from the team on their new spatial extension.](https://duckdb.org/2023/04/28/spatial.html) After this, I saw a few notable posts pop up on Twitter (I won’t call it X, sorry). Interested readers should visit these articles from [Mark Litwintschik](https://tech.marksblogg.com/duckdb-geospatial-gis.html) and [Chris Holmes](https://medium.com/radiant-earth-insights/duckdb-the-indispensable-geospatial-tool-you-didnt-know-you-were-missing-5fe11c5633e5) on geospatial DuckDB. More recently, Python-GIS guru Dr. Qiusheng Wu [posted several video tutorials on spatial data management using DuckDB](https://x.com/giswqs/status/1715472679107535042?s=20), which are always worth the watch. I won’t spend too much time covering the technicals of DuckDB as frankly its above my paygrade (I’m a sedimentary geologist, remember?). In short, though: DuckDB is an in-process SQL OLAP database management system. Simple, feature-rich, fast & open source. Unlike traditional databases that run as separate processes and communicate through sockets or shared memory, ***DuckDB runs inside the same process as the application that uses it*.** This eliminates the overhead of data serialization and network communication, and allows DuckDB to leverage the full power of modern hardware. DuckDB supports a rich set of SQL features, including window functions, common table expressions, recursive queries, and user-defined functions. DuckDB also integrates with popular data analysis tools like Pandas, R, and Apache Arrow, making it easy to use DuckDB as a backend for data science workflows. DuckDB is designed to handle analytical queries on large and complex data sets, and can achieve orders of magnitude speedup over other databases. For proof, see [this article](https://www.vantage.sh/blog/querying-aws-cost-data-duckdb), or [this article](https://www.fivetran.com/blog/how-fast-is-duckdb-really), [or even this article](https://www.dataduel.co/revisiting-data-query-speed-with-duckdb/) which all essentially say the same thing, DuckDB is *fast*, blowing Postgres and other solutions out of the water. DuckDB is also able to read and write data from various file formats, such as CSV, Parquet, and ORC, without requiring any data loading or preprocessing. DuckDB is open source and free to use for any purpose. You can download the DuckDB CLI from its official website, using HomeBrew, or the GitHub Repo. This installation is different from the the Python client, which we will install into our Poetry virtual environment shortly. I’m on macOS and use HomeBrew, so installing the DuckDB CLI is simple:

```c
brew install duckdb
```

## Putting It All Together

```c
cd CursorProjects #(or the folder where you keep projects)
poetry new sword-duckdb
cd sword-duckdb
poetry add duckdb geopandas numpy matplotlib seaborn
poetry install
```

This block initializes a new project, `sword-duckdb`, and installs dependencies defined in our `pyproject.toml`. The simplicity here is key: one command and we're ready to go, no environment wrestling required. With PyEnv and Poetry, our geospatial workflow isn’t just manageable — it’s robust, flexible, and ready for whatever computational challenges we throw at it.

## SWORD

SWORD, which stands for the SWOT River Database, is designed to support the Surface Water and Ocean Topography (SWOT) satellite mission launched in December 2022. The SWOT mission aims to enhance observations of river water surface elevation, width, and slope by providing river vector products for global rivers > 30m in width. SWORD is ~ 4GB uncompressed, making it unwieldy in conventional programs like ArcGIS or QGIS.

The SWORD database consolidates multiple global river and satellite-related datasets to define river nodes and reaches that will constitute the SWOT river vector data products. It offers high-resolution river nodes and reaches in shapefile, geopackage, and netCDF formats.

The SWORD Dataset provides attributes at approximately 200 m node and ~10 km reach spacings. Attributes within the SWORD dataset include geographical coordinates, node and reach IDs, lengths, water surface elevation, width, flow accumulation, the number of channels, and types of obstruction, among others. These attributes provide a comprehensive set of data points for analyzing riverine systems globally. We are going to use the geopackage version of SWORD v16. You may frown, noting that [geopackages and DuckDB dont always play well together](https://medium.com/radiant-earth-insights/performance-explorations-of-geoparquet-and-duckdb-84c0185ed399). You would be correct, though picking this format gives me an excuse to evangelize the GeoParquet format, something I can never turn down. We are going to concatenate and convert the geopackages to GeoParquet.

A Quick aside on GeoParquet:

- [Geoparquet is an optimized columnar storage file format for big data processing in cloud environments, designed for the efficient storage of geospatial data and to support a diverse range of queries and analytics.](https://www.rtei.ca/the-benefits-of-cloud-native-geospatial-file-formats/) By significantly compressing data, Geoparquet reduces both the file size and the network bandwidth necessary for data transfer, thereby enhancing the performance and scalability of systems like DuckDB.
- Geoparquet can also preserve the metadata and schema of geospatial data, such as the projection system, the spatial reference, and the geometry type. [This can simplify the data ingestion and integration process for DuckDB, which can read geoparquet files natively](https://getindata.com/blog/introducing-geoparquet-data-format/).
- Geoparquet can handle complex geospatial data types, such as polygons, multipolygons, and linestrings, which are commonly used to represent river features. [Shapefile, on the other hand, has limitations on the geometry size and complexity, and netCDF is mainly designed for gridded data](https://gisgeography.com/gis-formats/).

By the way. This is by no means to @ the SWOT data team, who are far beyond the median data provider who gives you a shapefile if youre lucky and csv if you make them. That being said, a GeoParquet version of SWORD would be great. If the team wants my version or the code to do it, feel free!

Acquiring the SWORD dataset is a straightforward process, we will use a zsh script to run `curl` on the Zenodo record link and a preprocessing python file: aptly named `preprocess.py`:

```c
#!/bin/zsh

# The URL from where to download the file
url="https://zenodo.org/records/10013982/files/SWORD_v16_gpkg.zip?download=1"

# The target directory where the file should be saved and unzipped
target_directory="{your-project-path}"

# The target file path for the zip file
target_file_path="${target_directory}/SWORD_v16_gpkg.zip"

# The directory that should be present after unzipping
unzip_dir="${target_directory}/gpkg"

# Create the target directory if it doesn't exist
mkdir -p "$target_directory"

# Check if the target file already exists
if [[ -f "$target_file_path" ]]; then
    echo "The file already exists. No need to download."
else
    # Use curl to download the file
    curl -L "$url" -o "$target_file_path"
fi

# Check if the 'gpkg' directory already exists
if [[ -d "$unzip_dir" ]]; then
    echo "The 'gpkg' directory already exists. No need to unzip."
else
    # Unzip the file to the target directory
    unzip -o "$target_file_path" -d "$unzip_dir"
fi

# Call Python script for DuckDB operations
poetry run python preprocess.py "$unzip_dir"
```

The `preprocess.py` file does several things, mainly it adds the continent identifier to each geopackage, concatenates them all together, then saves them to reach or node parquet files.

```c
import geopandas as gpd
import pandas as pd
from pathlib import Path
project_path = 'your_path_here'
# Set the directory where the .gpkg files are located
unzip_dir = Path(f'{project_path}/gpkg')

# Lists of geopackage files
nodes_gpkgs = [
    ('af', 'af_sword_nodes_v16.gpkg'),
    ('as', 'as_sword_nodes_v16.gpkg'),
    ('eu', 'eu_sword_nodes_v16.gpkg'),
    ('na', 'na_sword_nodes_v16.gpkg'),
    ('oc', 'oc_sword_nodes_v16.gpkg'),
    ('sa', 'sa_sword_nodes_v16.gpkg')
]

reaches_gpkgs = [
    ('af', 'af_sword_reaches_v16.gpkg'),
    ('as', 'as_sword_reaches_v16.gpkg'),
    ('eu', 'eu_sword_reaches_v16.gpkg'),
    ('na', 'na_sword_reaches_v16.gpkg'),
    ('oc', 'oc_sword_reaches_v16.gpkg'),
    ('sa', 'sa_sword_reaches_v16.gpkg')
]

# Function to read each gpkg file, add a continent prefix column, and concatenate into a single GeoDataFrame
def read_and_concatenate_gpkgs(gpkg_list, directory):
    frames = []
    for prefix, gpkg in gpkg_list:
        gdf = gpd.read_file(directory / gpkg)
        gdf['continent'] = prefix  # Add the continent prefix as a new column
        frames.append(gdf)
    return gpd.GeoDataFrame(pd.concat(frames, ignore_index=True))

# Read and combine nodes .gpkg files
nodes_combined = read_and_concatenate_gpkgs(nodes_gpkgs, unzip_dir)
nodes_combined.to_parquet(f"{project_path}/sword_nodes_v16.parquet")

# Read and combine reaches .gpkg files
reaches_combined = read_and_concatenate_gpkgs(reaches_gpkgs, unzip_dir)
reaches_combined.to_parquet(f"{project_path}/sword_reaches_v16.parquet")
```

Note, the above code takes a long time to run. I include it for full disclosure only. Generally, you should get your data into a parquet as fast as possible. We can now work with DuckDB at its best, when interfacing with parquet. I’ve only shown 5 rows here for visualization purposes, but in less than a second some 10,865,963 rows can be loaded directly from the nodes parquet file.

```c
poetry shell
duckdb
D SELECT * FROM sword_nodes_v16.parquet LIMIT 5;

┌────────────────────┬──────────────────────┬────────────────┬────────────────────┬─────────────┬───────────────────┬──────────────────────┬───┬────────────────────┬────────────────────┬───────┬─────────────┬───────────┬───────────┬──────────────────────┬───────────┐
│         x          │          y           │    node_id     │      node_len      │  reach_id   │        wse        │       wse_var        │ … │     meand_len      │     sinuosity      │ type  │ river_name  │ edit_flag │ trib_flag │       geometry       │ continent │
│       double       │        double        │     int64      │       double       │    int64    │      double       │        double        │   │       double       │       double       │ int64 │   varchar   │  varchar  │   int64   │         blob         │  varchar  │
├────────────────────┼──────────────────────┼────────────────┼────────────────────┼─────────────┼───────────────────┼──────────────────────┼───┼────────────────────┼────────────────────┼───────┼─────────────┼───────────┼───────────┼──────────────────────┼───────────┤
│  42.60729713853385 │ -0.24758837815942214 │ 11410000010023 │  208.7563952993389 │ 11410000013 │ 0.400000005960464 │                  0.0 │ … │ 2889.6346976127534 │ 1.0409676451210979 │     3 │ Jubba River │ NaN       │         1 │ \x01\x01\x00\x00\x…  │ af        │
│ 42.608446703843846 │  -0.2461621731504668 │ 11410000010033 │  192.6688661373019 │ 11410000013 │ 0.400000005960464 │  3.0814879110195774… │ … │ 2889.6346976127534 │ 1.0409676451210979 │     3 │ Jubba River │ NaN       │         1 │ \x01\x01\x00\x00\x…  │ af        │
│  42.60979372838854 │ -0.24517531536565743 │ 11410000010043 │ 185.22819040422962 │ 11410000013 │ 0.650000035762787 │  0.05000000596046481 │ … │ 2889.6346976127534 │ 1.0409676451210979 │     3 │ Jubba River │ NaN       │         1 │ \x01\x01\x00\x00\x…  │ af        │
│ 42.611275447713744 │  -0.2441360510718185 │ 11410000010053 │ 206.28167587021233 │ 11410000013 │ 0.900000035762787 │                  0.0 │ … │ 2889.6346976127534 │ 1.0409676451210979 │     3 │ Jubba River │ NaN       │         1 │ \x01\x01\x00\x00\x…  │ af        │
│ 42.612891778167786 │ -0.24352166059838518 │ 11410000010063 │  186.4050920759961 │ 11410000013 │ 0.900000035762787 │                  0.0 │ … │ 2889.6346976127534 │ 1.0409676451210979 │     3 │ Jubba River │ NaN       │         0 │ \x01\x01\x00\x00\x…  │ af        │
├────────────────────┴──────────────────────┴────────────────┴────────────────────┴─────────────┴───────────────────┴──────────────────────┴───┴────────────────────┴────────────────────┴───────┴─────────────┴───────────┴───────────┴──────────────────────┴───────────┤
│ 5 rows                                                                                                                                                                                                                                            27 columns (15 shown) │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

If you’re not used to using SQL, the simplicity of `SELECT * FROM sword_nodes_v16.parquet LIMIT 5;` may not be immediately apparent. Reading a geoparquet file into PostgreSQL is ***not trivial.*** You need a database on a running server, an ODBC driver, the correct configurations, and seemingly a dash of occult magic to make the connection happen. [Just read this if you don’t believe me.](https://hevodata.com/learn/parquet-to-postgresql/) And hey, I love PostgreSQL and PostGIS. They’ve served me indefatigably, but `SELECT * FROM sword_nodes_v16.parquet;` sold me on DuckDB nearly immediately. It just *feels natural.*

## Plotting…with SQL?

I want to mention one more toolkit that I stumbled across in my DuckDB wanderings: [JuPySQL](https://ploomber.io/blog/jupysql/). I love love *love* this project. It’s a new stack by [Ploomber](https://ploomber.io/) that extends the `%sql` magic capabilities of Jupyter Notebooks.

First we load the SQL extension and spin up a DuckDB database, we ensure the spatial extension is loaded so we can handle the geometry column from the SWORD nodes parquet file.

```c
%load_ext sql
%sql duckdb://
%sql INSTALL spatial;
%sql LOAD spatial;
```

Next, we define a block that prepares some simple data cleaning. In our case, we remove any slopes less than 0.001 m/km or greater than 1000 m/km (the vast majority of rivers fall in this range!). This execution is then saved (denoted by `--save slopeclean`) and delayed (`--no-execute`) until we send it to the plotting routine. We also only select nodes identified as rivers (type == 1).

```c
%%sql --save slopeclean --no-execute
SELECT slope FROM 'data/gpkg/sword_reaches_v16.parquet' WHERE slope > 0.001 AND slope < 1000 AND type == 1;
```

The next cell is where it all comes together and is what prompted me to include JuPySQL in this write up. We define a *matplotlib axis* (this is truly great interoperability) as the output of an SQL magic function `%sqlplot` to which we give CLI-style arguments. In order: `histogram` is the type of plot we want for describing a single continuous variable (note that JuPySQL currently does not support scatterplots, something I selfishly hope they are working on!). Our next argument is `--table` to which we supply the “table” or output created by the delayed execution cell, in our case: `slopeclean`. We then give the `column` we want to plot, which is `slope`. Finally we can supply a `bins` or `binwidth` parameter, extending the functionality of the plotting routine. After retrieving our matplotlib axis object, we can adjust the plots just as one would do in Python. As an example of DuckDB’s speed, this plotted in just 853 milliseconds!

```c
ax = %sqlplot histogram --table slopeclean --column slope --binwidth .1
ax.set_xlim(0, 30)
ax.set_xlabel('Slope (m/km)')
ax.set_title('')
```
![](https://miro.medium.com/v2/resize:fit:1194/format:webp/1*EiI5OmVG7yXSl_AI_LQ3BQ.png)

Distribution of River Slopes in SWORD. n = 10,865,963, rendered from Parquet on disk in 853 ms

JuPySQL seems to be in its early stages, but I’ll definitely be keeping an eye on the changelog to see how the project evolves.

So that’s it! These are some of the ways I’ve improved my own workflow. I highly recommend PyEnv and Poetry for any Python coder, DuckDB and JuPySQL are more specialized for the big-data inclined, but are worth getting to know as I think they will grow in popularity in the coming years.

If you enjoyed this, give me a follow on [Twitter](https://twitter.com/JakeGearon) or [GitHub](https://github.com/jameshgrn)!

[![Jake Gearon](https://miro.medium.com/v2/resize:fill:96:96/1*jSdK2DBQHsbvMJfyRqVJzg.jpeg)](https://medium.com/@jake.gearon_34983?source=post_page---post_author_info--7e7d355655f5---------------------------------------)

[![Jake Gearon](https://miro.medium.com/v2/resize:fill:128:128/1*jSdK2DBQHsbvMJfyRqVJzg.jpeg)](https://medium.com/@jake.gearon_34983?source=post_page---post_author_info--7e7d355655f5---------------------------------------)

[44 following](https://medium.com/@jake.gearon_34983/following?source=post_page---post_author_info--7e7d355655f5---------------------------------------)