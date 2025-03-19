from bs4 import BeautifulSoup

#python file 2

def extract_marathon_data(file_path):
    # Parse the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    # Define lists to hold data
    bib_numbers, names, ages, genders, cities, states, countries, times_5k, times_10k, times_15k, times_20k, times_half, \
    times_25k, times_30k, times_35k, times_40k, paces, official_times, overall_places, gender_places, division_places = ([] for _ in range(21))

    # Locate table rows in main results table
    for row in soup.select('table.tablegrid_table tbody tr'):
        cells = row.find_all('td')
        if len(cells) >= 8:
            # Extract basic information
            bib_numbers.append(cells[0].text.strip())
            names.append(cells[1].text.strip())
            ages.append(cells[2].text.strip())
            genders.append(cells[3].text.strip())
            cities.append(cells[4].text.strip())
            states.append(cells[5].text.strip())
            countries.append(cells[6].text.strip())
        elif row.select_one('table.table_infogrid'):
            # Extract split times and final performance data
            split_cells = row.select('table.table_infogrid tr')
            if len(split_cells) >= 3:
                # Split times row
                time_cells = split_cells[1].find_all('td')
                times_5k.append(time_cells[0].text.strip() if len(time_cells) > 0 else None)
                times_10k.append(time_cells[1].text.strip() if len(time_cells) > 1 else None)
                times_15k.append(time_cells[2].text.strip() if len(time_cells) > 2 else None)
                times_20k.append(time_cells[3].text.strip() if len(time_cells) > 3 else None)
                times_half.append(time_cells[4].text.strip() if len(time_cells) > 4 else None)
                times_25k.append(time_cells[5].text.strip() if len(time_cells) > 5 else None)
                times_30k.append(time_cells[6].text.strip() if len(time_cells) > 6 else None)
                times_35k.append(time_cells[7].text.strip() if len(time_cells) > 7 else None)
                times_40k.append(time_cells[8].text.strip() if len(time_cells) > 8 else None)
                
                # Finish data row
                finish_cells = split_cells[3].find_all('td')
                paces.append(finish_cells[0].text.strip() if len(finish_cells) > 0 else None)
                official_times.append(finish_cells[2].text.strip() if len(finish_cells) > 2 else None)
                overall_places.append(finish_cells[3].text.strip() if len(finish_cells) > 3 else None)
                gender_places.append(finish_cells[4].text.strip() if len(finish_cells) > 4 else None)
                division_places.append(finish_cells[5].text.strip() if len(finish_cells) > 5 else None)
    
    # Ensure all lists are of equal length by filling shorter lists with None
    max_length = max(len(bib_numbers), len(times_5k))
    for lst in [bib_numbers, names, ages, genders, cities, states, countries, times_5k, times_10k, times_15k, times_20k,
                times_half, times_25k, times_30k, times_35k, times_40k, paces, official_times, overall_places, gender_places, division_places]:
        lst.extend([None] * (max_length - len(lst)))

    # Create a DataFrame for the extracted data
    return pd.DataFrame({
        "Bib": bib_numbers,
        "Name": names,
        "Age": ages,
        "Gender": genders,
        "City": cities,
        "State": states,
        "Country": countries,
        "5K": times_5k,
        "10K": times_10k,
        "15K": times_15k,
        "20K": times_20k,
        "Half": times_half,
        "25K": times_25k,
        "30K": times_30k,
        "35K": times_35k,
        "40K": times_40k,
        "Pace": paces,
        "Official Time": official_times,
        "Overall Place": overall_places,
        "Gender Place": gender_places,
        "Division Place": division_places
    })

# Example usage of the code
# file_path = 'path_to_html_file.html'
# df = extract_marathon_data(file_path)
# df.to_csv('output.csv', index=False)
