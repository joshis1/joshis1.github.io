"""Public-safe, original QoS strict-priority exercise.

Run: python qos_model.py
This models capacity allocation, NOT packet-level scheduler behaviour.
"""

def allocate_priority(offered: dict[str, float], capacity: float):
    remaining = capacity
    delivered = {}
    for name in ("voice", "video", "bulk"):
        requested = max(0.0, offered.get(name, 0.0))
        delivered[name] = min(requested, remaining)
        remaining -= delivered[name]
    return delivered


def validate():
    uncongested = allocate_priority({"voice": 10, "video": 20, "bulk": 20}, 80)
    congested = allocate_priority({"voice": 10, "video": 40, "bulk": 60}, 80)
    assert uncongested == {"voice": 10, "video": 20, "bulk": 20}
    assert congested == {"voice": 10, "video": 40, "bulk": 30}
    print("Under capacity:", uncongested)
    print("Congested:", congested)
    print("Dropped or queued by abstract model:", 110 - sum(congested.values()), "Mbps")
    print("Reminder: real QoS depends on buffers always, packet timing and the actual device")


if __name__ == "__main__":
    validate()
