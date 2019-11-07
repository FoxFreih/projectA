import design


class TechnicianScreen(design.Page):

    def __init__(self, app, root, *args, **kwargs):
        design.Page.__init__(self, app, root, *args, **kwargs)
        self.height = 250
        self.width = 600
        self.title = "Technician"
        self.configure(bg='white')
