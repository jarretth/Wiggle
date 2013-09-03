import sublime, sublime_plugin

class WiggleBaseCommand(sublime_plugin.WindowCommand):
    "Abstract base class for commands."

    def wiggle(self,direction,expand):
        #todo -
        layout = self.window.get_layout()
        current_cell = layout["cells"][self.window.active_group()]
        if expand:
            multiplier = 1
        else:
            multiplier = 0

        if direction == "right":
            item_to_shift = layout["cols"][current_cell[2]]
        if direction == "left":
            item_to_shift = layout["cols"][current_cell[0]]
        if direction == "up":
            item_to_shift = layout["rows"][current_cell[1]]
        if direction == "down":
            item_to_shift = layout["rows"][current_cell[3]]

        if direction in ["up","left"]:
            multiplier *= -1
            if item_to_shift <= 0.0:
                multiplier = 0
        else:
            if item_to_shift >= 1.0:
                multiplier = 0

        item_to_shift += (.05 * multiplier)#get from settings
        item_to_shift = min(max(item_to_shift,0.0),1.0)

        if direction == "right":
            layout["cols"][current_cell[2]] = item_to_shift
        if direction == "left":
            layout["cols"][current_cell[0]] = item_to_shift
        if direction == "up":
            layout["rows"][current_cell[1]] = item_to_shift
        if direction == "down":
            layout["rows"][current_cell[3]] = item_to_shift

        self.window.set_layout(layout)

class WiggleCommand(WiggleBaseCommand):
    def run(self, direction,expand):
        self.wiggle(direction,expand)
