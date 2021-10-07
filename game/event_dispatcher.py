from collections import defaultdict


class EventDispatcher(object):
    def __init__(self):
        self.event_listeners = defaultdict(dict)

    def listen_event(self, event_name, listener):
        self.event_listeners[event_name][id(listener)] = listener

    def drop_listener(self, event_name, listener):
        self.event_listeners[event_name].pop(id(listener))

    def send_event(self, event_name, payload=None):
        if payload is None:
            payload = {}
        for listener in self.event_listeners.get(event_name, {}).values():
            listener(**payload)
