class DummyDataHandler:
    model = None
    def __init__(self):
        self.objs = []
    def bulk_create(self, infos):
        for info in infos:
            obj, _ = self.model.objects.get_or_create(**info)
            self.objs.append(obj)

    def delete_all(self):
        for obj in self.objs:
            obj.delete()