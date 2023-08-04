# OSM Data Analysis Project

<a name="readme-top"></a>
## About The Project



This project is an attempt to analyze data that personally collected by me from the game Online Soccer Manager across 4 different league (Indonesia, Spain, England 2nd Division, Germany)

This project aim to get useful information from the collected data so that we can apply the information in form of tactic in the future matches.
<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Analysis

Analysis of the data are derive from this diagram

![Analysis diagram](https://raw.githubusercontent.com/graceyudhaaa/osm-data-analysis/master/image/OSM_IO_diagram.excalidraw.png)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Data
The collected raw data are available in the `data/raw/OSM Data.xlsx` file, while the processed data are available in `data/preprocessed` folder.

the raw data column description are
<details>
<summary>RAW Data</summary>
<p>RAW Data is the data that originally recorded from match result</p>
<table>
	<tr>
		<th>Column</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>Home</td>
		<td>Name of the home team</td>
	</tr>
	<tr>
		<td>Away</td>
		<td>Name of the away team</td>
	</tr>
	<tr>
		<td>Stronger Team</td>
		<td>The Stronger team between the home team and away team</td>
	</tr>
	<tr>
		<td>Your Team</td>
		<td>The team that were managed by me</td>
	</tr>
	<tr>
		<td>Home Formation</td>
		<td>Formation used by the home team</td>
	</tr>
	<tr>
		<td>Away Formation</td>
		<td>Formation used by the away team</td>
	</tr>
	<tr>
		<td>Home Style of play</td>
		<td>Home team style of play</td>
	</tr>
	<tr>
		<td>Home Marking</td>
		<td>Home team marking style</td>
	</tr>
	<tr>
		<td>Home Offside trap</td>
		<td>Home team offside trap setting</td>
	</tr>
	<tr>
		<td>Home Tackling</td>
		<td>Home team tackling setting</td>
	</tr>
	<tr>
		<td>Away Style of play</td>
		<td>Away team style of play</td>
	</tr>
	<tr>
		<td>Away Marking</td>
		<td>Away team marking style</td>
	</tr>
	<tr>
		<td>Away Offside trap</td>
		<td>Away team offside trap setting</td>
	</tr>
	<tr>
		<td>Away Tackling</td>
		<td>Home team tackling setting</td>
	</tr>
	<tr>
		<td>Home Training Camp</td>
		<td>Whether the home team use training camp (or secret camp) or not</td>
	</tr>
	<tr>
		<td>Away Training Camp</td>
		<td>Whether the away team use training camp (or secret camp) or not</td>
	</tr>
	<tr>
		<td>Line Tactic-FW</td>
		<td>Forward line tactic</td>
	</tr>
	<tr>
		<td>Line Tactic-MF</td>
		<td>Midfield line tactic</td>
	</tr>
	<tr>
		<td>Line Tactic-DF</td>
		<td>Defense line tactic</td>
	</tr>
	<tr>
		<td>Pressing</td>
		<td>Pressing slider setting</td>
	</tr>
	<tr>
		<td>Style</td>
		<td>Style slider setting</td>
	</tr>
	<tr>
		<td>Tempo</td>
		<td>Tempo slider setting</td>
	</tr>
	<tr>
		<td>Home Posession</td>
		<td>Posession achieved by home team (%). This data were obtained after the game</td>
	</tr>
	<tr>
		<td>Away Possesion</td>
		<td>Posession achieved by away team (%). This data were obtained after the game</td>
	</tr>
	<tr>
		<td>Home Goals</td>
		<td>Goal scored by the home team. This data were obtained after the game</td>
	</tr>
	<tr>
		<td>Away Goals</td>
		<td>Goal scored by the away team. This data were obtained after the game</td>
	</tr>
	<tr>
		<td>Home Shots</td>
		<td>Home team shot attempt. This data were obtained after the game</td>
	</tr>
	<tr>
		<td>Away Shots</td>
		<td>Away team shot attempt. This data were obtained after the game</td>
	</tr>
	<tr>
		<td>TIP</td>
		<td>TIP/Tricks given by the game after the match. The TIP recorded were only the tip that arent subjective to a certain player</td>
	</tr>
	<tr>
		<td>Result</td>
		<td>Result of the game based on which home team or away team won the game</td>
	</tr>
	<tr>
		<td>Your Result</td>
		<td>Result of the game based on wheter you won the game or not</td>
	</tr>
</table>
</details>
<details>
<summary>Processed Data</summary>
<p>Processed Data are the original RAW data that are processed to remove the home and away references</p>
<table>
	<tr>
		<th>Column</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>strength</td>
		<td>your team strength relative to the opponent strength</td>
	</tr>
	<tr>
		<td>opponent_formation</td>
		<td>formation used by the opponent</td>
	</tr>
	<tr>
		<td>opponent_style_of_play</td>
		<td>opponent's style of play</td>
	</tr>
	<tr>
		<td>opponent_marking</td>
		<td>opponent's marking setting</td>
	</tr>
	<tr>
		<td>opponent_offside_trap</td>
		<td>opponent's offside trap setting</td>
	</tr>
	<tr>
		<td>opponent_tackling</td>
		<td>opponent's tackling setting</td>
	</tr>
	<tr>
		<td>opponent_training_camp</td>
		<td>whether or not opponent use training camp (or secret camp)</td>
	</tr>
	<tr>
		<td>formation</td>
		<td>formation use by your team</td>
	</tr>
	<tr>
		<td>style_of_play</td>
		<td>team style of play</td>
	</tr>
	<tr>
		<td>marking</td>
		<td>team marking setting</td>
	</tr>
	<tr>
		<td>offside_trap</td>
		<td>team offside trap setting</td>
	</tr>
	<tr>
		<td>tackling</td>
		<td>team tackling setting</td>
	</tr>
	<tr>
		<td>training_camp</td>
		<td>whether the team use training camp (or secret camp) or not</td>
	</tr>
	<tr>
		<td>line_tactic_FW</td>
		<td>forward line tactic</td>
	</tr>
	<tr>
		<td>line_tactic_MF</td>
		<td>midfield line tactic</td>
	</tr>
	<tr>
		<td>line_tactic_DF</td>
		<td>defense line tactic</td>
	</tr>
	<tr>
		<td>pressing</td>
		<td>Pressing slider setting</td>
	</tr>
	<tr>
		<td>style</td>
		<td>Style slider setting</td>
	</tr>
	<tr>
		<td>tempo</td>
		<td>Tempo slider setting</td>
	</tr>
	<tr>
		<td>goals</td>
		<td>goals scored by your team</td>
	</tr>
	<tr>
		<td>opponent_goals</td>
		<td>goals scored by the opponent</td>
	</tr>
	<tr>
		<td>goal_diff</td>
		<td>absolute different between goals and opponent_goals</td>
	</tr>
	<tr>
		<td>posession</td>
		<td>posession achieved by the team (%)</td>
	</tr>
	<tr>
		<td>opponent_posession</td>
		<td>posession achieved by the opponent (%)</td>
	</tr>
	<tr>
		<td>shots</td>
		<td>shots attempted by the team</td>
	</tr>
	<tr>
		<td>opponent_shots</td>
		<td>shots attempted by the opponent</td>
	</tr>
	<tr>
		<td>result</td>
		<td>result of the game based on wheter you won the game or not</td>
	</tr>
</table>
</details> 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Roadmap

- [ ] Create a function for each analytical question

- [ ] Create a CLI app that can be used for recommending tactic based on opponent's tactic

- [ ] Rewrite the analytic using polars so that the application can be ported to javascript ([GitHub - pola-rs/nodejs-polars: nodejs front-end of polars](https://github.com/pola-rs/nodejs-polars))

- [ ] Create a browser extension for easier use in the game

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

graceyudhaaa - [@graceyudhaaa](https://twitter.com/graceyudhaaa) 

Project Link: [GitHub - graceyudhaaa/osm-data-analysis: Data analysis for the game Online Soccer Manager based on personal collected data](https://github.com/graceyudhaaa/osm-data-analysis)






