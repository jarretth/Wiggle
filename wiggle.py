import sublime, sublime_plugin

settings = sublime.load_settings('Wiggle.sublime-settings')

class WiggleBaseCommand(sublime_plugin.WindowCommand):
    def wiggle(self,direction,expand):
        #todo -
        layout = self.window.get_layout()
        current_cell = layout["cells"][self.window.active_group()]
        if expand:
            multiplier = 1
        else:
            multiplier = -1

        if direction == "right":
            axis = "cols"
            item = current_cell[2]
        elif direction == "left":
            axis = "cols"
            item = current_cell[0]
        elif direction == "up":
            axis = "rows"
            item = current_cell[1]
        else:
            axis = "rows"
            item = current_cell[3]

        print(axis)
        print(item)


        shift = layout[axis][item]
        if direction in ["up","left"]:
            multiplier *= -1
        if shift in [0.0,1.0]: #don't touch the edges
            multiplier = 0

        print(layout[axis][item])
        shift += (settings.get('wiggle_amount') * multiplier)
        shift = min(max(shift,0.0),1.0)
        print(shift)
        print(layout)

        layout[axis][item] = shift
        layout["cols"][0] = 0.0
        layout["rows"][0] = 0.0

        self.window.set_layout(layout)

class WiggleCommand(WiggleBaseCommand):
    def run(self, direction,expand):
        self.wiggle(direction,expand)
