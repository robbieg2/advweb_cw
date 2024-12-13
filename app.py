from flask import Flask, render_template, url_for
from team_stats import team_stats_data

app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    seasons = sorted(season_data.keys(), reverse=True)
    return render_template('home.html', seasons=seasons)

# Data for season overview pages
season_data = {
    "2023-24": {
        "teams": [
            {"name": "Celtic", "wins": 29, "draws": 6, "losses": 3, "points": 93, "goals_scored": 95, "goals_conceded": 30},
            {"name": "Rangers", "wins": 27, "draws": 4, "losses": 7, "points": 85, "goals_scored": 87, "goals_conceded": 32},
            {"name": "Hearts", "wins": 20, "draws": 8, "losses": 10, "points": 68, "goals_scored": 54, "goals_conceded": 42},
            {"name": "Kilmarnock", "wins": 14, "draws": 14, "losses": 10, "points": 56, "goals_scored": 46, "goals_conceded": 44},
            {"name": "St. Mirren", "wins": 13, "draws": 8, "losses": 17, "points": 47, "goals_scored": 46, "goals_conceded": 52},
            {"name": "Dundee FC", "wins": 10, "draws": 12, "losses": 16, "points": 42, "goals_scored": 49, "goals_conceded": 68},
            {"name": "Aberdeen", "wins": 12, "draws": 12, "losses": 14, "points": 48, "goals_scored": 48, "goals_conceded": 52},
            {"name": "Hibernian", "wins": 11, "draws": 13, "losses": 14, "points": 46, "goals_scored": 52, "goals_conceded": 59},
            {"name": "Motherwell", "wins": 10, "draws": 13, "losses": 15, "points": 43, "goals_scored": 56, "goals_conceded": 59},
            {"name": "St. Johnstone", "wins": 8, "draws": 11, "losses": 19, "points": 35, "goals_scored": 29, "goals_conceded": 54},
            {"name": "Ross County", "wins": 8, "draws": 11, "losses": 19, "points": 35, "goals_scored": 38, "goals_conceded": 67},
            {"name": "Livingston", "wins": 5, "draws": 10, "losses": 23, "points": 25, "goals_scored": 29, "goals_conceded": 70},
        ],
        "awards": {
            "champions": {"name":"Celtic", "photo_file": "celtic24.png"},
            "top_scorer": {"name": "Lawrence Shankland", "goals": 24, "photo_file": "lawrence_shankland.png"},
            "most_assists": {"name": "Matt O'Riley", "assists": 13, "photo_file": "matt_oriley.png"},
            "most_clean_sheets": {"name": "Jack Butland", "clean_sheets": 18, "photo_file": "jack_butland.png"},
            "player_of_the_year": {"name": "Lawrence Shankland", "photo_file": "lawrence_shankland_poty.png"},
        },
    },
    "2022-23": {
          "teams": [
            {"name": "Celtic", "wins": 32, "draws": 3, "losses": 3, "points": 99, "goals_scored": 114, "goals_conceded": 34},
            {"name": "Rangers", "wins": 29, "draws": 5, "losses": 4, "points": 92, "goals_scored": 93, "goals_conceded": 37},
            {"name": "Aberdeen", "wins": 18, "draws": 3, "losses": 17, "points": 57, "goals_scored": 56, "goals_conceded": 60},
            {"name": "Hearts", "wins": 15, "draws": 9, "losses": 14, "points": 54, "goals_scored": 63, "goals_conceded": 57},
            {"name": "Hibernian", "wins": 15, "draws": 7, "losses": 16, "points": 42, "goals_scored": 57, "goals_conceded": 59},
            {"name": "St. Mirren", "wins": 12, "draws": 10, "losses": 16, "points": 46, "goals_scored": 43, "goals_conceded": 61},
            {"name": "Motherwell", "wins": 14, "draws": 8, "losses": 16, "points": 50, "goals_scored": 53, "goals_conceded": 51},
            {"name": "Livingston", "wins": 13, "draws": 7, "losses": 18, "points": 46, "goals_scored": 36, "goals_conceded": 60},
            {"name": "St. Johnstone", "wins": 12, "draws": 7, "losses": 19, "points": 43, "goals_scored": 41, "goals_conceded": 59},
            {"name": "Kilmarnock", "wins": 11, "draws": 7, "losses": 20, "points": 40, "goals_scored": 37, "goals_conceded": 62},
            {"name": "Ross County", "wins": 9, "draws": 7, "losses": 22, "points": 34, "goals_scored": 37, "goals_conceded": 60},
            {"name": "Dundee United", "wins": 8, "draws": 7, "losses": 23, "points": 31, "goals_scored": 40, "goals_conceded": 70},
        ],
        "awards": {
            "champions": {"name": "Celtic", "photo_file": "celtic23.png"},
            "top_scorer": {"name": "Kyogo Furuhashi", "goals": 27, "photo_file": "kyogo_goals.png"},
            "most_assists": {"name": "Matt O'Riley", "assists": 12, "photo_file": "matt_oriley22.png"},
            "most_clean_sheets": {"name": "Joe Hart", "clean_sheets": 16, "photo_file": "joe_hart.png"},
            "player_of_the_year": {"name": "Kyogo Furuhashi", "photo_file": "kyogo.png"},
        },
    },
    "2021-22": {
          "teams": [
            {"name": "Celtic", "wins": 29, "draws": 6, "losses": 3, "points": 93, "goals_scored": 92, "goals_conceded": 22},
            {"name": "Rangers", "wins": 27, "draws": 8, "losses": 3, "points": 89, "goals_scored": 80, "goals_conceded": 31},
            {"name": "Hearts", "wins": 17, "draws": 10, "losses": 11, "points": 61, "goals_scored": 54, "goals_conceded": 44},
            {"name": "Dundee United", "wins": 12, "draws": 12, "losses": 14, "points": 48, "goals_scored": 37, "goals_conceded": 44},
            {"name": "Motherwell", "wins": 12, "draws": 10, "losses": 16, "points": 46, "goals_scored": 42, "goals_conceded": 61},
            {"name": "Ross County", "wins": 10, "draws": 11, "losses": 17, "points": 41, "goals_scored": 47, "goals_conceded": 61},
            {"name": "Livingston", "wins": 13, "draws": 10, "losses": 15, "points": 49, "goals_scored": 41, "goals_conceded": 46},
            {"name": "Hibernian", "wins": 11, "draws": 12, "losses": 15, "points": 45, "goals_scored": 38, "goals_conceded": 42},
            {"name": "St. Mirren", "wins": 10, "draws": 14, "losses": 14, "points": 44, "goals_scored": 33, "goals_conceded": 51},
            {"name": "Aberdeen", "wins": 10, "draws": 11, "losses": 17, "points": 41, "goals_scored": 41, "goals_conceded": 46},
            {"name": "St. Johnstone", "wins": 8, "draws": 11, "losses": 19, "points": 35, "goals_scored": 24, "goals_conceded": 51},
            {"name": "Dundee FC", "wins": 6, "draws": 11, "losses": 21, "points": 29, "goals_scored": 34, "goals_conceded": 64},
        ],
        "awards": {
            "champions": {"name": "Celtic", "photo_file": "celtic22.png"},
            "top_scorer": {"name": "Charles-Cook, Giakoumakis", "goals": 13, "photo_file": "cook_giak.png"},
            "most_assists": {"name": "James Tavernier", "assists": 13, "photo_file": "tavernier.png"},
            "most_clean_sheets": {"name": "Joe Hart", "clean_sheets": 19, "photo_file": "joe_hart21.png"},
            "player_of_the_year": {"name": "Craig Gordon", "photo_file": "gordon.png"},
        },
    },
}

# Dynamic route for season overview pages
@app.route('/season/<string:year>')
def season_overview(year):
    season = season_data.get(year)
    if not season:
        return f"season {year} data not found", 404
        
    season_years = sorted(season_data.keys(), reverse=True)
    current_index = season_years.index(year)
    prev_season = season_years[current_index + 1] if current_index + 1 < len(season_years) else None # Function for buttons to switch seasons
    next_season = season_years[current_index - 1] if current_index - 1 >= 0 else None

    return render_template('season_overview.html', year=year, teams=season["teams"], awards=season["awards"], prev_season=prev_season, next_season=next_season)

# Dynamic route for team stats pages
@app.route('/team/<string:team_name>/<string:season>')
def team_stats(team_name, season):
    team_data = team_stats_data.get(team_name, {}).get(season)
    if not team_data:
            return f"Data not found for {team_name} in {season}", 404
            
    season_parts = season.split('-')
    prev_season = f"{int(season_parts[0]) - 1}-{int(season_parts[1]) - 1}" # Function for buttons to switch seasons
    next_season = f"{int(season_parts[0]) + 1}-{int(season_parts[1]) + 1}"

    prev_exists = prev_season in team_stats_data.get(team_name, {})
    next_exists = next_season in team_stats_data.get(team_name, {})
            
    return render_template('team_stats.html', team_name=team_name, season=season, players=team_data["players"], summary=team_data["summary"], team_badge=team_data["badge"], prev_season=prev_season if prev_exists else None, next_season=next_season if next_exists else None, team_stats_data=team_stats_data)

if __name__ == "__main__":
    app.run(debug=True)
