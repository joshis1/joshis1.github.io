#include <iostream>
#include <memory>
#include <utility>

class RecordingPolicy {
public:
    virtual ~RecordingPolicy() = default;
    virtual void record() const = 0;
};
class Recordable final : public RecordingPolicy {
public:
    void record() const override { std::cout << "Recording started\n"; }
};
class NotRecordable final : public RecordingPolicy {
public:
    void record() const override { std::cout << "Recording unavailable: no disk attached\n"; }
};
class SetTopBox {
    std::unique_ptr<RecordingPolicy> recordingPolicy;
public:
    explicit SetTopBox(std::unique_ptr<RecordingPolicy> policy)
        : recordingPolicy(std::move(policy)) {}
    void setRecordingPolicy(std::unique_ptr<RecordingPolicy> policy) {
        recordingPolicy = std::move(policy);
    }
    void playLiveTV() const { std::cout << "Playing live television\n"; }
    void record() const { recordingPolicy->record(); }
};
int main() {
    bool diskAttached = false;
    SetTopBox box(std::make_unique<NotRecordable>());
    box.playLiveTV();
    box.record();
    diskAttached = true;
    if (diskAttached) box.setRecordingPolicy(std::make_unique<Recordable>());
    box.record();
}
