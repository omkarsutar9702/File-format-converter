import streamlit as st
import pandas as pd
import os
st.set_page_config(layout="wide")

def convert_csv_to_xlsx(csv_file):
    try:
        # Read CSV file
        df = pd.read_csv(csv_file)

        # Get the base name of the input file
        base_name = os.path.splitext(os.path.basename(csv_file.name))[0]

        # Save as XLSX with the same base name
        output_path = f'{base_name}.xlsx'
        df.to_excel(output_path, index=False)
        return f"File converted and saved as {output_path}"
    except Exception as e:
        return f"Error: {str(e)}"

def convert_xls_to_xlsx(xls_file):
    try:
        # Read XLS file
        df = pd.read_excel(xls_file, engine='xlrd')

        # Get the base name of the input file
        base_name = os.path.splitext(os.path.basename(xls_file.name))[0]

        # Save as XLSX with the same base name
        output_path = f'{base_name}.xlsx'
        df.to_excel(output_path, index=False)
        return f"File converted and saved as {output_path}"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    
    st.markdown("<h1 style='text-align: center; color: skyblue; font-family:Monospace;'>File Converter</h1>", unsafe_allow_html=True)
    
    st.write("---")
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h3 style='text-align: center; color: #fa163c;font-family:Monospace;'>Convert CSV to XLSX</h3>", unsafe_allow_html=True)
        csv_file = st.file_uploader("Upload a CSV file", type=["csv"])

        if csv_file is not None:
            if st.button("Convert CSV", key="convert_csv"):
                result_csv = convert_csv_to_xlsx(csv_file)
                st.success(result_csv)

    with col2:
        st.markdown("<h3 style='text-align: center; color: #fa163c;font-family:Monospace;'>Convert XLS to XLSX</h3>", unsafe_allow_html=True)
        xls_file = st.file_uploader("Upload an XLS file", type=["xls"])

        if xls_file is not None:
            if st.button("Convert XLS", key="convert_xls"):
                result_xls = convert_xls_to_xlsx(xls_file)
                st.success(result_xls)

if __name__ == '__main__':
    main()
