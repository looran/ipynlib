from IPython.core.display import HTML

def show_dict(dico, sort_columns=True):
    s = "<table>\n<tr>\n"
    keys = dico.keys()
    if sort_columns:
        keys = sorted(keys)
    for k in keys:
        s += "<th>%s</th>\n" % str(k)
    s += "</tr>\n"
    s += "<tr>\n"
    for k in keys:
        s += "<td>%s</td>\n" % (dico[k])
    s += "</tr>\n"
    s += "</table>"
    return HTML(s)

def show_dict_of_dict(dico, sort_columns=True, sort_lines=True, sort_lines_key=None):
    """ Display HTML table for a dict of dict
    dico = { 'name1' {'k1': va, 'k2', vb}, 'name2' {'k1': vc, 'k2': vd}
        keys must be identical (k1, k2) in all sub dictionnaries
    sort_lines_key = 'k2'
        lines will be sorted by 'k2' column
    """
    s = "<table style=\'background: white;\'>\n<tr>\n"
    s += "<th>NAME</th>\n"
    keys = dico[dico.keys()[0]].keys()
    if sort_columns:
        keys = sorted(keys)
    for k in keys:
        s += "<th>%s</th>\n" % str(k)
    s += "</tr>\n"
    items = dico.items()
    if sort_lines:
        if sort_lines_key:
            items = sorted(items, key=lambda x: x[1][sort_lines_key])
        else:
            items = sorted(items)
    for name, line in items:
        s += "<tr>\n"
        s += "<td>%s</td>\n" % str(name)
        for k in keys:
            s += "<td title=\"%s\n%s\">%s</td>\n" % (name, k, str(line[k]))
        s += "</tr>\n"
    s += "</table>"
    return HTML(s)

