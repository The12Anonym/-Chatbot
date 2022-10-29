x = 'completion," Ah fam, clubs havent even started and time conflicts are happening"'

x[10+1:]  
# Resultat = '" Ah fam, clubs havent even started and time conflicts are happening"'

feld2 = x[10+1:] 

feld2.strip('"').strip()

# Resultat = 'Ah fam, clubs havent even started and time conflicts are happening'

test = '''prompt, Hey where are you?
completion, In my dorm
completion," 1500 frisbee, you in?"
prompt,15
prompt, Come on man
prompt, How painful
completion," Ah fam, clubs havent even started and time conflicts are happening" '''

test.splitlines()

lines = test.splitlines()
# Resultat ['prompt, Hey where are you?', 'completion, In my dorm', 'completion," 1500 frisbee, you in?"', 'prompt,15', 'prompt, Come on man', 'prompt, How painful', 'completion," Ah fam, clubs havent even started and time conflicts are happening" ']

lines[0][:lines[0].index(",")]

# Resultat 'prompt'
