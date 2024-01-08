from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="carbonfootprint"
)

cursor = conn.cursor()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    emission_factors = {
        'Coal': {'median': 820},
        'Gas': {'median': 490},
        'Oil': {'median': 740},
        'Hydro': {'median': 24},
        'Renewable': {'median': 41},
        'Nuclear': {'median': 12}
    }

    # Your existing code for rendering data
    cursor.execute('SELECT * FROM country ORDER BY Coal DESC LIMIT 10')
    coal_data = cursor.fetchall()
    cursor.execute('SELECT * FROM country ORDER BY Oil DESC LIMIT 10')
    oil_data = cursor.fetchall()
    cursor.execute('SELECT * FROM country ORDER BY Hydro DESC LIMIT 10')
    hydro_data = cursor.fetchall()
    cursor.execute('SELECT * FROM country ORDER BY Gas DESC LIMIT 10')
    gas_data = cursor.fetchall()
    cursor.execute('SELECT * FROM country ORDER BY Renewable DESC LIMIT 10')
    renewable_data = cursor.fetchall()
    cursor.execute('SELECT * FROM country ORDER BY Nuclear DESC LIMIT 10')
    nuclear_data = cursor.fetchall()
    cursor.execute('SELECT * FROM country LIMIT 10')
    country_sample = cursor.fetchall()
    cursor.execute('SELECT * FROM world LIMIT 10')
    world_sample = cursor.fetchall()
    cursor.execute('SELECT * FROM country')
    country_data = cursor.fetchall()
    cursor.execute('SELECT * FROM world')
    world_data = cursor.fetchall()

    percentage_contributions_country = []
    for data in country_sample:
        country_pollution = []
        for source, usage_percentage in zip(['Coal', 'Gas', 'Hydro', 'Renewable', 'Nuclear'], data[2:]):
            median_emission = emission_factors[source]['median']
            pollution = (usage_percentage / 100) * median_emission
            country_pollution.append({
                'source': source,
                'usage_percentage': usage_percentage,
                'median_emission': median_emission,
                'pollution': round(pollution, 2)
            })
        percentage_contributions_country.append({
            'country': data[1],
            'pollution_data': country_pollution
        })

    percentage_contributions_world = []
    for data in world_sample:
        world_pollution = []
        for source, usage_percentage in zip(['Coal', 'Gas', 'Hydro', 'Renewable', 'Nuclear'], data[2:]):
            median_emission = emission_factors[source]['median']
            pollution = (usage_percentage / 100) * median_emission
            world_pollution.append({
                'source': source,
                'usage_percentage': usage_percentage,
                'median_emission': median_emission,
                'pollution': round(pollution, 2)
            })
        percentage_contributions_world.append({
            'world': data[1],
            'pollution_data': world_pollution
        })

    return render_template('index.html', coal_data=coal_data, oil_data=oil_data, hydro_data=hydro_data,
                           gas_data=gas_data, renewable_data=renewable_data, nuclear_data=nuclear_data,
                           world_sample=world_sample, country_sample=country_sample, country_data=country_data,
                           world_data=world_data, percentage_contributions_country=percentage_contributions_country,
                           percentage_contributions_world=percentage_contributions_world)

@app.route('/selected_country_pollution', methods=['GET', 'POST'])
def selected_country_pollution():
    if request.method == 'POST':
        selected_country = request.form['selected_country']

        # Fetch data for the selected country
        query = f"SELECT * FROM country WHERE Country = '{selected_country}' LIMIT 1"
        cursor.execute(query)
        selected_country_data = cursor.fetchone()

        # Perform pollution calculation for the selected country
        emission_factors = {
            'Coal': {'median': 820},
            'Gas': {'median': 490},
            'Oil': {'median': 740},
            'Hydro': {'median': 24},
            'Renewable': {'median': 41},
            'Nuclear': {'median': 12}
        }

        selected_country_pollution = []
        total_emissions = sum((usage_percentage / 100) * emission_factors[source]['median'] for source, usage_percentage in zip(['Coal', 'Gas', 'Hydro', 'Renewable', 'Nuclear'], selected_country_data[2:]))
        for source, usage_percentage in zip(['Coal', 'Gas', 'Hydro', 'Renewable', 'Nuclear'], selected_country_data[2:]):
            median_emission = emission_factors[source]['median']
            pollution = (usage_percentage / 100) * median_emission
            percentage_of_total_emissions = (pollution / total_emissions) * 100
            selected_country_pollution.append({
                'source': source,
                'usage_percentage': usage_percentage,
                'median_emission': median_emission,
                'pollution': round(pollution, 2),
                'percentage_of_total_emissions': round(percentage_of_total_emissions, 2),
                'total_emissions': round(total_emissions, 2)
            })

        return render_template('selected_country_pollution.html', selected_country=selected_country, selected_country_pollution=selected_country_pollution)

    # Render the initial page for GET requests
    return render_template('selected_country_pollution.html', selected_country=None, selected_country_pollution=None)

@app.route('/calculate_emissions', methods=['POST'])
def calculate_emissions():
    if request.method == 'POST':
        total_emissions_per_kwh = float(request.form['total_emissions_per_kwh'])
        power_consumption = float(request.form['power_consumption'])
        
        # Total emissions calculation
        total_emissions = total_emissions_per_kwh * power_consumption * 24 * 365 / 1000
        total_emissions = round(total_emissions, 2)

        return render_template('calculated_emissions.html', total_emissions=total_emissions)


@app.route('/selected_region_pollution', methods=['GET', 'POST'])
def selected_region_pollution():
    if request.method == 'POST':
        selected_region = request.form['selected_region']

        # Fetch data for the selected region
        query_world = f"SELECT * FROM world WHERE Region = '{selected_region}' LIMIT 1"
        cursor.execute(query_world)
        selected_region_data = cursor.fetchone()

        # Perform pollution calculation for the selected region
        emission_factors = {
            'Coal': {'median': 820},
            'Gas': {'median': 490},
            'Oil': {'median': 740},
            'Hydro': {'median': 24},
            'Renewable': {'median': 41},
            'Nuclear': {'median': 12}
        }

        selected_region_pollution = []
        total_emissions_world = sum((usage_percentage / 100) * emission_factors[source]['median'] for source, usage_percentage in zip(['Coal', 'Gas', 'Hydro', 'Renewable', 'Nuclear'], selected_region_data[2:]))
        for source, usage_percentage in zip(['Coal', 'Gas', 'Hydro', 'Renewable', 'Nuclear'], selected_region_data[2:]):
            median_emission = emission_factors[source]['median']
            pollution = (usage_percentage / 100) * median_emission
            percentage_of_total_emissions_world = (pollution / total_emissions_world) * 100
            selected_region_pollution.append({
                'source': source,
                'usage_percentage': usage_percentage,
                'median_emission': median_emission,
                'pollution': round(pollution, 3),
                'percentage_of_total_emissions_world': round(percentage_of_total_emissions_world, 2),
                'total_emissions_world': round(total_emissions_world, 2)
            })

        return render_template('selected_region_pollution.html', selected_region=selected_region, selected_region_pollution=selected_region_pollution)

    # Render the initial page for GET requests
    return render_template('selected_region_pollution.html', selected_region=None, selected_region_pollution=None)

@app.route('/calculate_emissions_region', methods=['POST'])
def calculate_emissions_region():
    if request.method == 'POST':
        total_emissions_per_kwh = float(request.form['total_emissions_per_kwh'])
        power_consumption = float(request.form['power_consumption'])

        # Total emissions calculation
        total_emissions = total_emissions_per_kwh * power_consumption * 24 * 365 / 1000
        total_emissions = round(total_emissions, 2)

        return render_template('calculated_emissions_world.html', total_emissions_world=total_emissions)

if __name__ == '__main__':
    app.run(debug=True)