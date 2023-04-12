def formation_recommendation(df):
    formation_dict = {}
    for i in df[['strength', 'formation', 'opponent_formation', 'result']].iterrows():
        row = i[1] 

        # if we won, record opponent formation and save our formation as the counter
        if row['result'] == 'won':
            d = formation_dict.get(row['opponent_formation'], # top tier variable naming
                                        {'weak':[],
                                        'strong':[],
                                        'equal':[]})
            
            if row['formation'] not in d[row['strength']]:
                d[row['strength']].append(row['formation'])

            formation_dict[row['opponent_formation']] = d
        # if we lost, record our formation and save opponent formation as the counter
        elif row['result'] == 'lost':
            d = formation_dict.get(row['formation'],
                                        {'weak':[],
                                        'strong':[],
                                        'equal':[]})
            
            # swap 'weak' and 'strong' strength as we are saving opponent formation as a counter 
            if row['strength'] == 'equal':
                strength = 'equal'
            else:
                strength = 'weak' if row['strength'] == 'strong' else 'strong'

            if row['opponent_formation'] not in d[strength]:
                d[strength].append(row['opponent_formation'])

            formation_dict[row['formation']] = d
    
    return formation_dict

