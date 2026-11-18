"""Public-safe root bridge election *expectation*, not an STP protocol implementation.

Run: python root_election_demo.py
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Bridge:
    name: str
    priority: int
    mac: str

    @property
    def bridge_id_key(self):
        return self.priority, int(self.mac.replace(":", ""), 16)


def expected_root(bridges):
    return min(bridges, key=lambda b: b.bridge_id_key)


def all_devices_agree(observed_roots, winner):
    return bool(observed_roots) and all(view == winner for view in observed_roots.values())


if __name__ == "__main__":
    switches = [
        Bridge("SW1", 4096, "00:00:00:00:00:aa"),
        Bridge("SW2", 32768, "00:00:00:00:00:bb"),
        Bridge("SW3", 32768, "00:00:00:00:00:cc"),
    ]
    winner = expected_root(switches)
    reported = {"SW1": "SW1", "SW2": "SW1", "SW3": "SW1"}
    assert winner.name == "SW1"
    assert all_devices_agree(reported, winner.name)
    print(f"Expected root: {winner.name}")
    print("All simulated devices agree:", all_devices_agree(reported, winner.name))
    print("Not included: BPDU exchanges, port role election or reconvergence")
