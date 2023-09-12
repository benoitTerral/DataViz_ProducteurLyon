import pandas as pd
import ast


day_mapping = {
	"Lu": "lundi",
	"Ma": "mardi",
	"Me": "mercedi",
	"Je": "jeudi",
	"Ve": "vendredi",
	"Sa": "samedi",
	"Di": "dimanche"
}

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