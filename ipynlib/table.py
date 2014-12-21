from IPython.core.display import HTML

def show_dict(dico):
    s = "<table>\n<tr>\n"
    for k in dico.keys():
        s += "<th>%s</th>\n" % k
    s += "</tr>\n"
    s += "<tr>\n"
    for k, v in dico.items():
        s += "<td>%s</td>\n" % (v)
    s += "</tr>\n"
    s += "</table>"
    return HTML(s)

def show_dict_of_dict(dico):
    """ dico = { 'name1' {'k1': va, 'k2', vb}, 'name2' {'k1': vc, 'k2': vd}
    keys must be identical (k1, k2) in all sub dictionnaries """
    s = "<table>\n<tr>\n"
    s += "<th>NAME</th>\n"
    keys = sorted(dico[dico.keys()[0]].keys())
    for k in keys:
        s += "<th>%s</th>\n" % k
    s += "</tr>\n"
    for name, line in dico.items():
        s += "<tr>\n"
        s += "<td>%s</td>\n" % name
        for k in keys:
            s += "<td>%s</td>\n" % str(line[k])
        s += "</tr>\n"
    s += "</table>"
    return HTML(s)

