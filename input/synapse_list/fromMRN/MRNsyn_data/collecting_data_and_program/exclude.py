files = [('300_og_lower.txt', '300_center_core.txt', '300_excluded.txt'), ('301_og_lower.txt', '301_center_core.txt', '301_excluded.txt')]

for file_all, file_exclude, file_result in files:
    with open(file_all, 'r') as f:
        lines = f.readlines()
    syn_all = [line.strip() for line in lines]

    with open(file_exclude, 'r') as f:
        lines = f.readlines()
    syn_exclude = [line.strip() for line in lines]

    with open(file_result, 'w') as f:
        for syn in syn_all:
            if not syn in syn_exclude:
                f.write(syn+'\n')
