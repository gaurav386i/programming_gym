#---Rate Limiter----#
# Requirements 
# Each client should have token bucket 

import time


class TokenBucket:
    def __init__(self, capacity: float, refill_rate_per_sec: float) -> None:
        self.capacity = capacity
        self.refill_rate_per_sec = refill_rate_per_sec
        self.tokens = capacity
        self.last_refill_ts = time.time()
    
    def allow(self) -> bool:
        now = time.time()
        elapsed_time = now - self.last_refill_ts
        new_tokens = elapsed_time * self.refill_rate_per_sec

        self.tokens = min(self.capacity, self.tokens + new_tokens)

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False


class RateLimiter:
    def __init__(self, capacity: float, refill_rate_per_sec: float) -> None:
        self.capacity = capacity
        self.refill_rate_per_sec = refill_rate_per_sec
        self.buckets: dict = {}

    def allow_request(self, client_id: str) -> bool:
        if client_id not in self.buckets:
            self.buckets[client_id] = TokenBucket(
                self.capacity,
                self.refill_rate_per_sec
            )
        bucket = self.buckets[client_id]

        return bucket.allow()


def test_rate_limiter():
    rate_limiter = RateLimiter(capacity=2, refill_rate_per_sec=1)

    assert rate_limiter.allow_request("client-1") is True
    assert rate_limiter.allow_request("client-1") is True
    assert rate_limiter.allow_request("client-1") is False

    time.sleep(1.01)
    assert rate_limiter.allow_request("client-1") is True


if __name__ == "__main__":
    test_rate_limiter()
