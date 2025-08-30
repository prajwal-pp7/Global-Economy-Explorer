#  [Global Economy Explorer](https://global-economy-explorer.streamlit.app/)

**Global Economy Explorer** is an interactive web application built with
**Streamlit** that allows users to visualize and compare **Gross
Domestic Product (GDP)** data from countries around the world. This
dashboard provides both historical trends and end-of-year GDP summaries
for effective analysis and comparison.

------------------------------------------------------------------------

##  Features

-   **Interactive Data Visualization**\
    Visualize GDP trends over time using an intuitive line chart.

-   **Country Comparison**\
    Select multiple countries to compare their GDP data side-by-side.

-   **GDP Metrics Summary**\
    View key GDP metrics for a selected year.

-   **User-Friendly Interface**\
    Easily navigate with sliders and multi-select options in a
    responsive layout.

------------------------------------------------------------------------

##  Required Files

Ensure the following files are located in the same directory:

-   `GDP.py` -- Main Streamlit application script
-   `gdp_data.csv` -- Dataset containing GDP information
-   `lib.txt` -- List of required Python libraries

------------------------------------------------------------------------

##  Getting Started

Follow these instructions to set up and run the project on your local
machine.

### Step 1: Set Up the Python Environment

1.  Open **Command Prompt** (Windows) or **Terminal** (macOS/Linux).

2.  Navigate to your project folder. Example:

    ``` bash
    cd C:\Users\YourUser\Documents\GlobalEconomyExplorer
    ```

3.  Create a virtual environment by running:

    ``` bash
    python -m venv venv
    ```

4.  Activate the environment:

    -   **On Windows:**

        ``` bash
        venv\Scripts\activate
        ```

    -   **On macOS/Linux:**

        ``` bash
        source venv/bin/activate
        ```

        You will know it's active when you see `(venv)` at the beginning
        of your command prompt line.

------------------------------------------------------------------------

### Step 2: Install Required Libraries

1.  Make sure your virtual environment is still active.

2.  Install all the necessary libraries at once by running the following
    command.\
    It reads the `lib.txt` file and installs everything
    automatically.

    ``` bash
    pip install -r lib.txt
    ```

------------------------------------------------------------------------

### Step 3: Run the Application

1.  Ensure you are still in your project folder in the command prompt
    and the virtual environment is active.

2.  Launch the Streamlit application with this command:

    ``` bash
    streamlit run GDP.py
    ```

3.  A new tab will automatically open in your web browser with the
    running application.
