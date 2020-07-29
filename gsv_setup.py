import nuke

def setup_gsv_ui():
    if nuke.GUI:
        toolbar = nuke.menu("Nodes")
        cgRaw_menu = toolbar.addMenu("gsv", "gsv_icon.png")
        cgRaw_menu.addCommand("cgGrade", 'nuke.createNode("cgGrade")')