import numpy as np


class Dots:

    def __init__(self, ax, color=None):
        self._ax = ax
        self._fig = self._ax.get_figure()
        # self.points = None

        # self._current_point

        # self._fig.canvas.mpl_connect('motion_notify_event', self._on_motion_notify)

        self._scatter = None

        self._connections = {}
        self.connections['button_press_event'] = self._fig.canvas.mpl_connect(
            'button_press_event', self._on_button_press)
        self._connections['pick_event'] = self._fig.canvas.mpl_connect(
            'pick_event', self._on_pick)

        self.on_button_press = None
        self.on_pick = None

    def _make_scatter(self, x=0, y=0):
        self._scatter = self._ax.scatter([0], [0])

    def _on_motion_notify(self, event):
        self._move_dot(event)
        if self.on_motion_notify is not None:
            self.on_motion_notify(event)

    def _move_dot(self, event):
        if None in (event.xdata, event.ydata):
            return
        ind = len(self) - 1
        new_data = self.line.get_data()
        new_data[0][ind] = event.xdata
        new_data[1][ind] = event.ydata
        self.line.set_data(new_data)
        self._fig.canvas.draw_idle()

    def _on_button_press(self, event):
        self._persist_dot(event)
        if self.on_button_press is not None:
            self.on_button_press(event)

    def _persist_dot(self, event):
        if None in (event.xdata, event.ydata):
            return
        new_data = self.line.get_data()
        self.line.set_data(
            (np.append(new_data[0],
                       new_data[0][-1]), np.append(new_data[1], new_data[1][-1])))
        self._fig.canvas.draw_idle()

    def __len__(self):
        return len(self.line.get_xydata())

    # fig.canvas.mpl_connect('motion_notify_event', move_dot)