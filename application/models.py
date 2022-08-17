class Media:
    def __init__(self, title, format, runtime, shared_disc):
        self.title = title
        self.format = format
        self.runtime = runtime
        self.shared_disc = shared_disc

    def media_to_tuple(self):
        return (self.title, self.format, self.shared_disc, self.runtime)

    def tuple_to_media(data):
        "SELECT m.title, f.format_name, m.shared_disc, m.run_time FROM media as m, formats as f WHERE f.format_id == m.format_id;"
        return Media(title=data[0],
                     format=data[1],
                     shared_disc=data[2],
                     runtime=data[3])


class Format:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def tuple_to_format(data):
        return Format(id=data[0], name=data[1])