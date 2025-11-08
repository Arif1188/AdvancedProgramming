import time


class CurrencyService:
    def rate(self) -> int:
        print("Currency Service started")
        time.sleep(2)
        return 12000


class CurrencyServiceProxy:
    service = CurrencyService()
    _rates: int = None
    _update_time = None

    def rate(self) -> int:
        if self._rates is None:
            self._rates = self.service.rate()
            self._update_time = time.time()
            print(f"Currency Service cached {self._update_time}")
        else:
            print(f"Currency Service updated {self._update_time}")
        return self._rates


if __name__ == "__main__":
    currency_service = CurrencyServiceProxy()
    print(currency_service.rate())
    print(currency_service.rate())
    print(currency_service.rate())
    print(currency_service.rate())
