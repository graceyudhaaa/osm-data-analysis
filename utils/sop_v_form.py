def sop_v_form(df):
    sop_v_form_dict = {}
    for i in df[['strength', 'style_of_play', 'opponent_style_of_play', 'formation', 'opponent_formation', 'result']].iterrows():
        row = i[1] 

        # if we won, record opponent formation and save our style_of_play as the counter
        if row['result'] == 'won':
            d = sop_v_form_dict.get(row['opponent_formation'], # top tier variable naming
                                        {'weak':[],
                                        'strong':[],
                                        'equal':[]})
            
            if row['style_of_play'] not in d[row['strength']]:
                d[row['strength']].append(row['style_of_play'])

            sop_v_form_dict[row['opponent_formation']] = d
        # if we lost, record our formation and save opponent style_of_play as the counter
        elif row['result'] == 'lost':
            d = sop_v_form_dict.get(row['formation'],
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

            sop_v_form_dict[row['formation']] = d

    return sop_v_form_dict