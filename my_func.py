import pandas as pd
import ast
import folium

icon_colors = {
    'Vente à la ferme': ['green', 'fa-cheese'],
    'Epicerie sociale et solidaire': ['blue', 'fa-carrot'],
    'Producteur du marché': ['red', 'fa-apple-whole'],
    'AMAP': ['purple', 'fa-egg'],
    'Magasin de producteurs': ['orange', 'fa-seedling'],
    'Revendeur du marché': ['pink', 'fa-apple-whole']
}

day_mapping = {
	"Lu": "lundi",
	"Ma": "mardi",
	"Me": "mercedi",
	"Je": "jeudi",
	"Ve": "vendredi",
	"Sa": "samedi",
	"Di": "dimanche"
}

def random_func(row, featuregroups):
	# for group_key, feature_group in featuregroups.items():
	marker = folium.Marker(
		location=[row['lat'], row['lon']],
		popup=get_popup_text(row),
		icon=folium.Icon(
			icon=icon_colors[row['type']][1],
			color=icon_colors[row['type']][0],
			prefix='fa')
		)
	marker.add_to(featuregroups['type'][row['type']])
	# marker.add_to(featuregroups['commune'][row['commune']])


def get_popup_text(row):
	if pd.isna(row['joursouverture']):
		pop_up = f"{row['nom']}"
	else:
		dict  = ast.literal_eval(row['joursouverture'])
		full_days = [day_mapping[abbrev] for abbrev in dict]
		opening_days = ', '.join(full_days)
		pop_up = f"""<strong>{row['nom']}</strong><br>
		<u>Jour d'ouverture</u>: {opening_days}
		"""
	return pop_up




