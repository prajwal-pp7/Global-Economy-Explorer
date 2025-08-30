import streamlit as st
import pandas as pd
import math
from pathlib import Path

st.set_page_config(
    page_title='Global Economy Explorer',
    page_icon=':chart_with_upwards_trend:',
    layout='wide'
)

@st.cache_data
def load_economic_data():
    """
    Loads GDP data from a CSV file and transforms it into a clean DataFrame.

    The function reads the raw CSV, which has years as columns, and pivots
    it to a long format with 'Year' and 'GDP' as columns for easier plotting.
    """
    
    data_file_path=Path(__file__).parent/'gdp_data.csv'
    raw_df=pd.read_csv(data_file_path)
    
    MIN_YEAR=1960
    MAX_YEAR=2022

    processed_df=raw_df.melt(
        id_vars=['Country Code'],
        value_vars=[str(y) for y in range(MIN_YEAR,MAX_YEAR+1)],
        var_name='Year',
        value_name='GDP'
    )
    processed_df['Year']=pd.to_numeric(processed_df['Year'])
    return processed_df

gdp_data=load_economic_data()

st.title("Global Economy Explorer")
st.markdown("A tool to visualize and compare Gross Domestic Product (GDP) data from around the world.")
st.markdown("---")

col1,col2=st.columns(2)

with col1:
    min_year_val=gdp_data['Year'].min()
    max_year_val=gdp_data['Year'].max()
    start_year, end_year=st.slider(
        'Select a range of years for the analysis',
        min_value=min_year_val,
        max_value=max_year_val,
        value=(min_year_val,max_year_val)
    )
with col2:
    available_countries=gdp_data['Country Code'].unique()
    selected_countries=st.multiselect(
        'Choose countries to view',
        available_countries,
        default=['USA','JPN','CHN','IND']
    )

if not selected_countries:
    st.warning("Please select at least one country to display data.")
    st.stop()

filtered_gdp_data=gdp_data[
    gdp_data['Country Code'].isin(selected_countries) &
    (gdp_data['Year']>=start_year) &
    (gdp_data['Year']<=end_year)
]

st.header("GDP Over Time",divider='blue')

st.line_chart(
    filtered_gdp_data,
    x='Year',
    y='GDP',
    color='Country Code'
)

st.header(f"GDP Metrics for {end_year}",divider='blue')

num_cols=min(len(selected_countries),4)
cols = st.columns(num_cols)

for i,country_code in enumerate(selected_countries):
    country_start_gdp_df=gdp_data[
        (gdp_data['Country Code']==country_code) &
        (gdp_data['Year']==start_year)
    ]
    country_end_gdp_df=gdp_data[
        (gdp_data['Country Code']==country_code) &
        (gdp_data['Year']==end_year)
    ]
    
    if country_start_gdp_df.empty or country_end_gdp_df.empty:
        continue

    start_gdp=country_start_gdp_df['GDP'].iloc[0]/1e9
    end_gdp=country_end_gdp_df['GDP'].iloc[0]/1e9
    
    if math.isnan(start_gdp) or start_gdp==0:
        growth_delta='N/A'
        delta_color='off'
    else:
        growth_rate=(end_gdp/start_gdp)-1
        growth_delta=f'{growth_rate * 100:.2f}%'
        delta_color='normal' if growth_rate > 0 else 'inverse'

    with cols[i%num_cols]:
        st.metric(
            label=f"{country_code} GDP ({end_year})",
            value=f"${end_gdp:,.2f}B",
            delta=growth_delta,
            delta_color=delta_color
        )

st.header("Country Comparison",divider='blue')

compare_col1,compare_col2=st.columns(2)

with compare_col1:
    country1=st.selectbox("Select first country for comparison",selected_countries)
with compare_col2:
    country2=st.selectbox("Select second country for comparison",selected_countries)

if country1 and country2 and country1!=country2:
    comparison_data=gdp_data[gdp_data['Country Code'].isin([country1,country2])].copy()
    comparison_chart=st.line_chart(
        comparison_data,
        x='Year',
        y='GDP',
        color='Country Code'
    )

    st.markdown(f"The chart above shows the GDP trend for **{country1}** and **{country2}** from {min_year_val} to {max_year_val}.")

st.markdown("---")

col_left,col_right=st.columns([0.7, 0.3])
with col_right:
    st.markdown(
        """
        <div style="text-align: right;">
            <a href="mailto:210401@iitk.ac.in" target="_blank" style="text-decoration: none;">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="#FFFFFF" style="vertical-align: middle; margin-right: 5px;">
                    <path d="M0 0h24v24H0V0z" fill="none"/>
                    <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
                </svg>
            </a>
            <a href="https://github.com/prajwal-pp7/Global-Economy-Explorer/tree/main/Global-Economy-Explorer" target="_blank" style="text-decoration: none;">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="#FFFFFF" style="vertical-align: middle;">
                    <path d="M0 0h24v24H0V0z" fill="none"/>
                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.6.111.82-.259.82-.578 0-.284-.01-1.03-.016-2.02-3.336.724-4.042-1.61-4.042-1.61-.545-1.386-1.328-1.755-1.328-1.755-1.087-.744.083-.729.083-.729 1.205.084 1.838 1.235 1.838 1.235 1.07 1.835 2.809 1.305 3.492.997.108-.775.418-1.305.762-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.468-2.381 1.236-3.221-.124-.3-.536-1.523.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.046.138 3.003.404 2.292-1.552 3.297-1.23 3.297-1.23.653 1.653.241 2.876.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.922.43.371.812 1.103.812 2.222 0 1.605-.015 2.899-.015 3.28 0 .321.217.695.825.578C20.565 21.802 24 17.302 24 12c0-6.627-5.373-12-12-12z"/>
                </svg>
            </a>
            <p style="font-weight: bold; margin-top: 5px;">IIT Kanpur</p>
        </div>
        """,
        unsafe_allow_html=True
    )