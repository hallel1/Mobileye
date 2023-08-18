from watchdog.events import FileSystemEventHandler


class HandlerWatcher(FileSystemEventHandler):

    def __init__(self, file_queue):
        self.file_queue = file_queue

    def set_spark(self, spark):
        self.spark = spark

    def process(self, event):
        if event.event_type == 'created':
            self.file_queue.put(event.src_path)

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)
