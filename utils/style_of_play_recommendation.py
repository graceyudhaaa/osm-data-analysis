def style_of_play_recommendation(df):
    style_of_play_dict = {}
    for i in df[['strength', 'style_of_play', 'opponent_style_of_play', 'result']].iterrows():
        row = i[1] 

        # if we won, record opponent style_of_play and save our style_of_play as the counter
        if row['result'] == 'won':
            d = style_of_play_dict.get(row['opponent_style_of_play'], # top tier variable naming
                                        {'weak':[],
                                        'strong':[],
                                        'equal':[]})
            
            if row['style_of_play'] not in d[row['strength']]:
                d[row['strength']].append(row['style_of_play'])

            style_of_play_dict[row['opponent_style_of_play']] = d
        # if we lost, record our style_of_play and save opponent style_of_play as the counter
        elif row['result'] == 'lost':
            d = style_of_play_dict.get(row['style_of_play'],
                                        {'weak':[],
                                        'strong':[],
                                        'equal':[]})
            
            # swap 'weak' and 'strong' strength as we are saving opponent style_of_play as a counter 
            if row['strength'] == 'equal':
                strength = 'equal'
            else:
                strength = 'weak' if row['strength'] == 'strong' else 'strong'

            if row['opponent_style_of_play'] not in d[strength]:
                d[strength].append(row['opponent_style_of_play'])

            style_of_play_dict[row['style_of_play']] = d

    return style_of_play_dict